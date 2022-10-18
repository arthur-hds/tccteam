import os
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import urllib
import arrow
import datetime
import sqlite3
import subprocess
from bibliotecas import *

import os
import webbrowser as web
import pyperclip
from pyautogui import hotkey
import ast


class Mensagem:

    def __init__(self):
        close = subprocess.run("taskkill /im chrome.exe /f", shell=True, stderr=True)

        # os.system("taskkill /im chrome.exe /f").as_integer_ratio()
        print(close.stderr)
        self.options = webdriver.ChromeOptions()

        self.options.add_argument(f'user-data-dir=C:\\Users\\Usuario\\AppData\\Local\\Google\\Chrome\\User Data')
        # self.options.add_argument('--profile-directory=Profile 2')

        self.driver = webdriver.Chrome(options=self.options)

        if close.returncode == 0:
            hotkey('ctrl', 'shift', 't')

        # driver.get("https://www.hardware.com.br/comunidade/notebook-internet/1316476/")
        self.driver.get("https://web.whatsapp.com/")

        # INJECT DE BANCO DE DADOS

        # FAZ ESPERAR O USUARIO LOGAR COM O CELULAR // XPATH = HEADER DO USUARIO
        esperar = WebDriverWait(driver=self.driver, timeout=100).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[3]/header/div[1]/div/div/span')))
        print(esperar)
        sleep(3)






    def enviar(self):


        valores = extrairMensagensDiaria(cursor)[0]
        if valores is None:
            verificarDBDiaria(cursor)
        print(valores)
        print(valores)
        print(valores)
        msg = ast.literal_eval(valores[0])
        ctt = ast.literal_eval(valores[3])
        tipo = valores[4]
        midia = valores[5]

        print(ctt)
        print(msg)

        for i in ctt:
            print(i)
            link = f'https://web.whatsapp.com/send?phone={i}'
            # link = f'https://web.whatsapp.com/send?phone={i}&text={msg}'
            self.driver.get(link)

            WebDriverWait(driver=self.driver, timeout=100).until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')))
            # self.driver.find_element(By.XPATH,
            #                          '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button').click()


            for j in msg:

                if '(Nome do destinatário)' in j:
                    conexaoInterface = sqlite3.connect(r'C:\Users\Usuario\PycharmProjects\Git\tccteam\TCC\Interface\InterfaceDB.db')
                    cursorInterface = conexaoInterface.cursor()

                    NomesContatos = extrairContatos(cursorInterface)
                    for keys in NomesContatos.keys():
                        if NomesContatos[keys] == i:
                            j = j.replace('(Nome do destinatário)', keys)
                            break


                    cursorInterface.close()
                    conexaoInterface.close()


                # CASO HAJA ENTER ENTRE AS MENSAGENS
                if '\n' in j:

                    j = j.split('\n')
                    for msgCortada in j:
                        self.driver.find_element(By.XPATH,
                        '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]').send_keys(
                        msgCortada, Keys.SHIFT + Keys.ENTER)
                    self.driver.find_element(By.XPATH,
                    '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]').send_keys(
                    Keys.ENTER)
                    sleep(2)

                else:
                # pyperclip.copy(r'C:/Users/Usuario/PycharmProjects/Interface/OneTickLogo.png')
                # j = pyperclip.paste()
                # self.driver.find_element(By.CSS_SELECTOR, "span[data-icon='clip']").click()
                # self.driver.find_element(By.CSS_SELECTOR, "span[data-icon='attach-image']").click()
                # self.driver.find_element(By.CSS_SELECTOR, "input[type='file']").send_keys("C:/Users/Usuario/PycharmProjects/Interface/OneTickLogo.png", Keys.ENTER)
                    self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]').send_keys(j)
                    self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]').send_keys(Keys.ENTER)
                    sleep(2)

                    # self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]').send_keys(Keys.CONTROL+'w')
                    print(self.driver.find_element(By.XPATH,
                                                   '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div').get_attribute(
                        'value'))
                    sleep(1)

        self.__quit()






    def __quit(self):
        self.driver.quit()

conexao = sqlite3.connect(r'C:\Users\Usuario\PycharmProjects\Git\tccteam\TCC\localContent.db')
cursor = conexao.cursor()


#
a = Mensagem().enviar()
verificarDBDiaria(cursor)
#

conexao.commit()
cursor.close()
conexao.close()