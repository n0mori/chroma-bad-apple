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
    self.effects = []

  def __del__(self):
    time.sleep(5)
    print(requests.delete(url=self.uri))

  def send_layout(self, layout):
    time.sleep(1)
    resp = requests.post(url = rs.uri + '/keyboard', json = open('effect.json', 'r')).json()
    self.effects.append(resp['id'])
    print(self.effects)
    print(requests.post(url = rs.uri + '/effect', json = {"id": self.effects[0]}).text)
# {'effect': 'CHROMA_STATIC', 'params': {'color': 0xFF00FF}}
rs = RazerService()
print(rs.sessionid, rs.uri)
rs.send_layout(None)
del rs
