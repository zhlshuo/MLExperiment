# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protoc/loader.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13protoc/loader.proto\"\"\n\x12ImageLoaderRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\")\n\x13ImageLoaderResponse\x12\x12\n\nisFinished\x18\x01 \x01(\x08\x32\x42\n\x0bImageLoader\x12\x33\n\x04load\x12\x13.ImageLoaderRequest\x1a\x14.ImageLoaderResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protoc.loader_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_IMAGELOADERREQUEST']._serialized_start=23
  _globals['_IMAGELOADERREQUEST']._serialized_end=57
  _globals['_IMAGELOADERRESPONSE']._serialized_start=59
  _globals['_IMAGELOADERRESPONSE']._serialized_end=100
  _globals['_IMAGELOADER']._serialized_start=102
  _globals['_IMAGELOADER']._serialized_end=168
# @@protoc_insertion_point(module_scope)
