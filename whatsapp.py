import webbrowser, sys
from selenium import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys 
import time

def click_buttons():
	continue_btn = driver.find_element_by_id('action-button')
	continue_btn.click()
	WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.LINK_TEXT, "use WhatsApp Web"))).click()

def open_new_tab(number):
	driver.execute_script("window.open('https://api.WhatsApp.com/');")
	driver.switch_to.window(driver.window_handles[-1])
	driver.get('https://api.WhatsApp.com/send?phone='+str(number))

def send_message():
	WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//div[@data-tab="6"]')))
	text_field = driver.find_element_by_xpath('//div[@data-tab="6"]')
	text_field.send_keys("You are so dumb!")
	#msg_send = driver.find_element_by_xpath('//button[@class="_1U1xa"]')
	WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="_1E0Oz"]'))).click()

def send_message_in_group():
	WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//div[@data-tab="6"]')))
	x = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//span[@title="🦋 Cousins & Arya blast 💛"]')))
	x.click()
	print(x.get_attribute('innerHTML'))
	text_field = driver.find_element_by_xpath('//div[@data-tab="6"]')
	for i in range(200):
		text_field.send_keys(i, ": Natto toh pagal hai")
		#msg_send = driver.find_element_by_xpath('//button[@class="_1U1xa"]')
		WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="_1E0Oz"]'))).click()

def switch_tab(no):
	driver.switch_to.window(driver.window_handles[no])

def use_whatsapp_here():
	btn_clik = driver.find_element_by_xpath("//div[text()='Use Here']")
	btn_clik.click()

def click_on_invalid_url():
	btn_clik = driver.find_element_by_xpath("//div[text()='OK']")
	btn_clik.click()

number = 917303504177
no_of_times = 1

no_of_pages = int(input("Please enter the number of tabs you want to open at once: "))

no_of_times = int(input("Please enter the number of times you want to repeat this process: "))

#Does not require you to login using QR CODE
options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=/Users/pushpitbhardwaj/Library/Application Support/Google/Chrome/Default')
options.add_argument('--profile-directory=Default')

# webbrowser.open('https://api.WhatsApp.com/send?phone='+str(number))
driver = webdriver.Chrome(options=options)

driver.maximize_window()
open_new_tab(number)
click_buttons()
time.sleep(8)
send_message()

for k in range(2000):
	send_message()
	# send_message_in_group()
	
# number = number + 1
# for i in range(int(no_of_times)):
# 	if i != 0:
# 		open_new_tab(number)
# 		click_buttons()
# 		time.sleep(0.3)
# 		switch_tab(1)
# 		driver.close()
# 		time.sleep(1)
# 		switch_tab(1)
# 		time.sleep(0.3)

# 	for i in range(no_of_pages):
# 		open_new_tab(number)
# 		number = number + 1

# 	switch_tab(1)
# 	driver.close()

# 	for i in range(1,no_of_pages):
# 		switch_tab(i)
# 		click_buttons()

# 	switch_tab(no_of_pages)
# 	click_buttons()
# 	time.sleep(7)
	
# 	elem = len(driver.find_elements_by_xpath("//div[text()='OK']")) > 0
# 	print(elem)
# 	if elem:
# 		click_on_invalid_url()
# 		driver.close()
# 	else:
# 		time.sleep(5)
# 		print("sending message")
# 		send_message()
# 		print("sent")
# 		driver.close()

# 	no = no_of_pages -1

# 	for p in range(no_of_pages-1,1,-1):
# 		if no > 2:
# 			switch_tab(p)
# 			use_whatsapp_here()
# 			time.sleep(7)
# 			elem = len(driver.find_elements_by_xpath("//div[text()='OK']")) > 0
# 			print(elem)
# 			if elem:
# 				print("yeah")
# 				driver.close()
# 			else:
# 				print("Not found")
# 				send_message()
# 				driver.close()
		
# 		else:
# 			print("It is tab 2")
# 			switch_tab(2)
# 			use_whatsapp_here()
# 			time.sleep(5)
# 			elem = len(driver.find_elements_by_xpath("//div[text()='OK']")) > 0
# 			print(elem)
# 			if elem:
# 				print("yeah")
# 			else:
# 				print("Nah")
# 				send_message()
# 			time.sleep(1)
# 			switch_tab(1)
# 			driver.close()
# 			switch_tab(1)
# 		no = no - 1


