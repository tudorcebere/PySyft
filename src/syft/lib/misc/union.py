from ...util import get_fully_qualified_name
from ...ast.globals import Globals
from ...ast.module import Module
from ...ast.klass import Class
import sys

class Any:
    def __abs__(self):
        pass



# @dataclass(frozen=True)
# class UnionPointerCache:
#     # check if this union has been solved already
#     cached_solved_unions: Dict[str, type]
#
#     # dynamic misc_ast
#     misc_union: Globals
#
#     # utility function that should go into Globals (reused across the codebase)
#     def get_ast_parent(self, path) -> Globals:
#         parent = self.misc_ast
#         for step in path.split(".")[:-1]:
#             parent = parent.attrs[step]
#         return parent

union_ast: Globals = Globals()

union_ast.add_attr(
    attr_name="syft",
    attr=Module(
        "syft",
        "syft",
        None,
        return_type_name="",
    ),
)

union_ast.syft.add_attr(
    attr_name="lib",
    attr=Module(
        "lib",
        "syft.lib",
        None,
        return_type_name="",
    ),
)

union_ast.syft.lib.add_attr(
    attr_name="misc",
    attr=Module(
        "misc",
        "syft.lib.misc",
        None,
        return_type_name="",
    ),
)

union_ast.syft.lib.misc.add_attr(
    attr_name="union",
    attr=Module(
        "union",
        "syft.lib.misc.union",
        None,
        return_type_name="",
    ),
)


ignored_methods = {
    "__delattr__",
    "__reduce__",
    "__getattribute__",
    "__sizeof__",
    "__init__",
    "__repr__",
    "__dir__",
    "__class__",
    "__new__",
    "__setattr__",
    "__init_subclass__",
    "__subclasshook__",
    "__dict__",
    "__format__",
    "__doc__",
    "__reduce_ex__",
    "__weakref__",
    "__module__",
    "get_protobuf_schema"
}


def generate_err(method_name: str):
    def raise_err(*args):
        raise ValueError(f"Can't call {method_name}.")

    return raise_err


def get_set_of_functions_for_pointer(union_type_fqn: str) -> set:
    from syft.lib import lib_ast

    path = union_type_fqn.split(".")
    root = lib_ast
    for sub_path in path:
        root = getattr(root, sub_path)

    pointer_api = set(dir(root.pointer_type)) - ignored_methods

    return pointer_api


def generate_func(self, target_func):
    def proxy_func(*args):
        func = getattr(self.value, target_func)
        return func(*args)

    return proxy_func

def generate_lazy_method(fqn) -> set:
    parts = fqn.split(".")
    klass_name = parts.pop()
    klass = getattr(sys.modules[".".join(parts)], klass_name)
    return set(dir(klass)) - ignored_methods

def generate_lazy_methods(fqns) -> set:
    result = set()
    for fqn in fqns:
        result |= generate_lazy_method(fqn)
    return result



def generate_init():
    def __init__(self, value):
        self.value = value
        fqn = get_fully_qualified_name(obj=value)
        allowed_funcs = get_set_of_functions_for_pointer(fqn)
        real_funcs = ["__abs__"] #generate_lazy_method(fqn)

        for func in real_funcs:
            if func in allowed_funcs:
                setattr(self, func, lambda: generate_func(self, func))

    return __init__


class PointerUnion(type):
    def __init__(self, *args):
        super().__init__(self)

    def __new__(cls, name, bases, dct, union_types):
        # new_type_fqn = "syft.lib.misc.union." + name
        # methods = ["__abs__"] #generate_lazy_methods(union_types)
        # dct = {
        #     key: generate_err(key) for key in methods
        # }
        # dct["__init__"] = generate_init()
        # dct["__qualname__"] = "syft.lib.misc.union." + name
        # new_type = super().__new__(cls, name, bases, dct)

        # new_type = type("UnionAny", tuple(), {"__abs__": lambda: 0})
        # globals()[new_type.__name__] = new_type

        ast = union_ast

        ast.syft.lib.misc.union.add_attr(
            attr_name="Any",
            attr=Class(
                "Any",
                "syft.lib.misc.union.Any",
                Any,  # type: ignore
                return_type_name="syft.lib.misc.union.Any",
            ),
        )

        print(ast)
        ast.add_path(
            "syft.lib.misc.union.Any.__abs__",
            return_type_name="syft.lib.misc.union.Any")

        for klass in ast.classes:
            klass.create_pointer_class()
            klass.create_send_method()
            klass.create_serialization_methods()
            klass.create_storable_object_attr_convenience_methods()

        return Any

    @staticmethod
    def from_qualnames(*union_types) -> (str, type):

        # union_types = sorted(union_types)
        # name = (
        #     "".join([union_type.split(".")[-1] for union_type in union_types]) + "Union"
        # )

        # if name in union_cache.cached_solved_unions:
        #     target_type = union_cache.cached_solved_unions[name]
        # else:
        target_type = PointerUnion("UnionAny", tuple(), {}, union_types)
        # union_cache.cached_solved_unions[target_type.__qualname__] = target_type
        # qualname = target_type.__qualname__

        qualname = "syft.lib.misc.union.Any"
        return qualname, target_type
