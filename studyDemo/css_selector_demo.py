from selenium import webdriver
driver = webdriver.Firefox()
driver.implicitly_wait(2)
driver.get('https://www.baidu.com/')
# element = driver.find_element_by_css_selector('input[name=\'wd\']')
# element.send_keys('123')
butELement = driver.find_element_by_css_selector("a:contains(\"hao123\")'")

butELement.click()
