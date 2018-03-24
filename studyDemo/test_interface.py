
import unittest
import requests
import json

class TestInterface(unittest.TestCase):
    def setUp(self):
        pass
    # @unittest.skip(/"111")
    def test_case(self):
        url = "http://pctest2.xjuke.com/site/index?c=a-92d#/crm/elect"
        data = {
            "Accept": "application / json, text / plain, * / *",
            "Accept - Encoding": "gzip, deflate",
            "Accept - Language": "zh-CN,zh;q=0.8",
            "Cache - Control": "max - age = 0",
            "Connection": "keep - alive",
            "Content - Length": 97,
            "Content - Type": "application / json;charset = UTF - 8",
            "Cookie": "Hm_lvt_8e255a4d8e4a0180aa15c7c102a02c8f = 1511675745, 1513391411, 1513435331, 1513606388;\
                                XJKSESSID = 1dnuq6b067nut9l0lsdfj0qut0",
            "Host": "pctest2.xjuke.com",
           "Origin": "http: // pctest2.xjuke.com",
            "Referer": "http: // pctest2.xjuke.com / site / index?c = a - 92d",
            "User - Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
                            Chrome/51.0.2704.103 Safari/537.36",
            "cModuleId": "382",
            "cSetsId": "176",
            "currentPage": 1,
            "pageSize" : 10,
            "searchName": "",
            "timeStatus": -1
        }
        res = requests.post(url=url, data=data)
        print("112")
        print(res.text)
        print(json.load(res.text).get('data'))
    @unittest.skip("11")
    def test_json(self):

        r = requests.get('https://github.com/timeline.json')
        print(r.text)
    def tearDown(self):
        pass
if __name__ =="__main__":
    unittest.main()

