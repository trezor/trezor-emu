# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import trezor_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='wallet.proto',
  package='',
  serialized_pb='\n\x0cwallet.proto\x1a\x0ctrezor.proto\"#\n\x06Wallet\x12\x0c\n\x04seed\x18\x01 \x02(\x0c\x12\x0b\n\x03pin\x18\x02 \x01(\x0c')




_WALLET = descriptor.Descriptor(
  name='Wallet',
  full_name='Wallet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='seed', full_name='Wallet.seed', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='pin', full_name='Wallet.pin', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=30,
  serialized_end=65,
)

DESCRIPTOR.message_types_by_name['Wallet'] = _WALLET

class Wallet(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _WALLET
  
  # @@protoc_insertion_point(class_scope:Wallet)

# @@protoc_insertion_point(module_scope)
