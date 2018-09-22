# check out https://hackernoon.com/learn-blockchains-by-building-one-117428612f46
# which gives a different blockchain implementation using python, but which uses
# an http server which I try to copy here
#
#
# (whatabout http://ecomunsing.com/build-your-own-blockchain)
# flask run --host=0.0.0.0 to make it readable from other computers on the network
from .. import node # fix this import please
import json
from uuid import uuid4

from flask import Flask

identifier = str(uuid4()).replace('-', '')

app = Flask(__name__)

# this is an example app route
@app.route('/')
def hello_world():
    return 'Hello, World!'

# requests for pool and transaction will provide conditions for the requests to be met

# params for pool should be {'size':<int:size>,'amount':<int:amount>}
@app.route('/request_pool', methods=['POST'])
def request_pool():
    values = request.get_json()
    return 'please wait'

# once a pool has been accepted, the node will be able to verify transaction presented by a client
# transaction should be a json with inputs, n_output_groups, v_output_groups, output_group, and timeout parameters
# where (as in the client python file):
#inputs: a list of unspent outputs. The format of an unspent output is a tuple of the format (transaction, pkey), where transaction is the hash of a complete signed, confirmed, transaction in the blockchain, and pkey is the public key associated with the ouput of that transaction to be spent.
#n_output_groups: specifies the number of output groups; ie. the number of transactions that share the same input as this one, including this one. 
#v_output_groups: specifies the value of each output group.
#output_group: lists the outputs to this part of this transaction; the form is a list of tuples of the format (value, key).
#timeout: unix time after which the transaction becomes invalid if it has not been confirmed. 
@app.route('/verify_transaction', methods=['POST'])
def verify_transaction():
    values = request.get_json()
    node.verify_transaction_part(values) # fix this
    return 'verifying'



# ok, so the easiest way to do this will be to run a flask server for our nodes and then have the clients send requests