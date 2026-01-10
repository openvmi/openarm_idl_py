from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor
DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
description: _descriptor.FieldDescriptor
IS_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
is_supported: _descriptor.FieldDescriptor

class SetJointEnableStateRequest(_message.Message):
    __slots__ = ()
    JOINT_ID_FIELD_NUMBER: _ClassVar[int]
    IS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    joint_id: int
    is_enabled: bool
    def __init__(self, joint_id: _Optional[int] = ..., is_enabled: _Optional[bool] = ...) -> None: ...

class SetJointEnableStateResponse(_message.Message):
    __slots__ = ()
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    def __init__(self, success: _Optional[bool] = ..., message: _Optional[str] = ...) -> None: ...

class SetJointZeroPositionRequest(_message.Message):
    __slots__ = ()
    JOINT_ID_FIELD_NUMBER: _ClassVar[int]
    joint_id: int
    def __init__(self, joint_id: _Optional[int] = ...) -> None: ...

class SetJointZeroPositionResponse(_message.Message):
    __slots__ = ()
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    def __init__(self, success: _Optional[bool] = ..., message: _Optional[str] = ...) -> None: ...

class SetJointMinPositionRequest(_message.Message):
    __slots__ = ()
    JOINT_ID_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    joint_id: int
    position: int
    def __init__(self, joint_id: _Optional[int] = ..., position: _Optional[int] = ...) -> None: ...

class SetJointMinPositionResponse(_message.Message):
    __slots__ = ()
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    def __init__(self, success: _Optional[bool] = ..., message: _Optional[str] = ...) -> None: ...

class SetJointMaxPositionRequest(_message.Message):
    __slots__ = ()
    JOINT_ID_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    joint_id: int
    position: int
    def __init__(self, joint_id: _Optional[int] = ..., position: _Optional[int] = ...) -> None: ...

class SetJointMaxPositionResponse(_message.Message):
    __slots__ = ()
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    def __init__(self, success: _Optional[bool] = ..., message: _Optional[str] = ...) -> None: ...

class SetJointMaxSpeedRequest(_message.Message):
    __slots__ = ()
    JOINT_ID_FIELD_NUMBER: _ClassVar[int]
    SPEED_FIELD_NUMBER: _ClassVar[int]
    joint_id: int
    speed: int
    def __init__(self, joint_id: _Optional[int] = ..., speed: _Optional[int] = ...) -> None: ...

class SetJointMaxSpeedResponse(_message.Message):
    __slots__ = ()
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    def __init__(self, success: _Optional[bool] = ..., message: _Optional[str] = ...) -> None: ...

class SetJointMaxAccelerationRequest(_message.Message):
    __slots__ = ()
    JOINT_ID_FIELD_NUMBER: _ClassVar[int]
    ACCELERATION_FIELD_NUMBER: _ClassVar[int]
    joint_id: int
    acceleration: int
    def __init__(self, joint_id: _Optional[int] = ..., acceleration: _Optional[int] = ...) -> None: ...

class SetJointMaxAccelerationResponse(_message.Message):
    __slots__ = ()
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    def __init__(self, success: _Optional[bool] = ..., message: _Optional[str] = ...) -> None: ...
