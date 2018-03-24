# coding=UTF-8
from selenium import webdriver
import time
def get_attribute_demo (driver , url, telepone):
	driver.get(url)
	time.sleep(2)
	element =driver.find_element_by_xpath("//i[text()='密码登录']")
	element.click()
	time.sleep(2)
	element = driver.find_element_by_link_text("手机动态码登录")
	element.click()
	element = driver.find_element_by_id("loginMobile")
	element.send_keys(telepone)
	elementbut = driver.find_element_by_id("loginMobilecodeSendBtn")
	while (True):
		elementbutvalue = elementbut.get_attribute('value')
		if ((elementbutvalue in '获取动态码') or  (elementbutvalue in '重新获取')):
			elementbut.click()
			time.sleep(3)#等到按钮反应过来后在去判断
		
if __name__ == '__main__':
	driver = webdriver.Firefox()
	get_attribute_demo (driver,'https://passport.58.com/login/?path=http%3A//sz.58.com/&PGTID=0d100000-0000-4253-06a4-2bee4e07c01a&ClickID=1','18038168889')
