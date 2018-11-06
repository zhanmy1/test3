class Dog:

	#私有方法
	def __send_msg(self):
		print("--------正在发送短信---------")

	#公有方法
	def send_msg(self,new_money):
		if new_money>10000:
			self.__send_msg()
		else:
			print("余额不足，请先充值 再发送短信")

dog = Dog()
dog.send_msg(100)

'''如果调用的是继承的父类的公有方法
可以在这个公有方法中访问父类中的私有属性和私有方法

但是如果在子类中实现了一个公有方法，
那么这个方法是不能够调用继承的父类中的私有方法和私有属性'''