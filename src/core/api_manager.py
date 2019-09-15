# Copyright | 2019 | All rights reserved
# MIHAIL BUTNARU
""" API Manager, used to get all the information from the api """
import json
import requests

class APIManager():

    def __init__(self, endpoint):
        """
            Args (str) : api endpoint
        """
        self._endpoint = endpoint


    def get(self):
        """ Gets the data from the API """
        response = requests.get(self._endpoint)
        return response.json()