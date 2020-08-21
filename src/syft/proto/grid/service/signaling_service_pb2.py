# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/grid/service/signaling_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from syft.proto.core.common import (
    common_object_pb2 as proto_dot_core_dot_common_dot_common__object__pb2,
)
from syft.proto.core.io import address_pb2 as proto_dot_core_dot_io_dot_address__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="proto/grid/service/signaling_service.proto",
    package="syft.grid.service",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n*proto/grid/service/signaling_service.proto\x12\x11syft.grid.service\x1a%proto/core/common/common_object.proto\x1a\x1bproto/core/io/address.proto"x\n\x16SignalingAnswerMessage\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12\x0f\n\x07payload\x18\x04 \x01(\t"w\n\x15SignalingOfferMessage\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12\x0f\n\x07payload\x18\x04 \x01(\tb\x06proto3',
    dependencies=[
        proto_dot_core_dot_common_dot_common__object__pb2.DESCRIPTOR,
        proto_dot_core_dot_io_dot_address__pb2.DESCRIPTOR,
    ],
)


_SIGNALINGANSWERMESSAGE = _descriptor.Descriptor(
    name="SignalingAnswerMessage",
    full_name="syft.grid.service.SignalingAnswerMessage",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="msg_id",
            full_name="syft.grid.service.SignalingAnswerMessage.msg_id",
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
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="address",
            full_name="syft.grid.service.SignalingAnswerMessage.address",
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
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="payload",
            full_name="syft.grid.service.SignalingAnswerMessage.payload",
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
            create_key=_descriptor._internal_create_key,
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
    serialized_start=133,
    serialized_end=253,
)


_SIGNALINGOFFERMESSAGE = _descriptor.Descriptor(
    name="SignalingOfferMessage",
    full_name="syft.grid.service.SignalingOfferMessage",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="msg_id",
            full_name="syft.grid.service.SignalingOfferMessage.msg_id",
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
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="address",
            full_name="syft.grid.service.SignalingOfferMessage.address",
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
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="payload",
            full_name="syft.grid.service.SignalingOfferMessage.payload",
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
            create_key=_descriptor._internal_create_key,
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
    serialized_start=255,
    serialized_end=374,
)

_SIGNALINGANSWERMESSAGE.fields_by_name[
    "msg_id"
].message_type = proto_dot_core_dot_common_dot_common__object__pb2._UID
_SIGNALINGANSWERMESSAGE.fields_by_name[
    "address"
].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
_SIGNALINGOFFERMESSAGE.fields_by_name[
    "msg_id"
].message_type = proto_dot_core_dot_common_dot_common__object__pb2._UID
_SIGNALINGOFFERMESSAGE.fields_by_name[
    "address"
].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
DESCRIPTOR.message_types_by_name["SignalingAnswerMessage"] = _SIGNALINGANSWERMESSAGE
DESCRIPTOR.message_types_by_name["SignalingOfferMessage"] = _SIGNALINGOFFERMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SignalingAnswerMessage = _reflection.GeneratedProtocolMessageType(
    "SignalingAnswerMessage",
    (_message.Message,),
    {
        "DESCRIPTOR": _SIGNALINGANSWERMESSAGE,
        "__module__": "proto.grid.service.signaling_service_pb2"
        # @@protoc_insertion_point(class_scope:syft.grid.service.SignalingAnswerMessage)
    },
)
_sym_db.RegisterMessage(SignalingAnswerMessage)

SignalingOfferMessage = _reflection.GeneratedProtocolMessageType(
    "SignalingOfferMessage",
    (_message.Message,),
    {
        "DESCRIPTOR": _SIGNALINGOFFERMESSAGE,
        "__module__": "proto.grid.service.signaling_service_pb2"
        # @@protoc_insertion_point(class_scope:syft.grid.service.SignalingOfferMessage)
    },
)
_sym_db.RegisterMessage(SignalingOfferMessage)


# @@protoc_insertion_point(module_scope)
