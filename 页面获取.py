#对网页进行访问需要用到urllib之类的包
import urllib.request
#这个包中有urllib.urlopen(str)方法用于打开网页并返回一个对象，
#调用这个对象的read方法后能直接获得网页的源代码，内容与浏览器右键查看源码内容一样

def get_html(url):
	page = urllib.request.urlopen(url)  #打开网页
	html = page.read()  #读取页面源代码
	return html

page1 = get_html("http://sohu.com")
pageFile = open('pageCode.txt','wb+')  #以写的方式打开pagecode.txt,存储方式默认二进制
pageFile.write(page1)  #写入
pageFile.close()  #关闭