import requests
""" Auth Credentials, used to get the Bearer token from the auth api """

class AuthToken():

    def __init__(self):
        pass

    def access(self):
        """ Access to the API endpoint """
        header = {
            "Accept" : "application/json",
            "Content-Type" : "application/json",
            "Authorization" : "Bearer " + self._auth()
        }
        return header

    def _auth(self):
        """ Authentication """
        header = {
            "username" : "username",
            "password" : "password"
        }
        response = requests.post('api/auth/login', data=header)
        return response.json()['access_token']
