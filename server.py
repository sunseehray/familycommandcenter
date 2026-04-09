import socket

HOST = '0.0.0.0'  # listen on all interfaces
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"[SERVER] Listening on {HOST}:{PORT}")

conn, addr = server.accept()
print(f"[CONNECTED] {addr} connected.")

while True:
    message = conn.recv(1024).decode()
    if not message:
        break
    print(f"[CLIENT]: {message}")

    reply = input("You: ")
    conn.send(reply.encode())

conn.close()