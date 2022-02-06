# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: person.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='person.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0elocation.proto\x1a\x1cgoogle/api/annotations.proto\"Y\n\x08Location\x12\x11\n\tperson_id\x18\x02 \x01(\x05\x12\x10\n\x08latitude\x18\x03 \x01(\t\x12\x11\n\tlongitude\x18\x04 \x01(\t\x12\x15\n\rcreation_time\x18\x05 \x01(\t\"$\n\x0fLocationRequest\x12\x11\n\tperson_id\x18\x01 \x01(\x05\",\n\x0cLocationList\x12\x1c\n\tlocations\x18\x01 \x03(\x0b\x32\t.Location2\xbf\x01\n\x0fLocationService\x12G\n\x06\x43reate\x12\t.Location\x1a\t.Location\"\'\x82\xd3\xe4\x93\x02!\"\x1c/api/locations/{location_id}:\x01*\x12\x63\n\x08Retrieve\x12\x10.LocationRequest\x1a\r.LocationList\"6\x82\xd3\xe4\x93\x02\x30\x12\x1c/api/locations/{location_id}Z\x10\x12\x0e/api/locationsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_LOCATION = _descriptor.Descriptor(
  name='Location',
  full_name='Location',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='person_id', full_name='Location.person_id', index=0,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='Location.latitude', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='Location.longitude', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='creation_time', full_name='Location.creation_time', index=3,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=48,
  serialized_end=137,
)


_LOCATIONREQUEST = _descriptor.Descriptor(
  name='LocationRequest',
  full_name='LocationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='person_id', full_name='LocationRequest.person_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=139,
  serialized_end=175,
)


_LOCATIONLIST = _descriptor.Descriptor(
  name='LocationList',
  full_name='LocationList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='locations', full_name='LocationList.locations', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=177,
  serialized_end=221,
)

_LOCATIONLIST.fields_by_name['locations'].message_type = _LOCATION
DESCRIPTOR.message_types_by_name['Location'] = _LOCATION
DESCRIPTOR.message_types_by_name['LocationRequest'] = _LOCATIONREQUEST
DESCRIPTOR.message_types_by_name['LocationList'] = _LOCATIONLIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Location = _reflection.GeneratedProtocolMessageType('Location', (_message.Message,), {
  'DESCRIPTOR' : _LOCATION,
  '__module__' : 'location_pb2'
  # @@protoc_insertion_point(class_scope:Location)
  })
_sym_db.RegisterMessage(Location)

LocationRequest = _reflection.GeneratedProtocolMessageType('LocationRequest', (_message.Message,), {
  'DESCRIPTOR' : _LOCATIONREQUEST,
  '__module__' : 'location_pb2'
  # @@protoc_insertion_point(class_scope:LocationRequest)
  })
_sym_db.RegisterMessage(LocationRequest)

LocationList = _reflection.GeneratedProtocolMessageType('LocationList', (_message.Message,), {
  'DESCRIPTOR' : _LOCATIONLIST,
  '__module__' : 'location_pb2'
  # @@protoc_insertion_point(class_scope:LocationList)
  })
_sym_db.RegisterMessage(LocationList)



_LOCATIONSERVICE = _descriptor.ServiceDescriptor(
  name='LocationService',
  full_name='LocationService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=224,
  serialized_end=415,
  methods=[
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='LocationService.Create',
    index=0,
    containing_service=None,
    input_type=_LOCATION,
    output_type=_LOCATION,
    serialized_options=b'\202\323\344\223\002!\"\034/api/locations/{location_id}:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Retrieve',
    full_name='LocationService.Retrieve',
    index=1,
    containing_service=None,
    input_type=_LOCATIONREQUEST,
    output_type=_LOCATIONLIST,
    serialized_options=b'\202\323\344\223\0020\022\034/api/locations/{location_id}Z\020\022\016/api/locations',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_LOCATIONSERVICE)

DESCRIPTOR.services_by_name['LocationService'] = _LOCATIONSERVICE

# @@protoc_insertion_point(module_scope)
