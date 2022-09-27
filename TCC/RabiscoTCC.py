from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# options = webdriver.ChromeOptions()
# options.add_argument('user-data-dir=C:\\Users\\Usuario\\AppData\\Local\\Google\\Chrome\\User Data')
options = webdriver.ChromeOptions()
options.add_argument(f'user-data-dir=C:\\Users\\Usuario\\AppData\\Local\\Google\\Chrome\\User Data')
# options.add_argument('--profile-directory=Profile 1')
# options.headless=True




driver = webdriver.Chrome(options=options)


driver.get('https://web.whatsapp.com/')
sleep(3)
print(driver.get_cookies())
print(driver.title)
driver.save_screenshot('C:\\Users\\Usuario\\PycharmProjects\\Git\\tccteam\\TCC\\foto.png')
esperar = WebDriverWait(driver=driver, timeout=5).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[3]/header/div[1]/div/div/span')))


sleep(5)
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






# ElementoAchado = driver.find_element(By.XPATH, '//*[@id="pane-side"]/div[1]/div/div')
    # valor = ElementoAchado.text
    # valor2 = ElementoAchado.get_attribute('value')
    # valor3 = ElementoAchado.get_attribute('innerHTML')
    #
    # bs = BeautifulSoup(valor3, 'html.parser')
    # classesChats = bs.find_all('div', {'class':'_3GlyB'})


# print(EC.presence_of_element_located((By.ID, 'headerMover')))

    # html = driver.page_source


    # bs = BeautifulSoup(html, 'html.parser')
    #
    # print(bs.find_all('div',{'class':'a_message_inline a_locala_not_simple'}))
    #
    #
    # enviar('q cabelos lindos bb', 1)
    # horario(2022, 10, 22, 5, 6)