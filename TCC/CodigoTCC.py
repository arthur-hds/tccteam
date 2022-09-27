import os

from bs4 import BeautifulSoup
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib
import arrow
import datetime
import sqlite3
import subprocess


class Mensagem:

    def __init__(self):

        self.options = webdriver.ChromeOptions()
        self.options.add_argument(f'user-data-dir=C:\\Users\\Usuario\\AppData\\Local\\Google\\Chrome\\User Data')
        self.driver = webdriver.Chrome(options=self.options)



        # driver.get("https://www.hardware.com.br/comunidade/notebook-internet/1316476/")
        self.driver.get("https://web.whatsapp.com/")

        # INJECT DE BANCO DE DADOS

        # FAZ ESPERAR O USUARIO LOGAR COM O CELULAR // XPATH = HEADER DO USUARIO
        esperar = WebDriverWait(driver=self.driver, timeout=100).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[3]/header/div[1]/div/div/span')))
        print(esperar)
        sleep(3)


    def enviar(self, msg, vezes, ctt):

        for i in range(1 ,vezes):
            msg = f'https://web.whatsapp.com/send?phone={ctt}&text={msg + str(i)}'
            self.driver.get(msg)
            WebDriverWait(driver=self.driver, timeout=100).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')))
            self.driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button').click()
            sleep(2)
            print(self.driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div').get_attribute('value'))
            sleep(5)
        self.__quit()


    def __quit(self):
        self.driver.quit()



class Agendar():
    def __init__(self, horas, minutos):
        self.horas = horas.strip()
        self.minutos = minutos.strip()


    def __horario(self):
        minutos = 0
        atual = arrow.now()
        horario_usuario = arrow.Arrow(2022, 9, 26, int(self.horas), int(self.minutos))

        for tempo in arrow.Arrow.range(frame='minutes', tz=atual.tzinfo, start=atual, end=horario_usuario):
            minutos += 1

        envio_horas_minutos = horario_usuario.format('HH:mm')

        return envio_horas_minutos, horario_usuario, minutos


    def criar_rotina(self):
        horario = self.__horario()[0]
        pasta = os.getcwd()+'\RabiscoTCC.exe'
        self.rotina = subprocess.run(f'schtasks /create /tn testeCMDbanana /tr "{pasta}" /sc once /st {horario}', shell=True, text=True)
        # self.rotina = subprocess.run('where python', shell=True, capture_output=True, text=True)


#--------------------------------------------------------------
#CODIGOS
#--------------------------------------------------------------
# conexao = sqlite3.connect('localContent.db')
# cursor = conexao.cursor()

ag = Agendar('21', '25')
ag.criar_rotina()

#


# msg.enviar('', 2, )


# cursor.close()
# conexao.close()