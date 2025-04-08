from PodSixNet.Channel import Channel
from PodSixNet.Server import Server


class ClientChannel(Channel):
    def Network(self, data):
        pass


class GameServer(Server):
    channelClass = ClientChannel

    def __init__(self, *, ip: str = "0.0.0.0", port: int = 8686, listeners=10):
        print(f"Server listening on {ip}:{port}...")
        super().__init__(localaddr=(ip, port), listeners=listeners)

    def Connected(self, channel: ClientChannel, addr: str):
        pass
