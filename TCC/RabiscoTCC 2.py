from bs4 import BeautifulSoup
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
sleep(15)

html = driver.page_source
bs = BeautifulSoup(str(html), 'html.parser')
sleep(2)
htmlPrettify = bs.prettify()
print(htmlPrettify)

print(driver.find_elements())






