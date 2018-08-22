import hashlib

#sha512 hash. 
def digest(msg):
  h = hashlib.sha512()
  h.update(bytes(msg, 'utf-8'))
  return int.from_bytes(h.digest(), byteorder='big')

