import os
from selenium import webdriver
import time
driver = webdriver.Firefox()
nowTime = time.strftime('%Y%m%d.%H.%M.%S')
pwd =os.path.dirname(os.getcwd())
time.sleep(1)
driver.get_screenshot_as_file(pwd+'/Screenshots/%s.png'%nowTime)

