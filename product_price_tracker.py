import requests
from bs4 import BeautifulSoup           #a web scrapping tool
import smtplib
import time
import getpass

#Amazon's or any other platform's URL of the required product 
URL = 'https://www.amazon.in/Test-Exclusive_2020_1180-Multi-3GB-Storage/dp/B089MT34QL/ref=sr_1_10?dchild=1&qid=1625984349&refinements=p_89%3AOnePlus&rnid=3837712031&s=electronics&sr=1-10'

#user agent of your browser- to get it simply search 'my user agent' in google 
myheader={
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.64'
}


def check_price():
    #Trying to retrive data from that url
    page=requests.get(URL, headers=myheader)

    soup=BeautifulSoup(page.content,'html.parser')

    #print(soup.prettify())

    #finding the block of data with the help of id
    title = soup.find(id="productTitle")

    price = soup.find(id="priceblock_ourprice")

    try:
        converted_price=price.get_text()[1:8]
    except TypeError:
        pass

    if title is not None:
        print(title.get_text(strip=True))
    if price is not None:
        print(price.get_text(strip=True))

    converted_price=float(''.join(converted_price.split(',')))
    print(converted_price)
    if(converted_price>35000):
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('hithardh1412200@gmail.com', getpass.getpass('Enter u r password'))

    mysubject="Hey..! price fell down..!"
    body = 'check the amazon link https://www.amazon.in/Test-Exclusive_2020_1180-Multi-3GB-Storage/dp/B089MT34QL/ref=sr_1_10?dchild=1&qid=1625984349&refinements=p_89%3AOnePlus&rnid=3837712031&s=electronics&sr=1-10'

    msg= f"Subject: {subject}\n\n{body}"
    server.sendmail('hithardh1412200@gmail.com', 'hithardh1412200@gmail.com', msg)
    print('HEY EMAIL HAS BEEN SENT')
    
    server.quit()
#while(True):
check_price()
    #time.sleep(3600)