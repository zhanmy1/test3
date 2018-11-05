import urllib.request
import re

def get_html(url):
	page = urllib.request.urlopen(url)  
	html = page.read()
	html = html.decode('utf-8')  
	return html



def get_img(html_code):
	
	reg = r'src="(.+?\.jpg)" width' #正则表达式,匹配以src="开头然后接一个或多个任意字符串
	                                #以.jpg"width结尾的字符串

	reg_img = re.compile(reg) #编译一下，运行更快
	imglist = reg_img.findall(html_code)  #进行匹配
	x = 0
	for img in imglist:
		urllib.request.urlretrieve(img,'%s.jpg'%x)  #以第二个参数为名字下载链接中的内容
		x +=1

print("------------网页图片抓取------------")
print("请输入要提取的网址：")
url = input()
if url:
	pass
else:
	print("---没有地址输入正在使用默认地址---")
	url = "http://www.sohu.com"
print("------------正在获取网页------------")
html_code = get_html(url)
print("------------正在下载图片------------")
get_img(html_code)
print("--------------下载成功--------------")