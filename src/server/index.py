from server import GameServer
from time import sleep

server = GameServer()
while True:
    server.Pump()
    sleep(0.0001)
