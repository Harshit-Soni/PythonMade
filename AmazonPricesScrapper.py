import requests
from bs4 import BeautifulSoup
import smtplib
def checkPrice():
    URL = 'https://www.amazon.in/Test-Exclusive-748/dp/B07DJLVJ5M/ref=sr_1_1?dchild=1&keywords=oneplus+7t&qid=1593597098&s=electronics&sr=1-1'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id='productTitle').getText().strip()
    price = soup.find(id='priceblock_ourprice')
    if price is None:
        print('here')
        msg='Sold out'
        send_mail(msg)
        exit()
    price=price.getText()
    price = float(''.join(price[2:].split(',')))
    print(title)
    print(price)
    if price < 40000:
        subject = 'price fell down! to {}'.format(price)
        body = 'check the amazon link \n\n'+URL
        msg = 'Subject: {}\n\n {}'.format(subject, body)
        send_mail(msg)

def send_mail(msg):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('harsh111soni@gmail.com','vowjqanksukgzzvf')
    server.sendmail('harsh111soni@gmail.com','harsh222soni@gmail.com',msg)
    print('Mail is sent')
    server.quit()

checkPrice()
