from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ImageLoaderRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ImageLoaderResponse(_message.Message):
    __slots__ = ("isFinished",)
    ISFINISHED_FIELD_NUMBER: _ClassVar[int]
    isFinished: bool
    def __init__(self, isFinished: bool = ...) -> None: ...
