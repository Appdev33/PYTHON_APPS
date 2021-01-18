import requests
import json



#Url = \
payload= {}
headers= {}

response = requests.request("GET", Url, headers=headers, data = payload)
status_code = response.status_code
content = json.loads(response.content)
#print(status_code)
#print (json.dumps(content, indent=2))
print(content['vendorDetails']['companyName'])
