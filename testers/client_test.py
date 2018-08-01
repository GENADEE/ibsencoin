import rsa
import json
import client
import sys
import random

#test keys are piped into the client test; each i is a key.
for i in sys.stdin:
  k = json.loads(i)
  pkey = rsa.PrivateKey(k["n"], k["e"], k["d"], k["p"], k["q"])
  key = rsa.PublicKey(k["n"], k["e"])
  inputs = [{"key": {"n": key.n, "e": key.e}}]
  transaction = client.create_transaction(inputs, 1, 1, [], 1) #using dummy arguments for n, v, outputs, and timeout
  blinds = client.create_transaction_blinds(transaction)
  sig = client.sign_blind(pkey, blinds[0]["blind"]) # blind signature
  csig = sig - 1 # corrupted signature.  
  print("signature: " + str(sig))
  print(client.verify_blind_signature(transaction, key, blinds[0]["r"], sig))#verifies that it accepts proper signatures.
  print(not client.verify_blind_signature(transaction, key, blinds[0]["r"], csig))#verifies that it rejects improper signatures.  
