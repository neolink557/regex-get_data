import json
import requests

class Connection(object):
    """docstring for ConectTeachers."""
    URL='https://u4uapp.herokuapp.com/api/v1/'

    def __init__(self):
        super(Connection, self).__init__()

    def post(self,url,json,**kwargs):
        response = requests.post(self.URL+url,json=json)
        print(json,"STATUS_CODE: " + response.status_code)
        return response
