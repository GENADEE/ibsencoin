import hashlib
import json
from time import time
from urllib.parse import urlparse
from uuid import uuid4

import requests
from flask import Flask, jsonify, request


# based on blockchain.py from 'https://hackernoon.com/learn-blockchains-by-building-one-117428612f46'

# each transaction is a json akin to those from blockchain.py, however each transaction encapsulates the flow of money
# throughout a group of people rather than two individuals, since we are using group signing for anonnymity

# each node has a copy of the blockchain in chain, the set of other nodes, and the current transactions going on
class Blockchain:
	def __init__(self):

		self.current_transactions = []
		self.chain = [] #stores the list of blocks before it (each block will store the hash of the previous)
		self.nodes = set() #set of nodes

		pass

		#
		# PLEASE ADD BLOCKCHAIN FUNCTIONALITY
		#

		# FIX ME PLEASE
		def new_block(self, proof, previous_hash):
	        """
	        Create a new Block in the Blockchain

	        :param proof: The proof given by the Proof of Work algorithm
	        :param previous_hash: Hash of previous Block
	        :return: New Block
	        """

	        block = {
	            'index': len(self.chain) + 1,
	            'timestamp': time(),
	            'transactions': self.current_transactions,
	            'proof': proof,
	            'previous_hash': previous_hash or self.hash(self.chain[-1]),
	        }

	        # Reset the current list of transactions
	        self.current_transactions = []

	        self.chain.append(block)
	        return block

	pass


# Instantiate the Node
app = Flask(__name__)

# Generate a globally unique address for this node
node_identifier = str(uuid4()).replace('-', '')

# Instantiate the Blockchain
blockchain = Blockchain()

#
# PLEASE ADD NODE SERVER FUNCTIONALITY
#

if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app.run(host='0.0.0.0', port=port)
