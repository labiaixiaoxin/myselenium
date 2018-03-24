from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener

class MyTestListenner(AbstractEventListener):
	def before_navigate_to(self, url, driver):
		print("前面一个执行地址 %s" % url)
	def after_navigate_to(self, url, driver):
		print("后面一个执行地址是 %s" % url)
	def on_exception(self,exception, driver):
		
		
driver = webdriver.Firefox()
el_driver = EventFiringWebDriver(driver, MyTestListenner())
el_driver.get('http://www.baidu.com')

element = driver.find_element_by_id('kw')
element.send_keys('1233455')

sorcheElement  = driver.find_element_by_id('su')
sorcheElement.click()
el_driver.back()