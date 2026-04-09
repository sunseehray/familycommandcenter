import socket
import os
from dotenv import load_dotenv

load_dotenv()

SERVER_IP = os.getenv("SERVER_IP")
PORT = int(os.getenv("PORT"))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, PORT))

while True:
        msg = input("You: ")
        client.send(msg.encode())

        reply = client.recv(1024).decode()
        print(f"[SERVER]: {reply}")