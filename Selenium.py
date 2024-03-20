import time
from selenium import webdriver
from selenium.webdriver.safari.service import Service
from selenium.webdriver.safari.options import Options
# Set Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
chrome_options.add_argument("--no-sandbox")  # Bypass OS security model

# Set Chrome driver path
chrome_driver_path = "/Users/chromedriver-mac-arm64/chromedriver"

# Create a Chrome WebDriver instance
driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)

# Navigate to a website
driver.get("https://www.facebook.com/")
time.sleep(20)

# Rest of your Selenium code...
