from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/login")
driver.maximize_window()
sleep(2)
username = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
print("Username field located", username)
password = driver.find_element(By.CSS_SELECTOR, "input#password")
print("Password field located",password)
username.send_keys("")
password.send_keys("")
login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
print("Login button located",login_button)
footer_link = driver.find_element(By.CSS_SELECTOR, "div#page-footer a")
print("Footer link text:", footer_link)

sleep(5)

driver.quit()