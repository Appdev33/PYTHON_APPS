import json
import re
import requests

regex = "^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$"

Mac_Add = input("Enter The Mac Address  ")
if Mac_Add == "":
    print("No value Entered!!!")
    exit()
elif(re.search(regex, Mac_Add) is None):
    print('PLEASE Check Mac Address Format!!!')
    exit()


Url = "https://api.macaddress.io/v1?apiKey=at_Xv2Z6uVSr0a5O045KtgDw2F0Ri5gQ&output=json"
params = {"search": Mac_Add}
payload = {}
headers = {}

try:
    response = requests.request("GET", Url, params=params, headers=headers, data=payload, timeout=50)
    status_code = response.status_code
    content = json.loads(response.content)

    if status_code == 200 and content['vendorDetails']['companyName']=='':
        print("No Values Found in Our Database for this Mac Address!!!")
    elif status_code==200 and re.search(regex, Mac_Add):
        print("This Mac Address Belongs To: " + content['vendorDetails']['companyName'])
    else:
        print('Irregular Status Code Returned !!!' + str(status_code))
except requests.ConnectionError as e:
    print("Connection Error. Make sure you are connected to Internet. Technical Details given below.\n")
    print(str(e))
except requests.Timeout as e:
    print("OOPS!! Timeout Error")
    print(str(e))
except requests.RequestException as e:
    print("OOPS!! General Error")
    print(str(e))
except KeyboardInterrupt:
    print("Someone closed the program")
finally:
    print('*********END OF CODE***********')
