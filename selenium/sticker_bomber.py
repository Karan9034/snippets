from selenium import webdriver
import os, random, time
from webdriver_manager.chrome import ChromeDriverManager

def bomb():
	driver = webdriver.Chrome(ChromeDriverManager().install())
	driver.get('https://web.whatsapp.com/')
	name = input('Enter the name of user or group: ')
	count = input('Enter the number of times you want to send: ')
	input('Scan the QR code and then press any key to proceed.')
	try:
		user = driver.find_element_by_xpath(f'//span[@title="{name}"]')
		user.click()
		msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
		msg_box.send_keys(f'Hey {name}!!! Sticker Bombing Coming Up')
		
		send_button = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
		send_button.click()
		
		emoji_button = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div[1]/button[2]/span')
		emoji_button.click()
		sticker_button = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div[1]/button[4]/span')
		sticker_button.click()
		
		time.sleep(10)

		for i in range(int(count)):
			n = random.randint(1,5)
			sticker = driver.find_element_by_xpath(f'//*[@id="main"]/footer/div[2]/div/div[3]/div[1]/div/div[1]/div[2]/div/div[{n}]/div/span/img')
			sticker.click()

		time.sleep(10)
	except:
		print("Some Error Happened! You've been logged out safely!")
	finally:
		options = driver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[3]/div/span')
		options.click()
		logout = driver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[3]/span/div[1]/ul/li[7]/div[1]')
		logout.click()
		print('Task Complete!')


if __name__ == '__main__':
	bomb()