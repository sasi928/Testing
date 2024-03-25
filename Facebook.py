import os  # Importing the os module for operating system-related functionalities.
import time  # Importing the time module for time-related functions.
from selenium import webdriver  # Importing the Selenium WebDriver module for browser automation.
from selenium.webdriver.chrome.service import Service  # Importing the Chrome service for WebDriver.
from selenium.webdriver.common.by import By  # Importing the By module for locating elements by different strategies.
from selenium.webdriver.chrome.options import Options  # Importing ChromeOptions for setting browser options.

option1 = Options()  # Creating an instance of ChromeOptions.
option1.add_argument("--disable-notifications")  # Adding an argument to disable notifications.
ser_obj = Service("/Users/chromedriver-mac-arm64/chromedriver")  # Creating a service object for ChromeDriver.
driver = webdriver.Chrome(service=ser_obj, options=option1)  # Initializing the Chrome WebDriver with service and options.
driver.get("https://www.facebook.com/")  # Opening the Facebook login page in the browser.
email = driver.find_element(By.XPATH, "//*[@id=\"email\"]")  # Finding the email input field using XPath.
email.send_keys('goud.sasi@gmail.com')  # Entering the email address into the email input field.
password = driver.find_element(By.XPATH, '//*[@id=\"pass\"]')  # Finding the password input field using XPath.
password.send_keys('Sasi@123456')  # Entering the password into the password input field.
driver.find_element(By.NAME, ('login')).click()  # Clicking the login button to log in to Facebook.
driver.find_element(By.XPATH, "(//*[name()='image'])[1]").click()  # Clicking on the user profile image.
driver.find_element(By.XPATH, "(//span[normalize-space()='Log Out'])[1]").click()  # Clicking on the Log Out option.
time.sleep(20)  # Pausing execution for 20 seconds (not recommended, consider using WebDriverWait instead).
# driver.switch_to.alert.accept()  # Uncomment this line if you want to handle any alert that may appear after logout.
