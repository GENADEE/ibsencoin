import rsa
import json
import time

def verify_transaction_part(transaction):
  #loads transaction part from json string.
  otransaction = json.loads(json.loads(transaction)["body"])
  #checks that transaction is not expired
  if otransaction["timeout"] < time.time():
    return false
  #gets total value of inputs.
  tv = 0
  for uo in otransaction["inputs"]:
    tv += get_unspent_value(uo)
  #checks that total value of outputs for the group of transactions does not exceed the total vlaue of inputs.
  if tv < otransaction["n"] + otransaction["v"]:
    return false
  tov = 0
  #finds total value of outputs and and makes sure it equals declared value of outputs
  for o in otransaction["outputs"]:
    tov += o["v"]
  if tov != v:
    return false
  #finally, checks whether the signatures are valid. 
  return check_transaction_signatures(transaction)

#unimplemented. Checks whether or not uo represents a valid unspent output. If not, returns 0. Otherwise, returns the value of the unspent output represented by uo. 
def get_unspent_value(uo):
  return 1
#unimplemented. Checks whehter a transaction was signed by all of its inputs.
def check_transaction_signatures(transaction):
  return True 
