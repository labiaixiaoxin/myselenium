def before_fun():
	print('这是一个修饰符作用的测试')

@before_fun
def after_fun():
	print('这里测试调用！')

if __name__ == '__main__':
	after_fun()