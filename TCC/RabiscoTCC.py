from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument(E_PROFILE_PATH)

driver = webdriver.Chrome(executable_path='chromedriver_win32_86.0.4240.22\chromedriver.exe', options=options)
driver.get('https://web.whatsapp.com/')