from selenium import webdriver
import os
from webdriver_manager.chrome import ChromeDriverManager

def bomb():
	driver = webdriver.Chrome(ChromeDriverManager().install())
	driver.get('https://web.whatsapp.com/')

	name = input('Enter the name of user or group: ')
	msg = input('Enter the message you want to bomb: ')
	count = input('Enter the number of times you want to send: ')

	input('Scan the QR code and then press any key to proceed.')

	user = driver.find_element_by_xpath(f'//span[@title="{name}"]')
	user.click()

	msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
	for i in range(int(count)):
		msg_box.send_keys(msg)
		button = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
		button.click()

	print('Task Complete!')


if __name__ == '__main__':
	bomb()