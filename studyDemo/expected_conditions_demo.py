from selenium import webdriver
from  selenium.webdriver.support import  expected_conditions as EC
driver = webdriver.Firefox()
driver.get('https://www.baidu.com/index.php?tn=06008006_2_pg')
driver.implicitly_wait(2)
#js = 'var element = document.getElementById(\"kw\");element.style.border=\"1px solid red\";'
#driver.execute_script(js)
#element = driver.find_element_by_id('kw')
#driver.execute_script("arguments[0].style.border=\'1px solid red\'",element)

#driver.execute_script("arguments[0].style.display=\'block\'",element)
#element1 =EC.visibility_of(element)
# element = driver.find_element_by_id('quickdelete')
# element1 =EC.visibility_of(element)
# print(element1)

# if  ((EC.visibility_of(element))._element_if_visible()):
		# print(u'元素是可见的')
# else:
		# print(u'元素是不可见的')
		
class visibility_of(object):
    """ An expectation for checking that an element, known to be present on the
    DOM of a page, is visible. Visibility means that the element is not only
    displayed but also has a height and width that is greater than 0.
    element is the WebElement
    returns the (same) WebElement once it is visible
    """
    def __init__(self, element):
        self.element = element

    def __call__(self, ignored):
        return _element_if_visible(self.element)


def _element_if_visible( self, visibility=True):
    return element if element.is_displayed() == visibility else False

		 
