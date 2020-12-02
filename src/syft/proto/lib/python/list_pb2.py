# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/lib/python/list.proto

# stdlib
import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
# third party
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


# syft absolute
from syft.proto.core.common import (
    common_object_pb2 as proto_dot_core_dot_common_dot_common__object__pb2,
)
from syft.proto.core.store import (
    store_object_pb2 as proto_dot_core_dot_store_dot_store__object__pb2,
)

DESCRIPTOR = _descriptor.FileDescriptor(
    name="proto/lib/python/list.proto",
    package="syft.lib.python",
    syntax="proto3",
    serialized_options=None,
    serialized_pb=_b(
        '\n\x1bproto/lib/python/list.proto\x12\x0fsyft.lib.python\x1a%proto/core/common/common_object.proto\x1a#proto/core/store/store_object.proto"X\n\x04List\x12-\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x1f.syft.core.store.StorableObject\x12!\n\x02id\x18\x02 \x01(\x0b\x32\x15.syft.core.common.UIDb\x06proto3'
    ),
    dependencies=[
        proto_dot_core_dot_common_dot_common__object__pb2.DESCRIPTOR,
        proto_dot_core_dot_store_dot_store__object__pb2.DESCRIPTOR,
    ],
)


_LIST = _descriptor.Descriptor(
    name="List",
    full_name="syft.lib.python.List",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="data",
            full_name="syft.lib.python.List.data",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="id",
            full_name="syft.lib.python.List.id",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=124,
    serialized_end=212,
)

_LIST.fields_by_name[
    "data"
].message_type = proto_dot_core_dot_store_dot_store__object__pb2._STORABLEOBJECT
_LIST.fields_by_name[
    "id"
].message_type = proto_dot_core_dot_common_dot_common__object__pb2._UID
DESCRIPTOR.message_types_by_name["List"] = _LIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

List = _reflection.GeneratedProtocolMessageType(
    "List",
    (_message.Message,),
    dict(
        DESCRIPTOR=_LIST,
        __module__="proto.lib.python.list_pb2"
        # @@protoc_insertion_point(class_scope:syft.lib.python.List)
    ),
)
_sym_db.RegisterMessage(List)


# @@protoc_insertion_point(module_scope)
