# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bodyinfo.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0e\x62odyinfo.proto\x12\tcommander\"l\n\tQueryInfo\x12\x0b\n\x03qid\x18\x01 \x01(\r\x12\n\n\x02\x61x\x18\x02 \x01(\x02\x12\n\n\x02\x61y\x18\x03 \x01(\x02\x12\n\n\x02\x62x\x18\x04 \x01(\x02\x12\n\n\x02\x62y\x18\x05 \x01(\x02\x12\x0b\n\x03max\x18\x06 \x01(\r\x12\x15\n\rtrackableOnly\x18\x07 \x01(\x08\"\xdc\x02\n\x08\x42odyInfo\x12\x0b\n\x03\x62id\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12#\n\x05shape\x18\x03 \x01(\x0e\x32\x14.commander.BodyShape\x12\t\n\x01x\x18\x04 \x01(\x02\x12\t\n\x01y\x18\x05 \x01(\x02\x12\r\n\x05width\x18\x06 \x01(\x02\x12\x0e\n\x06height\x18\x07 \x01(\x02\x12\x13\n\x0brestitution\x18\x08 \x01(\x02\x12\x10\n\x08\x66riction\x18\t \x01(\x02\x12\x0f\n\x07\x64\x65nsity\x18\n \x01(\x02\x12\x10\n\x08isSensor\x18\x0b \x01(\x08\x12\x14\n\x0c\x63\x61tegoryBits\x18\x0c \x01(\r\x12\x10\n\x08maskBits\x18\r \x01(\r\x12\x15\n\rfixedRotation\x18\x0e \x01(\x08\x12!\n\x04type\x18\x0f \x01(\x0e\x32\x13.commander.BodyType\x12\x0c\n\x04skin\x18\x10 \x01(\t\x12\x11\n\ttrackable\x18\x11 \x01(\x08\x12\x0e\n\x06\x66loats\x18\x12 \x03(\x02\"\x8e\x01\n\x0c\x42odySkinInfo\x12\x0b\n\x03\x62id\x18\x01 \x01(\r\x12!\n\x04skin\x18\x02 \x01(\x0e\x32\x13.commander.BodySkin\x12%\n\x04type\x18\x03 \x01(\x0e\x32\x17.commander.BodySkinType\x12\'\n\x05\x65xtra\x18\x04 \x01(\x0e\x32\x18.commander.BodySkinExtra\"N\n\nBodyOpInfo\x12\x0b\n\x03\x62id\x18\x01 \x01(\r\x12\x1d\n\x02op\x18\x02 \x01(\x0e\x32\x11.commander.BodyOp\x12\t\n\x01x\x18\x03 \x01(\x02\x12\t\n\x01y\x18\x04 \x01(\x02\"e\n\x0b\x43ontactInfo\x12\x0c\n\x04\x62id0\x18\x01 \x01(\r\x12\x0c\n\x04\x62id1\x18\x02 \x01(\r\x12\t\n\x01x\x18\x03 \x01(\x02\x12\t\n\x01y\x18\x04 \x01(\x02\x12$\n\x04type\x18\x05 \x01(\x0e\x32\x16.commander.ContactType\"R\n\tEventInfo\x12\x0b\n\x03\x62id\x18\x01 \x01(\r\x12\t\n\x01x\x18\x02 \x01(\x02\x12\t\n\x01y\x18\x03 \x01(\x02\x12\"\n\x04type\x18\x04 \x01(\x0e\x32\x14.commander.EventType\"9\n\x07KeyInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12 \n\x04type\x18\x02 \x01(\x0e\x32\x12.commander.KeyType\"%\n\x07\x41\x63kInfo\x12\x0c\n\x04info\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\r\"\x93\x01\n\x0f\x44irectionalInfo\x12$\n\x03iid\x18\x01 \x01(\x0e\x32\x17.commander.TouchInputId\x12\x35\n\tdirection\x18\x02 \x01(\x0e\x32\".commander.JoystickMoveDirectional\x12\x11\n\tintensity\x18\x03 \x01(\x01\x12\x10\n\x08radAngle\x18\x04 \x01(\x01\"Y\n\nButtonInfo\x12$\n\x03iid\x18\x01 \x01(\x0e\x32\x17.commander.TouchInputId\x12%\n\x05\x65vent\x18\x02 \x01(\x0e\x32\x16.commander.ActionEvent\"l\n\x07TabInfo\x12$\n\x03iid\x18\x01 \x01(\x0e\x32\x17.commander.TouchInputId\x12%\n\x05\x65vent\x18\x02 \x01(\x0e\x32\x16.commander.ActionEvent\x12\t\n\x01x\x18\x03 \x01(\x01\x12\t\n\x01y\x18\x04 \x01(\x01\"3\n\x0eObjectPosition\x12\x0b\n\x03\x62id\x18\x01 \x01(\r\x12\t\n\x01x\x18\x02 \x01(\x01\x12\t\n\x01y\x18\x03 \x01(\x01\"C\n\x0bQueryResult\x12\x0b\n\x03qid\x18\x01 \x01(\r\x12\'\n\x04objs\x18\x02 \x03(\x0b\x32\x19.commander.ObjectPosition\"\xd9\x02\n\x07\x43mdInfo\x12\x1d\n\x04head\x18\x01 \x01(\x0e\x32\x0f.commander.Head\x12\'\n\x07\x63ontact\x18\x02 \x01(\x0b\x32\x16.commander.ContactInfo\x12#\n\x05\x65vent\x18\x03 \x01(\x0b\x32\x14.commander.EventInfo\x12\x1f\n\x03key\x18\x04 \x01(\x0b\x32\x12.commander.KeyInfo\x12\x1f\n\x03\x61\x63k\x18\x05 \x01(\x0b\x32\x12.commander.AckInfo\x12/\n\x0b\x64irectional\x18\x06 \x01(\x0b\x32\x1a.commander.DirectionalInfo\x12%\n\x06\x62utton\x18\x07 \x01(\x0b\x32\x15.commander.ButtonInfo\x12\x1f\n\x03tab\x18\x08 \x01(\x0b\x32\x12.commander.TabInfo\x12&\n\x06result\x18\t \x01(\x0b\x32\x16.commander.QueryResult\"\xbf\x02\n\x08InitInfo\x12\x0c\n\x04json\x18\x01 \x01(\t\x12\x11\n\tgravity_x\x18\x02 \x01(\x01\x12\x11\n\tgravity_y\x18\x03 \x01(\x01\x12\r\n\x05width\x18\x04 \x01(\x01\x12\x0e\n\x06height\x18\x05 \x01(\x01\x12\r\n\x05\x64\x65\x62ug\x18\x06 \x01(\x08\x12>\n\x15joystick_directionals\x18\x07 \x01(\x0e\x32\x1f.commander.JoystickDirectionals\x12\x1a\n\x12joystick_precision\x18\x08 \x01(\r\x12\'\n\x07\x62utton1\x18\t \x01(\x0e\x32\x16.commander.ActionEvent\x12\'\n\x07\x62utton2\x18\n \x01(\x0e\x32\x16.commander.ActionEvent\x12#\n\x03tab\x18\x64 \x01(\x0e\x32\x16.commander.ActionEvent*\xcd\x01\n\x04Head\x12\x0b\n\x07unknown\x10\x00\x12\n\n\x04init\x10\x80\xfe\x03\x12\x0e\n\x08\x62odyinfo\x10\x81\xfe\x03\x12\x10\n\nbodystatus\x10\x82\xfe\x03\x12\x0c\n\x06\x62odyop\x10\x83\xfe\x03\x12\x0b\n\x05query\x10\x84\xfe\x03\x12\r\n\x07\x63ontact\x10\xf0\xe1\x03\x12\x0b\n\x05\x65vent\x10\xf1\xe1\x03\x12\t\n\x03key\x10\xf2\xe1\x03\x12\t\n\x03\x61\x63k\x10\xf3\xe1\x03\x12\x11\n\x0b\x64irectional\x10\xf4\xe1\x03\x12\x0c\n\x06\x62utton\x10\xf5\xe1\x03\x12\t\n\x03tab\x10\xf6\xe1\x03\x12\x11\n\x0bqueryresult\x10\xf7\xe1\x03*V\n\tBodyShape\x12\r\n\trectangle\x10\x00\x12\t\n\x05\x61\x63tor\x10\x01\x12\n\n\x06\x63ircle\x10\x02\x12\x0c\n\x08triangle\x10\x03\x12\x08\n\x04\x65\x64ge\x10\x04\x12\x0b\n\x07polygon\x10\x05*2\n\x08\x42odyType\x12\n\n\x06static\x10\x00\x12\r\n\tkinematic\x10\x01\x12\x0b\n\x07\x64ynamic\x10\x02*\xc5\x01\n\x08\x42odySkin\x12\x08\n\x04idle\x10\x00\x12\x07\n\x03run\x10\x01\x12\x08\n\x04jump\x10\x02\x12\x07\n\x03hit\x10\x03\x12\x08\n\x04\x66\x61ll\x10\x04\x12\x0c\n\x08wallJump\x10\x05\x12\x0e\n\ndoubleJump\x10\x06\x12\x0b\n\x07hitSide\x10\x07\x12\n\n\x06hitTop\x10\x08\x12\x07\n\x03off\x10\t\x12\x06\n\x02on\x10\n\x12\t\n\x05\x62link\x10\x0b\x12\x0b\n\x07hitLeft\x10\x0c\x12\x0c\n\x08hitRight\x10\r\x12\r\n\thitBottom\x10\x0e\x12\x0c\n\x08noChange\x10\x0f*.\n\x0c\x42odySkinType\x12\x08\n\x04loop\x10\x00\x12\x08\n\x04once\x10\x01\x12\n\n\x06notify\x10\x02*$\n\rBodySkinExtra\x12\x08\n\x04left\x10\x00\x12\t\n\x05right\x10\x01*\xe1\x01\n\x06\x42odyOp\x12\x12\n\x0elinearVelocity\x10\x00\x12\x13\n\x0f\x61ngularVelocity\x10\x01\x12\t\n\x05\x66orce\x10\x02\x12\x11\n\rlinearImpulse\x10\x03\x12\n\n\x06torque\x10\x04\x12\x15\n\x11xConstantVelocity\x10\x05\x12\x15\n\x11yConstantVelocity\x10\x06\x12\x13\n\x0fxLinearVelocity\x10\x07\x12\x13\n\x0fyLinearVelocity\x10\x08\x12\x14\n\x10\x63onstantVelocity\x10\t\x12\n\n\x06\x61\x63tion\x10\n\x12\n\n\x06remove\x10\x0b*!\n\x0b\x43ontactType\x12\t\n\x05\x62\x65gin\x10\x00\x12\x07\n\x03\x65nd\x10\x01*\x19\n\tEventType\x12\x0c\n\x08\x63omplete\x10\x00*\x1b\n\x07KeyType\x12\x08\n\x04\x64own\x10\x00\x12\x06\n\x02up\x10\x01*\xac\x01\n\x17JoystickMoveDirectional\x12\x0b\n\x07MOVE_UP\x10\x00\x12\x10\n\x0cMOVE_UP_LEFT\x10\x01\x12\x11\n\rMOVE_UP_RIGHT\x10\x02\x12\x0e\n\nMOVE_RIGHT\x10\x03\x12\r\n\tMOVE_DOWN\x10\x04\x12\x13\n\x0fMOVE_DOWN_RIGHT\x10\x05\x12\x12\n\x0eMOVE_DOWN_LEFT\x10\x06\x12\r\n\tMOVE_LEFT\x10\x07\x12\x08\n\x04IDLE\x10\x08*e\n\x0b\x41\x63tionEvent\x12\x08\n\x04\x44OWN\x10\x00\x12\x06\n\x02UP\x10\x01\x12\x08\n\x04MOVE\x10\x02\x12\x08\n\x04NONE\x10\x03\x12\x0b\n\x07UP_DOWN\x10\x04\x12\r\n\tDOWN_MOVE\x10\x05\x12\x07\n\x03\x41LL\x10\x06\x12\x0b\n\x07UP_MOVE\x10\x07*W\n\x0cTouchInputId\x12\x12\n\x0ejoystick_input\x10\x00\x12\x11\n\rbutton1_input\x10\x01\x12\x11\n\rbutton2_input\x10\x02\x12\r\n\ttab_input\x10\x03*G\n\x14JoystickDirectionals\x12\x08\n\x04none\x10\x00\x12\x07\n\x03\x61ll\x10\x01\x12\x0e\n\nhorizontal\x10\x02\x12\x0c\n\x08vertical\x10\x03\x62\x06proto3')

_HEAD = DESCRIPTOR.enum_types_by_name['Head']
Head = enum_type_wrapper.EnumTypeWrapper(_HEAD)
_BODYSHAPE = DESCRIPTOR.enum_types_by_name['BodyShape']
BodyShape = enum_type_wrapper.EnumTypeWrapper(_BODYSHAPE)
_BODYTYPE = DESCRIPTOR.enum_types_by_name['BodyType']
BodyType = enum_type_wrapper.EnumTypeWrapper(_BODYTYPE)
_BODYSKIN = DESCRIPTOR.enum_types_by_name['BodySkin']
BodySkin = enum_type_wrapper.EnumTypeWrapper(_BODYSKIN)
_BODYSKINTYPE = DESCRIPTOR.enum_types_by_name['BodySkinType']
BodySkinType = enum_type_wrapper.EnumTypeWrapper(_BODYSKINTYPE)
_BODYSKINEXTRA = DESCRIPTOR.enum_types_by_name['BodySkinExtra']
BodySkinExtra = enum_type_wrapper.EnumTypeWrapper(_BODYSKINEXTRA)
_BODYOP = DESCRIPTOR.enum_types_by_name['BodyOp']
BodyOp = enum_type_wrapper.EnumTypeWrapper(_BODYOP)
_CONTACTTYPE = DESCRIPTOR.enum_types_by_name['ContactType']
ContactType = enum_type_wrapper.EnumTypeWrapper(_CONTACTTYPE)
_EVENTTYPE = DESCRIPTOR.enum_types_by_name['EventType']
EventType = enum_type_wrapper.EnumTypeWrapper(_EVENTTYPE)
_KEYTYPE = DESCRIPTOR.enum_types_by_name['KeyType']
KeyType = enum_type_wrapper.EnumTypeWrapper(_KEYTYPE)
_JOYSTICKMOVEDIRECTIONAL = DESCRIPTOR.enum_types_by_name['JoystickMoveDirectional']
JoystickMoveDirectional = enum_type_wrapper.EnumTypeWrapper(_JOYSTICKMOVEDIRECTIONAL)
_ACTIONEVENT = DESCRIPTOR.enum_types_by_name['ActionEvent']
ActionEvent = enum_type_wrapper.EnumTypeWrapper(_ACTIONEVENT)
_TOUCHINPUTID = DESCRIPTOR.enum_types_by_name['TouchInputId']
TouchInputId = enum_type_wrapper.EnumTypeWrapper(_TOUCHINPUTID)
_JOYSTICKDIRECTIONALS = DESCRIPTOR.enum_types_by_name['JoystickDirectionals']
JoystickDirectionals = enum_type_wrapper.EnumTypeWrapper(_JOYSTICKDIRECTIONALS)
unknown = 0
init = 65280
bodyinfo = 65281
bodystatus = 65282
bodyop = 65283
query = 65284
contact = 61680
event = 61681
key = 61682
ack = 61683
directional = 61684
button = 61685
tab = 61686
queryresult = 61687
rectangle = 0
actor = 1
circle = 2
triangle = 3
edge = 4
polygon = 5
static = 0
kinematic = 1
dynamic = 2
idle = 0
run = 1
jump = 2
hit = 3
fall = 4
wallJump = 5
doubleJump = 6
hitSide = 7
hitTop = 8
off = 9
on = 10
blink = 11
hitLeft = 12
hitRight = 13
hitBottom = 14
noChange = 15
loop = 0
once = 1
notify = 2
left = 0
right = 1
linearVelocity = 0
angularVelocity = 1
force = 2
linearImpulse = 3
torque = 4
xConstantVelocity = 5
yConstantVelocity = 6
xLinearVelocity = 7
yLinearVelocity = 8
constantVelocity = 9
action = 10
remove = 11
begin = 0
end = 1
complete = 0
down = 0
up = 1
MOVE_UP = 0
MOVE_UP_LEFT = 1
MOVE_UP_RIGHT = 2
MOVE_RIGHT = 3
MOVE_DOWN = 4
MOVE_DOWN_RIGHT = 5
MOVE_DOWN_LEFT = 6
MOVE_LEFT = 7
IDLE = 8
DOWN = 0
UP = 1
MOVE = 2
NONE = 3
UP_DOWN = 4
DOWN_MOVE = 5
ALL = 6
UP_MOVE = 7
joystick_input = 0
button1_input = 1
button2_input = 2
tab_input = 3
none = 0
all = 1
horizontal = 2
vertical = 3


_QUERYINFO = DESCRIPTOR.message_types_by_name['QueryInfo']
_BODYINFO = DESCRIPTOR.message_types_by_name['BodyInfo']
_BODYSKININFO = DESCRIPTOR.message_types_by_name['BodySkinInfo']
_BODYOPINFO = DESCRIPTOR.message_types_by_name['BodyOpInfo']
_CONTACTINFO = DESCRIPTOR.message_types_by_name['ContactInfo']
_EVENTINFO = DESCRIPTOR.message_types_by_name['EventInfo']
_KEYINFO = DESCRIPTOR.message_types_by_name['KeyInfo']
_ACKINFO = DESCRIPTOR.message_types_by_name['AckInfo']
_DIRECTIONALINFO = DESCRIPTOR.message_types_by_name['DirectionalInfo']
_BUTTONINFO = DESCRIPTOR.message_types_by_name['ButtonInfo']
_TABINFO = DESCRIPTOR.message_types_by_name['TabInfo']
_OBJECTPOSITION = DESCRIPTOR.message_types_by_name['ObjectPosition']
_QUERYRESULT = DESCRIPTOR.message_types_by_name['QueryResult']
_CMDINFO = DESCRIPTOR.message_types_by_name['CmdInfo']
_INITINFO = DESCRIPTOR.message_types_by_name['InitInfo']
QueryInfo = _reflection.GeneratedProtocolMessageType('QueryInfo', (_message.Message,), {
  'DESCRIPTOR' : _QUERYINFO,
  '__module__' : 'bodyinfo_pb2'
  # @@protoc_insertion_point(class_scope:commander.QueryInfo)
  })
_sym_db.RegisterMessage(QueryInfo)

BodyInfo = _reflection.GeneratedProtocolMessageType('BodyInfo', (_message.Message,), {
  'DESCRIPTOR' : _BODYINFO,
  '__module__' : 'bodyinfo_pb2'
  # @@protoc_insertion_point(class_scope:commander.BodyInfo)
  })
_sym_db.RegisterMessage(BodyInfo)

BodySkinInfo = _reflection.GeneratedProtocolMessageType('BodySkinInfo', (_message.Message,), {
  'DESCRIPTOR' : _BODYSKININFO,
  '__module__' : 'bodyinfo_pb2'
  # @@protoc_insertion_point(class_scope:commander.BodySkinInfo)
  })
_sym_db.RegisterMessage(BodySkinInfo)

BodyOpInfo = _reflection.GeneratedProtocolMessageType('BodyOpInfo', (_message.Message,), {
  'DESCRIPTOR' : _BODYOPINFO,
  '__module__' : 'bodyinfo_pb2'
  # @@protoc_insertion_point(class_scope:commander.BodyOpInfo)
  })
_sym_db.RegisterMessage(BodyOpInfo)

ContactInfo = _reflection.GeneratedProtocolMessageType('ContactInfo', (_message.Message,), {
  'DESCRIPTOR' : _CONTACTINFO,
  '__module__' : 'bodyinfo_pb2'
  # @@protoc_insertion_point(class_scope:commander.ContactInfo)
  })
_sym_db.RegisterMessage(ContactInfo)

EventInfo = _reflection.GeneratedProtocolMessageType('EventInfo', (_message.Message,), {
  'DESCRIPTOR' : _EVENTINFO,
  '__module__' : 'bodyinfo_pb2'
  # @@protoc_insertion_point(class_scope:commander.EventInfo)
  })
_sym_db.RegisterMessage(EventInfo)

KeyInfo = _reflection.GeneratedProtocolMessageType('KeyInfo', (_message.Message,), {
  'DESCRIPTOR' : _KEYINFO,
  '__module__' : 'bodyinfo_pb2'
  # @@protoc_insertion_point(class_scope:commander.KeyInfo)
  })
_sym_db.RegisterMessage(KeyInfo)

AckInfo = _reflection.GeneratedProtocolMessageType('AckInfo', (_message.Message,), {
  'DESCRIPTOR' : _ACKINFO,
  '__module__' : 'bodyinfo_pb2'
  # @@protoc_insertion_point(class_scope:commander.AckInfo)
  })
_sym_db.RegisterMessage(AckInfo)

DirectionalInfo = _reflection.GeneratedProtocolMessageType('DirectionalInfo', (_message.Message,), {
  'DESCRIPTOR' : _DIRECTIONALINFO,
  '__module__' : 'bodyinfo_pb2'
  # @@protoc_insertion_point(class_scope:commander.DirectionalInfo)
  })
_sym_db.RegisterMessage(DirectionalInfo)

ButtonInfo = _reflection.GeneratedProtocolMessageType('ButtonInfo', (_message.Message,), {
  'DESCRIPTOR' : _BUTTONINFO,
  '__module__' : 'bodyinfo_pb2'
  # @@protoc_insertion_point(class_scope:commander.ButtonInfo)
  })
_sym_db.RegisterMessage(ButtonInfo)

TabInfo = _reflection.GeneratedProtocolMessageType('TabInfo', (_message.Message,), {
  'DESCRIPTOR' : _TABINFO,
  '__module__' : 'bodyinfo_pb2'
  # @@protoc_insertion_point(class_scope:commander.TabInfo)
  })
_sym_db.RegisterMessage(TabInfo)

ObjectPosition = _reflection.GeneratedProtocolMessageType('ObjectPosition', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTPOSITION,
  '__module__' : 'bodyinfo_pb2'
  # @@protoc_insertion_point(class_scope:commander.ObjectPosition)
  })
_sym_db.RegisterMessage(ObjectPosition)

QueryResult = _reflection.GeneratedProtocolMessageType('QueryResult', (_message.Message,), {
  'DESCRIPTOR' : _QUERYRESULT,
  '__module__' : 'bodyinfo_pb2'
  # @@protoc_insertion_point(class_scope:commander.QueryResult)
  })
_sym_db.RegisterMessage(QueryResult)

CmdInfo = _reflection.GeneratedProtocolMessageType('CmdInfo', (_message.Message,), {
  'DESCRIPTOR' : _CMDINFO,
  '__module__' : 'bodyinfo_pb2'
  # @@protoc_insertion_point(class_scope:commander.CmdInfo)
  })
_sym_db.RegisterMessage(CmdInfo)

InitInfo = _reflection.GeneratedProtocolMessageType('InitInfo', (_message.Message,), {
  'DESCRIPTOR' : _INITINFO,
  '__module__' : 'bodyinfo_pb2'
  # @@protoc_insertion_point(class_scope:commander.InitInfo)
  })
_sym_db.RegisterMessage(InitInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _HEAD._serialized_start=2144
  _HEAD._serialized_end=2349
  _BODYSHAPE._serialized_start=2351
  _BODYSHAPE._serialized_end=2437
  _BODYTYPE._serialized_start=2439
  _BODYTYPE._serialized_end=2489
  _BODYSKIN._serialized_start=2492
  _BODYSKIN._serialized_end=2689
  _BODYSKINTYPE._serialized_start=2691
  _BODYSKINTYPE._serialized_end=2737
  _BODYSKINEXTRA._serialized_start=2739
  _BODYSKINEXTRA._serialized_end=2775
  _BODYOP._serialized_start=2778
  _BODYOP._serialized_end=3003
  _CONTACTTYPE._serialized_start=3005
  _CONTACTTYPE._serialized_end=3038
  _EVENTTYPE._serialized_start=3040
  _EVENTTYPE._serialized_end=3065
  _KEYTYPE._serialized_start=3067
  _KEYTYPE._serialized_end=3094
  _JOYSTICKMOVEDIRECTIONAL._serialized_start=3097
  _JOYSTICKMOVEDIRECTIONAL._serialized_end=3269
  _ACTIONEVENT._serialized_start=3271
  _ACTIONEVENT._serialized_end=3372
  _TOUCHINPUTID._serialized_start=3374
  _TOUCHINPUTID._serialized_end=3461
  _JOYSTICKDIRECTIONALS._serialized_start=3463
  _JOYSTICKDIRECTIONALS._serialized_end=3534
  _QUERYINFO._serialized_start=29
  _QUERYINFO._serialized_end=137
  _BODYINFO._serialized_start=140
  _BODYINFO._serialized_end=488
  _BODYSKININFO._serialized_start=491
  _BODYSKININFO._serialized_end=633
  _BODYOPINFO._serialized_start=635
  _BODYOPINFO._serialized_end=713
  _CONTACTINFO._serialized_start=715
  _CONTACTINFO._serialized_end=816
  _EVENTINFO._serialized_start=818
  _EVENTINFO._serialized_end=900
  _KEYINFO._serialized_start=902
  _KEYINFO._serialized_end=959
  _ACKINFO._serialized_start=961
  _ACKINFO._serialized_end=998
  _DIRECTIONALINFO._serialized_start=1001
  _DIRECTIONALINFO._serialized_end=1148
  _BUTTONINFO._serialized_start=1150
  _BUTTONINFO._serialized_end=1239
  _TABINFO._serialized_start=1241
  _TABINFO._serialized_end=1349
  _OBJECTPOSITION._serialized_start=1351
  _OBJECTPOSITION._serialized_end=1402
  _QUERYRESULT._serialized_start=1404
  _QUERYRESULT._serialized_end=1471
  _CMDINFO._serialized_start=1474
  _CMDINFO._serialized_end=1819
  _INITINFO._serialized_start=1822
  _INITINFO._serialized_end=2141
# @@protoc_insertion_point(module_scope)
