#where onReceive and onVerify are callbacks for when a transaction is correctly received by the server and when the transaction is verified along with its cotransactions, respectively.
def post_transaction(transaction, onReceive=None, onVerify=None):
  pass

#gets all unspent outputs associated with the public key, address, and returns them using the callback.
def get_value(address, callback):
  pass

#asks the node to notify the client through callback if address receives a transaction. The node should respond immediately if a transaction has already happened after the time specified by since, and should stop listening after timeout. 
def listen(address, since, timeout, callback):
  pass
