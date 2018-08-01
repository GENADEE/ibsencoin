import httplib
import urllib
import requests

#https://www.geeksforgeeks.org/get-post-requests-using-python/
# ^^^ tutoial for requests
class NClient:
    # client class has instance of this class
    def __init__(self):
        self.data = {'url'='http://127.0.0.1:5000/','params':{'message'='this is a test message'}}
        pass

    #data should be {'url':URL,'params':PARAMS_JSON}
    def get_request(self,data=self.data):
        return requests.get(url = data['url'], params = data['params'])
    def post_request(self,data=self.data):
        return requests.post(url = data['url'], data = data['params'])
        
    pass