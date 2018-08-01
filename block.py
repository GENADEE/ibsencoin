import json

class Block:
    def __init__(self,previous, transactions_list):
        self.previous = previous
        self.transactions_list = transactions_list
        pass

    def serialize(self):
        return str(self.previous) + "," + str(self.transactions_list)
    pass