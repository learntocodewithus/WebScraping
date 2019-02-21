from urllib.request import urlopen
from bs4 import BeautifulSoup

def fetching_url():
	html = urlopen("http://shakespeare.mit.edu/lll/full.html")
	print(html)
fetching_url()