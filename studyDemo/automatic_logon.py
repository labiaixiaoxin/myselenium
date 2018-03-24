import urllib
import urllib.request
import gzip
import http
import http.cookiejar

#定义一个方法用于生成请求头信息，处理cookie  
def getOpener(head):
	# 初始化一个CookieJar来处理Cookie <pre name="code" class="python">  
	cj = http.cookiejar.CookieJar()
	#实例化一个opener
	pro = urllib.request.HTTPCookieProcessor(cj)
	opener = urllib.request.build_opener(pro)
	
	header = []
	for key, value in head.items():
		elem = (key, value)
		header.append(elem)
	opener.addheaders = header
	return opener
	
def ungzip(data):
#定义一个方法来解压返回信息
	try:     # 尝试解压
		print('正在解压.....')
		data = gzip.decompress(data)
		print('解压完毕!')
	except:
		print('未经压缩, 无需解压')
	return data
	
	
#执行操作，就是登陆
def  login(header,url,postDict):
	# #封装头信息，伪装成浏览器  
	# header = {  
		# 'Connection': 'Keep-Alive',  
		# 'Accept-Language': 'zh-CN,zh;q=0.8',  
		# 'Accept': 'application/json, text/javascript, */*; q=0.01',  
		# 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',  
		# 'Accept-Encoding': 'gzip, deflate',  
		# 'X-Requested-With': 'XMLHttpRequest',  
		# 'Host': 'www.17sucai.com',  
# }  
# url = 'http://www.17sucai.com/auth'  
# id = 'xxxxxxxxxxxxx'#你的用户名   
# password = 'xxxxxxx'#你的密码  
	# postDict = {  
		# 'username': id,
		# 'password': password,
		# 'wechatCode':'q-5ce'
	# }
	opener = getOpener(header)
	postData = urllib.parse.urlencode(postDict).encode()
	op = opener.open(url, postData)
	data = op.read()
	data = ungzip(data)
	print(data)
if  __name__ == '__main__':
	header = {
		'Host': 'pcpre2.xjuke.com',
		'Connection': 'keep-alive',
		'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
		'Accept': 'application/json, text/plain, */*',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0',
		'Accept-Encoding': 'gzip, deflate',
		'Content-Type': 'application/json;charset=utf-8',
		'Referer': 'http://pcpre2.xjuke.com/?c=q-5ce/',
		'Content-Length': '58'
	}
	
	postDict = {
		'username': 'wyp',
		'password': '123456',
		'wechatCode':'q-5ce'
	}
	login(header,'http://pcpre2.xjuke.com/login/login',postDict)
