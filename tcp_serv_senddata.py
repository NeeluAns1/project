import os
import socket
from tqdm import tqdm

IP = socket.gethostbyname(socket.gethostname())
PORT = 4457                           # to connect server to client and establish connection
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
FILENAME = "neel.txt"
FILESIZE = os.path.getsize(FILENAME)

def main():
    """ TCP socket and connecting to the CLIENT """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect(ADDR)

    """ Sending the filename and filesize to the server. """
    data = f"{FILENAME}_{FILESIZE}"
    server.send(data.encode(FORMAT))
    msg = server.recv(SIZE).decode(FORMAT)
    print(f"CLIENT: {msg}")

    """ Data transfer. """
    bar = tqdm(range(FILESIZE), f"Sending {FILENAME}", unit="B", unit_scale=True, unit_divisor=SIZE)

    with open(FILENAME, "r") as f:
        while True:
            data = f.read(SIZE)

            if not data:
                break

            server.send(data.encode(FORMAT))
            msg = server.recv(SIZE).decode(FORMAT)

            bar.update(len(data))

    """ Closing the connection """
    server.close()

if __name__ == "__main__":
    main()