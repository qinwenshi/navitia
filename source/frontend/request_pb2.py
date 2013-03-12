# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import type_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='request.proto',
  package='pbnavitia',
  serialized_pb='\n\rrequest.proto\x12\tpbnavitia\x1a\ntype.proto\"J\n\x13\x41utocompleteRequest\x12\x0c\n\x04name\x18\x01 \x02(\t\x12%\n\x05types\x18\x02 \x03(\x0e\x32\x16.pbnavitia.NavitiaType\"\x95\x01\n\x13NextStopTimeRequest\x12\x18\n\x10\x64\x65parture_filter\x18\x01 \x02(\t\x12\x16\n\x0e\x61rrival_filter\x18\x02 \x02(\t\x12\x15\n\rfrom_datetime\x18\x03 \x02(\t\x12\x10\n\x08\x64uration\x18\x04 \x02(\x05\x12\r\n\x05\x64\x65pth\x18\x05 \x02(\x05\x12\x14\n\x0cnb_stoptimes\x18\x07 \x02(\x05\"\xa5\x01\n\x0fJourneysRequest\x12\x0e\n\x06origin\x18\x01 \x02(\t\x12\x13\n\x0b\x64\x65stination\x18\x02 \x02(\t\x12\x11\n\tdatetimes\x18\x03 \x03(\t\x12\x11\n\tclockwise\x18\x04 \x02(\x08\x12\x16\n\x0e\x66orbidden_uris\x18\x07 \x03(\t\x12\x15\n\rwalking_speed\x18\x08 \x02(\x01\x12\x18\n\x10walking_distance\x18\n \x02(\x05\"|\n\x14ProximityListRequest\x12+\n\x05\x63oord\x18\x01 \x02(\x0b\x32\x1c.pbnavitia.GeographicalCoord\x12\x10\n\x08\x64istance\x18\x02 \x02(\x01\x12%\n\x05types\x18\x03 \x03(\x0e\x32\x16.pbnavitia.NavitiaType\"]\n\x0cPTRefRequest\x12.\n\x0erequested_type\x18\x01 \x02(\x0e\x32\x16.pbnavitia.NavitiaType\x12\x0e\n\x06\x66ilter\x18\x02 \x02(\t\x12\r\n\x05\x64\x65pth\x18\x03 \x02(\x05\"\xae\x02\n\x07Request\x12%\n\rrequested_api\x18\x01 \x02(\x0e\x32\x0e.pbnavitia.API\x12\x34\n\x0c\x61utocomplete\x18\x02 \x01(\x0b\x32\x1e.pbnavitia.AutocompleteRequest\x12\x37\n\x0fnext_stop_times\x18\x04 \x01(\x0b\x32\x1e.pbnavitia.NextStopTimeRequest\x12\x37\n\x0eproximity_list\x18\x05 \x01(\x0b\x32\x1f.pbnavitia.ProximityListRequest\x12,\n\x08journeys\x18\x06 \x01(\x0b\x32\x1a.pbnavitia.JourneysRequest\x12&\n\x05ptref\x18\x07 \x01(\x0b\x32\x17.pbnavitia.PTRefRequest')




_AUTOCOMPLETEREQUEST = descriptor.Descriptor(
  name='AutocompleteRequest',
  full_name='pbnavitia.AutocompleteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='pbnavitia.AutocompleteRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='types', full_name='pbnavitia.AutocompleteRequest.types', index=1,
      number=2, type=14, cpp_type=8, label=3,
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
  extension_ranges=[],
  serialized_start=40,
  serialized_end=114,
)


_NEXTSTOPTIMEREQUEST = descriptor.Descriptor(
  name='NextStopTimeRequest',
  full_name='pbnavitia.NextStopTimeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='departure_filter', full_name='pbnavitia.NextStopTimeRequest.departure_filter', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='arrival_filter', full_name='pbnavitia.NextStopTimeRequest.arrival_filter', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='from_datetime', full_name='pbnavitia.NextStopTimeRequest.from_datetime', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='duration', full_name='pbnavitia.NextStopTimeRequest.duration', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='depth', full_name='pbnavitia.NextStopTimeRequest.depth', index=4,
      number=5, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='nb_stoptimes', full_name='pbnavitia.NextStopTimeRequest.nb_stoptimes', index=5,
      number=7, type=5, cpp_type=1, label=2,
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
  extension_ranges=[],
  serialized_start=117,
  serialized_end=266,
)


_JOURNEYSREQUEST = descriptor.Descriptor(
  name='JourneysRequest',
  full_name='pbnavitia.JourneysRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='origin', full_name='pbnavitia.JourneysRequest.origin', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='destination', full_name='pbnavitia.JourneysRequest.destination', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='datetimes', full_name='pbnavitia.JourneysRequest.datetimes', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='clockwise', full_name='pbnavitia.JourneysRequest.clockwise', index=3,
      number=4, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='forbidden_uris', full_name='pbnavitia.JourneysRequest.forbidden_uris', index=4,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='walking_speed', full_name='pbnavitia.JourneysRequest.walking_speed', index=5,
      number=8, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='walking_distance', full_name='pbnavitia.JourneysRequest.walking_distance', index=6,
      number=10, type=5, cpp_type=1, label=2,
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
  extension_ranges=[],
  serialized_start=269,
  serialized_end=434,
)


_PROXIMITYLISTREQUEST = descriptor.Descriptor(
  name='ProximityListRequest',
  full_name='pbnavitia.ProximityListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='coord', full_name='pbnavitia.ProximityListRequest.coord', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='distance', full_name='pbnavitia.ProximityListRequest.distance', index=1,
      number=2, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='types', full_name='pbnavitia.ProximityListRequest.types', index=2,
      number=3, type=14, cpp_type=8, label=3,
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
  extension_ranges=[],
  serialized_start=436,
  serialized_end=560,
)


_PTREFREQUEST = descriptor.Descriptor(
  name='PTRefRequest',
  full_name='pbnavitia.PTRefRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='requested_type', full_name='pbnavitia.PTRefRequest.requested_type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='filter', full_name='pbnavitia.PTRefRequest.filter', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='depth', full_name='pbnavitia.PTRefRequest.depth', index=2,
      number=3, type=5, cpp_type=1, label=2,
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
  extension_ranges=[],
  serialized_start=562,
  serialized_end=655,
)


_REQUEST = descriptor.Descriptor(
  name='Request',
  full_name='pbnavitia.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='requested_api', full_name='pbnavitia.Request.requested_api', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='autocomplete', full_name='pbnavitia.Request.autocomplete', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='next_stop_times', full_name='pbnavitia.Request.next_stop_times', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='proximity_list', full_name='pbnavitia.Request.proximity_list', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='journeys', full_name='pbnavitia.Request.journeys', index=4,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='ptref', full_name='pbnavitia.Request.ptref', index=5,
      number=7, type=11, cpp_type=10, label=1,
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
  extension_ranges=[],
  serialized_start=658,
  serialized_end=960,
)

_AUTOCOMPLETEREQUEST.fields_by_name['types'].enum_type = type_pb2._NAVITIATYPE
_PROXIMITYLISTREQUEST.fields_by_name['coord'].message_type = type_pb2._GEOGRAPHICALCOORD
_PROXIMITYLISTREQUEST.fields_by_name['types'].enum_type = type_pb2._NAVITIATYPE
_PTREFREQUEST.fields_by_name['requested_type'].enum_type = type_pb2._NAVITIATYPE
_REQUEST.fields_by_name['requested_api'].enum_type = type_pb2._API
_REQUEST.fields_by_name['autocomplete'].message_type = _AUTOCOMPLETEREQUEST
_REQUEST.fields_by_name['next_stop_times'].message_type = _NEXTSTOPTIMEREQUEST
_REQUEST.fields_by_name['proximity_list'].message_type = _PROXIMITYLISTREQUEST
_REQUEST.fields_by_name['journeys'].message_type = _JOURNEYSREQUEST
_REQUEST.fields_by_name['ptref'].message_type = _PTREFREQUEST
DESCRIPTOR.message_types_by_name['AutocompleteRequest'] = _AUTOCOMPLETEREQUEST
DESCRIPTOR.message_types_by_name['NextStopTimeRequest'] = _NEXTSTOPTIMEREQUEST
DESCRIPTOR.message_types_by_name['JourneysRequest'] = _JOURNEYSREQUEST
DESCRIPTOR.message_types_by_name['ProximityListRequest'] = _PROXIMITYLISTREQUEST
DESCRIPTOR.message_types_by_name['PTRefRequest'] = _PTREFREQUEST
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST

class AutocompleteRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _AUTOCOMPLETEREQUEST
  
  # @@protoc_insertion_point(class_scope:pbnavitia.AutocompleteRequest)

class NextStopTimeRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _NEXTSTOPTIMEREQUEST
  
  # @@protoc_insertion_point(class_scope:pbnavitia.NextStopTimeRequest)

class JourneysRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _JOURNEYSREQUEST
  
  # @@protoc_insertion_point(class_scope:pbnavitia.JourneysRequest)

class ProximityListRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PROXIMITYLISTREQUEST
  
  # @@protoc_insertion_point(class_scope:pbnavitia.ProximityListRequest)

class PTRefRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PTREFREQUEST
  
  # @@protoc_insertion_point(class_scope:pbnavitia.PTRefRequest)

class Request(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REQUEST
  
  # @@protoc_insertion_point(class_scope:pbnavitia.Request)

# @@protoc_insertion_point(module_scope)