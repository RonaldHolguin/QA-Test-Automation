from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_argument('--lang=en')

driver = webdriver.Chrome(options=options)
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
    WebDriverWait(driver, 10)
    first_result = results[0]
    first_result.click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "title"))
    )

    page_title = driver.title
    print(f"Page Title : {page_title}")
    if keyword in page_title.lower():
        print(f"The keyword : {keyword} is in the Title.")
    else:  
        print(f"The keyword : {keyword} is not in the Title.")

finally:
    WebDriverWait(driver, 10)
    driver.quit()
