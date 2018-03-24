from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get('https://www.baidu.com/?tn=80035161_1_dg&ocid=msncn')
childrenelement = driver.find_element_by_id('kw')
#'.' 表示当前节点 ，'.. '表示父节点# 
#parentelement = childrenelement.find_element_by_xpath('./..')
# xpath轴 parent
parentelement = childrenelement.find_element_by_xpath('parent::*')

print(parentelement.get_attribute('class'))
