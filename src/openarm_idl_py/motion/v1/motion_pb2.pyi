from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MoveJRequest(_message.Message):
    __slots__ = ()
    VELOCITY_FIELD_NUMBER: _ClassVar[int]
    JOINT_POSITIONS_FIELD_NUMBER: _ClassVar[int]
    velocity: int
    joint_positions: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, velocity: _Optional[int] = ..., joint_positions: _Optional[_Iterable[int]] = ...) -> None: ...

class MoveJResponse(_message.Message):
    __slots__ = ()
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    def __init__(self, success: _Optional[bool] = ..., message: _Optional[str] = ...) -> None: ...

class JogJointRequest(_message.Message):
    __slots__ = ()
    JOINT_ID_FIELD_NUMBER: _ClassVar[int]
    VELOCITY_FIELD_NUMBER: _ClassVar[int]
    joint_id: int
    velocity: int
    def __init__(self, joint_id: _Optional[int] = ..., velocity: _Optional[int] = ...) -> None: ...

class JogJointResponse(_message.Message):
    __slots__ = ()
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    def __init__(self, success: _Optional[bool] = ..., message: _Optional[str] = ...) -> None: ...
