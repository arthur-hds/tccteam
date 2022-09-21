from bs4 import BeautifulSoup
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# opt = webdriver.ChromeOptions()
# opt.add_argument('headless')
driver = webdriver.Chrome()

driver.get("https://www.hardware.com.br/comunidade/notebook-internet/1316476/")
sleep(1)


elemento = driver.find_element(By.XPATH, '//*[@id="post6652596"]/div[1]/div/div[1]/a/img').get_attribute('src')
elemento = driver.find_element(By.XPATH, '//*[@id="post6652596"]/div[1]/div/div[1]/a/img').get_attribute('src')
print(elemento)







elementosTESTE = (driver.execute_script('return document.querySelector("div")'))
# bs = BeautifulSoup(driver.page_source, 'html.parser')
# bs.

# print(driver.find_elements('div'))


driver.quit()
