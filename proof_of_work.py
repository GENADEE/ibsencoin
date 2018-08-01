import hashlib
import random

#sha512 hash as int.
def digest(msg):
    h = hashlib.sha512()
    h.update(bytes(msg, 'utf-8'))
    return int.from_bytes(h.digest(), byteorder='big')
# some nonce
# the block has already had the new elements appended
# block is already serialized as a string

# the condition we check is : sufficient amount of leading zeroes
#
# difficulty is the number of bits that are all zero
def verify_pow(block_str,difficulty):
    test = digest(block_str)
    print("test is {:0128x}".format(test)) #debug
    return test <= 2**((512)-difficulty)-1

# we'll see about this method
# mining (append the proof of work)
# retunr the new block string
#def pow_step(block_str,difficulty):
#    # we want to generate a random string
#    random.randint(2,2**(32))
#    pass

# mine until it's solved
def pow(block_str,difficulty):
    i = 0
    while True:
        i += 1
        value = block_str + str(int.to_bytes(4, i,byteorder='big'),'utf-8') #pow_step(block_str,difficulty)
        print("intermediate value is " + str(value))

        if verify_pow(value,difficulty):
            return value # new block string

        pass

    pass
