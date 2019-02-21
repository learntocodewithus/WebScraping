from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time
 
 



	
url = "https://www3.hilton.com/en/index.html"
chromedriver = '/Users/mclaren/Downloads/CodingFor/chromedriver'
driver = Chrome(chromedriver)
driver.get(url)

form = driver.find_element_by_id("hotelSearchOneBox")
print(form)
checkin = driver.find_element_by_id("checkin")
checkout = driver.find_element_by_id("checkout")
checkin.clear()
checkout.clear()
checkin.send_keys("03 Mar 2019")
checkout.send_keys("10 Mar 2019")
checkin.send_keys(Keys.ENTER)
checkout.send_keys(Keys.ENTER)
form.send_keys("Miami")
form.send_keys(Keys.ENTER)
form.submit() 
# # Wait for 1 second
# time.sleep(1)

hotels = driver.find_elements_by_class_name('hotelDescription')
hotels = [[hotel.text] for hotel in hotels]
print(hotels)
# hotels = hotels.find_elements_by_tag_name("span")
prices = driver.find_elements_by_class_name('statusPrice')
prices = [price.text for price in prices]
print(prices)
print(list(zip(hotels,prices)))






