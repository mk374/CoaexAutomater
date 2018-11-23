'''
Created on Nov 22, 2018

@author: minsookim
'''
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

from tkinter import *

import re




driver = webdriver.Chrome()


"""
time.sleep(18)

firstBtn = driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[2]')
firstBtn.click()


secBtn = driver.find_element_by_link_text('로그인')
//*[@id="navigation"]/ul/li[1]/a
secBtn.click()
"""

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
