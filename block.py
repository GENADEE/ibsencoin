import json

class Block:
    def __init__(previous, transactions_list):
        self.previous = previous
        self.transactions_list = transactions_list
        pass

    def serialize():
        return str(self.previous) + "," + str(self.transactions_list)
    pass