from ...ast.globals import Globals
from ...ast.module import Module
from ...ast.klass import Class
from .union import union_ast

def add_modules(ast: Globals, modules) -> None:
    for module in modules:
        parent = get_parent(module, ast)
        attr_name = module.rsplit(".", 1)[-1]

        parent.add_attr(
            attr_name=attr_name,
            attr=Module(
                attr_name,
                module,
                None,
                return_type_name="",
            ),
        )


def add_classes(ast, paths) -> None:
    for path, return_type, ref in paths:
        parent = get_parent(path, ast)

        attr_name = path.rsplit(".", 1)[-1]

        parent.add_attr(
            attr_name=attr_name,
            attr=Class(
                attr_name,
                path,
                ref,  # type: ignore
                return_type_name=return_type,
            ),
        )

def get_parent(path: str, root):
    parent = root
    for step in path.split(".")[:-1]:
        parent = parent.attrs[step]
    return parent

def add_methods(ast, paths) -> None:
    for path, return_type, _ in paths:
        parent = get_parent(path, ast)
        path_list = path.split(".")
        parent.add_path(
            path=path_list, index=len(path_list) - 1, return_type_name=return_type
        )


def create_misc_ast() -> Globals:
    return union_ast