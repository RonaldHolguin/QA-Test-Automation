from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()  
driver.get("https://www.google.com")

text_to_search="automation test"
keyword="automation"

try:
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    search_box.send_keys(text_to_search)

    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "btnK")) 
    )

    search_button.click() 

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "h3"))
    )
   
    results = driver.find_elements(By.CSS_SELECTOR, "h3")
    count = 0
    for result in results:
        if keyword in result.text.lower():
            count += 1
            print(f"{result.text}")
        if count == 3:
            break
finally:
    WebDriverWait(driver, 10)
    driver.quit()
