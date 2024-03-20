
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.maximize_window() # testing
print(driver.title) # title of the page
print(driver.current_url)#print the url
driver.close()