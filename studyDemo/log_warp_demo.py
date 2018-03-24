import logging
import time
import traceback
from selenium import webdriver

def log(test_case_func):
	def wraps(*args, **keywords):
		log_name= time.strftime("%Y%m%d%H%M%S", time.localtime())+test_case_func.__name__
		logging.basicConfig(level=logging.INFO,filemode='w',filename='./'+log_name+'.log')
		test_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
		logging.info(test_time+':现在开始测试:'+test_case_func.__name__)
		try:
			test_case_func(*args, **keywords)
			logging.info(test_time+':测试成功完成！' )
		except:
			logging.info(test_time+':测试有异常:'+traceback.format_exc())
	return wraps
@log
def test_case1(driver):
	driver.get('https://www.baidu.com/?tn=sitehao123_15')
	driver.maximize_window()
	driver.find_element_by_id('kw11')


if __name__ == '__main__':
	driver = webdriver.Firefox()
	test_case1(driver)
