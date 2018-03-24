from  selenium  import webdriver
import requests
import json

base_url = 'http://www.baidu.com'
r = requests.get(base_url)
code = r.status_code
text = json.dumps(r.text,sort_keys=True)

print(code)
print(text)