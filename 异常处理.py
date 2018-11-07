try:
	11/0
	open("123.txt")
	print(num)
	print("---------1-------")

except (NameError,FileNotFoundError):
	print("如果捕获到异常后做的处理。。。。")
except Exception as ret:  #产生异常的原因会放到ret里
	print("如果用了Exception，那么意味着只要上面的except没有捕获到异常，这个一定会捕获到")
	print(ret)
else:
	print("没有异常才会执行的效果")
finally:
	print("-------finally---------")


print("-------2---------")
