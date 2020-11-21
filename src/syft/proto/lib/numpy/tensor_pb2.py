# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/lib/numpy/tensor.proto

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


DESCRIPTOR = _descriptor.FileDescriptor(
    name="proto/lib/numpy/tensor.proto",
    package="syft.lib.numpy",
    syntax="proto3",
    serialized_options=None,
    serialized_pb=_b(
        '\n\x1cproto/lib/numpy/tensor.proto\x12\x0esyft.lib.numpy";\n\x0cTensorProtos\x12+\n\x06protos\x18\x01 \x03(\x0b\x32\x1b.syft.lib.numpy.TensorProto"\xef\x02\n\x0bTensorProto\x12\x0c\n\x04\x64ims\x18\x01 \x03(\x03\x12\x37\n\tdata_type\x18\x02 \x01(\x0e\x32$.syft.lib.numpy.TensorProto.DataType\x12\x12\n\nfloat_data\x18\x03 \x03(\x02\x12\x12\n\nint32_data\x18\x04 \x03(\x05\x12\x11\n\tbyte_data\x18\x05 \x01(\x0c\x12\x13\n\x0bstring_data\x18\x06 \x03(\x0c\x12\x13\n\x0b\x64ouble_data\x18\x07 \x03(\x01\x12\x12\n\nint64_data\x18\x08 \x03(\x03"\x9f\x01\n\x08\x44\x61taType\x12\r\n\tUNDEFINED\x10\x00\x12\t\n\x05\x46LOAT\x10\x01\x12\t\n\x05INT32\x10\x02\x12\x08\n\x04\x42YTE\x10\x03\x12\n\n\x06STRING\x10\x04\x12\x08\n\x04\x42OOL\x10\x05\x12\t\n\x05UINT8\x10\x06\x12\x08\n\x04INT8\x10\x07\x12\n\n\x06UINT16\x10\x08\x12\t\n\x05INT16\x10\t\x12\t\n\x05INT64\x10\n\x12\x0b\n\x07\x46LOAT16\x10\x0c\x12\n\n\x06\x44OUBLE\x10\rb\x06proto3'
    ),
)


_TENSORPROTO_DATATYPE = _descriptor.EnumDescriptor(
    name="DataType",
    full_name="syft.lib.numpy.TensorProto.DataType",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="UNDEFINED", index=0, number=0, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="FLOAT", index=1, number=1, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="INT32", index=2, number=2, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="BYTE", index=3, number=3, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="STRING", index=4, number=4, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="BOOL", index=5, number=5, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="UINT8", index=6, number=6, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="INT8", index=7, number=7, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="UINT16", index=8, number=8, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="INT16", index=9, number=9, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="INT64", index=10, number=10, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="FLOAT16", index=11, number=12, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="DOUBLE", index=12, number=13, serialized_options=None, type=None
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=318,
    serialized_end=477,
)
_sym_db.RegisterEnumDescriptor(_TENSORPROTO_DATATYPE)


_TENSORPROTOS = _descriptor.Descriptor(
    name="TensorProtos",
    full_name="syft.lib.numpy.TensorProtos",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="protos",
            full_name="syft.lib.numpy.TensorProtos.protos",
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=48,
    serialized_end=107,
)


_TENSORPROTO = _descriptor.Descriptor(
    name="TensorProto",
    full_name="syft.lib.numpy.TensorProto",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="dims",
            full_name="syft.lib.numpy.TensorProto.dims",
            index=0,
            number=1,
            type=3,
            cpp_type=2,
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
            name="data_type",
            full_name="syft.lib.numpy.TensorProto.data_type",
            index=1,
            number=2,
            type=14,
            cpp_type=8,
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
            name="float_data",
            full_name="syft.lib.numpy.TensorProto.float_data",
            index=2,
            number=3,
            type=2,
            cpp_type=6,
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
            name="int32_data",
            full_name="syft.lib.numpy.TensorProto.int32_data",
            index=3,
            number=4,
            type=5,
            cpp_type=1,
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
            name="byte_data",
            full_name="syft.lib.numpy.TensorProto.byte_data",
            index=4,
            number=5,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b(""),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="string_data",
            full_name="syft.lib.numpy.TensorProto.string_data",
            index=5,
            number=6,
            type=12,
            cpp_type=9,
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
            name="double_data",
            full_name="syft.lib.numpy.TensorProto.double_data",
            index=6,
            number=7,
            type=1,
            cpp_type=5,
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
            name="int64_data",
            full_name="syft.lib.numpy.TensorProto.int64_data",
            index=7,
            number=8,
            type=3,
            cpp_type=2,
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[
        _TENSORPROTO_DATATYPE,
    ],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=110,
    serialized_end=477,
)

_TENSORPROTOS.fields_by_name["protos"].message_type = _TENSORPROTO
_TENSORPROTO.fields_by_name["data_type"].enum_type = _TENSORPROTO_DATATYPE
_TENSORPROTO_DATATYPE.containing_type = _TENSORPROTO
DESCRIPTOR.message_types_by_name["TensorProtos"] = _TENSORPROTOS
DESCRIPTOR.message_types_by_name["TensorProto"] = _TENSORPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TensorProtos = _reflection.GeneratedProtocolMessageType(
    "TensorProtos",
    (_message.Message,),
    dict(
        DESCRIPTOR=_TENSORPROTOS,
        __module__="proto.lib.numpy.tensor_pb2"
        # @@protoc_insertion_point(class_scope:syft.lib.numpy.TensorProtos)
    ),
)
_sym_db.RegisterMessage(TensorProtos)

TensorProto = _reflection.GeneratedProtocolMessageType(
    "TensorProto",
    (_message.Message,),
    dict(
        DESCRIPTOR=_TENSORPROTO,
        __module__="proto.lib.numpy.tensor_pb2"
        # @@protoc_insertion_point(class_scope:syft.lib.numpy.TensorProto)
    ),
)
_sym_db.RegisterMessage(TensorProto)


# @@protoc_insertion_point(module_scope)
