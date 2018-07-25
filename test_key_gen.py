import rsa
import json

while True:
  key, pk = rsa.newkeys(1024)
  print(json.dumps({'n': pk.n, 'e': pk.e, 'd': pk.d, 'p': pk.p, 'q': pk.q}))

