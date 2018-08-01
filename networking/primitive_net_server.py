# on startup will designate sockets and ports for communcation
# it has a handle command which a message and can respond to it
# for now it stores stuff in memory

import socket

class Net_Server:
    # has self.sockets which is a map of sockets with names for their purposes (ie pooling, etcetera)
    def __init__(self):
        # default server will have only one socket because ok doke
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostname()
        port = 8887
        sock.bind((host, port)) 

        self.sockets = { 'main' :  sock }
        self.poll()
        pass

    def __init__(self, sockets):
        self.sockets = sockets
        pass

    def poll(self):
        for sock in sockets:
            sock.listen(5)
            while True:
                connec, addr = sock.accept()
                print 'Got connection from', addr
                connec.send('Thank you for connecting')
                connec.close()
                pass
            pass
        pass
pass