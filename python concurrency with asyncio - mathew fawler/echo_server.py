import socket
import asyncio
import select
import selectors
from typing import Tuple, List
from selectors import SelectorKey

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

address = ("127.0.0.1", 8000)
server_socket.bind(address)
server_socket.setblocking(False)
server_socket.listen()
selector = selectors.DefaultSelector()
select.register()

selector.register(server_socket)

try:
    while True:
        events: List[Tuple[SelectorKey, int]] = selector.select(timeout=1)
        if len(events) == 0:
            print("No New Event")
        
        for event , _ in events:
            event_socket = event.fileobj

            if event_socket == server_socket:
                print("New Connection is Here...")
                connection, address = socket.accept()
                buffer = b''
                while buffer[-2:] != '\r\n':
                    data = connection.recv(2)
                    if not data:
                        break
                    buffer += data
                print(f"All the data is: {buffer}")
                connection.sendall(buffer)
        break
finally:
    server_socket.close()