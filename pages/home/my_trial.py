from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://letskodeit.teachable.com/")
driver.find_element_by_link_text("Login").click()

#time.sleep(10)
driver.find_element_by_id("user_email").send_keys("twinkleSTAR")
time.sleep(10)