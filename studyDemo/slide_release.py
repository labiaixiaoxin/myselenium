from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time

#driver = webdriver.Firefox()
driver = webdriver.Chrome()
#driver.get('http://passport.csdn.net/account/mobileregister?ref=toolbar&action=mobileRegister')
driver.implicitly_wait(2)

# slideElement = driver.find_element_by_id('nc_1_n1z')
# action = ActionChains(driver)
# action.click_and_hold(slideElement).perform()  #鼠标左键按下不放

# for i in range(1,200):
	# try:
		# action.move_by_offset(10,0).perform() #平行移动鼠标
		# driver.find_element_by_xpath('//b[text=\'验证通过\']')
		# print("解码成功")
		# break
	# except NoSuchElementException:
		# action.reset_actions()
		# time.sleep(0.1)  #等待停顿时间
		
# driver.get("https://www.helloweba.com/demo/2017/unlock/")

# dragger = driver.find_elements_by_class_name("slide-to-unlock-handle")[0]

# action = ActionChains(driver)

# action.click_and_hold(dragger).perform()  #鼠标左键按下不放

# for index in range(200):
    # try:
        # action.move_by_offset(2, 0).perform() #平行移动鼠标
    # except UnexpectedAlertPresentException:
        # break
    # action.reset_actions()
    # time.sleep(0.1)  #等待停顿时间





