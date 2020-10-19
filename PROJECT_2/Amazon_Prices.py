import requests
from bs4 import BeautifulSoup
import smtplib
import time
import winsound



def check_price():
      PresentLow = 0.0
      URL = 'https://www.amazon.in/HP-23-8-inch-Ultra-Slim-Anti-Glare-Display/dp/B01H1Q8TQC?th=1'
      headers = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
      try:
            page = requests.get(URL, headers=headers)
            soup = BeautifulSoup(page.content, 'html.parser')
            title = soup.find(id="productTitle").get_text()
            print(title.strip())

            Mrp =soup.find(id="priceBlockStrikePriceString a-text-strike")
            price1 = soup.find(id="priceblock_ourprice")
            price2 = soup.find(id="priceblock_dealprice")
            #print(price2)
            if(price2):
                  PresentLow = float(price2.get_text()[2:8].replace(',',''))
            elif(price1):
                  PresentLow = float(price1.get_text()[2:8].replace(',', ''))
            elif(Mrp):
                  PresentLow = float(Mrp.get_text()[2:8].replace(',', ''))
            else:
                  Print('No Price For This Product Exists on the Website')



            print('Present Lowest Price is: '+ str(PresentLow))
            if(PresentLow<12499):
                  print('Check Amazon ')
                  frequency = 1500  # Set Frequency To 2500 Hertz
                  duration = 1000  # Set Duration To 1000 ms == 1 second
                  i=1
                  while(i<=20):
                        winsound.Beep(frequency, duration)
                        time.sleep(0.2)
                        i=i+1
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



def send_Email():
      server = smtplib.SMTP('smtp.gmail.com',587)
      server.ehlo()
      server.starttls()
      server.ehlo()
      server.login('app.devplatform@gmail.com','nxdrcppusioaywby')
      subject = 'Price Fell Down For'
      body = 'Check the amazon link  https://www.amazon.in/dp/B07SQXPW35/ref=s9_acsd_hps_bw_c2_x_0_i?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-4&pf_rd_r=1P0WWYXN281RXPJWSB83&pf_rd_t=101&pf_rd_p=7c00f914-cf00-443d-a66f-f9afe38e169a&pf_rd_i=21243324031'
      msg = 'hw'#f'Subject:{subject}\n\n{body}'
      server.sendmail('app.devplatform@gmail.com',
                      'ntsh334u@gmail.com',
                      msg
                      )
      print('HEY EMAIL HAS BEEN SENT!')

      server.quit()

while(True):
      check_price()
      time.sleep(300)