import requests
from bs4 import BeautifulSoup


html = requests.get("http://shakespeare.mit.edu/lll/full.html")
bsobj = BeautifulSoup(html.content, "html.parser")
print(bsobj)
h3 = bsobj.findAll("h3")  
# print(h3)


nameList = bsobj.findAll(text="DUMAIN")
print(nameList)
print(len(nameList))

	
new_object = bsobj.find("a",{"name":"1.1.9"})
# print(new_object.get_text())

# allTags = bsobj.findAll('h3',limit=2)
# for t in allTags:
# 	print(t)

