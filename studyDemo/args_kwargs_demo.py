def test_args(*args):
	print(args)
	
	
def test_kwargs(**kwargs):
	print(kwargs)
	
if __name__ == '__main__':
	test_args(1,2,3,4)#输出结果是(1, 2, 3, 4)
	test_kwargs(one=1,two=2)#输出结果是{'one': 1, 'two': 2}
