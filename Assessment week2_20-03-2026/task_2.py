'''

Automation script for the following

Open signup page https://automationexercise.com/signup
Enter name & email
Select Title (Mr/Mrs) → Radio button
Select checkboxes: Newsletter Special offers
Use get_attribute("checked") to verify selection
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from time import sleep

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

driver.get("https://automationexercise.com/signup")
driver.maximize_window()

home = driver.find_element(By.XPATH, '//a[text()=" Home"]').click()
signup = driver.find_element(By.XPATH, '//a[text()=" Signup / Login"]').click()

wait = WebDriverWait(driver, 5)
name = driver.find_element(By.XPATH, '//input[@data-qa="signup-name"]')
name.send_keys("Gabbar")

email = driver.find_element(By.XPATH, '//input[@data-qa="signup-email"]')
email.send_keys("gabbar09@hotmail")
sleep(2)

submit_button = wait.until(EC.presence_of_element_located((By.XPATH, '//button[@data-qa="signup-button"]')))
sleep(2)
submit_button.click()

gender = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="id_gender1"]')))
gender.click()

newsletter = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="newsletter"]')))
newsletter.click()

special_offer = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="optin"]')))
special_offer.click()

print(newsletter.get_attribute('checked'))
print(special_offer.get_attribute('checked'))

sleep(5)
driver.quit()