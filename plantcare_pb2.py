# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: plantcare.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='plantcare.proto',
  package='plantcare',
  syntax='proto3',
  serialized_pb=_b('\n\x0fplantcare.proto\x12\tplantcare\"\xaa\x01\n\x05Query\x12)\n\x07get_ids\x18\x01 \x01(\x0b\x32\x16.plantcare.GetIdsQueryH\x00\x12\x38\n\x0fget_flower_data\x18\x02 \x01(\x0b\x32\x1d.plantcare.GetFlowerDataQueryH\x00\x12\x33\n\x0cset_watering\x18\x03 \x01(\x0b\x32\x1b.plantcare.SetWateringQueryH\x00\x42\x07\n\x05query\"\xab\x01\n\x08Response\x12%\n\x03ids\x18\x01 \x01(\x0b\x32\x16.plantcare.IdsResponseH\x00\x12\x34\n\x0b\x66lower_data\x18\x02 \x01(\x0b\x32\x1d.plantcare.FlowerDataResponseH\x00\x12\x36\n\x0cwatering_set\x18\x03 \x01(\x0b\x32\x1e.plantcare.WateringSetResponseH\x00\x42\n\n\x08response\"\r\n\x0bGetIdsQuery\";\n\x12GetFlowerDataQuery\x12\x11\n\tflower_id\x18\x01 \x01(\r\x12\x12\n\nsince_time\x18\x02 \x01(\r\"A\n\x10SetWateringQuery\x12\x11\n\tflower_id\x18\x01 \x01(\r\x12\x0c\n\x04hour\x18\x02 \x01(\x11\x12\x0c\n\x04\x64\x61ys\x18\x03 \x03(\x11\"!\n\x0bIdsResponse\x12\x12\n\nflower_ids\x18\x01 \x03(\r\"\x82\x01\n\x12\x46lowerDataResponse\x12\x11\n\tflower_id\x18\x01 \x01(\r\x12\x1e\n\x16measurement_timestamps\x18\x02 \x03(\r\x12\x1d\n\x15moisture_measurements\x18\x03 \x03(\r\x12\x1a\n\x12light_measurements\x18\x04 \x03(\r\"\x15\n\x13WateringSetResponseB\x02H\x03\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_QUERY = _descriptor.Descriptor(
  name='Query',
  full_name='plantcare.Query',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='get_ids', full_name='plantcare.Query.get_ids', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='get_flower_data', full_name='plantcare.Query.get_flower_data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='set_watering', full_name='plantcare.Query.set_watering', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='query', full_name='plantcare.Query.query',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=31,
  serialized_end=201,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='plantcare.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ids', full_name='plantcare.Response.ids', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='flower_data', full_name='plantcare.Response.flower_data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='watering_set', full_name='plantcare.Response.watering_set', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='response', full_name='plantcare.Response.response',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=204,
  serialized_end=375,
)


_GETIDSQUERY = _descriptor.Descriptor(
  name='GetIdsQuery',
  full_name='plantcare.GetIdsQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=377,
  serialized_end=390,
)


_GETFLOWERDATAQUERY = _descriptor.Descriptor(
  name='GetFlowerDataQuery',
  full_name='plantcare.GetFlowerDataQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='flower_id', full_name='plantcare.GetFlowerDataQuery.flower_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='since_time', full_name='plantcare.GetFlowerDataQuery.since_time', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=392,
  serialized_end=451,
)


_SETWATERINGQUERY = _descriptor.Descriptor(
  name='SetWateringQuery',
  full_name='plantcare.SetWateringQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='flower_id', full_name='plantcare.SetWateringQuery.flower_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hour', full_name='plantcare.SetWateringQuery.hour', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='days', full_name='plantcare.SetWateringQuery.days', index=2,
      number=3, type=17, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=453,
  serialized_end=518,
)


_IDSRESPONSE = _descriptor.Descriptor(
  name='IdsResponse',
  full_name='plantcare.IdsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='flower_ids', full_name='plantcare.IdsResponse.flower_ids', index=0,
      number=1, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=520,
  serialized_end=553,
)


_FLOWERDATARESPONSE = _descriptor.Descriptor(
  name='FlowerDataResponse',
  full_name='plantcare.FlowerDataResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='flower_id', full_name='plantcare.FlowerDataResponse.flower_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='measurement_timestamps', full_name='plantcare.FlowerDataResponse.measurement_timestamps', index=1,
      number=2, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='moisture_measurements', full_name='plantcare.FlowerDataResponse.moisture_measurements', index=2,
      number=3, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='light_measurements', full_name='plantcare.FlowerDataResponse.light_measurements', index=3,
      number=4, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=556,
  serialized_end=686,
)


_WATERINGSETRESPONSE = _descriptor.Descriptor(
  name='WateringSetResponse',
  full_name='plantcare.WateringSetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=688,
  serialized_end=709,
)

_QUERY.fields_by_name['get_ids'].message_type = _GETIDSQUERY
_QUERY.fields_by_name['get_flower_data'].message_type = _GETFLOWERDATAQUERY
_QUERY.fields_by_name['set_watering'].message_type = _SETWATERINGQUERY
_QUERY.oneofs_by_name['query'].fields.append(
  _QUERY.fields_by_name['get_ids'])
_QUERY.fields_by_name['get_ids'].containing_oneof = _QUERY.oneofs_by_name['query']
_QUERY.oneofs_by_name['query'].fields.append(
  _QUERY.fields_by_name['get_flower_data'])
_QUERY.fields_by_name['get_flower_data'].containing_oneof = _QUERY.oneofs_by_name['query']
_QUERY.oneofs_by_name['query'].fields.append(
  _QUERY.fields_by_name['set_watering'])
_QUERY.fields_by_name['set_watering'].containing_oneof = _QUERY.oneofs_by_name['query']
_RESPONSE.fields_by_name['ids'].message_type = _IDSRESPONSE
_RESPONSE.fields_by_name['flower_data'].message_type = _FLOWERDATARESPONSE
_RESPONSE.fields_by_name['watering_set'].message_type = _WATERINGSETRESPONSE
_RESPONSE.oneofs_by_name['response'].fields.append(
  _RESPONSE.fields_by_name['ids'])
_RESPONSE.fields_by_name['ids'].containing_oneof = _RESPONSE.oneofs_by_name['response']
_RESPONSE.oneofs_by_name['response'].fields.append(
  _RESPONSE.fields_by_name['flower_data'])
_RESPONSE.fields_by_name['flower_data'].containing_oneof = _RESPONSE.oneofs_by_name['response']
_RESPONSE.oneofs_by_name['response'].fields.append(
  _RESPONSE.fields_by_name['watering_set'])
_RESPONSE.fields_by_name['watering_set'].containing_oneof = _RESPONSE.oneofs_by_name['response']
DESCRIPTOR.message_types_by_name['Query'] = _QUERY
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.message_types_by_name['GetIdsQuery'] = _GETIDSQUERY
DESCRIPTOR.message_types_by_name['GetFlowerDataQuery'] = _GETFLOWERDATAQUERY
DESCRIPTOR.message_types_by_name['SetWateringQuery'] = _SETWATERINGQUERY
DESCRIPTOR.message_types_by_name['IdsResponse'] = _IDSRESPONSE
DESCRIPTOR.message_types_by_name['FlowerDataResponse'] = _FLOWERDATARESPONSE
DESCRIPTOR.message_types_by_name['WateringSetResponse'] = _WATERINGSETRESPONSE

Query = _reflection.GeneratedProtocolMessageType('Query', (_message.Message,), dict(
  DESCRIPTOR = _QUERY,
  __module__ = 'plantcare_pb2'
  # @@protoc_insertion_point(class_scope:plantcare.Query)
  ))
_sym_db.RegisterMessage(Query)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'plantcare_pb2'
  # @@protoc_insertion_point(class_scope:plantcare.Response)
  ))
_sym_db.RegisterMessage(Response)

GetIdsQuery = _reflection.GeneratedProtocolMessageType('GetIdsQuery', (_message.Message,), dict(
  DESCRIPTOR = _GETIDSQUERY,
  __module__ = 'plantcare_pb2'
  # @@protoc_insertion_point(class_scope:plantcare.GetIdsQuery)
  ))
_sym_db.RegisterMessage(GetIdsQuery)

GetFlowerDataQuery = _reflection.GeneratedProtocolMessageType('GetFlowerDataQuery', (_message.Message,), dict(
  DESCRIPTOR = _GETFLOWERDATAQUERY,
  __module__ = 'plantcare_pb2'
  # @@protoc_insertion_point(class_scope:plantcare.GetFlowerDataQuery)
  ))
_sym_db.RegisterMessage(GetFlowerDataQuery)

SetWateringQuery = _reflection.GeneratedProtocolMessageType('SetWateringQuery', (_message.Message,), dict(
  DESCRIPTOR = _SETWATERINGQUERY,
  __module__ = 'plantcare_pb2'
  # @@protoc_insertion_point(class_scope:plantcare.SetWateringQuery)
  ))
_sym_db.RegisterMessage(SetWateringQuery)

IdsResponse = _reflection.GeneratedProtocolMessageType('IdsResponse', (_message.Message,), dict(
  DESCRIPTOR = _IDSRESPONSE,
  __module__ = 'plantcare_pb2'
  # @@protoc_insertion_point(class_scope:plantcare.IdsResponse)
  ))
_sym_db.RegisterMessage(IdsResponse)

FlowerDataResponse = _reflection.GeneratedProtocolMessageType('FlowerDataResponse', (_message.Message,), dict(
  DESCRIPTOR = _FLOWERDATARESPONSE,
  __module__ = 'plantcare_pb2'
  # @@protoc_insertion_point(class_scope:plantcare.FlowerDataResponse)
  ))
_sym_db.RegisterMessage(FlowerDataResponse)

WateringSetResponse = _reflection.GeneratedProtocolMessageType('WateringSetResponse', (_message.Message,), dict(
  DESCRIPTOR = _WATERINGSETRESPONSE,
  __module__ = 'plantcare_pb2'
  # @@protoc_insertion_point(class_scope:plantcare.WateringSetResponse)
  ))
_sym_db.RegisterMessage(WateringSetResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('H\003'))
# @@protoc_insertion_point(module_scope)
