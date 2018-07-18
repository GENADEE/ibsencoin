import rsa
import json

#creates an unsigned transaction.
#params:
#inputs: a list of unspent outputs. The format of an unspent output is a tuple of the format (transaction, pkey), where transaction is the hash of a complete signed, confirmed, transaction in the blockchain, and pkey is the public key associated with the ouput of that transaction to be spent.
#n_output_groups: specifies the number of output groups; ie. the number of transactions that share the same input as this one, including this one. 
#v_output_groups: specifies the value of each output group.
#output_group: lists the outputs to this part of this transaction; the form is a list of tuples of the format (value, pkey).
#timeout: unix time after which the transaction becomes invalid if it has not been confirmed. 
def create_transaction(inputs, n_output_groups, v_output_groups, output_group, timeout):
  return json.dumps({'inputs': inputs, 'n': n_output_groups, 'v': v_output_groups, 'outputs': output_group, 'timeout': timeout})

def create_transaction_blinds(transaction):
  otransaction = json.loads(transaction)
  m = digest(transaction) 
  blinds = []
  for i in otransaction['inputs']:
    key = rsa.PublicKey(i['key']['n'],i['key']['e'])
    r = 0
    blind = 0  
    while blind  == 0:
      r = random.randrange(3*2^4094, 2^4096)
      blind = key.blind(m,r)
    blinds += [['input': i, 'r': r, 'blind': blind]]
  return blinds


def digest(msg):
  h = hashlib.sha512()
  h.update(bytes(msg, 'utf-8'))
  return int.from_bytes(h.digest(), byteorder='big')

