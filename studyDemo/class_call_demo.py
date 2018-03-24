class CountDemo:
	def __init__(self,a,b):
		self.a = a
		self.b = b

	def __call__(self):
		return count(self.a,self.b)

def count(a,b):
		return a + b
	
if  __name__ == '__main__':
	countdemo = CountDemo(1,3)
	countdemo1=countdemo.__call__()
	print(str(countdemo1))
