# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: helloworld.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10helloworld.proto\x12\nhelloworld\"\x1c\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1d\n\nHelloReply\x12\x0f\n\x07message\x18\x01 \x01(\t\"\'\n\x11\x45xperimentDetails\x12\x12\n\nproject_id\x18\x02 \x01(\t\".\n\x04\x44\x61ta\x12\x0f\n\x07\x64\x61ta_id\x18\x03 \x01(\t\x12\x15\n\rdata_elements\x18\x04 \x01(\t2\xd1\x01\n\x07Greeter\x12>\n\x08SayHello\x12\x18.helloworld.HelloRequest\x1a\x16.helloworld.HelloReply\"\x00\x12\x43\n\rSayHelloAgain\x12\x18.helloworld.HelloRequest\x1a\x16.helloworld.HelloReply\"\x00\x12\x41\n\x0c\x44\x61taProvider\x12\x1d.helloworld.ExperimentDetails\x1a\x10.helloworld.Data\"\x00\x42\x36\n\x1bio.grpc.examples.helloworldB\x0fHelloWorldProtoP\x01\xa2\x02\x03HLWb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'helloworld_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\033io.grpc.examples.helloworldB\017HelloWorldProtoP\001\242\002\003HLW'
  _HELLOREQUEST._serialized_start=32
  _HELLOREQUEST._serialized_end=60
  _HELLOREPLY._serialized_start=62
  _HELLOREPLY._serialized_end=91
  _EXPERIMENTDETAILS._serialized_start=93
  _EXPERIMENTDETAILS._serialized_end=132
  _DATA._serialized_start=134
  _DATA._serialized_end=180
  _GREETER._serialized_start=183
  _GREETER._serialized_end=392
# @@protoc_insertion_point(module_scope)
