
#1.获取要复制的文件名 input（）
old_file_name = input("请输入要复制的文件名（需要后缀）：")

#2.打开这个文件（“r”）
f_read = open(old_file_name,"r")

#3.创建一个文件 xxx[复件].txt
position = old_file_name.rfind(".")
new_file_name = old_file_name[0:position] + "[复件]" + old_file_name[position:]
f_write = open(new_file_name,"w")

#4.从原文件中读取数据
content = f_read.read()

#5.将读取的数据写入到新文件中
f_write.write(content)


#6.关闭两个文件
f_read.close()
f_write.close()