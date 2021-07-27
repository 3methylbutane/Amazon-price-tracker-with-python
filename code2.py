import requests
from bs4 import BeautifulSoup
import smtplib
import time
URL="https://www.amazon.in/Samsung-500GB-Portable-Solid-State/dp/B074WZJ4MF/ref=sr_1_3?dchild=1&keywords=external+ssd&psr=PDAY&qid=1627364490&s=prime-day&smid=A14CZOWI0VEHLG&sr=1-3"
headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"}
def check_price():
   page=requests.get(URL,headers=headers)
   soup=BeautifulSoup(page.content,'html.parser')
   name=soup.find(id="productTitle").get_text()
   print(name.strip())
   price=soup.find(id="priceblock_dealprice").get_text().replace(',','').replace('₹','').replace(' ','').strip()
   price=float(price[0:5])
   print(price)
   if (price<5200):
     send_mail()

def send_mail():
   server =smtplib.SMTP("smtp.gmail.com",587)
   server.ehlo()
   server.starttls()
   server.ehlo()
   server.login('xyz@gmail.com',
#    user-id
   '*****'
#    user-password
   )
   msg="prices fell down"
   chop="check the amazon link https://www.amazon.in/Samsung-500GB-Portable-Solid-State/dp/B074WZJ4MF/ref=sr_1_3?dchild=1&keywords=external+ssd&psr=PDAY&qid=1627364490&s=prime-day&smid=A14CZOWI0VEHLG&sr=1-3"
   subject=f"Subject :{msg}\n\n{chop}"
   server.sendmail("xyz@gmail.com",   
#    user-id who sends the mail
   "abc@gmail.com",
#    user-id who receives the mail
   subject
   )
   print("hey!! server has started")
   server.quit()

while(True):
   check_price()
   time.sleep(60*60)
