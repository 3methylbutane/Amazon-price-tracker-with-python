import requests 
from bs4 import BeautifulSoup
import smtplib
import time
# URL="https://www.amazon.in/Samsung-500GB-Portable-Solid-State/dp/B074WZJ4MF/ref=sr_1_3?dchild=1&keywords=external+ssd&psr=PDAY&qid=1627364490&s=prime-day&smid=A14CZOWI0VEHLG&sr=1-3"

# setting header and user agent
headers={"user-agent":"Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML,like Gecko) Chrome/92.0.4515.107 Safari/537.36"}

# send request to find HTML of the amazon webpage
response=requests.get('https://www.amazon.in/Samsung-500GB-Portable-Solid-State/dp/B074WZJ4MF/ref=sr_1_3?dchild=1&keywords=external+ssd&psr=PDAY&qid=1627364490&s=prime-day&smid=A14CZOWI0VEHLG&sr=1-3', headers=headers)

soup=BeautifulSoup(response.content, 'html.parser')

soup.encode('utf-8')

def check_price():
	title=soup.find(id="productTitle").get_text()
	price=soup.find(id="priceblock_dealprice").get_text().replace(',', '').replace('₹', '').replace(' ','').strip()
	
	#print(price)

	converted_price=float(price[0:5])
	print(converted_price)
	if(converted_price<5200):
		send_mail()
	print(title.strip())

def send_mail():
	server=smtplib.SMTP("smtp.gmail.com",587)
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login('xyz@gmail.com','password')

	msg="prices are low"
	lnk="Open link https://www.amazon.in/Samsung-500GB-Portable-Solid-State/dp/B074WZJ4MF/ref=sr_1_3?dchild=1&keywords=external+ssd&psr=PDAY&qid=1627364490&s=prime-day&smid=A14CZOWI0VEHLG&sr=1-3"
	
	sub=f"Subject :{msg}\n\n{lnk}"

	server.sendmail('xyz@gmail.com','abc@gmail.com',sub)
	print('Hey! The email has been sent')
	server.quit()

while(True):
	check_price()
	time.sleep(60*60)