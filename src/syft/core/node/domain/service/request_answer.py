from typing import List

from ..... import serialize, deserialize
from ....common import UID
from .....proto.core.node.domain.service.request_message_pb2 import (
    RequestMessage as RequestMessage_PB,
)
from ....io.address import Address
from ....common.message import ImmediateSyftMessageWithoutReply
from ...common.service.node_service import ImmediateNodeServiceWithoutReply
from ..domain import Domain
from .....decorators import syft_decorator
from .request_answer_response import RequestAnswerResponse, RequestStatus


class RequestMessage(ImmediateSyftMessageWithoutReply):

    __slots__ = ["request_name", "request_description", "request_id"]

    def __init__(
        self,
        object_id: UID,
        address: Address,
        owner_address,
        request_name: str = "",
        request_description: str = "",
    ):
        super().__init__(address)
        self.request_name = request_name
        self.request_description = request_description
        self.request_id = UID()
        self.object_id = object_id
        self.owner_address = owner_address

    @syft_decorator(typechecking=True)
    def _object2proto(self) -> RequestMessage_PB:
        msg = RequestMessage_PB()
        msg.request_name = self.request_name
        msg.request_description = self.request_description
        msg.request_id.CopyFrom(serialize(obj=self.request_id))
        msg.target_address.CopyFrom(serialize(self.address))
        msg.object_id.CopyFrom(serialize(self.object_id))
        msg.owner_address.CopyFrom(serialize(self.owner_address))
        return msg

    @staticmethod
    @syft_decorator(typechecking=True)
    def _proto2object(proto: RequestMessage_PB) -> "RequestMessage":
        request_msg = RequestMessage(
            request_name=proto.request_name,
            request_description=proto.request_description,
            target_address=deserialize(proto.address),
            object_id=deserialize(proto.owner_address),
            owner_address=deserialize(proto.owner_address),
        )
        request_msg.request_id = deserialize(blob=proto.request_id)
        return request_msg

    @staticmethod
    @syft_decorator(typechecking=True)
    def get_protobuf_schema() -> type:
        return RequestMessage_PB


class RequestService(ImmediateNodeServiceWithoutReply):
    @staticmethod
    @syft_decorator(typechecking=True)
    def message_handler_types() -> List[type]:
        return [RequestMessage]

    @staticmethod
    @syft_decorator(typechecking=True)
    def process(node: Domain, msg: RequestMessage) -> None:
        node.requests[msg.request_id] = {
            "message": msg,
            "status": RequestStatus.Pending,
        }
