import json
import requests
import logging

#Init logging
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True


url = ""

content = open('content.md','r')

#Python dict
json_data = {
    'title':'test_for_balakriu',
    'content':content.read()
}
while true:
req = requests.Request('POST',url,headers={'Content-Type':'application/json'},data=json.dumps(json_data))
prepared = req.prepare()
s = requests.Session()
s.send(prepared)
print(dir(s))