class Store(object):

	def select_car(self):
		pass

	def order(self,money,car_type):
		return self.select_car(car_type)

class BNWCarStore(object):
	def select_car(self,car_type):
		return BNWFactory(),select_car_by_type(car_type)

bnw_store = BNWCarStore()
bnw = bnw_store.order("720li")



class CarStore(object):
	def select_car(self,car_type):
		return Factory.select_car_by_type(car_type)

class BNWFactory(object):
	def select_car_by_type(car_type):
		pass
		
class Factory(object):
	def select_car_by_type(car_type):
		if car_type=="索纳塔":
				return Suonata()
			elif car_type=="名图":
				return Mingtu()

class Car(object):
	def move():
		print("车在移动。。。。。。。。。")
	def musice():
		print("正在播放音乐。。。。。。")
	def stop():
		print("车在停止。。。。。。。。。")

class Suonata(Car):
	pass

class Mingtu(Car):
	pass


car_store = CarStore()
car = car_store.order("索纳塔")
car.move()
car.musice()
car.stop()