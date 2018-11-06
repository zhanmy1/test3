class Dog(object):
	def print_self(self):
		print("----------hello-----------")

class Xiaotq(Dog):
	def print_self(self):
		print("hello everybody,----------")

def introduce(temp):
	temp.print_self()  #根据当前的对象调用不同的方法

dog1 = Dog()
dog2  =Xiaotq()

introduce(dog1)
introduce(dog2)