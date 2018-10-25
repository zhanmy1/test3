
func = lambda x,y:x+y    #func指向匿名函数
a = func(5,3)
print(a)


nums = [15,52,44,11,26,95,20,2]
nums.sort()    #排序
print(nums)   


stus = [{"name":"laowang","age":18},{"name":"zhangsan","age":13},{"name":"wangwu","age":19}]
stus.sort(key=lambda x:x['name'])
print(stus)

stus.sort(key=lambda y:y['age'])
print(stus)

def test(a,b,func):
	result = func(a,b)
	print(result)

func_new = input("请输入一个匿名函数")
func_new = eval(func_new)
test(11,22,func_new)

