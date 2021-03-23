import requests

class Network:
    def __init__(self, baseUrl):
        self._baseUrl = baseUrl

    def request(self):
        req = requests.get(self._baseUrl)
        statusCode = req.status_code
        content = req.content
        return statusCode, content