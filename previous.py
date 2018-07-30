import json

#previous as a class stores both the hash and the pointer to a previous block
#a "hash/reference" class for any type of object (remember python is typeless... this would be generic in another language)
class Previous:
    #previous is a pointer or reference or whatever python uses
    #unimplemented because the previous block doesn't have serialize method yet
    def from_pointer(previous):
        self.previous = previous
        self.hash = "hi my name is jeff" # change this to be hashed from the pointer
        pass
    #unimplemented because there is no blockchain yet
    def from_hash(hash):
        self.hash = hash
        pass
    
    def __str__():
        return self.hash #already a string remember
    pass