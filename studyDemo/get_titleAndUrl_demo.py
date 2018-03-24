from selenium import webdriver
import sqlite3

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://toutiao.io/')
elements = driver.find_elements_by_css_selector('div#daily a[target=\'_blank\']')
elemeDataList = []
# for i in range(0,10):
     # elemeDataList.append((elements[i].get_attribute('title'),elements[i].get_attribute('href')))
# print (elemeDataList)

conn = sqlite3.connect("C:\\sqlite3\\db\\storeddata.db")
cur = conn.cursor()
# sqli="insert into INPUTDATA values(%s,%s)"
print('开始插入数据！')
for i in range(0,10):
    cur.execute("insert into INPUTDATA values('"+elements[i].get_attribute('title')+"','"+elements[i].get_attribute('href')+"')")
conn.commit()
print('提交完成！')
conn.close()
print('好了！')
