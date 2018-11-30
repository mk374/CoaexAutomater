'''
Created on Nov 25, 2018

@author: minsookim
'''

from tkinter import *

class CryptoBotAssist(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)                 
        self.master = master
        self.init_window()

    #Creation of init_window
    def init_window(self, driver): 
        
        
        self.master.title("COAEX AUTOMATER")

        self.pack(fill=BOTH, expand=1)
        listbox = Listbox(self.master)
        listbox.pack(fill=BOTH, expand=1)
        
        #implement while loop so that it will work
        while(default):
            bitcoinPrice = driver.find_element_by_xpath('//*[@id="asset-cards"]/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[2]/div[1]/span[2]/span[2]').text
            listbox.insert(END, bitcoinPrice)
            time.sleep(4)
        