# check out https://hackernoon.com/learn-blockchains-by-building-one-117428612f46
# which gives a different blockchain implementation using python, but which uses
# an http server which I try to copy here
#
#
# (whatabout http://ecomunsing.com/build-your-own-blockchain)
# flask run --host=0.0.0.0 to make it readable from other computers on the network
import hashlib
import json
from textwrap import dedent
from time import time
from uuid import uuid4

from flask import Flask
class NServer:
    # has instance of coin server/node object
    def __init__(self):
        '''
        # Instantiate our Node
        self.app = Flask(__name__)

        # Generate a globally unique address for this node/server
        self.identifier = str(uuid4()).replace('-', '')

        @app.route('/test', methods=['GET']) #test response
        '''
        pass
    pass

print 'start'

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
@app.route('/request_pool', methods=['POST'])
def request_pool():
     values = request.get_json()
    return 'please wait'
@app.route('/verify_transaction', methods=['POST'])
def verify_transaction():
     values = request.get_json()
    return 'verifying'

print 'end'


# ok, so the easiest way to do this will be to run a flask server for our nodes and then have the clients send requests