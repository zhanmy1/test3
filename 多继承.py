class Base(object):   #object是所有类的基类
	def test(self):
		print("-------test")

class A(Base):
	def test1(self):
		print("-------test1")

class B(Base):
	def test2(self):
		print("--------test2")

class C(A,B):  #多继承
	pass

c = C()
c.test1()
c.test2()
c.test()

print(C.__mro__)  
#打印一个元组，决定着调用一个方法的时候搜索的顺序，如果在某一个类中找到了方法就停止搜索