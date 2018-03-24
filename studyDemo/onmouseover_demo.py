from selenium import webdriver
driver = webdriver.Firefox()
driver.get('https://www.baidu.com/index.php?tn=06008006_2_pg')
driver.implicitly_wait(2)
set_element = driver.find_element_by_link_text('设置')
driver.execute_script("$(arguments[0]).mouseover()",set_element)
search_set_ele = driver.find_element_by_link_text('搜索设置')
search_set_ele.click()
