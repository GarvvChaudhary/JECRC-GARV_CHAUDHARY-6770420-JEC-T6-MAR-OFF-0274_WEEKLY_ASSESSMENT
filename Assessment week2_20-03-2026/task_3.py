'''
Automation script for google.com

Open Google
Enter "Selenium Python"
Use explicit wait for suggestions
Capture all suggestions using find_elements
Print them
Click one suggestion
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.google.com")
wait = WebDriverWait(driver, 10)

search = wait.until(EC.visibility_of_element_located((By.NAME, "q")))
search.send_keys("Selenium Python")
print("Search text entered")

wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//ul[@role='listbox']//li")))
suggestions = driver.find_elements(By.XPATH, "//ul[@role='listbox']//li")

print("Suggestions:")
for i in suggestions:
    print(i.text)
suggestions[1].click()

print("Suggestion clicked")

sleep(8)

driver.quit()