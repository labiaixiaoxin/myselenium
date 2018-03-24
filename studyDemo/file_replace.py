def replace_file(sourceName , ObjectName):
	#print(2)
	#源文件
	source_file = open(sourceName,'r')
	
	#读取源文件的所有内容
	all = source_file.read()
	#print(1)
	print(all)
	replace_all = all.replace(',',';')
	print(replace_all)
	source_file.close()
	
	#目标文件
	Object_file = open(ObjectName,'w')
	Object_file.write(replace_all)
	Object_file.close()
if __name__ == '__main__':
	#print(3)
	replace_file('./1.txt' , './2.txt')
	#source_file = open('C:\\study\\selenium\\code\\studyDemo\\1.txt','r')
	#print(source_file.read())
