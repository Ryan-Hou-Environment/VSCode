from _typeshed import Incomplete, Self
from asyncio import AbstractEventLoop
from collections.abc import Callable
from logging import Logger

from ..connection import Parameters
from .base_connection import BaseConnection
from .utils import io_services_utils, nbio_interface

LOGGER: Logger

class AsyncioConnection(BaseConnection):
    def __init__(
        self: Self,
        parameters: Parameters | None = ...,
        on_open_callback: Callable[[Self], object] | None = ...,
        on_open_error_callback: Callable[[Self, BaseException], object] | None = ...,
        on_close_callback: Callable[[Self, BaseException], object] | None = ...,
        custom_ioloop: AbstractEventLoop | None = ...,
        internal_connection_workflow: bool = ...,
    ) -> None: ...
    @classmethod
    def create_connection(
        cls, connection_configs, on_done, custom_ioloop: AbstractEventLoop | None = ..., workflow: Incomplete | None = ...
    ): ...

class _AsyncioIOServicesAdapter(
    io_services_utils.SocketConnectionMixin,
    io_services_utils.StreamingConnectionMixin,
    nbio_interface.AbstractIOServices,
    nbio_interface.AbstractFileDescriptorServices,
):
    def __init__(self, loop: Incomplete | None = ...) -> None: ...
    def get_native_ioloop(self): ...
    def close(self) -> None: ...
    def run(self) -> None: ...
    def stop(self) -> None: ...
    def add_callback_threadsafe(self, callback) -> None: ...
    def call_later(self, delay, callback): ...
    def getaddrinfo(self, host, port, on_done, family: int = ..., socktype: int = ..., proto: int = ..., flags: int = ...): ...
    def set_reader(self, fd, on_readable) -> None: ...
    def remove_reader(self, fd): ...
    def set_writer(self, fd, on_writable) -> None: ...
    def remove_writer(self, fd): ...

class _TimerHandle(nbio_interface.AbstractTimerReference):
    def __init__(self, handle) -> None: ...
    def cancel(self) -> None: ...

class _AsyncioIOReference(nbio_interface.AbstractIOReference):
    def __init__(self, future, on_done) -> None: ...
    def cancel(self): ...
