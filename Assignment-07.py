import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('http://www.gmail.com')

emailElem = browser.find_element_by_id('Email')
emailElem.send_keys('My_email@gmail.com')
emailElem.submit()

time.sleep(2)

passwordElem = browser.find_element_by_id('Passwd')
passwordElem.send_keys('My_password_here')
passwordElem.submit()


time.sleep(2)

composeElem = browser.find_element_by_class_name('z0') #this only works half of the time
composeElem.click()

time.sleep(7)

toElem = browser.find_element_by_name("to")
toElem.send_keys('my_other_email@gmail.com')

time.sleep(2)

subjElem = browser.find_element_by_name("subjectbox")
subjElem.send_keys('Test with selenium')

time.sleep(2)

bodyElem = browser.find_element_by_???('???') #this is where I get stuck and not sure what to do here
bodyElem.send_keys('A test email with selenium')

time.sleep(2)

sendElem = browser.find_element_by_link_text('send') #not sure if this is correct too
sendElem.submit()