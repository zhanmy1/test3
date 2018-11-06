import sys

class Dog:
	
	def __del__(self):
		print("------释放了内存------")

dog1 = Dog()
dog2 = dog1 #与dog1指向同一个对象
print(sys.getrefcount(dog1)) #测量一个对象的引用计数的方式
del dog1 #不会调用__del__方法，因为这个对象还有其他的变量指向它，即引用计算不是0
del dog2 #此时会调用__del__方法，因为没有变量指向它了
print("==================")
#如果在程序结束时，有些对象还存在，那么python解释器会自动调用他们的__del__方法来完成清理工作