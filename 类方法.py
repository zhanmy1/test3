class Game(object):

	#类属型
	num = 0

	#实例方法
	def __init__(self):
		#实例属性
		self.name = "laowang"

	#类方法
	@classmethod
	def add_num(cls): #cls用来保存类的引用
		cls.num = 100

	#静态方法
	@staticmethod
	def print_menu():
		print("--------------")
		print("-------1-------")
		print("-------2-------")
		print("---------------")

game = Game()
Game.add_num() #可以通过类的名字调用类方法
#game.add_num() #还可以通过这个类创建出来的对象去调用这个类方法
print(Game.num)

#Game.print_menu() #通过类调用静态方法
game.print_menu() #通过实例对象调用