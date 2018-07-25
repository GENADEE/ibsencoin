import rsa
import json
import hashlib
import random

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
  return rsa.core.decrypt_int(blind, pkey.d, pkey.n)

def verify_blind_signature(transaction, key, r, signature):
  m = digest(transaction)
  m1 = rsa.core.encrypt_int(key.unblind(signature, r), key.e, key.n)
  return m == m1
  


