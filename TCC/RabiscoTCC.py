from bs4 import BeautifulSoup
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle

# options = webdriver.ChromeOptions()
# options.add_argument('user-data-dir=C:\\Users\\Usuario\\AppData\\Local\\Google\\Chrome\\User Data')
options = webdriver.ChromeOptions()
options.add_argument(f'user-data-dir=C:\\Users\\Usuario\\AppData\\Local\\Google\\Chrome\\User Data')
# options.add_argument('--profile-directory=Profile 1')

driver = webdriver.Chrome(options=options)
driver.get('https://web.whatsapp.com/')
esperar = WebDriverWait(driver=driver, timeout=100).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[3]/header/div[1]/div/div/span')))

for i in range(1, 10):
    sleep(4)


print(driver.get_cookies())
cookies = driver.get_cookies()

# for cookie in cookies:



driver.close()
driver.quit()


driver1 = webdriver.Chrome()
driver1.get('https://web.whatsapp.com/')

print('Guenta')
sleep(3)

driver.add_cookie({'domain': '.web.whatsapp.com', 'expiry': 1665164759, 'httpOnly': True, 'name': 'wa_beta_version', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'production%2F1663276994%2F2.2234.13'})
print('cokies add')
esperar = WebDriverWait(driver=driver, timeout=100).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[3]/header/div[1]/div/div/span')))


sleep(10)

driver1.quit()

