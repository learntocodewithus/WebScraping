import requests
from bs4 import BeautifulSoup
from time import sleep
import csv
from selenium import webdriver
from selenium.webdriver import Chrome


	
url = "https://www.youtube.com/user/whatsg/videos"
chromedriver = '/Users/mclaren/Downloads/CodingFor/chromedriver'
driver = Chrome(chromedriver)
driver.get(url)
title = driver.find_elements_by_id('video-title')

titles = [i.text for i in title]
print(titles)

# print(bsobj.findAll("a",{"class":"yt-simple-endpoint style-scope ytd-grid-video-renderer"}))


# headers = {'User-Agent': 'Mozilla/5.0'}
# page = requests.get(url,headers=headers)
# bsobj = BeautifulSoup(page.content, "html.parser")
# titles = bsobj.findAll()









# print(bsobj)