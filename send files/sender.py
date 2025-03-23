import os
import socket

# recive a file parh from the user
file_path = input("Please choose a file to send: ")

# ensure the file exists
if not os.path.exists(file_path):
    print("File not found, choose an existing file")
    exit()

file_name = os.path.basename(file_path)


# Server details

IP_SERVER = "127.0.0.1"  
PORT = 4548
ADDR = (IP_SERVER, PORT)





# Create a socket and connect
sender =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sender.connect(ADDR)

with open(file_path, "rb") as file:
    file_size = os.path.getsize(file_path)

    # Send file name and size (add newline after both)
    sender.send(f"{file_name}\n{file_size}\n".encode())


    # Read and send the file data

    while data := file.read(4096):  
        sender.sendall(data)

# Send end marker
sender.send(b"<END>")


# Close the connection
sender.close()

print(f"File '{file_name}' sent successfully.")
