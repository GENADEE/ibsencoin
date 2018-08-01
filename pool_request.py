# when called, sends request to the transaction pooling server.
# Once a pool has been found and agreed on, it returns a pool object
#   to the client by calling the callback function.
# param: request is a pool_request object.
# param: callback is a function. It had no return value, and it takes one argument, a pool object.
#   It is called to respond to the request.
def request_pool(request, callback):
  pass

#An object representing a request to pool transactions; specifying the inputs that the requester is offering to put in the pool, the minimum and maximum number of transactions to pool together and the value of the transactions to pool, along with an timeout specifying the unix time at which the request expires. 
class pool_request:

  #inputs lists the inputs that the sender is offering to put in the pool. It is a list of 2-tuples pairing an unspent output and a function of format (hash) -> signature that signs a hash with the private key associated with the unspent output. 
  #  !!!!! The private keys inside the signing function MUST NOT be sent over the network for obvious security reasons.
  # n_range is a tuple specifying the minimum and maximum numbers of transactions in the pool.
  # v specifies the value of each transaction in the pool
  # timeout is a unix timestamp specifying when the request should expire. 
  def __init__(self, inputs, n_range, v, timeout):
    self.inputs = inputs
    self.n_range = n_range
    self.v = v
    self.timeout = timeout


# An object representing a pool of IbsenCoin senders.
# Consensus on the composition of the pool should be verified before the pool object is returned to the requester. 
class pool:

  #the n property specifies the number of senders in the pool.
  @property
  def n(self):
    return self.n

  #the v property specifies the value of each transaction in the pool.
  @property
  def v(self):
    return self.v

  #the inputs property lists the inputs. It consists of a list of 2-tuples, where the first member is the input, and the second member is a function that gets the signature from that input. The signing function takes two arguments, the hash to sign and a callback taking one argument, the signature, to call once the signing is finished. 
  @property
  def inputs(self):
    return self.inputs

