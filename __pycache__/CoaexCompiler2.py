from selenium import webdriver
from tkinter import *
import tkinter as tk
import time

class WindowMaster:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)

        self.button1 = tk.Button(self.frame, text = 'New Window', width = 25, command = self.new_window)
        self.button2 = tk.Button(self.frame, text = "QUIT", width = 25, command = self.exit)
        self.beginTimer = tk.Button(self.frame, text = "Start Timer", width = 30, command = self.timer)

        self.timerBool = True
        self.var = StringVar()
        self.timeLabel = tk.Label(self.frame, textvariable = self.var)
        self.var.set("0")
        self.timeLabel.pack()
        self.beginTimer.pack()
        self.button1.pack()
        self.button2.pack()
        self.frame.pack()

    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = WindowChild(self.newWindow)

    def timer(self):
        if (self.timerBool == True):
            self.var.set(str(int(self.var.get()) + 1))
            self.master.after(1000, self.timer)


    def stop_timer(self):
        self.timerBool = False

    def exit(self):
        self.master.destroy()
        
class WindowChild:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)


        
        # #sets up the website
        self.crypto_setup()
        self.COA_BTC_setup()

        # #initializes the counters
        # self.crypto_setup_threading_test_back()

        # #set up our coins
        # self.setup_coin_base()
        # #sets up our wallet
        # self.setup_Wallet()
        

        # #setting up the buttons
        # #bitcoinPrice = driver.find_element_by_xpath('//*[@id="asset-cards"]/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[2]/div[1]/span[2]/span[2]').text
        # self.testButton = tk.Button(self.frame, text = 'TESTING', width = 30, command = self.crypto_threading_test())

        # self.beginTradingButton = tk.Button(self.frame, text = 'BEGIN TRADING AND SELLING', width = 40, command = self.begin_trading_selling())
        # #self.testButton = tk.Button(self.frame, text = 'TESTING', width = 30, command = self.threading_test)

        # self.testButton.pack()
        # self.stopButton = tk.Button(self.frame, text = 'STOP', width = 30, command = self.tester_exit)

        # self.beginTradingButton.pack()
        # self.stopButton.pack()
        # self.quitButton.pack()

        self.frame.pack()
    
    # run the coaex application actual one   
    
        
    #opens up the website
    def crypto_setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.coaex.io/login")
  
        time.sleep(2)
  
        emailBox = self.driver.find_element_by_xpath('//*[@id="email"]')
  
        pwdBox = self.driver.find_element_by_xpath('//*[@id="pwd"]')
  
        emailBox.send_keys("mail4hang@yahoo.com")
        pwdBox.send_keys("Kim10190820")
  
        loginBtn = self.driver.find_element_by_xpath('/html/body/div/form/div[5]/div[2]/button')
        loginBtn.click()
  
        time.sleep(10)
  
        okBtn = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[1]')
        okBtn.click()

        enterCOABTC = self.driver.find_element_by_xpath('//*[@id="coinCategoriesSiseBodyId"]/tr[1]/td[2]/h4/span[1]')
        enterCOABTC.click()


  
    #RETURNS THE CURRENT VALUE OF THE COIN
    def crypto_setup_back(self):
        return self.driver.find_element_by_xpath('//*[@id="asset-cards"]/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[2]/div[1]/span[2]/span[2]').text

    #sets up all the Crypto PRICES
    def crypto_setup_threading_test_back(self):
        self.setter = True
        self.generalCounter = 0
        self.counter5SecAgo = self.crypto_setup_back()
        self.counter0SecAgo = self.crypto_setup_back()
        self.var = StringVar()
        self.label0Sec = tk.Label(self.frame, textvariable = self.var)
        self.var2 = StringVar()
        self.label5Sec = tk.Label(self.frame, textvariable = self.var2)
        self.var.set(str(self.counter5SecAgo))
        self.var2.set(str(self.counter0SecAgo))

        self.varAmount = float(self.var.get())
        self.var2Amount = float(self.var2.get())
        self.avgAmount = (self.varAmount + self.var2Amount) / 2
        self.currentAmount = float(self.crypto_setup_back())

        self.label0Sec.pack()
        self.label5Sec.pack()

    #updates the counters
    def crypto_threading_test(self):
        if (self.setter == True):
            self.var.set("20 sec ago " + str(self.var2Amount))
            self.varAmount = self.var2Amount

            self.var2.set("now " + self.crypto_setup_back())
            self.var2Amount = self.crypto_setup_back()

            self.master.after(20000, self.crypto_threading_test)

    #set up our wallet(total dollar amount we have)
    def setup_Wallet(self):
        self.AMOUNT = 50000 #50,000
        self.amountVar = StringVar()
        self.amountLabel = tk.Label(self.frame, textvariable = self.amountVar)
        self.amountVar.set("Total Liquid = " + str(self.AMOUNT))

        #EVERYTHING INCLUDING COINS AND LIQUID
        self.totalAmount = self.AMOUNT + self.totalValueOfMyCoins
        self.totalAmountVar= StringVar()
        self.totalAmountLabel = tk.Label(self.frame, textvariable = self.totalAmountVar)
        self.totalAmountVar.set ("total amount of everything = " + str(self.totalAmount))

        self.amountLabel.pack()
        self.totalAmountLabel.pack()


    #with a set amount, established in the beginning, keep trading until money runs out or I tell it to stop
    def begin_trading_selling(self):
        if (self.setter == True):
            self.avgAmount = (float(self.varAmount) + float(self.var2Amount)) / 2.0
            self.currentAmount = float(self.crypto_setup_back())
            print("we out here")
            if (self.currentAmount < self.avgAmount):
        
                if (self.AMOUNT > self.currentAmount):
                    self.buy_Coin()
            if (self.currentAmount >= self.avgAmount):
                
                if (self.numberOfCoins > 0):
                    self.sell_Coin()

            self.update_Value_Coin()

            self.master.after(3000, self.begin_trading_selling)

    #buy an imaginary coin
    def buy_Coin(self):
        self.numberOfCoins = self.numberOfCoins + 1
        self.AMOUNT = self.AMOUNT - self.currentAmount
        self.coinVar.set("number of coins " + str(self.numberOfCoins))
        self.amountVar.set("Total Liquid = " + str(self.AMOUNT))

    #sell an imaginary coin
    def sell_Coin(self):
        self.numberOfCoins = self.numberOfCoins - 1
        self.AMOUNT =  self.AMOUNT + self.currentAmount
        self.coinVar.set("number of coins " + str(self.numberOfCoins))
        self.amountVar.set("Total Liquid = " + str(self.AMOUNT))

    #THE COIN VALUE OF OUR WALLET IS UPDATE
    def update_Value_Coin(self):
        
        self.currentValueOfCoin = self.currentAmount

        self.totalValueOfMyCoins = self.numberOfCoins * self.currentValueOfCoin
        self.valueVar.set("total value of coins" + str(self.totalValueOfMyCoins))

        self.totalAmount = self.totalValueOfMyCoins + self.AMOUNT
        self.totalAmountVar.set("tottal value of everthing = " + str(self.totalAmount))
    
    #SET UP OUR COINS
    def setup_coin_base(self):
        self.numberOfCoins = 10
        self.totalValueOfMyCoins = self.numberOfCoins * self.currentAmount

        self.coinVar = StringVar()
        self.numberOfCoinsLabel = tk.Label(self.frame, textvariable = self.coinVar)
        self.coinVar.set("number of coins" + str(self.numberOfCoins))

        self.valueVar = StringVar()
        self.totalValueOfCoinsLabel = tk.Label(self.frame, textvariable = self.valueVar)
        self.valueVar.set("total value of coins" + str(self.totalValueOfMyCoins))


        self.numberOfCoinsLabel.pack()
        self.totalValueOfCoinsLabel.pack()


    #sets to false when used which cancels the counters and stops them
    def tester_exit(self):
        self.setter = False
    
    def close_windows(self):
        self.master.destroy()

def main(): 
    root = tk.Tk()
    app = WindowMaster(root)
    root.mainloop()

if __name__ == '__main__':
    main()