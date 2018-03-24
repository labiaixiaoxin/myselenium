from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

def get_element (driver, option, value):
	elementDic = {
					'n':try：driver.find_elements_by_name(value)
						except NoSuchElementException:
						print (u'元素未找到')
						