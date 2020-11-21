# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/core/io/connection.proto

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
from syft.proto.core.io import address_pb2 as proto_dot_core_dot_io_dot_address__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name="proto/core/io/connection.proto",
    package="syft.core.io",
    syntax="proto3",
    serialized_options=None,
    serialized_pb=_b(
        '\n\x1eproto/core/io/connection.proto\x12\x0csyft.core.io\x1a\x1bproto/core/io/address.proto">\n\x17VirtualServerConnection\x12#\n\x04node\x18\x01 \x01(\x0b\x32\x15.syft.core.io.Address"P\n\x17VirtualClientConnection\x12\x35\n\x06server\x18\x01 \x01(\x0b\x32%.syft.core.io.VirtualServerConnectionb\x06proto3'
    ),
    dependencies=[
        proto_dot_core_dot_io_dot_address__pb2.DESCRIPTOR,
    ],
)


_VIRTUALSERVERCONNECTION = _descriptor.Descriptor(
    name="VirtualServerConnection",
    full_name="syft.core.io.VirtualServerConnection",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="node",
            full_name="syft.core.io.VirtualServerConnection.node",
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=77,
    serialized_end=139,
)


_VIRTUALCLIENTCONNECTION = _descriptor.Descriptor(
    name="VirtualClientConnection",
    full_name="syft.core.io.VirtualClientConnection",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="server",
            full_name="syft.core.io.VirtualClientConnection.server",
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=141,
    serialized_end=221,
)

_VIRTUALSERVERCONNECTION.fields_by_name[
    "node"
].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
_VIRTUALCLIENTCONNECTION.fields_by_name[
    "server"
].message_type = _VIRTUALSERVERCONNECTION
DESCRIPTOR.message_types_by_name["VirtualServerConnection"] = _VIRTUALSERVERCONNECTION
DESCRIPTOR.message_types_by_name["VirtualClientConnection"] = _VIRTUALCLIENTCONNECTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VirtualServerConnection = _reflection.GeneratedProtocolMessageType(
    "VirtualServerConnection",
    (_message.Message,),
    dict(
        DESCRIPTOR=_VIRTUALSERVERCONNECTION,
        __module__="proto.core.io.connection_pb2"
        # @@protoc_insertion_point(class_scope:syft.core.io.VirtualServerConnection)
    ),
)
_sym_db.RegisterMessage(VirtualServerConnection)

VirtualClientConnection = _reflection.GeneratedProtocolMessageType(
    "VirtualClientConnection",
    (_message.Message,),
    dict(
        DESCRIPTOR=_VIRTUALCLIENTCONNECTION,
        __module__="proto.core.io.connection_pb2"
        # @@protoc_insertion_point(class_scope:syft.core.io.VirtualClientConnection)
    ),
)
_sym_db.RegisterMessage(VirtualClientConnection)


# @@protoc_insertion_point(module_scope)
