import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.hulu.com/search")
driver.maximize_window()
driver.close()
driver.switch_to.new_window()
driver.get("https://www.netflix.com/browse")
time.sleep(10)

# driver.quit()

