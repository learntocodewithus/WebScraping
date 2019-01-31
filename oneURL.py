from urllib.request import urlopen
from bs4 import BeautifulSoup

def fetching_url():
	html = urlopen("http://shakespeare.mit.edu/lll/full.html")
	# print(html)
	bsobj = BeautifulSoup(html.read(), "html.parser")
	# print(bsobj.h3.get_text())

	h3 = bsobj.findAll("h3")  
	# print(h3)

	# # step four
	nameList = bsobj.findAll(text="DUMAIN")
	print(nameList)
	print(len(nameList))

	# # step four
	new_object = bsobj.find("a",{"name":"1.1.9"})
	# print(new_object.get_text())

	# allTags = bsobj.findAll('h3',limit=2)
	# for t in allTags:
	# 	print(t)


fetching_url()