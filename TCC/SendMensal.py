import os
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from subprocess import CREATE_NO_WINDOW
import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service
import arrow
import sqlite3
import subprocess
from bibliotecas import *
from pywhatkit.core.core import copy_image
import os
import webbrowser as web
from pyautogui import hotkey
import ast

class Mensagem(object):

    def __init__(self, fechar=False):
        self.fechar = fechar
        close = subprocess.run("taskkill /im chrome.exe /f", shell=True, stderr=True)

        # os.system("taskkill /im chrome.exe /f").as_integer_ratio()
        print(close.stderr)
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("excludeSwitches", ['enable-automation'])
        self.options.add_argument(f'user-data-dir={os.path.expanduser("~")}\\AppData\\Local\\Google\\Chrome\\User Data')
        # self.options.add_argument('--profile-directory=Profile 2')
        service = Service()
        service.creationflags = CREATE_NO_WINDOW

        self.driver = webdriver.Chrome(options=self.options, service=service)

        if close.returncode == 0:
            hotkey('ctrl', 'shift', 't')

        self.driver.get("https://web.whatsapp.com/")

        # FAZ ESPERAR O USUARIO LOGAR COM O CELULAR // XPATH = HEADER DO USUARIO
        try:
            esperar = WebDriverWait(driver=self.driver, timeout=100).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[3]/header/div[1]/div/div/span')))
        except:
            self.driver.refresh()
            esperar = WebDriverWait(driver=self.driver, timeout=100).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[3]/header/div[1]/div/div/span')))

        print(esperar)
        sleep(3)






    def enviar(self):

        try:
            self.valores = extrairMensagensMensal(cursor)[0]
            if self.valores is None:
                verificarDBMensal(cursor)
            self.msg = ast.literal_eval(self.valores[0])
            self.ctt = ast.literal_eval(self.valores[3])
            self.tipo = self.valores[4]
            self.midia = self.valores[5]

            if self.tipo == 'Contato':
                # MANDAR PARA CONTATOS
                for i in self.ctt:
                    print(i)
                    link = f'https://web.whatsapp.com/send?phone={i}'
                    self.driver.get(link)

                    # ATUALIZAR PAGINA CASO NÃO CARREGADO
                    WebDriverWait(driver=self.driver, timeout=50).until(EC.element_to_be_clickable(
                        (By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')))

                    self.enviandoMensagem(i)
                self.__quit()
                atualizarLogin(cursor, 1)
                return True
            else:
                # MANDAR PARA GRUPOS
                for i in self.ctt:
                    WebDriverWait(driver=self.driver, timeout=100).until(EC.element_to_be_clickable(
                        (By.XPATH, '/html/body/div[1]/div/div/div[3]/div/div[1]/div/div/div[2]')))

                    self.driver.find_element(By.XPATH,
                                             '/html/body/div[1]/div/div/div[3]/div/div[1]/div/div/div[2]').click()
                    sleep(1)

                    # Esperar até o nome do grupo for digitado
                    while self.driver.find_element(By.XPATH,
                                                   '/html/body/div[1]/div/div/div[3]/div/div[1]/div/div/div[2]/div/div[2]').text != i:
                        sleep(1)
                        self.driver.find_element(By.XPATH,
                                                 '/html/body/div[1]/div/div/div[3]/div/div[1]/div/div/div[2]/div/div[2]').send_keys(
                            i)

                    # ESPERAR ATÉ ACHAR A BARRA ONDE APARECE O GRUPO
                    WebDriverWait(driver=self.driver, timeout=15).until(EC.element_to_be_clickable(
                        (By.XPATH,
                         '/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div/div[1]/div/div/div/div[2]')))

                    self.driver.find_element(By.XPATH,
                                             '/html/body/div[1]/div/div/div[3]/div/div[1]/div/div/div[2]/div/div[2]').send_keys(
                        Keys.ENTER)
                    sleep(2)


                    #ESPERAR PARA APARECER CAIXA DE TEXTO PARA DIGITAR
                    WebDriverWait(driver=self.driver, timeout=20).until(EC.element_to_be_clickable(
                        (By.XPATH,
                         '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]')))

                    self.enviandoMensagem(i)

                self.__quit()
                atualizarLogin(cursor, 1)
                return True
        except:
            atualizarLogin(cursor, 2)
            self.__quit()
            return False

    def enviandoMensagem(self, nomeContato):
        for j in self.msg:
            # NOME DO DESTINATARIO VARIAVEL PRESENTE
            if '(Nome do destinatário)' in j and self.tipo == 'Contato':
                conexaoInterface = sqlite3.connect(
                    r'C:\Users\Usuario\PycharmProjects\Git\tccteam\TCC\Interface\InterfaceDB.db')
                cursorInterface = conexaoInterface.cursor()

                NomesContatos = extrairContatos(cursorInterface)
                for keys in NomesContatos.keys():
                    if NomesContatos[keys] == nomeContato:
                        j = j.replace('(Nome do destinatário)', keys)
                        break

                cursorInterface.close()
                conexaoInterface.close()

            elif '(Nome do destinatário)' in j and self.tipo == 'Grupo':
                j = j.replace('(Nome do destinatário)', nomeContato)

            # CHECAR POR MIDIA
            if self.midia == 'SIM' and "C:" in j[:3]:

                self.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]').click()

                try:

                    copy_image(j)

                    sleep(1)

                    self.driver.find_element(By.XPATH,
                                             '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]').send_keys(
                        Keys.CONTROL + 'v')
                    print('CONTROL V DADO')

                    sleep(4)
                    self.driver.find_element(By.XPATH,
                                             '/html/body/div[1]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div').click()
                    sleep(5)

                except:
                    pass
            else:
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
                    self.driver.find_element(By.XPATH,
                                             '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]').send_keys(
                        j)
                    self.driver.find_element(By.XPATH,
                                             '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]').send_keys(
                        Keys.ENTER)
                    sleep(2)

                    print(self.driver.find_element(By.XPATH,
                                                   '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div').get_attribute(
                        'value'))
                    sleep(1)

    def __quit(self):
        self.driver.close()


    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.fechar:
            self.driver.quit()



conexao = sqlite3.connect(r'C:\Users\Usuario\PycharmProjects\Git\tccteam\TCC\localContent.db')
cursor = conexao.cursor()


#
msg = Mensagem(fechar=False)
if msg.enviar():
    msg.enviar()
    verificarDBMensal(cursor)
#

conexao.commit()
cursor.close()
conexao.close()