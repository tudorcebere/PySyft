"""
This file exists to provide a common place for all Protobuf
serialisation for native Python objects. If you're adding
something here that isn't for `None`, think twice and either
use an existing sub-class of Message or add a new one.
"""

import syft
from collections import OrderedDict
from google.protobuf.empty_pb2 import Empty
from syft.workers.abstract import AbstractWorker
from syft_proto.execution.v1.type_wrapper_pb2 import ClassType as ClassTypePB

def _bufferize_none(worker: AbstractWorker, obj: "type(None)") -> "Empty":
    """
    This function converts None into an empty Protobuf message.

    Args:
        obj (None): makes signature match other bufferize methods

    Returns:
        protobuf_obj: Empty Protobuf message
    """
    return Empty()


def _unbufferize_none(worker: AbstractWorker, obj: "Empty") -> "type(None)":
    """
    This function converts an empty Protobuf message back into None.

    Args:
        obj (Empty): Empty Protobuf message

    Returns:
        obj: None
    """
    return None

def _bufferize_type(worker: AbstractWorker, obj) -> ClassTypePB:
    proto_type = ClassTypePB()

    if isinstance(obj, type):
        serialized_type = syft.serde.msgpack.serde._simplify(worker, obj)
        proto_type.id = serialized_type[0]
        proto_type.type = serialized_type[1]

    return proto_type

def _unbufferize_type(worker: AbstractWorker, obj: ClassTypePB):
    if obj.type:
        original_type = syft.serde.msgpack.serde._detail(worker, (obj.id, obj.type))
        return original_type

    return object

# Maps a type to its bufferizer and unbufferizer functions
MAP_NATIVE_PROTOBUF_TRANSLATORS = OrderedDict(
    {
        type(None): (_bufferize_none, _unbufferize_none),
        type: (_bufferize_type, _unbufferize_type)

    }
)
