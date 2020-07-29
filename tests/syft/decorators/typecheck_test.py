import pytest
from typing import List, Union, Optional, Dict
from syft.decorators import type_hints


def test_typecheck_basic_dtypes():
    @syft_decorator(typechecking=True)
    def func(x: int, y: int) -> int:
        return x + y

    func(x=1, y=2)

    with pytest.raises(TypeError) as e:
        func(x="test", y=2)

    assert str(e.value) == 'type of argument "x" must be int; got str instead'


def test_typecheck_generic_dtypes():
    @syft_decorator(typechecking=True)
    def func(x: List[str], y: Union[List[str], List[int]]) -> int:
        return 0

    func(x=["1", "2", "3"], y=[1, 2, 3])
    func(x=["2", "2", "3"], y=["unu", "doi", "trei"])

    with pytest.raises(TypeError) as e:
        func(x=[1, 2, 3], y=["unu", "doi", "trei"])

    assert str(e.value) == 'type of argument "x"[0] must be str; got int instead'

    with pytest.raises(TypeError) as e:
        func(x=["1", "2", "3"], y=[1, 2, 2.0])


def test_optional():
    @syft_decorator(typechecking=True)
    def func(x: Optional[int]) -> int:
        return 0

    func(x=0)
    func(x=None)

    with pytest.raises(TypeError) as e:
        func(x="test")


def test_mappings():
    @syft_decorator(typechecking=True)
    def func(x: Dict[str, str]) -> int:
        return 0

    func(x={"1": "2"})

    with pytest.raises(TypeError) as e:
        func(x={1: "1"})

    assert str(e.value) == 'type of keys of argument "x" must be str; got int instead'


def test_ret_type():
    @syft_decorator(typechecking=True)
    def func() -> int:
        return 0

    func()

    with pytest.raises(TypeError) as e:

        @syft_decorator(typechecking=True)
        def func() -> int:
            return 1.0

        func()

    assert str(e.value) == "type of the return value must be int; got float instead"
