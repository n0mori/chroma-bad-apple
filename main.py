import requests
import time
import json

class RazerService:
  def __init__(self):
    response = requests.post(url='http://localhost:54235/razer/chromasdk', 
        headers = {
          'content-type': 'application/json',
        }, data = open('starter.json', 'r'))
    body = response.json()
    print(body)
    self.sessionid = body['sessionid']
    self.uri = body['uri']

  def __del__(self):
    time.sleep(5)
    print(requests.delete(url=self.uri))

  def send_layout(self, layout):
    pass

rs = RazerService()
print(rs.sessionid, rs.uri)
del rs
