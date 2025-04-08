import os
from dotenv import load_dotenv
from PodSixNet.Connection import ConnectionListener

load_dotenv()
SERVER_ADDRESS = os.getenv("SERVER_ADDRESS") or "0.0.0.0"
SERVER_PORT = int(os.getenv("SERVER_PORT") or 8686)
connection = ConnectionListener()
connection.Connect((SERVER_ADDRESS, SERVER_PORT))
