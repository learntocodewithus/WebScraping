import requests
from bs4 import BeautifulSoup
from time import sleep
import csv


headers = {'User-Agent': 'Mozilla/5.0'}

# inputs 	
# position = input("Please enter job title: ")
# city = input("Please enter city: ")
# state = input("Please enter state: ")

position = "Python"
city = "New York"
state = "NY"
	
url = "https://www.indeed.com/jobs?q="+position+"&l="+city+"%2C+"+state
print ("Processing: "+url)
page = requests.get(url,headers=headers)
bsobj = BeautifulSoup(page.content, "html.parser")
# print(bsobj)

hrefs = bsobj.find_all('a', {"data-tn-element":"jobTitle"}, href=True)
hrefs = [link['href'].strip() for link in hrefs]

titles = bsobj.findAll("a", {"data-tn-element":"jobTitle"})
# print(titles)
titles = [t.get_text().strip() for t in titles]
# print(titles)
# for t in titles:
# 	print(t.get_text().strip())

salary = bsobj.findAll("span", class_="no-wrap")
# print(salary)
snippets = bsobj.findAll("span", class_="summary")
snippets = [s.get_text().strip() for s in snippets]
hyperlink_format = '<a href="{link}">{text}</a>'
links =[]
for link in hrefs:
	links.append(hyperlink_format.format(link='https://www.indeed.com'+link, text='Read More'))

TMPL = '''
	
	Title: {title}

	Snippet: {snippet}

	Link: {link}
	'''
positions = zip(titles, snippets, links)
# # print(titles)
# # for i in positions:
# # 	print(i)

for pos in positions:
	print(TMPL.format(title=pos[0],snippet=pos[1],link=pos[2]))













