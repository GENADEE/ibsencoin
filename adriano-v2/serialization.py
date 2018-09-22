import json

# both unimplemented; using default json for now
# json not necessarily order preserving; may not always work.

def encode(obj):
  return json.dumps(obj)

def decode(code):
  return json.loads(code)
