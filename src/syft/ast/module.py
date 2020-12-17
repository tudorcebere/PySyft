# stdlib
import inspect
from types import BuiltinFunctionType
from types import FunctionType
from types import ModuleType
from typing import Any
from typing import Callable as CallableT
from typing import Dict
from typing import List
from typing import Optional
from typing import Union

# syft relative
from .. import ast
from ..ast.callable import Callable


class Module(ast.attribute.Attribute):

    """A module which contains other modules or callables."""

    lookup_cache: Dict[Any, Any] = {}

    def __init__(
        self,
        name: Optional[str] = None,
        path_and_name: Optional[str] = None,
        ref: Optional[Union["ast.callable.Callable", CallableT]] = None,
        return_type_name: Optional[str] = None,
        is_property: bool = False,
    ):
        super().__init__(name, path_and_name, ref, return_type_name, is_property)

    def add_attr(
        self,
        attr_name: str,
        attr: Optional[Union[Callable, CallableT]],
    ) -> None:
        self.__setattr__(attr_name, attr)
        if attr is not None:
            self.attrs[attr_name] = attr

            # if add_attr is called directly we need to cache the path as well
            attr_ref = getattr(attr, "ref", None)
            path = getattr(attr, "path_and_name", None)
            if attr_ref not in self.lookup_cache and path is not None:
                self.lookup_cache[attr_ref] = path

    def __call__(
        self,
        path: Optional[List[str]] = None,
        index: int = 0,
        return_callable: bool = False,
        obj_type: Optional[type] = None,
    ) -> Optional[Union[Callable, CallableT]]:

        _path: Union[List[str]] = path if path is not None else []

        if obj_type is not None:
            if obj_type in self.lookup_cache:
                _path = self.lookup_cache[obj_type]

        resolved = self.attrs[_path[index]](
            path=_path,
            index=index + 1,
            return_callable=return_callable,
            obj_type=obj_type,
        )
        return resolved

    def __repr__(self) -> str:
        out = "Module:\n"
        for name, module in self.attrs.items():
            out += "\t." + name + " -> " + str(module).replace("\t.", "\t\t.") + "\n"

        return out

    def add_path(
        self,
        path: List[str],
        index: int,
        return_type_name: Optional[str] = None,
        framework_reference: Optional[Union[Callable, CallableT]] = None,
    ) -> None:
        if path[index] not in self.attrs:
            attr_ref = getattr(self.ref, path[index])

            if isinstance(attr_ref, ModuleType):
                self.add_attr(
                    attr_name=path[index],
                    attr=ast.module.Module(
                        path[index],
                        ".".join(path[: index + 1]),
                        attr_ref,  # type: ignore
                        return_type_name=return_type_name,
                    ),
                )
            elif inspect.isclass(attr_ref):
                klass = ast.klass.Class(
                    name=path[index],
                    path_and_name=".".join(path[: index + 1]),
                    ref=attr_ref,
                    return_type_name=return_type_name,
                )
                self.add_attr(
                    attr_name=path[index],
                    attr=klass,
                )
            elif isinstance(attr_ref, (FunctionType, BuiltinFunctionType)):
                self.add_attr(
                    attr_name=path[index],
                    attr=ast.callable.Callable(
                        path[index],
                        ".".join(path[: index + 1]),
                        attr_ref,
                        return_type_name=return_type_name,
                    ),
                )
            elif index == len(path) - 1:
                if "globals" not in self.attrs:
                    # syft absolute
                    from syft.lib.misc.scope import Scope

                    scope, scope_name = Scope.from_qualname(".".join(path[:-1]))
                    path.insert(len(path) - 1, "globals")
                    self.add_attr(
                        attr_name="globals",
                        attr=ast.klass.Class(
                            "globals",
                            ".".join(path[: index + 1]),
                            scope,
                            return_type_name=scope_name,
                        ),
                    )

        attr = self.attrs[path[index]]
        attr_ref = getattr(self.ref, path[index], None)

        if attr_ref is not None and attr_ref not in self.lookup_cache:
            self.lookup_cache[attr_ref] = path

        if hasattr(attr, "add_path"):
            attr.add_path(  # type: ignore
                path=path, index=index + 1, return_type_name=return_type_name
            )
