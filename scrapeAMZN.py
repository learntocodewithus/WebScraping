import csv
from selenium import webdriver
from selenium.webdriver import Chrome
#NEW AMAZON SCRIPT

asin_list = ['B07FPRZ69X','B06XCM9LJ4','B079QHML21']
chromedriver = '/Users/mclaren/Downloads/CodingFor/chromedriver'
driver = Chrome(chromedriver)

csvFile = open("amzn.csv", 'wt')
writer = csv.writer(csvFile)


# title = bsobj.find("span",{"id":"productTitle"})
# print(title)
for product in asin_list:
	csvRow = []
	url = "https://www.amazon.com/dp/"+product
	driver.get(url)

	p_element = driver.find_element_by_id('productTitle')
	p_element =  p_element.text
	print(p_element)
	try:
		price = driver.find_element_by_id('priceblock_dealprice')
		price = price.text
	except:
		pass
	try:
		price = driver.find_element_by_id('priceblock_ourprice')
		price = price.text
	except:
		pass
	bullets = driver.find_element_by_id("feature-bullets")
	bullets = bullets.text
	bulletsList = bullets.split("\n")
	bulletsList = [i for i in bulletsList]
	csvRow.extend((p_element,price))
	csvRow.extend(bulletsList)
	print(csvRow)
	writer.writerow(csvRow)