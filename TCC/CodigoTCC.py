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
# from bibliotecas import extrair_dados, salvar_db


class Agendar:
    def __init__(self, horas, minutos):
        self.horas = horas.strip()
        self.minutos = minutos.strip()

    def __horario(self):
        minutos = 0
        atual = arrow.now()
        horario_usuario = arrow.Arrow(2022, 9, 27, int(self.horas), int(self.minutos))

        for tempo in arrow.Arrow.range(frame='minutes', tz=atual.tzinfo, start=atual, end=horario_usuario):
            minutos += 1

        envio_horas_minutos = horario_usuario.format('HH:mm')

        return envio_horas_minutos, horario_usuario, minutos

    def criar_rotina(self):
        horario = self.__horario()[0]
        pasta = os.getcwd() + '\Send.exe'

        self.rotina = subprocess.run(
            f'schtasks /create /tn testeCMDbanana /tr {pasta}  /SC ONSTART /RU desktop-c7hji7m\\usuario  /RP 123 ', shell=True,
            text=True)

        # subprocess.run(f'schtasks /change /tn testeCMDbanana /st 14:00 ', shell=True, text=True, input='')


        # self.rotina = subprocess.run(
        #     f'schtasks /Delete /tn testeCMDbanana /F', shell=True,
        #     text=True)


        # self.rotina = subprocess.run('where python', shell=True, capture_output=True, text=True)


class Executar:
    def __init__(self, msg, vezes, ctt, horas, minutos):
        self.minutos = minutos
        self.horas = horas
        self.ctt = ctt
        self.vezes = vezes
        self.msg = msg

        # salvar_db(msg=self.msg, numero_contato=self.ctt, vezes=self.vezes, horario=self.horas)


# --------------------------------------------------------------
# CODIGOS
# --------------------------------------------------------------
# conexao = sqlite3.connect('localContent.db')
# cursor = conexao.cursor()

ag = Agendar('14', '38')
ag.criar_rotina()

# tst = Executar('fala', 1, 5547988314131, '11:30', '1')


# msg.enviar('', 2, )


# cursor.close()
# conexao.close()
