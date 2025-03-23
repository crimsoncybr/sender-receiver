import socket
import os
import tqdm

IP_SERVER = "127.0.0.1"
PORT = 4548
ADDR = (IP_SERVER, PORT)
BUFFER_SIZE = 4096

reciver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
reciver.bind(ADDR)
reciver.listen(1)

print("[+] Waiting for connection...")
client, addr = reciver.accept()
print(f"[+] Connected by {addr}")

# Read until two newlines: file name and file size
metadata = b""
newline_count = 0
while newline_count < 2:
    byte = client.recv(1)
    if not byte:
        break
    metadata += byte
    if byte == b'\n':
        newline_count += 1

# Split metadata safely
file_name, file_size = metadata.decode().split("\n", 1)
file_size = int(file_size.strip())

print(f"[+] Receiving '{file_name}' ({file_size} bytes)")

# Set up progress bar
progress = tqdm.tqdm(range(file_size), f"Receiving {file_name}", unit="B", unit_scale=True)

# Receive and save file
with open(file_name, "wb") as f:
    while True:
        data = client.recv(BUFFER_SIZE)
        if b"<END>" in data:
            data = data.replace(b"<END>", b"")
            f.write(data)
            progress.update(len(data))
            break
        f.write(data)
        progress.update(len(data))

progress.close()
print(f"[+] File '{file_name}' received successfully.")

client.close()
reciver.close()
