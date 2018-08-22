# on startup connects to the first available node with a socket (servers may use more than one socket which can designate information)
# node urls, etcetera are stored on a json file
# when prompted it can send a message to the server

# nodes.json should have the format
#   { nodename : node_information }
# and node_information has the format
#   {'address' : address , 'port' : port }

import socket
import json

class Net_Client:

    def __init__(self):
        self.nodes = {}
        try:
            with open('nodes.json') as json_file:  
                self.nodes = json.load(json_file)
                print('found nodes.json')
                #print(self.nodes)
                pass
            pass
        except:
            print('Failed to find nodes.json, trying to write a default.')
            default = {'firstnode':{'address':'dontminbitcoins.attlocal.net','port':8862}}
            with open('nodes.json', 'w') as outfile:
                json.dump(default, outfile)
            pass
        pass
    
    def connect(self):
        #print self.nodes
        for name in self.nodes:
            node = self.nodes[name]
            #print node
            try:
                # connection
                #print 'hi'
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                host = node['address']
                port = node['port']
                #print host #works
                #print port
                sock.connect((host, port))
                #onconnect(sock.recv(1024))
                sock.close
                return
            except:
                # try the next one
                pass
            pass

        pass
        

    def onconnect(self,message):
        print(message)
        pass

pass