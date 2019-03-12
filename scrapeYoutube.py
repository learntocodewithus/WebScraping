import requests
from bs4 import BeautifulSoup
from time import sleep
import csv
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys


	
url = "https://www.youtube.com/user/whatsg/videos"
chromedriver = '/Users/mclaren/Downloads/CodingFor/chromedriver'
driver = Chrome(chromedriver)
driver.get(url)
html = driver.find_element_by_tag_name('html')
# title = driver.find_elements_by_id('video-title')
html.send_keys(Keys.END)
# print("-------------sleeping-----------------")
sleep(3)
html.send_keys(Keys.END)
# print("-------------sleeping-----------------")
sleep(3)
title = driver.find_elements_by_id('video-title')


titles = [i.text for i in title]
print(titles)
print("----------------------Number of titles {} ---------------------------".format(len(titles)))

driver.close()




