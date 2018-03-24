from selenium import webdriver
from time import sleep
from selenium.webdriver.common import touch_actions as TA

WIDTH = 414
HEIGHT = 736
PIXEL_RATIO = 3.0
UA = 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'

mobileEmulation = {"deviceMetrics": {"width": WIDTH, "height": HEIGHT, "pixelRatio": PIXEL_RATIO}, "userAgent": UA}
options = webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation', mobileEmulation)

driver = webdriver.Chrome(chrome_options=options)
driver.implicitly_wait(2)
driver.get('http://pre2.xjuke.com/api/analog/login?userId=78')


employeeEle = driver.find_element_by_link_text('员工端')
employeeEle.click()

sleep(1)
srollELement = driver.find_element_by_css_selector('div.personal')
 
action = TA.TouchActions(driver)

action.scroll_from_element(srollELement,0,30).perform()


# microCardEle = driver.find_element_by_partial_link_text('微名片')
# microCardEle.click()
# sleep(1)
# imgeElement = driver.find_element_by_id('guide-qrcode')

# action = TA.TouchActions(driver)
# action.long_press(imgeElement).perform()
