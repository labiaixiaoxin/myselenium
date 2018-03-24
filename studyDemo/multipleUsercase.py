from selenium import webdriver
import threading
from time import sleep

def news(driver):
#	driver = webdriver.Firefox()
	driver.get('https://www.baidu.com/index.php?tn=06008006_2_pg')
	driver.implicitly_wait(2)
	elementnews = driver.find_element_by_name('tj_trnews')
	elementnews.click()

def map(driver):
#	driver = webdriver.Firefox()
	driver.get('https://www.baidu.com/index.php?tn=06008006_2_pg')
	driver.implicitly_wait(2)
	elementmap = driver.find_element_by_name('tj_trmap')
	elementmap.click()

threads = []
tnews = threading.Thread(target=news,args=(webdriver.Firefox(),))
threads.append(tnews)
tmap = threading.Thread(target=map,args=(webdriver.Firefox(),))
threads.append(tmap)

if __name__ == '__main__':
	for t in threads:
		t.setDaemon(True)
		t.start()
		
	t.join()
