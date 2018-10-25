ticket = input("你是否有车票？")
if ticket=="有":
	print("通过车票的检查，进入安检")
	knifeLenght = int(input("你携带的刀具的长度："))
	if knifeLenght<=10:
		print("通过")
	else:
		print("请留下你的刀")
else:
	print("请到售票厅买票")
#添加一个注释用于测试
#再添加一个注释用于测试
#000000