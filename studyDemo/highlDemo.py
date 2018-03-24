from selenium import webdriver
driver = webdriver.Firefox()
driver.get('https://www.baidu.com/index.php?tn=06008006_2_pg')
driver.implicitly_wait(2)
#js = 'var element = document.getElementById(\"kw\");element.style.border=\"1px solid red\";'
#driver.execute_script(js)
element = driver.find_element_by_id('kw')
driver.execute_script("arguments[0].style.border=\'1px solid red\'",element)