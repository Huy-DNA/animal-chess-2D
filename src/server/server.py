from http.server import BaseHTTPRequestHandler, HTTPServer


class GameClientRequestHandler(BaseHTTPRequestHandler):
    pass


class GameServer:
    __ip: str
    __port: int
    __server: HTTPServer

    def __init__(self, *, ip: str = "0.0.0.0", port: int = 8686):
        self.__ip = ip
        self.__port = port
        self.__server = HTTPServer((ip, port), GameClientRequestHandler)

    def start_server(self):
        print(f"Server listening on {self.__ip}:{self.__port}")
        self.__server.serve_forever()
