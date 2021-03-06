'''
Created on Nov 22, 2018

@author: minsookim
'''
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

from tkinter import *


import re
from doctest import master


"""
setting up user interface
"""
def is_number(n):
    try:
        float(n)   
    except ValueError:
        return False
    return True

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)                 
        self.master = master
        self.init_window()

    #Creation of init_window
    def init_window(self): 
        
        
        self.master.title("COAEX AUTOMATER")

        self.pack(fill=BOTH, expand=1)
        
        menu = Menu(self.master)
        self.master.config(menu=menu)
        
        file = Menu(menu)
        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        file.add_command(label="Exit", command=self.client_exit)
        #file.add_command(label = "Run", command = self.coaex_run)
        file.add_command(label = "Run", command = self.test_run)
        
        sellEntry = Entry(self)
        buyEntry = Entry(self)
        sellEntry.pack()
        buyEntry.pack()
        
        var = StringVar()
        var2 = StringVar()
        sellPriceLabel = Label(master, text = "Sell Price Label", textvariable = var)
        buyPriceLabel = Label(master, text = "Buy Price Label", textvariable = var2)
        sellPriceLabel.pack()
        buyPriceLabel.pack()
        
        def callback():
            if (is_number(sellEntry.get())):
                var.set(sellEntry.get())
            else: var.set("숫자를 입력 해주세")
        def callback2():
            if (is_number(buyEntry.get())):
                var2.set(buyEntry.get())
            else: var2.set("숫자를 입력 해주세")
    
        sellButton = Button(self, text="Sell Price Enter", width=20, command = callback)
        sellButton.pack()
        buyButton = Button(self, text = "Buy Price Enter", width = 20, command = callback2)
        buyButton.pack()

        #added "file" to our menu
        menu.add_cascade(label="File", menu=file)
        
        edit = Menu(menu)

        edit.add_command(label="Undo")

        #added "file" to our menu
        menu.add_cascade(label="Edit", menu=edit)
    
    # quit the application
    def client_exit(self):
        exit()
    
    # run the coaex application actual one    
    def coaex_run(self):
        #open chrome
        driver = webdriver.Chrome()
        driver.get("http://www.coaex.io/login")
  
        time.sleep(2)
  
        emailBox = driver.find_element_by_xpath('//*[@id="email"]')
  
        pwdBox = driver.find_element_by_xpath('//*[@id="pwd"]')
  
        emailBox.send_keys("mail4hang@yahoo.com")
        pwdBox.send_keys("Kim10190820")
  
        loginBtn = driver.find_element_by_xpath('/html/body/div/form/div[5]/div[2]/button')
        loginBtn.click()
  
        time.sleep(10)
  
        okBtn = driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[2]')
        okBtn.click()
        
    # checking live cryptocurrency market
    def test_run(self):
        driver = webdriver.Chrome()
        driver.get ("https://cryptowat.ch")

        #get live bitcoin prices
        time.sleep (3)
        
        #while loop to update the label in TK every 5 seconds
        bitcoinPrice = driver.find_element_by_xpath('//*[@id="asset-cards"]/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[2]/div[1]/span[2]/span[2]')
        
        
        
root = Tk()
#size of the window
root.geometry("400x300")
app = Window(root)

root.mainloop()



