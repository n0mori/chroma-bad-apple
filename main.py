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
    time.sleep(1)
    print(requests.put(url = rs.uri + '/keyboard', data = {'effect': 'CHROMA_STATIC', 'params': {'color': 0xFF00FF}}).text)

rs = RazerService()
print(rs.sessionid, rs.uri)
rs.send_layout(None)
del rs
