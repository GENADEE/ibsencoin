import socket

### CLIENT CODE
sock = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 8887             # Reserve a port for your service.

sock.connect((host, port))
print sock.recv(1024)
sock.close                     # Close the socket when done