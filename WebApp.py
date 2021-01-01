# Stock Price Checker

import sys
import requests
import time
from bs4 import BeautifulSoup

print("This application will determine the price of a Stock, and send you an email when a specified price tager is reached")

class Stock:

    Stock_Code = ""
    Stock_Price = 0.0

    def FindStock(self):
        check = True
        while(check == True):
            try:
                self.Stock_Code = input("Enter the Stock Code: ")
                url = ('https://finance.yahoo.com/quote/' + self.Stock_Code + '?p=' + self.Stock_Code + '&.tsrc=fin-srch')
                req = requests.get(url)

                self.Stock_Price = BeautifulSoup(req.text, 'lxml')
                self.Stock_Price = self.Stock_Price.find('div', {"class" : 'My(6px) Pos(r) smartphone_Mt(6px)'})

                self.Stock_Price = self.Stock_Price.find('span').text
                check = False
            except Exception:
                print(self.Stock_Code, " is not a Valid Stock Code")
            else:
                    self.Stock_Price = float(self.Stock_Price)

    def FindStockPrice(self):
        url = ('https://finance.yahoo.com/quote/' + self.Stock_Code + '?p=' + self.Stock_Code + '&.tsrc=fin-srch')
        req = requests.get(url)

        self.Stock_Price = BeautifulSoup(req.text, 'lxml')
        self.Stock_Price = self.Stock_Price.find('div', {"class" : 'My(6px) Pos(r) smartphone_Mt(6px)'})

        self.Stock_Price = self.Stock_Price.find('span').text

    def Send_mail():

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login('ahmadmaazin1@gmail.com', 'qjtgbeucfsjvnwnd')

        subject = 'Stock Alert!'
        body = 'Your stock has reached the desired price target! Check the Stock: ' ' https://www.tradingview.com/symbols/' + Stock_Code + '/'

        msg = f"Subject: {subject}\n\n{body}"

        server.sendmail('ahmadmaazin1@gmail.com','maahmed@ucdavis.edu', msg)
        print("Email Sent")

        server.quit()

    def PriceChecker(self):

        TargetPrice = float(input("Enter the Price Point for which you want to be notified: "))

        while(self.Stock_Price > TargetPrice):
            print("Price is currently at: ", self.Stock_Price)
            self.FindStockPrice(self)
            time.sleep(60)
        else:
            Send_mail()

Share = Stock
Share.FindStock(Share)
print(Share.Stock_Code, " is ", Share.Stock_Price)
Share.PriceChecker(Share)