from selenium import webdriver
driver = webdriver.Firefox()

driver.get('https://www.baidu.com/index.php?tn=06008006_2_pg')
driver.implicitly_wait(2)

parentElemtn = driver.find_element_by_id('form')
#childElemnt =parentElemtn.find_element_by_xpath('./span[@class="bg s_ipt_wr quickdelete-wrap"]')
#childElemnt =driver.find_element_by_xpath('//span[@class="bg s_ipt_wr quickdelete-wrap"]')
childElemnt =driver.find_element_by_xpath('descendant::input[@name=\'wd\']')
childElemnt.send_keys('1223')
