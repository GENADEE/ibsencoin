import httplib
import urllib
import requests

from .. import client # fix this import please

#https://www.geeksforgeeks.org/get-post-requests-using-python/
# ^^^ tutoial for requests
class NClient:
    # client class has instance of this class
    def __init__(self):
        self.data = {'url'='http://127.0.0.1:5000/','params':{'message'='this is a test message'}}
        pass

    def request_transaction(self,data=self.data):
        transaction = client.create_transaction(data['inputs'],data['n_outputs_groups'],data['v_output_groups'],data['output_group'],data['timeout'])
        self.post_request(transaction) # fix this so it uses blinds properly
        pass
    #these are to make work easier later
    #data should be {'url':URL,'params':PARAMS_AS_A_JSON}
    def get_request(self,data=self.data):
        return requests.get(url = data['url'], params = data['params'])
    def post_request(self,data=self.data):
        return requests.post(url = data['url'], data = data['params'])
        
    pass