class SweetPotato:
	
	def __init__(self):
		self.cookedString = "生的"
		self.cookedLevel = 0
		self.condiments = []#为了能够存储多个数据，让一个属性是列表

	def __str__(self):
		return "地瓜 状态：%s(%d),添加的佐料有：%s"%(self.cookedString,self.cookedLevel,str(self.condiments))

	def cook(self,cooked_time):

		'''因为这个方法被调用了多次，为了能够在一次调用这个方法的时候能够获取到
		上一次调用这个方法时的cooked_time所以需要在此把cooked_time保存到这个
		对象的属性中，因为属性不会随着方法的调用而结束（一个方法被调用的时候是
		可以用局部变量来保存数据的，但是当这个方法定义结束之后这个方法中的所有
		数据就没有了）'''
		self.cookedLevel += cooked_time

		if self.cookedLevel >=0 and self.cookedLevel<3:
			self.cookedString = "生的"
		elif self.cookedLevel >=3 and self.cookedLevel<5:
			self.cookedString = "半生不熟"
		elif self.cookedLevel >=5 and self.cookedLevel<8:
			self.cookedString = "熟了"
		elif self.cookedLevel >8:
			self.cookedString = "烤糊了"

	def addCondiments(self,item):
		#因为item这个变量指向了一个佐料，所以接下来需要将item放到append里面
		self.condiments.append(item)

#创建了一个地瓜对象
di_gua = SweetPotato()
print(di_gua)

#开始烤地瓜
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.addCondiments("大蒜")
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
di_gua.addCondiments("番茄酱")
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)
