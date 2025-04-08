from PodSixNet.Channel import Channel
from PodSixNet.Server import Server

class ClientChannel(Channel):
    def Network(self, data):
        pass

class GameServer(Server):
    channelClass = ClientChannel

    def Connected(self, channel: ClientChannel, addr: str):
        pass
