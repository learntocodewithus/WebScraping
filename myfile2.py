import requests
from bs4 import BeautifulSoup

def fetching_url():
	position = "Python"
	city = "New York"
	state = "NY"
	
	url = "https://www.indeed.com/jobs?q="+position+"&l="+city+"%2C+"+state
	print ("Processing: "+url)
	html = requests.get(url)
	bsobj = BeautifulSoup(html.content,"html.parser") 
	
	hrefs = bsobj.find_all('a', {"data-tn-element":"jobTitle"}, href=True)
	print(hrefs)
	hrefs = [link['href'].strip() for link in hrefs]
	# print(len(hrefs))

	titles = bsobj.findAll("a", {"data-tn-element":"jobTitle"})
	titles = [t.get_text().strip() for t in titles]
	# print(titles)
	# for t in titles:
# 	print(t.get_text().strip())
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
	# print(list(positions))
	for pos in positions:
		print(type(pos))
		print(TMPL.format(title=pos[0],snippet=pos[1],link=pos[2]))

fetching_url()



# name = "John"
# print("Hello {}, How are you?".format(name))






