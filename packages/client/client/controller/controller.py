import os
from dotenv import load_dotenv
from controller.network import ServerConnector
from ui.matchmaking_scene import MatchmakingScene
from pygame.surface import Surface


class NetworkGameController:
    def __init__(self, screen: Surface):
        load_dotenv()

        server_ip = os.getenv("SERVER_IP", "localhost")
        server_port = int(os.getenv("SERVER_PORT", "5555"))

        self.connector = ServerConnector(ip=server_ip, port=server_port)

        self.matchmaking_scene = MatchmakingScene(screen, self.connector)

    def get_matchmaking_scene(self):
        return self.matchmaking_scene
