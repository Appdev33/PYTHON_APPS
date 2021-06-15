
import requests
from bs4 import BeautifulSoup
import smtplib
import time
import winsound
import re
import concurrent.futures
from csv import reader

def AmazonPrices(URL,CostAim):
      headers = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
      try:
            page = requests.get(URL, headers=headers)
            soup = BeautifulSoup(page.content, 'html.parser')
            title = soup.find(id="productTitle").get_text()
            print(title.strip())

            Mrp = soup.find(id="priceBlockStrikePriceString a-text-strike")
            price1 = soup.find(id="priceblock_ourprice")
            price2 = soup.find(id="priceblock_dealprice")
            # print(price2)
            if (price2):
                  PresentLow = float(price2.get_text()[2:12].replace(',', ''))
            elif (price1):
                  PresentLow = float(price1.get_text()[2:12].replace(',', ''))
            elif (Mrp):
                  PresentLow = float(Mrp.get_text()[2:12].replace(',', ''))
            else:
                  print('No Price For This Product Exists on the Website')

            print('Present Lowest Price is: ' + str(PresentLow))

            if (PresentLow < CostAim):
                  print('Check Amazon ')
                  frequency = 1500  # Set Frequency To 2500 Hertz
                  duration = 1000  # Set Duration To 1000 ms == 1 second
                  i = 1
                  while (i <= 20):
                        winsound.Beep(frequency, duration)
                        time.sleep(0.2)
                        i = i + 1
      except requests.ConnectionError as e:
            print("Connection Error. Make sure you are connected to Internet. Technical Details given below.\n")
            print(str(e))
      except requests.Timeout as e:
            print("OOPS!! Timeout Error")
            print(str(e))
      except requests.RequestException as e:
            print("OOPS!! General Error")
            print(str(e))
      except AttributeError as e:
            print("There is no such attribute")
            print(str(e))
      except KeyboardInterrupt:
            print("Someone closed the program")
      finally:
            print('*********END OF CODE***********')


def FlipKartPrices():
      pass

urls=[]

with open('list.csv', 'r') as f:
      csv_reader = reader(f)
      for row in csv_reader:
            urls.append(row[0])


def check_price(url):
      #for line in url:   without multithreading
            link = url.split(';')[0]  #multithreading
      #     link = line.split(';')[0]   without multithreading
            price = 1
            AmazonPattern   = re.search('amazon',link,re.IGNORECASE)
            FlipKartPattern = re.search('flipkart', link, re.IGNORECASE)
            if (AmazonPattern):
                  AmazonPrices(link,price)
            elif (FlipKartPattern):
                  print(FlipKartPattern)


while(True):
      t1=time.perf_counter()
      with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(check_price, urls)
      # check_price(urls)   without multithreading
      t2 = time.perf_counter()
      print(f'Finished in {t2 - t1} seconds')
      time.sleep(1)





