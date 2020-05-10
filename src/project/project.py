import requests


class ApiWrapper:

    def __init__(self, url):
        self.url = url
    
    def get(self, endpoint):
        return requests.get(f'{self.url}/{endpoint}').json()
