import json
# import datetime
from datetime import date
# import telebot
# import telethon
import pywhatkit


today = date.today()
#open the file
f = open('data.json',"r")
data = json.load(f)

try:

    # sending message to reciever
    # using pywhatkit
    pywhatkit.sendwhatmsg("+919899480737",
                          "Hello from GeeksforGeeks",
                          22, 28)
    print("Successfully Sent!")

except:

    # handling exception
    # and printing error message
    print("An Unexpected Error!")

for i in data['Birthday_Details']:
    Cur = today.strftime("%d-%m")
    if( i['Date'] !=Cur ):
        print("Happy Birthday "+i['name']+" bhai!")



f.close()