import webbrowser, sys
from selenium import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys 

import time

number = 918130384841
no_of_times = 1

if len(sys.argv) > 1:
	no_of_times = sys.argv[1]

# webbrowser.open('https://api.WhatsApp.com/send?phone='+str(number))
driver = webdriver.Chrome(executable_path='/Users/pushpitbhardwaj/Downloads/cuba/chromedriver')

# driver.maximize_window()
def click_buttons():
	continue_btn = driver.find_element_by_id('action-button')
	continue_btn.click()
	WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.LINK_TEXT, "use WhatsApp Web"))).click()

def open_new_tab(i, number):
	new_tab = 'tab' + str(i)
	driver.execute_script("window.open('https://api.WhatsApp.com/','" + new_tab+"');")
	driver.switch_to.window(driver.window_handles[-1])
	driver.get('https://api.WhatsApp.com/send?phone='+str(number))

def send_message():
	text_field = driver.find_element_by_xpath('//div[@class="_3uMse"]')
	text_field.send_keys('Hello, I am the whatsapp bot again')

	msg_send = driver.find_element_by_xpath('//button[@class="_1U1xa"]')
	msg_send.click()

def switch_tab(no):
	driver.switch_to.window(driver.window_handles[no])

i = 2
open_new_tab(i, number)
click_buttons()
time.sleep(10)
send_message()

i = 3
open_new_tab(i, number)

i = 4
open_new_tab(i, number)

i = 5
open_new_tab(i, number)

i = 6
open_new_tab(i, number)

i = 7
open_new_tab(i, number)

switch_tab(1)
driver.close()

switch_tab(1)
click_buttons()

switch_tab(2)
click_buttons()

switch_tab(3)
click_buttons()

switch_tab(4)
click_buttons()

switch_tab(5)
click_buttons()
time.sleep(10)
send_message()
driver.close()

switch_tab(4)
btn_clik = driver.find_element_by_xpath("//div[text()='Use Here']")
btn_clik.click()
time.sleep(4)
send_message()
driver.close()

switch_tab(3)
btn_clik = driver.find_element_by_xpath("//div[text()='Use Here']")
btn_clik.click()
time.sleep(4)
send_message()
driver.close()

switch_tab(2)
btn_clik = driver.find_element_by_xpath("//div[text()='Use Here']")
btn_clik.click()
time.sleep(4)
send_message()
driver.close()


