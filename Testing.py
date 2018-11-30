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
        self.button1.pack()
        self.button2.pack()
        self.frame.pack()

    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = WindowChild(self.newWindow)
    
    def exit(self):
        self.master.destroy()
        
class WindowChild:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        #sets up the website
        self.crypto_setup()
        #initializes the counters
        #self.threading_test_back()
        self.crypto_setup_threading_test_back()
        #setting up the buttons
        #bitcoinPrice = driver.find_element_by_xpath('//*[@id="asset-cards"]/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[2]/div[1]/span[2]/span[2]').text
        self.testButton = tk.Button(self.frame, text = 'TESTING', width = 30, command = self.crypto_threading_test)
        #self.testButton = tk.Button(self.frame, text = 'TESTING', width = 30, command = self.threading_test)
        self.exitButton = tk.Button(self.frame, text = 'STOP', width = 30, command = self.tester_exit)
        self.quitButton.pack()
        self.testButton.pack()
        self.exitButton.pack()
        self.frame.pack()
    
    #opens up the website
    def crypto_setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://cryptowat.ch")
    
    def crypto_setup_back(self):
        return self.driver.find_element_by_xpath('//*[@id="asset-cards"]/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[2]/div[1]/span[2]/span[2]').text
    def crypto_setup_threading_test_back(self):
        self.setter = True
        self.generalCounter = 0
        self.counter5SecAgo = self.crypto_setup_back()
        self.counter0SecAgo = self.crypto_setup_back()
        self.var = StringVar()
        self.label0Sec = tk.Label(self.frame, textvariable = self.var)
        self.var2 = StringVar()
        self.label5Sec = tk.Label(self.frame, textvariable = self.var2)
        self.var.set("5sec ago" + str(self.counter5SecAgo))
        self.var2.set("now" + str(self.counter0SecAgo))
        self.label0Sec.pack()
        self.label5Sec.pack()

    #updates the counters
    def crypto_threading_test(self):
        if (self.setter == True):
            self.var.set(self.var2.get())
            self.var2.set(self.crypto_setup_back())
            self.master.after(10000, self.crypto_threading_test)
    
    #sets to false when used which cancels the counters and stops them
    def tester_exit(self):
        self.setter = False
    
    
    
    #command or method that initializes the counters
    def threading_test_back(self):
        self.setter = True
        self.generalCounter = 0
        self.counter0Sec = 0
        self.counter5Sec = 0
        self.var = StringVar()
        self.label0Sec = tk.Label(self.frame, textvariable = self.var)
        self.var2 = StringVar()
        self.label5Sec = tk.Label(self.frame, textvariable = self.var2)
        self.var.set("0 sec counter" + str(self.counter0Sec))
        self.var2.set("5 sec counter" + str(self.counter5Sec))
        self.label0Sec.pack()
        self.label5Sec.pack()
        
    #updates the counters
    def threading_test(self):
        if (self.setter == True):
            if(self.counter5Sec < 5):
                self.counter5Sec += 1
                self.var2.set("5 sec counter" + str(self.counter5Sec))
            else:
                self.update_counter()
                
            self.master.after(1000, self.threading_test)
            
    #used in threading_test to update the counters and print
    def update_counter(self):
        self.counter0Sec += 1
        self.counter5Sec += 1
        self.var.set("0 sec counter" + str(self.counter0Sec))
        self.var2.set("5 sec counter" + str(self.counter5Sec))
        
    #self explanatory, destroys the window
    def close_windows(self):
        self.master.destroy()

def main(): 
    root = tk.Tk()
    app = WindowMaster(root)
    root.mainloop()

if __name__ == '__main__':
    main()