print 'testing...'
# test it here

from primitive_net_client import Net_Client
from primitive_net_server import Net_Server

# multithread this or change infinite loop please

#server = Net_Server()
#server.poll()
client = Net_Client()
client.connect()