from selenium.webdriver import Chrome
import csv

#provide a path to chromedriver
chromedriver = '/Users/mclaren/Downloads/CodingFor/chromedriver'
driver = Chrome(chromedriver)

driver.get('http://www.cmegroup.com/trading/equity-index/us-index/e-mini-sandp500.html')

# def table_to_csv():
csvFile = open("sp_h.csv", 'wt')
writer = csv.writer(csvFile)

table = driver.find_element_by_id("quotesFuturesProductTable1")
# print(table.text)
rows = table.find_elements_by_tag_name("tr")
# for i in rows[3::]:
# 	print(i.text)
listOfRows = [row.text.split() for row in rows[3:]]
for csvRow in listOfRows:
	print("--->",csvRow)
	writer.writerow(csvRow)

driver.close()
