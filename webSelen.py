from selenium.webdriver import Chrome

#install ChromeDriver - WebDriver for Chrome
#chromium.org

#provide a path to chromedriver
chromedriver = '/Users/mclaren/Downloads/CodingFor/chromedriver'
driver = Chrome(chromedriver)

# chrome.open()  # this opens a Chrome window

driver.get('https://amazon.com')  # navigates to the target website in Chrome


