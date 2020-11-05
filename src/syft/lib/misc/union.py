from ...util import get_fully_qualified_name

from typing import List

union_cache = {}
union_api_cache = {}
functions_cache = {}

ignored_methods = {
    '__delattr__',
    '__reduce__',
    '__getattribute__',
    '__sizeof__',
    '__init__',
    '__repr__',
    '__dir__',
    '__class__',
    '__new__',
    '__setattr__',
    '__init_subclass__',
    '__subclasshook__',
    '__dict__',
    '__format__',
    '__doc__',
    '__reduce_ex__',
    '__weakref__',
    '__module__'
}

def generate_err(method_name: str):
    def raise_err(*args):
        raise ValueError(f"Can't call {method_name}.")

    return raise_err

def get_possible_functions(union_types: List[str], fqn: str) -> set:
    set_of_functions = set()

    if fqn in union_api_cache:
        return union_api_cache[fqn]

    for union_type in union_types:
        if union_type in functions_cache:
            set_of_functions.union(functions_cache[union_type])
        else:
            from syft.lib import lib_ast

            path = union_type.split(".")
            root = lib_ast
            for sub_path in path:
                root = getattr(root, sub_path)

            pointer_api = set(dir(root.pointer_type)) - ignored_methods
            functions_cache[union_type] = pointer_api
            set_of_functions = set_of_functions.union(pointer_api)

    union_api_cache[fqn] = set_of_functions
    return set_of_functions

def generate_func(self, target_func):
    def proxy_func(*args):
        func = getattr(self.value, target_func)
        return func(*args)
    return proxy_func

def generate_init(union_types):
    def __init__(self, value):
        self.value = value
        fqn = get_fully_qualified_name(obj=value)

        funcs = get_possible_functions(union_types, type(self).__qualname__)
        allowed_funcs = functions_cache[fqn]

        for func in funcs:
            if func not in allowed_funcs:
                setattr(self, func, generate_err(func))
            elif hasattr(self.value, func):
                target_func = generate_func(self, func)
                setattr(self, func, target_func)

    return __init__

class PointerUnion(type):
    def __init__(self, *args):
        super().__init__(self)

    def __new__(cls, name, bases, dct, union_types):
        dct["__init__"] = generate_init(union_types)
        dct["__qualname__"] = "syft.lib.misc.union." + name
        x = super().__new__(cls, name, bases, dct)
        return x

    @staticmethod
    def from_qualnames(*union_types) -> str:

        union_types = sorted(union_types)
        name = "".join([union_type.split(".")[-1] for union_type in union_types]) + "Union"

        if name in union_cache:
            target_type = union_cache[name]
        else:
            target_type = PointerUnion(name, tuple(), { }, union_types)
            union_cache[target_type.__qualname__] = target_type
        qualname = target_type.__qualname__
        return qualname