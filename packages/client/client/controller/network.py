from PodSixNet.Connection import ConnectionListener, connection
from PodSixNet.EndPoint import EndPoint


class ServerConnector(ConnectionListener):
    __connection: EndPoint

    def __init__(self, *, ip: str, port: int):
        super().__init__()
        self.__connection = connection
        connection.DoConnect((ip, port))

    def Network_error(self, data):
        pass

    def Send(self, data):
        self.__connection.Send(data)

    def Pump(self):
        super().Pump()
        self.__connection.Pump()
