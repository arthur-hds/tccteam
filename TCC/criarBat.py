# from bs4 import BeautifulSoup
# from selenium.webdriver.chrome.webdriver import WebDriver
# from selenium import webdriver
# from time import sleep
import subprocess
import os


# try:
#     subprocess.
# print(os.path)

pasta = os.getcwd()
print(pasta)


pyDir = subprocess.run('where python', shell=True, capture_output=True, text=True)
subprocess.run('where python', shell=True, capture_output=True, text=True)

localArqPython = pyDir.stdout.split()[0]



print(pyDir)
print('----')

#stdout = Saída padrão (se o codigo rodar bem)
print(pyDir.stdout.split())
print(localArqPython)

#strderr = Saída de erro (se der errado, o erro será printado)
print(pyDir.stderr)

#returncode = Status do código: 0 - Execução sem erros ; 1- Execução mal-sucedidada
print(pyDir.returncode)


# bat = open(fr'{pasta}\scriptMsg.bat','w+')
# bat.write(f'''@echo off
# "{localArqPython}" "{pasta}\CodigoTCC.py"
# pause''')
# bat.close()




# subprocess.run('schtasks /create /tn testeCMDbanana /tr "C:\\Users\\Usuario\\PycharmProjects\\TCC\\venv\\Scripts\\python.exe Codigo.py" /sc once /st 11:00', shell=True)


# driver = webdriver.Chrome()
# driver.get("https://web.whatsapp.com/")
# sleep(15)






# html = driver.page_source
# bs = BeautifulSoup(str(html), 'html.parser')
# sleep(2)
# htmlPrettify = bs.prettify()
# print(htmlPrettify)
#
# print(driver.find_elements())






