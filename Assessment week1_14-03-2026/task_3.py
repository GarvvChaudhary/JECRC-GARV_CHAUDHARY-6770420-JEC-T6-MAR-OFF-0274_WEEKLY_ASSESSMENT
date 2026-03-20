from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

sleep(3)
driver.get("https://www.thesouledstore.com")
print("Title:", driver.title)

sleep(3)
driver.get("https://www.nike.com")
print("Title:", driver.title)

sleep(3)
driver.get("https://www.amazon.in")
print("Title:", driver.title)

sleep(3)
driver.get("https://www.bbc.com/news")
print("Title:", driver.title)

sleep(3)
driver.get("https://www.python.org")
print("Title:", driver.title)

driver.quit()