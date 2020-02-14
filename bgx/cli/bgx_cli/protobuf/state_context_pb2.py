# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bgx_cli/protobuf/state_context.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bgx_cli.protobuf import events_pb2 as bgx__cli_dot_protobuf_dot_events__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='bgx_cli/protobuf/state_context.proto',
  package='',
  syntax='proto3',
  serialized_options=_b('\n\025sawtooth.sdk.protobufP\001Z\021state_context_pb2'),
  serialized_pb=_b('\n$bgx_cli/protobuf/state_context.proto\x1a\x1d\x62gx_cli/protobuf/events.proto\"-\n\x0cTpStateEntry\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\":\n\x11TpStateGetRequest\x12\x12\n\ncontext_id\x18\x01 \x01(\t\x12\x11\n\taddresses\x18\x02 \x03(\t\"\x9d\x01\n\x12TpStateGetResponse\x12\x1e\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\r.TpStateEntry\x12*\n\x06status\x18\x02 \x01(\x0e\x32\x1a.TpStateGetResponse.Status\";\n\x06Status\x12\x10\n\x0cSTATUS_UNSET\x10\x00\x12\x06\n\x02OK\x10\x01\x12\x17\n\x13\x41UTHORIZATION_ERROR\x10\x02\"G\n\x11TpStateSetRequest\x12\x12\n\ncontext_id\x18\x01 \x01(\t\x12\x1e\n\x07\x65ntries\x18\x02 \x03(\x0b\x32\r.TpStateEntry\"\x90\x01\n\x12TpStateSetResponse\x12\x11\n\taddresses\x18\x01 \x03(\t\x12*\n\x06status\x18\x02 \x01(\x0e\x32\x1a.TpStateSetResponse.Status\";\n\x06Status\x12\x10\n\x0cSTATUS_UNSET\x10\x00\x12\x06\n\x02OK\x10\x01\x12\x17\n\x13\x41UTHORIZATION_ERROR\x10\x02\"=\n\x14TpStateDeleteRequest\x12\x12\n\ncontext_id\x18\x01 \x01(\t\x12\x11\n\taddresses\x18\x02 \x03(\t\"\x96\x01\n\x15TpStateDeleteResponse\x12\x11\n\taddresses\x18\x01 \x03(\t\x12-\n\x06status\x18\x02 \x01(\x0e\x32\x1d.TpStateDeleteResponse.Status\";\n\x06Status\x12\x10\n\x0cSTATUS_UNSET\x10\x00\x12\x06\n\x02OK\x10\x01\x12\x17\n\x13\x41UTHORIZATION_ERROR\x10\x02\";\n\x17TpReceiptAddDataRequest\x12\x12\n\ncontext_id\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\"{\n\x18TpReceiptAddDataResponse\x12\x30\n\x06status\x18\x02 \x01(\x0e\x32 .TpReceiptAddDataResponse.Status\"-\n\x06Status\x12\x10\n\x0cSTATUS_UNSET\x10\x00\x12\x06\n\x02OK\x10\x01\x12\t\n\x05\x45RROR\x10\x02\">\n\x11TpEventAddRequest\x12\x12\n\ncontext_id\x18\x01 \x01(\t\x12\x15\n\x05\x65vent\x18\x02 \x01(\x0b\x32\x06.Event\"o\n\x12TpEventAddResponse\x12*\n\x06status\x18\x02 \x01(\x0e\x32\x1a.TpEventAddResponse.Status\"-\n\x06Status\x12\x10\n\x0cSTATUS_UNSET\x10\x00\x12\x06\n\x02OK\x10\x01\x12\t\n\x05\x45RROR\x10\x02\x42,\n\x15sawtooth.sdk.protobufP\x01Z\x11state_context_pb2b\x06proto3')
  ,
  dependencies=[bgx__cli_dot_protobuf_dot_events__pb2.DESCRIPTOR,])



_TPSTATEGETRESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='TpStateGetResponse.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATUS_UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OK', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTHORIZATION_ERROR', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=277,
  serialized_end=336,
)
_sym_db.RegisterEnumDescriptor(_TPSTATEGETRESPONSE_STATUS)

_TPSTATESETRESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='TpStateSetResponse.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATUS_UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OK', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTHORIZATION_ERROR', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=277,
  serialized_end=336,
)
_sym_db.RegisterEnumDescriptor(_TPSTATESETRESPONSE_STATUS)

_TPSTATEDELETERESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='TpStateDeleteResponse.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATUS_UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OK', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTHORIZATION_ERROR', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=277,
  serialized_end=336,
)
_sym_db.RegisterEnumDescriptor(_TPSTATEDELETERESPONSE_STATUS)

_TPRECEIPTADDDATARESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='TpReceiptAddDataResponse.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATUS_UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OK', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=913,
  serialized_end=958,
)
_sym_db.RegisterEnumDescriptor(_TPRECEIPTADDDATARESPONSE_STATUS)

_TPEVENTADDRESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='TpEventAddResponse.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATUS_UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OK', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=913,
  serialized_end=958,
)
_sym_db.RegisterEnumDescriptor(_TPEVENTADDRESPONSE_STATUS)


_TPSTATEENTRY = _descriptor.Descriptor(
  name='TpStateEntry',
  full_name='TpStateEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='TpStateEntry.address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='TpStateEntry.data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=71,
  serialized_end=116,
)


_TPSTATEGETREQUEST = _descriptor.Descriptor(
  name='TpStateGetRequest',
  full_name='TpStateGetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='context_id', full_name='TpStateGetRequest.context_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='addresses', full_name='TpStateGetRequest.addresses', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=118,
  serialized_end=176,
)


_TPSTATEGETRESPONSE = _descriptor.Descriptor(
  name='TpStateGetResponse',
  full_name='TpStateGetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entries', full_name='TpStateGetResponse.entries', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='TpStateGetResponse.status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TPSTATEGETRESPONSE_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=179,
  serialized_end=336,
)


_TPSTATESETREQUEST = _descriptor.Descriptor(
  name='TpStateSetRequest',
  full_name='TpStateSetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='context_id', full_name='TpStateSetRequest.context_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='entries', full_name='TpStateSetRequest.entries', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=338,
  serialized_end=409,
)


_TPSTATESETRESPONSE = _descriptor.Descriptor(
  name='TpStateSetResponse',
  full_name='TpStateSetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='addresses', full_name='TpStateSetResponse.addresses', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='TpStateSetResponse.status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TPSTATESETRESPONSE_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=412,
  serialized_end=556,
)


_TPSTATEDELETEREQUEST = _descriptor.Descriptor(
  name='TpStateDeleteRequest',
  full_name='TpStateDeleteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='context_id', full_name='TpStateDeleteRequest.context_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='addresses', full_name='TpStateDeleteRequest.addresses', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=558,
  serialized_end=619,
)


_TPSTATEDELETERESPONSE = _descriptor.Descriptor(
  name='TpStateDeleteResponse',
  full_name='TpStateDeleteResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='addresses', full_name='TpStateDeleteResponse.addresses', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='TpStateDeleteResponse.status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TPSTATEDELETERESPONSE_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=622,
  serialized_end=772,
)


_TPRECEIPTADDDATAREQUEST = _descriptor.Descriptor(
  name='TpReceiptAddDataRequest',
  full_name='TpReceiptAddDataRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='context_id', full_name='TpReceiptAddDataRequest.context_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='TpReceiptAddDataRequest.data', index=1,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=774,
  serialized_end=833,
)


_TPRECEIPTADDDATARESPONSE = _descriptor.Descriptor(
  name='TpReceiptAddDataResponse',
  full_name='TpReceiptAddDataResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='TpReceiptAddDataResponse.status', index=0,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TPRECEIPTADDDATARESPONSE_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=835,
  serialized_end=958,
)


_TPEVENTADDREQUEST = _descriptor.Descriptor(
  name='TpEventAddRequest',
  full_name='TpEventAddRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='context_id', full_name='TpEventAddRequest.context_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='event', full_name='TpEventAddRequest.event', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=960,
  serialized_end=1022,
)


_TPEVENTADDRESPONSE = _descriptor.Descriptor(
  name='TpEventAddResponse',
  full_name='TpEventAddResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='TpEventAddResponse.status', index=0,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TPEVENTADDRESPONSE_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1024,
  serialized_end=1135,
)

_TPSTATEGETRESPONSE.fields_by_name['entries'].message_type = _TPSTATEENTRY
_TPSTATEGETRESPONSE.fields_by_name['status'].enum_type = _TPSTATEGETRESPONSE_STATUS
_TPSTATEGETRESPONSE_STATUS.containing_type = _TPSTATEGETRESPONSE
_TPSTATESETREQUEST.fields_by_name['entries'].message_type = _TPSTATEENTRY
_TPSTATESETRESPONSE.fields_by_name['status'].enum_type = _TPSTATESETRESPONSE_STATUS
_TPSTATESETRESPONSE_STATUS.containing_type = _TPSTATESETRESPONSE
_TPSTATEDELETERESPONSE.fields_by_name['status'].enum_type = _TPSTATEDELETERESPONSE_STATUS
_TPSTATEDELETERESPONSE_STATUS.containing_type = _TPSTATEDELETERESPONSE
_TPRECEIPTADDDATARESPONSE.fields_by_name['status'].enum_type = _TPRECEIPTADDDATARESPONSE_STATUS
_TPRECEIPTADDDATARESPONSE_STATUS.containing_type = _TPRECEIPTADDDATARESPONSE
_TPEVENTADDREQUEST.fields_by_name['event'].message_type = bgx__cli_dot_protobuf_dot_events__pb2._EVENT
_TPEVENTADDRESPONSE.fields_by_name['status'].enum_type = _TPEVENTADDRESPONSE_STATUS
_TPEVENTADDRESPONSE_STATUS.containing_type = _TPEVENTADDRESPONSE
DESCRIPTOR.message_types_by_name['TpStateEntry'] = _TPSTATEENTRY
DESCRIPTOR.message_types_by_name['TpStateGetRequest'] = _TPSTATEGETREQUEST
DESCRIPTOR.message_types_by_name['TpStateGetResponse'] = _TPSTATEGETRESPONSE
DESCRIPTOR.message_types_by_name['TpStateSetRequest'] = _TPSTATESETREQUEST
DESCRIPTOR.message_types_by_name['TpStateSetResponse'] = _TPSTATESETRESPONSE
DESCRIPTOR.message_types_by_name['TpStateDeleteRequest'] = _TPSTATEDELETEREQUEST
DESCRIPTOR.message_types_by_name['TpStateDeleteResponse'] = _TPSTATEDELETERESPONSE
DESCRIPTOR.message_types_by_name['TpReceiptAddDataRequest'] = _TPRECEIPTADDDATAREQUEST
DESCRIPTOR.message_types_by_name['TpReceiptAddDataResponse'] = _TPRECEIPTADDDATARESPONSE
DESCRIPTOR.message_types_by_name['TpEventAddRequest'] = _TPEVENTADDREQUEST
DESCRIPTOR.message_types_by_name['TpEventAddResponse'] = _TPEVENTADDRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TpStateEntry = _reflection.GeneratedProtocolMessageType('TpStateEntry', (_message.Message,), dict(
  DESCRIPTOR = _TPSTATEENTRY,
  __module__ = 'bgx_cli.protobuf.state_context_pb2'
  # @@protoc_insertion_point(class_scope:TpStateEntry)
  ))
_sym_db.RegisterMessage(TpStateEntry)

TpStateGetRequest = _reflection.GeneratedProtocolMessageType('TpStateGetRequest', (_message.Message,), dict(
  DESCRIPTOR = _TPSTATEGETREQUEST,
  __module__ = 'bgx_cli.protobuf.state_context_pb2'
  # @@protoc_insertion_point(class_scope:TpStateGetRequest)
  ))
_sym_db.RegisterMessage(TpStateGetRequest)

TpStateGetResponse = _reflection.GeneratedProtocolMessageType('TpStateGetResponse', (_message.Message,), dict(
  DESCRIPTOR = _TPSTATEGETRESPONSE,
  __module__ = 'bgx_cli.protobuf.state_context_pb2'
  # @@protoc_insertion_point(class_scope:TpStateGetResponse)
  ))
_sym_db.RegisterMessage(TpStateGetResponse)

TpStateSetRequest = _reflection.GeneratedProtocolMessageType('TpStateSetRequest', (_message.Message,), dict(
  DESCRIPTOR = _TPSTATESETREQUEST,
  __module__ = 'bgx_cli.protobuf.state_context_pb2'
  # @@protoc_insertion_point(class_scope:TpStateSetRequest)
  ))
_sym_db.RegisterMessage(TpStateSetRequest)

TpStateSetResponse = _reflection.GeneratedProtocolMessageType('TpStateSetResponse', (_message.Message,), dict(
  DESCRIPTOR = _TPSTATESETRESPONSE,
  __module__ = 'bgx_cli.protobuf.state_context_pb2'
  # @@protoc_insertion_point(class_scope:TpStateSetResponse)
  ))
_sym_db.RegisterMessage(TpStateSetResponse)

TpStateDeleteRequest = _reflection.GeneratedProtocolMessageType('TpStateDeleteRequest', (_message.Message,), dict(
  DESCRIPTOR = _TPSTATEDELETEREQUEST,
  __module__ = 'bgx_cli.protobuf.state_context_pb2'
  # @@protoc_insertion_point(class_scope:TpStateDeleteRequest)
  ))
_sym_db.RegisterMessage(TpStateDeleteRequest)

TpStateDeleteResponse = _reflection.GeneratedProtocolMessageType('TpStateDeleteResponse', (_message.Message,), dict(
  DESCRIPTOR = _TPSTATEDELETERESPONSE,
  __module__ = 'bgx_cli.protobuf.state_context_pb2'
  # @@protoc_insertion_point(class_scope:TpStateDeleteResponse)
  ))
_sym_db.RegisterMessage(TpStateDeleteResponse)

TpReceiptAddDataRequest = _reflection.GeneratedProtocolMessageType('TpReceiptAddDataRequest', (_message.Message,), dict(
  DESCRIPTOR = _TPRECEIPTADDDATAREQUEST,
  __module__ = 'bgx_cli.protobuf.state_context_pb2'
  # @@protoc_insertion_point(class_scope:TpReceiptAddDataRequest)
  ))
_sym_db.RegisterMessage(TpReceiptAddDataRequest)

TpReceiptAddDataResponse = _reflection.GeneratedProtocolMessageType('TpReceiptAddDataResponse', (_message.Message,), dict(
  DESCRIPTOR = _TPRECEIPTADDDATARESPONSE,
  __module__ = 'bgx_cli.protobuf.state_context_pb2'
  # @@protoc_insertion_point(class_scope:TpReceiptAddDataResponse)
  ))
_sym_db.RegisterMessage(TpReceiptAddDataResponse)

TpEventAddRequest = _reflection.GeneratedProtocolMessageType('TpEventAddRequest', (_message.Message,), dict(
  DESCRIPTOR = _TPEVENTADDREQUEST,
  __module__ = 'bgx_cli.protobuf.state_context_pb2'
  # @@protoc_insertion_point(class_scope:TpEventAddRequest)
  ))
_sym_db.RegisterMessage(TpEventAddRequest)

TpEventAddResponse = _reflection.GeneratedProtocolMessageType('TpEventAddResponse', (_message.Message,), dict(
  DESCRIPTOR = _TPEVENTADDRESPONSE,
  __module__ = 'bgx_cli.protobuf.state_context_pb2'
  # @@protoc_insertion_point(class_scope:TpEventAddResponse)
  ))
_sym_db.RegisterMessage(TpEventAddResponse)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
