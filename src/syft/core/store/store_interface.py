from ...decorators import syft_decorator
from ...common.id import UID
from ..serialization import Serializable
from .storeable_object import StorableObject
from typing import Iterable


class ObjectStore(Serializable):
    """Logic to store and retrieve objects within a worker"""

    def __init__(self):
        self._objects = {}
        self.search_engine = None

    @syft_decorator(typechecking=True)
    def __sizeof__(self) -> int:
        raise NotImplementedError

    @syft_decorator(typechecking=True)
    def __str__(self) -> int:
        raise NotImplementedError

    @syft_decorator(typechecking=True)
    def __len__(self) -> int:
        raise NotImplementedError

    @syft_decorator(typechecking=True)
    def keys(self) -> Iterable[UID]:
        raise NotImplementedError

    @syft_decorator(typechecking=True)
    def values(self) -> Iterable[StorableObject]:
        raise NotImplementedError

    @syft_decorator(typechecking=True)
    def store(self, obj: StorableObject) -> None:
        raise NotImplementedError

    @syft_decorator(typechecking=True)
    def __contains__(self, key: UID) -> bool:
        raise NotImplementedError

    @syft_decorator(typechecking=True)
    def __getitem__(self, key: UID) -> StorableObject:
        raise NotImplementedError

    @syft_decorator(typechecking=True)
    def __setitem__(self, key: UID, value: StorableObject) -> None:
        raise NotImplementedError

    @syft_decorator(typechecking=True)
    def __delitem__(self, key: UID) -> None:
        raise NotImplementedError

    @syft_decorator(typechecking=True)
    def clear(self) -> None:
        raise NotImplementedError
