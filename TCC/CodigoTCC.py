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

    def __init__(self, horas, minutos):
        self.driver = webdriver.Chrome()
        self.horas = horas
        self.minutos = minutos





        # driver.get("https://www.hardware.com.br/comunidade/notebook-internet/1316476/")
        self.driver.get("https://web.whatsapp.com/")

        # INJECT DE BANCO DE DADOS

        # FAZ ESPERAR O USUARIO LOGAR COM O CELULAR // XPATH = HEADER DO USUARIO
        esperar = WebDriverWait(driver=self.driver, timeout=100).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[3]/header/div[1]/div/div/span')))
        print(esperar)
        sleep(3)

    def criar_rotina(self):
        # self.rotina = subprocess.run('schtasks /create /tn testeCMDbanana /tr "C:\\Users\\Usuario\\PycharmProjects\\TCC\\TCC\\test.bat" /sc once /st 11:00', shell=True, capture_output=True, text=True)
        self.rotina = subprocess.run('where python', shell=True, capture_output=True, text=True)



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
    # def horario(ano, mes, dia, hora, minuto):
    #     inicio = arrow.utcnow()
    #     fim = arrow.Arrow(ano, mes, dia, hora, minuto, 5)
    #     restante = fim - inicio
    #     print(type(restante))
    #     print(type(fim))
    #     # if restante.format('DD') <= 0:
    #     #     return None
    #     print(inicio)
    #     print(fim)
    #     print(restante.)


    # ElementoAchado = driver.find_element(By.XPATH, '//*[@id="pane-side"]/div[1]/div/div')
    # valor = ElementoAchado.text
    # valor2 = ElementoAchado.get_attribute('value')
    # valor3 = ElementoAchado.get_attribute('innerHTML')
    #
    # bs = BeautifulSoup(valor3, 'html.parser')
    # classesChats = bs.find_all('div', {'class':'_3GlyB'})






    # print(ElementoAchado)
    # print(valor)
    # print(valor2)



    # print(EC.presence_of_element_located((By.ID, 'headerMover')))

    # html = driver.page_source


    # bs = BeautifulSoup(html, 'html.parser')
    #
    # print(bs.find_all('div',{'class':'a_message_inline a_locala_not_simple'}))
    #
    #
    # enviar('q cabelos lindos bb', 1)
    # horario(2022, 10, 22, 5, 6)







#--------------------------------------------------------------
#CODIGOS
#--------------------------------------------------------------
# conexao = sqlite3.connect('localContent.db')
# cursor = conexao.cursor()

# msg = Mensagem('11', '00')
#
# msg.enviar('', 2, )


# cursor.close()
# conexao.close()