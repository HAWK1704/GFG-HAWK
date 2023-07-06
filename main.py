from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

edgeBrowser = webdriver.Edge()
edgeBrowser.get('https://google.com')
edgeBrowser.find_element(By.NAME, "q").send_keys("github")

# Wait for the options to be visible
wait = WebDriverWait(edgeBrowser, 10)
options = wait.until(EC.visibility_of_all_elements_located((By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div/ul/li')))

for i in options:
    print(i.text)
edgeBrowser.quit()
