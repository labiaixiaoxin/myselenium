from selenium import webdriver

from selenium.common.exceptions import  NoSuchElementException
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('http://www.iqiyi.com/index.html')
registerEle = driver.find_element_by_link_text('注册')
registerEle.click()
time.sleep(1)
inputEl = driver.find_element_by_css_selector('p:contains(\'请输入手机号\')')
inputEl.click()
#teleponeEle = driver.find_element_by_css_selector('input[class=\'txt-info txt-account\']')
teleponeEle = driver.find_element_by_xpath('//input[@data-regbox=\'name\']')
teleponeEle.send_keys('18038168889')

registerButEle = driver.find_element_by_css_selector('a.btn-green btn-login btn-next btn-gray')

registerButEle.click()

while (True):
	try :
		resendEle = driver.find_element_by_link_text('重新发送')
		resendEle.clcik()
	except NoSuchElementException:
		time.sleep(1)
	
		

