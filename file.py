f = open("haha.txt","w")
f.write("haha")
print(f)
f.close()
f1 = open("haha.txt","r")
print(f1.read(1))
print(f1.read(1))
print(f1.read(1))
print(f1.read(1))
print(f1.read(1))
#每一次根据上一次的结果往后读
f.close()