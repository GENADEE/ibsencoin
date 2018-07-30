import hashlib
import scrypt
import random

# some nonce
# the block has already had the new elements appended
# block is already serialized as a string

# the condition we check is : sufficient amount of leading zeroes
#
# difficulty is the number of bits that are all zero
def verify_pow(block_str,difficulty):
    test = int.from_byte(scrypt.hash(block_str,""), byteorder='big')
    return test <= 2**((64*8)-difficulty)-1

# we'll see about this method
# mining (append the proof of work)
# retunr the new block string
#def pow_step(block_str,difficulty):
#    # we want to generate a random string
#    random.randint(2,2**(32))
#    pass

# mine until it's solved
def pow(block_str,difficulty):
    for i in range(1,2**32):
        value = block_str + str(int.to_bytes(i,byteorder='big'),'utf-8') #pow_step(block_str,difficulty)

        if verify_pow(value,difficulty):
            return value # new block string

        pass

    pass