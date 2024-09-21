from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ModelTrainerRequest(_message.Message):
    __slots__ = ("code",)
    CODE_FIELD_NUMBER: _ClassVar[int]
    code: str
    def __init__(self, code: _Optional[str] = ...) -> None: ...

class ModelTrainerResponse(_message.Message):
    __slots__ = ("log",)
    LOG_FIELD_NUMBER: _ClassVar[int]
    log: str
    def __init__(self, log: _Optional[str] = ...) -> None: ...
