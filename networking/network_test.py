# this is from a tutorial
# OK I'LL USE THE HTTP SERVER AFTER I FINISH PRIMITIVE SERVER AND CLIENT USING RAW TCP

import socket

'''
HOST, PORT = '', 8888

# AF_INET is better because AF_UNIX uses a file on your system or something wierd
# SOCK_STREAM is better for TCP while SOCK_DGRAM is better for UDP (and obviously we want to use TCP here)
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(5)

print 'Serving HTTP on port %s ...' % PORT
while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    print request

    http_response = """\
HTTP/1.1 200 OK

Hello, World!
"""
    client_connection.sendall(http_response)
    client_connection.close()

# ^^^ this works fine

'''
# most of the following is from 
# https://www.tutorialspoint.com/python/python_networking.htm

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname() # Get local machine name
print host
port = 8887                # Reserve a port for your service.
sock.bind((host, port))        # Bind to the port

sock.listen(5)                 # Now wait for client connection.
while True:
   connec, addr = sock.accept()     # Establish connection with client.
   print 'Got connection from', addr
   connec.send('Thank you for connecting') #this doesn't work for browser, etcetera... but does work for client
   connec.close()                # Close the connection

'''
### CLIENT CODE
s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.

s.connect((host, port))
print s.recv(1024)
s.close                     # Close the socket when done
'''