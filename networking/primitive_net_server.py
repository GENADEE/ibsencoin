# on startup will designate sockets and ports for communcation
# it has a handle command which a message and can respond to it
# for now it stores stuff in memory

# similarly to nodes.json the sockets should have the format
#   { nodename : node_information }
# and node_information has the format
#   {'address' : address , 'port' : port }

import socket

class Net_Server:
    # has self.sockets which is a map of sockets with names for their purposes (ie pooling, etcetera)

    # add something to choose your own sockets
    def __init__(self):
        # default server will have only one socket because ok doke
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostname()
        port = 8862 # later change from hardcode because you get address already in use errors
        sock.bind((host, port)) 

        self.sockets = { 'main' :  sock }
        self.poll()
        pass

    def poll(self):
        for name,sock in self.sockets.iteritems():
            #print sock
            sock.listen(5)
            while True:
                print 'hi'
                connec, addr = sock.accept()
                print 'Got connection from', addr
                connec.send('Thank you for connecting')
                connec.close()
                pass
            pass
        pass
pass