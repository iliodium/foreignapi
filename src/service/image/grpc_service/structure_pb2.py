# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grpc_service/structure.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cgrpc_service/structure.proto\"\x16\n\x05\x43heck\x12\r\n\x05\x63heck\x18\x01 \x01(\x0c\"\x1a\n\x08Response\x12\x0e\n\x06\x61nswer\x18\x01 \x01(\t20\n\x0c\x43heckService\x12 \n\tSendCheck\x12\x06.Check\x1a\t.Response\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'grpc_service.structure_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_CHECK']._serialized_start=32
  _globals['_CHECK']._serialized_end=54
  _globals['_RESPONSE']._serialized_start=56
  _globals['_RESPONSE']._serialized_end=82
  _globals['_CHECKSERVICE']._serialized_start=84
  _globals['_CHECKSERVICE']._serialized_end=132
# @@protoc_insertion_point(module_scope)
