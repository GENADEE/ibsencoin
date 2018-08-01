# on startup connects to the first available node with a socket (servers may use more than one socket which can designate information)
# node urls, etcetera are stored on a json file
# when prompted it can send a message to the server

# nodes.txt should have the format
#   { nodename : node_information }
# and node_information has the format
#   {'address' : address , 'port' : port }

import socket
import json

class Net_Client:

    def __init__(self):
        self.nodes = {}
        try:
            with open('nodes.txt') as json_file:  
                self.nodes = json.load(json_file)
                print(nodes)
                pass
            pass
        except:
            print('Failed to find nodes.txt, please put a json in the proper format inside a new nodes.txt')
            pass
        pass
    
    def connect(self):
        for node in self.nodes:
            try:
                # try to connect to the first one possible
                self.connect(node)
                return
            except:
                # go to the next one
                pass
            pass
        pass

    def connect(self,node):
        try:
            sock = socket.socket()
            host = node['address']
            port = node['port']

            sock.connect((host, port))
            self.onconnect(sock.recv(1024))
            sock.close          

            pass

        except:
            print('whoops couldn't do onconnect)
            pass
        pass

    def onconnect(self,message):
        print(message)
        pass

pass