# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep

# WIDTH = 414
# HEIGHT = 736
# PIXEL_RATIO = 3.0
# UA = 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'

# mobileEmulation = {"deviceMetrics": {"width": WIDTH, "height": HEIGHT, "pixelRatio": PIXEL_RATIO}, "userAgent": UA}
# options = webdriver.ChromeOptions()
# options.add_experimental_option('mobileEmulation', mobileEmulation)

# driver = webdriver.Chrome(chrome_options=options)
# driver.get('http://m.baidu.com')

# sleep(3)
# driver.close()
mobileEmulation = {'deviceName': 'Apple iPhone 6 Plus'}
options = webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation', mobileEmulation)

driver = webdriver.Chrome(chrome_options=options)

driver.get('http://m.baidu.com')