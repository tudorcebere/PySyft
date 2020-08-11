# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/grid/duet/request.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from syft.proto.core.common import (
    common_object_pb2 as proto_dot_core_dot_common_dot_common__object__pb2,
)


DESCRIPTOR = _descriptor.FileDescriptor(
    name="proto/grid/duet/request.proto",
    package="syft.grid.duet",
    syntax="proto3",
    serialized_options=None,
    serialized_pb=b'\n\x1dproto/grid/duet/request.proto\x12\x0esyft.grid.duet\x1a%proto/core/common/common_object.proto"n\n\x0eRequestMessage\x12)\n\nrequest_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12\x14\n\x0crequest_name\x18\x03 \x01(\t\x12\x1b\n\x13request_description\x18\x04 \x01(\t"L\n\x0fRequestResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12)\n\nrequest_id\x18\x02 \x01(\x0b\x32\x15.syft.core.common.UIDb\x06proto3',
    dependencies=[proto_dot_core_dot_common_dot_common__object__pb2.DESCRIPTOR,],
)


_REQUESTMESSAGE = _descriptor.Descriptor(
    name="RequestMessage",
    full_name="syft.grid.duet.RequestMessage",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="request_id",
            full_name="syft.grid.duet.RequestMessage.request_id",
            index=0,
            number=1,
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
        _descriptor.FieldDescriptor(
            name="request_name",
            full_name="syft.grid.duet.RequestMessage.request_name",
            index=1,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="request_description",
            full_name="syft.grid.duet.RequestMessage.request_description",
            index=2,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
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
    serialized_start=88,
    serialized_end=198,
)


_REQUESTRESPONSE = _descriptor.Descriptor(
    name="RequestResponse",
    full_name="syft.grid.duet.RequestResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="status",
            full_name="syft.grid.duet.RequestResponse.status",
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="request_id",
            full_name="syft.grid.duet.RequestResponse.request_id",
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
    serialized_start=200,
    serialized_end=276,
)

_REQUESTMESSAGE.fields_by_name[
    "request_id"
].message_type = proto_dot_core_dot_common_dot_common__object__pb2._UID
_REQUESTRESPONSE.fields_by_name[
    "request_id"
].message_type = proto_dot_core_dot_common_dot_common__object__pb2._UID
DESCRIPTOR.message_types_by_name["RequestMessage"] = _REQUESTMESSAGE
DESCRIPTOR.message_types_by_name["RequestResponse"] = _REQUESTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RequestMessage = _reflection.GeneratedProtocolMessageType(
    "RequestMessage",
    (_message.Message,),
    {
        "DESCRIPTOR": _REQUESTMESSAGE,
        "__module__": "proto.grid.duet.request_pb2"
        # @@protoc_insertion_point(class_scope:syft.grid.duet.RequestMessage)
    },
)
_sym_db.RegisterMessage(RequestMessage)

RequestResponse = _reflection.GeneratedProtocolMessageType(
    "RequestResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _REQUESTRESPONSE,
        "__module__": "proto.grid.duet.request_pb2"
        # @@protoc_insertion_point(class_scope:syft.grid.duet.RequestResponse)
    },
)
_sym_db.RegisterMessage(RequestResponse)


# @@protoc_insertion_point(module_scope)
