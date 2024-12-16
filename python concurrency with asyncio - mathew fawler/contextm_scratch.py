# intention is to make a context manager to fully
# understand how it works and processes data internallly.
import asyncio
from types import TracebackType
from typing import Type
import socket

class ContextConnection():
    def __init__(self, server):
        self._connection = None
        self._server = server
    
    async def __aenter__(self):
        loop = asyncio.get_event_loop()
        connection , address = await loop.sock_accept(self._server)
        print(f"We Got a new connection -> {connection}")
        self._connection = connection
        return connection
    

    async def __aexit__(self,
                        exc_type: Type[BaseException] | None,
                        exc_val: BaseException | None,
                        exc_tb: TracebackType | None):
        print("Exiting context manager")
        self._connection.close() # pyright: ignore[reportOptionalMemberAccess]
        print("Closed connection")


async def main():
    loop = asyncio.get_event_loop()

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("127.0.0.1", 8000))
    server_socket.setblocking(False)
    server_socket.listen()

    async with ContextConnection(server_socket) as connection:
        data = loop.sock_recv(connection, 1024)
        print(data) 

print(asyncio.run(main))