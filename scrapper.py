from selenium import webdriver

TARGET_URL = "https://www.gst.gov.in"

driver = webdriver.chrome()

driver.get(TARGET_URL)

print(driver.title)

