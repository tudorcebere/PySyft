from ...decorators import syft_decorator
from ..common.uid import UID
from ..common.serializable import Serializable
from .storeable_object import StorableObject
from typing import Iterable
from abc import ABC


class ObjectStore(Serializable, ABC):
    """
    ObjectStore is the common interface for all the stores that a Node can handle. This should
    provide a dict-like interface on handling data on a worker. Indexing should be always done
    by using UID objects, while de indexed value should always be a SerizableObject.
    """

    @syft_decorator(typechecking=True)
    def __sizeof__(self) -> int:
        """
        Method to return the memory size of the object if possible, if not, it will return __len__.

        Returns:
            int: memory size of the store.
        """
        raise NotImplementedError

    @syft_decorator(typechecking=True)
    def __str__(self) -> str:
        """
        Method to print to first 5 entries of the ObjectStore in a database-like format.

        Returns:
            str: header and first 5 entries of store in a formatted manner.
        """
        raise NotImplementedError

    @syft_decorator(typechecking=True)
    def __len__(self) -> int:
        """
        Method to return the number of elements in the store.

        Returns:
            int: the number of objects in the store.
        """
        raise NotImplementedError

    @syft_decorator(typechecking=True)
    def keys(self) -> Iterable[UID]:
        """
        Method to return all indexes from the store.

        Returns:
            Iterable[UID]: an iterable containing the keys of the store.
        """
        raise NotImplementedError

    @syft_decorator(typechecking=True)
    def values(self) -> Iterable[StorableObject]:
        """
        Method to return all values from the store.

        Returns:
            Iterable[StorableObject]: an iterable containing the keys of the store.
        """
        raise NotImplementedError

    @syft_decorator(typechecking=True)
    def store(self, obj: StorableObject) -> None:
        """
        Method to store an object based on its own UID in the store.

        Args:
            obj (StorableObject): the object to be stored.
        """
        raise NotImplementedError

    @syft_decorator(typechecking=True)
    def __contains__(self, key: UID) -> bool:
        """
        Method to check if an UID is present in the store.

        Args:
            key (UID): the UID to be searched.

        Returns:
            bool: if the object is present or not.
        """
        raise NotImplementedError

    @syft_decorator(typechecking=True)
    def __getitem__(self, key: UID) -> StorableObject:
        """
        Method to retrieve an object from the store.

        Args:
            key (UID): The key to be searched for in the store.

        Returns:
            StorableObject: The object associated with the input key.

        Raises:
            ValueError: If the key is not present in the store.
        """
        raise NotImplementedError

    @syft_decorator(typechecking=True)
    def __setitem__(self, key: UID, value: StorableObject) -> None:
        """
        Method to store an object in the store. The difference between this and store is that you
        can you use self.store to store objects at a different key than the one specified in
        the StorableObject.

        This updates the value at the input UID if it exists already.

        Args:
            key (UID): the UID at which to store the StorableObject.
            value (StorableObject): the StorableObject to be stored.
        """
        raise NotImplementedError

    @syft_decorator(typechecking=True)
    def __delitem__(self, key: UID) -> None:
        """
        Method to remove an object from the store based on its UID.

        Args:
            key (UID): the key at which to delete the object.

        Raises:
            ValueError: if the key is not present in the store.
        """
        raise NotImplementedError

    @syft_decorator(typechecking=True)
    def clear(self) -> None:
        """
        Clears all storage owned by the store.
        """
        raise NotImplementedError

