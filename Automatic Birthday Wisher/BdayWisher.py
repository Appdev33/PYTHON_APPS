import json
import datetime
from datetime import date

today = date.today()
#open the file
f = open('data.json',"r")
data = json.load(f)

for i in data['Birthday_Details']:
    Cur = today.strftime("%d-%m")
    if( i['Date'] ==Cur ):
        print("Happy Birthday "+i['name']+" bhai")



f.close()