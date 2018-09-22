#
# PLEASE GET RID OF UNECESSARY IMPORTS
#

import rsa
import json
import hashlib
import random
import os
import serialization

from time import time
from urllib.parse import urlparse
from uuid import uuid4

import requests
from flask import Flask, jsonify, request

# simple client to send requests to node and store information

# a client will remember wallet values, have a copy of the blockchain (which can be updated from a node),
# and be able to engage with nodes and other clients to do transactions, etcetera...

#creates an unsigned transaction.
#params:
#inputs: a list of unspent outputs. The format of an unspent output is a tuple of the format (transaction, pkey), where transaction is the hash of a complete signed, confirmed, transaction in the blockchain, and pkey is the public key associated with the ouput of that transaction to be spent.
#n_output_groups: specifies the number of output groups; ie. the number of transactions that share the same input as this one, including this one.
#v_output_groups: specifies the value of each output group.
#output_group: lists the outputs to this part of this transaction; the form is a list of tuples of the format (value, key).
#timeout: unix time after which the transaction becomes invalid if it has not been confirmed.
def create_transaction(inputs, n_output_groups, v_output_groups, output_group, timeout):
  return json.dumps({'inputs': inputs, 'n': n_output_groups, 'v': v_output_groups, 'outputs': output_group, 'timeout': timeout})

#creates blinded hashes so that this transaction can be anonymously signed
def create_transaction_blinds(transaction):
  otransaction = json.loads(transaction)
  m = digest(transaction)
  print("m = " + str(m))
  blinds = []
  for i in otransaction['inputs']:
    key = rsa.PublicKey(i['key']['n'],i['key']['e'])
    r = 0
    blind = 0
    while blind  == 0:
      r = random.randrange(3*2^1022, 2^1022)
      print("trying r = " + str(r))
      blind = key.blind(m,r)
      print("got blind = " + str(blind))
    blinds += [{'input': i, 'r': r, 'blind': blind}]
  return blinds

#sha512 hash.
def digest(msg):
  h = hashlib.sha512()
  h.update(bytes(msg, 'utf-8'))
  return int.from_bytes(h.digest(), byteorder='big')

#where pkey is an rsa.PrivateKey
def sign_blind(pkey, blind):
  return rsa.core.decrypt_int(blind, pkey.d, pkey.n) #uses the rsa private key to sign the blind signature.

#unblinds blind signature "signature" that has been signed with the private key associuated with key and blinded with the key "key" and the random factor r.
def unblind_signature(key, signature, r):
  return key.unblind(signature, r)

#checks whether the signature is valid for the hash of the transaction once unblinded.
def verify_blind_signature(transaction, key, r, signature):
  m = digest(transaction)
  m1 = rsa.core.encrypt_int(unblind_signature(key, signature, r), key.e, key.n)
  return m == m1

class wallet:
  def __init__(self, keyfile_name, node_connection, bulletin_connection, backupdir=None, swapdir=None):
    self.keyfile_name = keyfile_name
    self.backupdir=backupdir
    self.swapdir=swapdir
    if self.backupdir==None:
      if os.path.dirname(keyfile_name)=="":
        self.backupdir="."
      else:
        self.backupdir=os.path.dirname(keyfile_name)
    if self.swapdir==None:
      if os.path.dirname(keyfile_name)=="":
        self.swapdir="."
      else:
        self.swapdir=os.path.dirname(keyfile_name)
    self.from_file(keyfile_name)

  #creates entry list from keyfile
  def from_file(self, keyfile_name):
    self.entries = []
    try:
      with open(keyfile_name) as f:
        for entry in f:
          self.entries += [serialization.decode(entry)]
    except IOError:
      pass

  #creates n new keys and adds them as empty addresses.
  def gen_keys(self, n):
    for i in range(n):
      key, pk = rsa.newkeys(1024)
      self.entries += [(pk, None, 0)]


# Instantiate the server for the client
# note that clients are also servers so they can recieve requests from other clients, etcetera...
# (this may change but will be the way it is right now)
app = Flask(__name__)

#
# PLEASE ADD NODE SERVER FUNCTIONALITY
#

# main
if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app.run(host='0.0.0.0', port=port)
