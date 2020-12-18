from selenium import webdriver
from twilio.rest import client

######################################################################################
# Your Account SID from twilio.com/console
account_sid = "your-account-id"
# Your Auth Token from twilio.com/console
auth_token  = "your-token"

timeCheck = datetime.utcnow()  

while timeCheck % 30 == 0
  browser = webdriver.Firefox()
  browser.get("https://www.gamestop.com/video-games/playstation-5/consoles/products/playstation-5/B225169V.html")
    
  btnColor = driver.getAttribute("background-color")

  if btnColor == 'DA362C':
    client = Client(account_sid, auth_token)
  
    message = client.messages.create(
        to="+YOUR-CELL-PHONE-NUMBER" 
        #you can buy a phone number here - https://www.twilio.com/console/phone-numbers/search
        from_="+YOUR-TWILIO-PHONE-NUMBER",
        body="Hey dumb dumb, Gamestop has PS5 in stock.")
######################################################################################

#todo: get price of ps5 on stock-x

#todo: get price curve using PANDAS

#todo: add listing to stock-x

#todo: scrape ARKK investments for top 10 stock holdings

#todo: import rhood and invest difference of MSRP and stock-x sale price 

#todo: check for stock cost basis difference, if diff > ps5 MSRP, repeat

