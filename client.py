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
  return json.dump([inputs, n_output_groups, v_output_groups, output_group, timeout])


