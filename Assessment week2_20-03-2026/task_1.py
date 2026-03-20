'''
Automation script for amazon.com

Open Amazon
Verify page title and current URL
Locate the category dropdown (next to search bar)
Select "Books" using Select class
Enter "Harry Potter" in search and press Enter
Use explicit wait to wait until results are visible
Get all product titles using find_elements
Print first 5 product names
Click on the first product
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver=webdriver.Chrome()
wait=WebDriverWait(driver,10)

driver.get("https://www.amazon.com/")
driver.maximize_window()

print(f"title found {driver.title}")

print(f"URL found {driver.current_url}")

dropdown=wait.until(EC.presence_of_element_located((By.XPATH,"//select[@id='searchDropdownBox']")))
select=Select(dropdown)
select.select_by_visible_text("Books")

search_box=wait.until(EC.visibility_of_element_located((By.ID,"twotabsearchtextbox")))
search_box.send_keys("Harry Potter",Keys.ENTER)

title_list=driver.find_elements(By.XPATH,"//div[@data-cy='title-recipe']/descendant::h2")
firstProduct=''
for i, item in enumerate(title_list):
    if(i==0):
        firstProduct=item.text
    print(item.text)

first_product=wait.until(EC.visibility_of_element_located((By.XPATH,f"//div[@data-cy='title-recipe']/descendant::h2")))
first_product.click()

sleep(10)

driver.quit()