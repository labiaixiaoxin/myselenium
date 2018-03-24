from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time, os.path

d={#'http://127.0.0.1:6666/wd/hub' :'chrome',
     'http://127.0.0.1:4444/wd/hub' : 'firefox'
     # 'http://127.0.0.1:5555/wd/hub':'internet explorer'
        }
# capabilities = DesiredCapabilities.CHROME.copy()
# capabilities['platform'] = "WINDOWS"
# capabilities['version'] = "10"
for host, browser in d.items():
    driver = webdriver.Remote(
        command_executor=host,
        desired_capabilities={
            'platform': 'WINDOWS',
            'browserName':browser
        }
    )
# host  ='http://127.0.0.1:6666/wd/hub'
# driver = webdriver.Remote(command_executor=host,desired_capabilities=capabilities)

driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys("中国")
driver.find_element_by_id("su").click()
time.sleep(3)

