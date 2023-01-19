import requests #gets all the html data from a webpage 
from bs4 import BeautifulSoup #allows you to extract html info
import smtplib #email 
from time import sleep #in order to slow down the programme 



email = "email@gmail.com"
passw = "password" #this will not work unless password is stated

url = "https://finance.yahoo.com/quote/GME/" #this is a website that lists gamestop stock
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"} #I don't think that this is necessary but I saw it in a tutorial
webdata = requests.get(url, headers=headers) 
soup = BeautifulSoup(webdata.content, "html.parser") # remember this second argument

def getGameStopPrice(): # simply returns Gamestop stock price. There is a span class on the website with this class where the stock price is listed. We strip this down in order to get an intiger
    price = soup.find("span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)").get_text().strip()[0:3]
    return int(price)


def serversetup(): #sends the email
    data =  "Gamestop Stock is valued at " + str(getGameStopPrice()) + " USD"
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, passw)
    server.sendmail(email, email, data)


def start(): #checks if price is below a certain point, and calls the send email function is it is. Repeats every 2 seconds.
    if getGameStopPrice() < 500:
        sleep(2)
        serversetup()
        start()

start() #starts the script