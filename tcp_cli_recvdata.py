import socket
from tqdm import tqdm

IP = socket.gethostbyname(socket.gethostname())
PORT = 4457
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"

def main():
    """ Creating a TCP client socket """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.bind(ADDR)
    client.listen()
    print("[+] Listening...")

    """ Accepting the connection from the server. """
    conn, addr = client.accept()
    print(f"[+] Client connected from {addr[0]}:{addr[1]}")

    """ Receiving the filename and filesize from the server. """
    data = conn.recv(SIZE).decode(FORMAT)
    item = data.split("_")
    FILENAME = item[0]
    FILESIZE = int(item[1])

    print("[+] Filename and filesize received from the server.")
    conn.send("Filename and filesize received".encode(FORMAT))

    """ Data transfer """
    bar = tqdm(range(FILESIZE), f"Receiving {FILENAME}", unit="B", unit_scale=True, unit_divisor=SIZE)

    with open(f"recv_{FILENAME}", "w") as f:
        while True:
            data = conn.recv(SIZE).decode(FORMAT)

            if not data:
                break

            f.write(data)
            conn.send("Data received.".encode(FORMAT))

            bar.update(len(data))

    """ Closing connection. """
    conn.close()
    client.close()

if __name__ == "__main__":
    main()
