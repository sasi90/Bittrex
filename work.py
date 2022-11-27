# import requests
#
#
# URL = r'https://api.bittrex.com/v3/markets/summaries'
# URL = r'https://api.bittrex.com/v3/markets/ltc-btc/summary'
#
# content = requests.get(url=URL)
# data = content.json()
# print(data)

import json
import base64


# with open('test.json') as jsonfile:
#     data = json.load(jsonfile)
#     print(type(data))  #dict
#     datastr = json.dumps(data)
#     print(type(datastr)) #str
#     print(datastr)
#     encoded = base64.b64encode(datastr.encode('utf-8'))  #1 way
#     print(encoded)
#
#     print(base64.encodebytes(datastr.encode()))

# data = {"username":"demo@gmail.com", "password":"demo@123"}
# datastr = json.dumps(data)
# print(type(datastr)) #str
# print(datastr)
# encoded = base64.b64encode(datastr.encode('utf-8'))  #1 way
# print(encoded)
#
# print(base64.encodebytes(datastr.encode()))
#
# print(base64.b64decode(encoded))
# print(json.loads(base64.b64decode(encoded)))
# print(type(json.loads(base64.b64decode(encoded))))

# base64_str = base64.b64decode(data)
# dic = json.loads(base64.b64decode(str(base64_str)))


import secrets

print(secrets.token_urlsafe(20))