from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Set up ChromeDriver service
service = Service(executable_path="C:/chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Open Google
driver.get("https://www.google.com")

# Wait for a few seconds before closing the browser (optional)
time.sleep(5)  # Browser will stay open for 5 seconds

# Close the browser
driver.quit()
