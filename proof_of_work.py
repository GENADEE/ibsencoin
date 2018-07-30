import hashlib

# some nonce
# the block has already had the new elements appended
# block is already serialized as a string
def verify_pow(block_str,difficulty):
    #scrypt here
    return False