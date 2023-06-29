from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep

edgeBrowser = webdriver.Edge()
edgeBrowser.get('https://google.com')
edgeBrowser.find_element(By.NAME,"q").send_keys("github")
options=edgeBrowser.find_elements(By.CSS_SELECTOR,'ul.G43f7e li span')
print(len(options))
for i in options:
    print(i.text)
sleep(1)
edgeBrowser.quit()