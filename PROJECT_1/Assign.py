import requests
import json


//Making some changes here

Url = "https://api.macaddress.io/v1?apiKey=at_Xv2Z6uVSr0a5O045KtgDw2F0Ri5gQ&output=json&search=44:38:39:ff:ef:57"
payload= {}
headers= {}

response = requests.request("GET", Url, headers=headers, data = payload)
status_code = response.status_code
content = json.loads(response.content)
#print(status_code)
#print (json.dumps(content, indent=2))
print(content['vendorDetails']['companyName'])
