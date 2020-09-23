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
    requests.delete(url=self.uri)

  def send_layout(self, layout):
    resp = requests.post(url = rs.uri + '/keyboard', json = {"effect": "CHROMA_STATIC", "param": {"color": 16711935}}).json()
    print(resp)
    self.effects.append(resp['id'])
    print(self.effects[0])
    print(requests.put(url = rs.uri + '/effect', json = {"id": self.effects[0]}).request)
    print(requests.put(url = rs.uri + '/effect', json = {"id": self.effects[0]}).request)

  def heartbeat(self):
    requests.put(url = rs.uri + '/heartbeat')



rs = RazerService()
print(rs.sessionid, rs.uri)

time.sleep(1)
rs.send_layout(None)
for i in range(1, 10):
  time.sleep(1)
  rs.heartbeat()

del rs
