"""A Pointer is the main handler when interacting with remote data.
A Pointer object represents an API for interacting with data (of any type)
at a specific location. The relation between pointers and data is many to one,
there can be multiple pointers pointing to the same piece of data, meanwhile,
a pointer cannot point to multiple data sources.

A pointer is just an object id on a remote location and a set of methods that can be
executed on the remote machine directly on that object. One note that has to be made
is that all operations between pointers will return a pointer, the only way to have access
to the result is by calling .get() on the pointer.

There are two proper ways of receiving a pointer on some data:
    1. When sending that data on a remote machine the user receives a pointer.
    2. When the user searches for the data in an object store it receives a pointer to that data,
    if it has the correct permissions for that.

After receiving a pointer, one might want to get the data behind the pointer locally. For that the
user should:
    1. Request access.
    2.1 - The data owner has to approve the request
    2.2 - The data user checks if the request has been approved.
    3. After the request has been approved, the data user can call .get() on the pointer to get the
    data locally.

Pointers are being generated for most types of objects in the data science scene, but what you can
do on them is not the pointers job, see the lib module for more details. One can see the pointer
as a proxy to the actual data, the filtering and the security being applied where the data is being
held.

"""
# external imports
from google.protobuf.reflection import GeneratedProtocolMessageType

# syft imports
import syft as sy
from ..common.uid import UID
from ..common.pointer import AbstractPointer
from ..node.abstract.node import AbstractNode
from ..common.serde.deserialize import _deserialize
from ...decorators.syft_decorator_impl import syft_decorator
from ..node.common.action.get_object_action import GetObjectAction
from ...proto.core.pointer.pointer_pb2 import Pointer as Pointer_PB


class Pointer(AbstractPointer):
    # automatically generated subclasses of Pointer need to be able to look up
    # the path and name of the object type they point to as a part of serde
    path_and_name: str

    def __init__(self, location, id_at_location=None, tags=list(), description=""):
        if id_at_location is None:
            id_at_location = UID()

        self.location = location
        self.id_at_location = id_at_location
        self.tags = tags
        self.description = description

    def get(self):
        obj_msg = GetObjectAction(
            obj_id=self.id_at_location,
            address=self.location.address,
            reply_to=self.location.address,
        )
        response = self.location.send_immediate_msg_with_reply(msg=obj_msg)

        return response.obj

    @syft_decorator(typechecking=True)
    def _object2proto(self) -> Pointer_PB:
        """Returns a protobuf serialization of self.

        As a requirement of all objects which inherit from Serializable,
        this method transforms the current object into the corresponding
        Protobuf object so that it can be further serialized.

        :return: returns a protobuf object
        :rtype: Pointer_PB

        .. note::
            This method is purely an internal method. Please use object.serialize() or one of
            the other public serialization methods if you wish to serialize an
            object.
        """
        return Pointer_PB(
            points_to_object_with_path=self.path_and_name,
            pointer_name=type(self).__name__,
            id_at_location=self.id_at_location.serialize(),
            location=self.location.address.serialize(),
            tags=self.tags,
            description=self.description,
        )

    @staticmethod
    def _proto2object(proto: Pointer_PB) -> "Pointer":
        """Creates a Pointer from a protobuf

        As a requirement of all objects which inherit from Serializable,
        this method transforms a protobuf object into an instance of this class.

        :return: returns an instance of Pointer
        :rtype: Pointer

        .. note::
            This method is purely an internal method. Please use syft.deserialize()
            if you wish to deserialize an object.
        """
        # TODO: we need _proto2object to include a reference to the node doing the
        # deserialization so that we can convert location into a client object. At present
        # it is an address object which will cause things to break later.

        points_to_type = sy.lib_ast(
            proto.points_to_object_with_path, return_callable=True
        )
        pointer_type = getattr(points_to_type, proto.pointer_name)
        return pointer_type(
            id_at_location=_deserialize(blob=proto.id_at_location),
            location=_deserialize(blob=proto.location),
            tags=proto.tags,
            description=proto.description,
        )

    @staticmethod
    def get_protobuf_schema() -> GeneratedProtocolMessageType:
        """ Return the type of protobuf object which stores a class of this type

        As a part of serialization and deserialization, we need the ability to
        lookup the protobuf object type directly from the object type. This
        static method allows us to do this.

        Importantly, this method is also used to create the reverse lookup ability within
        the metaclass of Serializable. In the metaclass, it calls this method and then
        it takes whatever type is returned from this method and adds an attribute to it
        with the type of this class attached to it. See the MetaSerializable class for details.

        :return: the type of protobuf object which corresponds to this class.
        :rtype: GeneratedProtocolMessageType

        """

        return Pointer_PB

    def request_access(self, request_name: str = "", reason: str = "",) -> None:
        """Method that requests access to the data on which the pointer points to.

        :param request_name: The title of the request that the data owner is going to see.
        :type request_name: str
        :param reason: The description of the request. This is the reason why you want to have
        access to the data.
        :type reason: str

        .. note::
            This method should be usen when the remote data associated with the pointer wants to be
            downloaded locally (or use .get() on the pointer).
        """
        from ..node.domain.service import RequestMessage

        msg = RequestMessage(
            request_name=request_name,
            request_description=reason,
            address=self.location.address,
            owner_address=self.location.address,
            object_id=self.id_at_location,
            requester_verify_key=self.location.verify_key,
        )

        self.location.send_immediate_msg_without_reply(msg=msg)

    def check_access(self, node: AbstractNode, request_id: UID) -> any:  # type: ignore
        """Method that checks the status of an already made request. There are three possible
        outcomes when requesting access:
            1. RequestStatus.Accepted - your request has been approved, you can not .get() your
            data.
            2. RequestStatus.Pending - your request has not been reviewed yet.
            3. RequestStatus.Rejected - your request has been rejected.

        :param node: The node that queries the request status.
        :type node: AbstractNode
        :param request_id: The request on which you are querying the status.
        :type request_id: UID
        """
        from ..node.domain.service import  RequestAnswerMessage

        msg = RequestAnswerMessage(
            request_id=request_id, address=self.location.address, reply_to=node.address
        )
        response = self.location.send_immediate_msg_with_reply(msg=msg)

        return response.status
