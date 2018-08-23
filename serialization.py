import json
import rsa
import cryptography

# both unimplemented; using default json for now
# json not necessarily order preserving; may not always work.

def encode(obj):
  return json.dumps(obj)

def decode(code):
  return json.loads(code)

def listSerialize(l):
  r = bytes.fromhex('01') + len(l).to_bytes(8, byteorder = 'big')
  for i in l:
    r += i.serialize()
  return r

def listDeserialize(data, deserialize):
  if not data[0]:
    return (None, data[1:])
  length = int.from_bytes(data[1:9], byteorder = 'big')
  data = data[9:]
  l = []
  while length > 0:
    i, data = deserialize(data)
    l += [i]
    length -= 1
  return l


class Output:
  def __init__(self, key, transaction_hashref, value):
    self.key = key
    self.transaction_hashref = transaction_hashref
    self.value = value
  def serialize(self):
    return bytes.fromhex('01') +  ( self.key.serialize() if self.key is not None else bytes.fromhex('00') ) +( self.transaction_hashref.serialize() if self.transaction_hashref is not None else bytes(64) ) + self.value.to_bytes(8, byteorder = 'big')
  #where data is an array of bytes
  def deserialize(data):
    if data[0]:
      key, data = PublicKey.deserialize(data[1:])
      transaction_hashref, data = Transaction_hashref.deserialize(data)
      value = int.from_bytes(data[:8], byteorder = 'big')
      return (Output(key, transaction_hashref, value), data[8:])
    return (None, data[1:])

class Entry: 
  def __init__(self, pkey, output):
    self.pkey = pkey
    self.output = output
  def serialize(self):
    return bytes.fromhex('01') + ( self.pkey.serialize() if self.pkey is not None else bytes.fromhex('00') ) + ( self.output.serialize() if self.output is not None else bytes.fromhex('00') )
  def deserialize(data):
    if data[0]:
      pkey, data = PrivateKey.deserialize(data[1:])
      output, data = Output.deserialize(data)
      return (Entry(pkey, output), data)
  @property
  def value(self):
    return (self.output or 0) and self.output.value

class Transaction_hashref:
  def __init__(self, thash):
    self.thash = thash
  def from_transaction(transaction):
    return Transaction_hashref(cryptography.digest(transaction.serialize()))
  def as_int(self):
    return int.from_bytes(thash, byteorder='big')
  def serialize(self):
    return thash
  def deserialize(data):
    return (Transaction_hashref(data[:64]), data[64:])


class PublicKey:
  def __init__(self, key):
    self.key = key
  def serialize(self):
    return bytes.fromhex('01') + self.key.n.to_bytes(128, byteorder = 'big') + self.key.e.to_bytes(8, byteorder = 'big')
  def deserialize(data):
    return (PublicKey(rsa.PublicKey(int.from_bytes(data[1:129], byteorder = 'big'), int.from_bytes(data[129:137], byteorder = 'big'))), data[137:]) if data[0] else (None, data[1:])

class PrivateKey: 
  def __init__(self, pkey):
    self.pkey = pkey
  def serialize(self):
    return bytes.fromhex('01') + self.pkey.n.to_bytes(128, byteorder = 'big') + self.pkey.e.to_bytes(8, byteorder = 'big') + self.pkey.d.to_bytes(128, byteorder = 'big') + self.pkey.p.to_bytes(96, byteorder = 'big') + self.pkey.q.to_bytes(96, byteorder = 'big')
  def deserialize(data):
    return (PrivateKey(rsa.PrivateKey(int.from_bytes(data[1:129], byteorder = 'big'), int.from_bytes(data[129:137], byteorder = 'big'), int.from_bytes(data[137:265], byteorder = 'big'), int.from_bytes(data[265:361], byteorder = 'big'), int.from_bytes(data[361:457], byteorder = 'big'))), data[457:]) if data[0] else (None, data[1:])
