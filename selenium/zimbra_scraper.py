# Yet to be completed

import os, time
from dotenv import load_dotenv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def scrape():
	load_dotenv()
	driver = webdriver.Chrome(ChromeDriverManager().install())
	driver.get('https://mail.nitrkl.ac.in')
	
	username = os.environ.get('ZIMBRA_USER')
	password = os.environ.get('ZIMBRA_PASS')

	user_box = driver.find_element_by_xpath('//input[@id="username"]')
	pass_box = driver.find_element_by_xpath('//input[@id="password"]')
	submit = driver.find_element_by_xpath('//input[@type="submit"]')
	user_box.send_keys(username)
	pass_box.send_keys(password)
	submit.click()

def get_unread_mails():
	pass 					# Yet to complete this function

if __name__ == '__main__':
	scrape()
	time.sleep(2)
	get_unread_mails()