#ONETICK PROGRAMA

from subprocess import CREATE_NO_WINDOW
import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
import icons.imagesQtMain
import sys
from bibliotecas import *
from selenium import webdriver
from pyautogui import hotkey
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PopupMensagens import Ui_Form



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1179, 763)
        MainWindow.setStyleSheet("background-color:rgb(46, 56, 92);")
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.localContent = r'C:\Users\Usuario\PycharmProjects\Git\tccteam\TCC\localContent.db'
        self.InterfaceDB = r'C:\Users\Usuario\PycharmProjects\Git\tccteam\TCC\Interface\InterfaceDB.db'
        self.InformacoesEPath()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, -10, 1181, 771))
        self.stackedWidget.setObjectName("stackedWidget")
        self.pageLogin = QtWidgets.QWidget()
        self.pageLogin.setObjectName("pageLogin")
        self.label_86 = QtWidgets.QLabel(self.pageLogin)
        self.label_86.setGeometry(QtCore.QRect(390, 200, 401, 351))
        self.label_86.setStyleSheet("image: url(:/pics/OneTickWhiteOneTickQT.png);\n"
"border:none;\n"
"background:none;")
        self.label_86.setText("")
        self.label_86.setObjectName("label_86")
        self.label_87 = QtWidgets.QLabel(self.pageLogin)
        self.label_87.setGeometry(QtCore.QRect(330, 140, 511, 41))
        self.label_87.setStyleSheet("font: 24pt \"Bahnschrift Condensed\";\n"
"color: rgb(255, 255, 255);\n"
"background:none;\n"
"border:None;")
        self.label_87.setAlignment(QtCore.Qt.AlignCenter)
        self.label_87.setObjectName("label_87")
        self.botaoComecar = QtWidgets.QPushButton(self.pageLogin)
        self.botaoComecar.setGeometry(QtCore.QRect(460, 620, 241, 71))
        self.botaoComecar.clicked.connect(self.verificarWhatsapp)
        self.botaoComecar.setStyleSheet("\n"
"\n"
"\n"
"QPushButton{\n"
"    \n"
"background-color: rgb(128, 62, 226);\n"
"border: 1px solid #4a4a4a;\n"
"border-radius:35%;\n"
"font: 87 10pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"\n"
"background-color: rgb(135, 65, 239);\n"
"borderr-radius: 10px rgb(70, 70, 70);\n"
"}\n"
"QPushButton:pressed {\n"
"\n"
"background-color: rgbrgb(170, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"")
        self.botaoComecar.setObjectName("botaoComecar")
        self.label_88 = QtWidgets.QLabel(self.pageLogin)
        self.label_88.setGeometry(QtCore.QRect(-160, 0, 1551, 781))
        self.label_88.setStyleSheet("QLabel{\n"
"    \n"
"    image: url(:/pics/whatsapp_webQT.jpg);\n"
"    \n"
"}\n"
"")
        self.label_88.setText("")
        self.label_88.setObjectName("label_88")
        self.label_89 = QtWidgets.QLabel(self.pageLogin)
        self.label_89.setGeometry(QtCore.QRect(-200, -10, 1551, 781))
        self.label_89.setStyleSheet("QLabel{\n"
"    \n"
"    background-color: rgba(81, 39, 144, 240);\n"
"    \n"
"}\n"
"")
        self.label_89.setText("")
        self.label_89.setObjectName("label_89")
        self.label_90 = QtWidgets.QLabel(self.pageLogin)
        self.label_90.setGeometry(QtCore.QRect(221, 569, 731, 41))
        self.label_90.setStyleSheet("font: 10pt \"Bahnschrift Condensed\";\n"
"color: rgb(255, 255, 255);\n"
"background:none;\n"
"border:None;")
        self.label_90.setAlignment(QtCore.Qt.AlignCenter)
        self.label_90.setObjectName("label_90")
        self.label_88.raise_()
        self.label_89.raise_()
        self.label_86.raise_()
        self.label_87.raise_()
        self.botaoComecar.raise_()
        self.label_90.raise_()
        self.stackedWidget.addWidget(self.pageLogin)
        self.pageOneTick = QtWidgets.QWidget()
        self.pageOneTick.setObjectName("pageOneTick")
        self.widgetRotinasDeDias = QtWidgets.QWidget(self.pageOneTick)
        self.widgetRotinasDeDias.setGeometry(QtCore.QRect(638, 456, 241, 221))
        self.widgetRotinasDeDias.setStyleSheet("background-color: rgb(79, 38, 140);\n"
"border-radius:40%\n"
"")
        self.widgetRotinasDeDias.setObjectName("widgetRotinasDeDias")
        self.botaoDias_4 = QtWidgets.QPushButton(self.widgetRotinasDeDias)
        self.botaoDias_4.setGeometry(QtCore.QRect(0, 150, 241, 71))
        self.botaoDias_4.clicked.connect(self.cliqueDeDias)
        self.botaoDias_4.setStyleSheet("\n"
"\n"
"\n"
"QPushButton{\n"
"    \n"
"background-color: rgb(128, 62, 226);\n"
"border: 1px solid #4a4a4a;\n"
"border-top-right-radius: 0%;\n"
"border-top-left-radius: 0%;\n"
"border-bottom-right-radius: 40%;\n"
"border-bottom-left-radius: 40%;\n"
"font: 87 10pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"\n"
"background-color: rgb(135, 65, 239);\n"
"borderr-radius: 10px rgb(70, 70, 70);\n"
"}\n"
"QPushButton:pressed {\n"
"\n"
"background-color: rgbrgb(170, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"")
        self.botaoDias_4.setObjectName("botaoDias_4")
        self.stackedWidgetDias_4 = QtWidgets.QStackedWidget(self.widgetRotinasDeDias)
        self.stackedWidgetDias_4.setGeometry(QtCore.QRect(10, 10, 221, 131))
        self.stackedWidgetDias_4.setObjectName("stackedWidgetDias_4")
        self.pageMensagensDias_4 = QtWidgets.QWidget()
        self.pageMensagensDias_4.setObjectName("pageMensagensDias_4")
        self.mensagemEnvDias_4 = QtWidgets.QWidget(self.pageMensagensDias_4)
        self.mensagemEnvDias_4.setGeometry(QtCore.QRect(14, 7, 201, 51))
        self.mensagemEnvDias_4.setStyleSheet("background-color: rgb(0, 176, 141);\n"
"border-radius:20%\n"
"")
        self.mensagemEnvDias_4.setObjectName("mensagemEnvDias_4")
        self.textoHorarioDias1_4 = QtWidgets.QLabel(self.mensagemEnvDias_4)
        self.textoHorarioDias1_4.setGeometry(QtCore.QRect(127, 28, 51, 21))
        self.textoHorarioDias1_4.setStyleSheet("font: 87 6pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"background:none;")
        self.textoHorarioDias1_4.setAlignment(QtCore.Qt.AlignCenter)
        self.textoHorarioDias1_4.setObjectName("textoHorarioDias1_4")
        self.label_45 = QtWidgets.QLabel(self.mensagemEnvDias_4)
        self.label_45.setGeometry(QtCore.QRect(170, 30, 20, 16))
        self.label_45.setStyleSheet("image: url(:/pics/20x20/cil-check.png);\n"
"background:none;")
        self.label_45.setText("")
        self.label_45.setAlignment(QtCore.Qt.AlignCenter)
        self.label_45.setObjectName("label_45")
        self.textoMsgFaltandoDias_4 = QtWidgets.QLabel(self.mensagemEnvDias_4)
        self.textoMsgFaltandoDias_4.setGeometry(QtCore.QRect(10, 10, 181, 21))
        self.textoMsgFaltandoDias_4.setStyleSheet("font: 87 6pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"background:none;")
        self.textoMsgFaltandoDias_4.setAlignment(QtCore.Qt.AlignCenter)
        self.textoMsgFaltandoDias_4.setObjectName("textoMsgFaltandoDias_4")
        self.mensagemRecDias_4 = QtWidgets.QWidget(self.pageMensagensDias_4)
        self.mensagemRecDias_4.setGeometry(QtCore.QRect(10, 70, 191, 51))
        self.mensagemRecDias_4.setStyleSheet("background-color: rgb(177, 189, 208);\n"
"border-radius:20%\n"
"")
        self.mensagemRecDias_4.setObjectName("mensagemRecDias_4")
        self.label_46 = QtWidgets.QLabel(self.mensagemRecDias_4)
        self.label_46.setGeometry(QtCore.QRect(10, 30, 20, 16))
        self.label_46.setStyleSheet("image: url(:/pics/20x20/cil-x-circle.png);\n"
"background:none;")
        self.label_46.setText("")
        self.label_46.setAlignment(QtCore.Qt.AlignCenter)
        self.label_46.setObjectName("label_46")
        self.textoHorarioDias2_4 = QtWidgets.QLabel(self.mensagemRecDias_4)
        self.textoHorarioDias2_4.setGeometry(QtCore.QRect(22, 26, 51, 21))
        self.textoHorarioDias2_4.setStyleSheet("font: 87 6pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"background:none;")
        self.textoHorarioDias2_4.setAlignment(QtCore.Qt.AlignCenter)
        self.textoHorarioDias2_4.setObjectName("textoHorarioDias2_4")
        self.textoMsgEnviadasDias_4 = QtWidgets.QLabel(self.mensagemRecDias_4)
        self.textoMsgEnviadasDias_4.setGeometry(QtCore.QRect(2, 8, 181, 21))
        self.textoMsgEnviadasDias_4.setStyleSheet("font: 87 6pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"background:none;")
        self.textoMsgEnviadasDias_4.setAlignment(QtCore.Qt.AlignCenter)
        self.textoMsgEnviadasDias_4.setObjectName("textoMsgEnviadasDias_4")
        self.stackedWidgetDias_4.addWidget(self.pageMensagensDias_4)
        self.pageVaziaDias_4 = QtWidgets.QWidget()
        self.pageVaziaDias_4.setObjectName("pageVaziaDias_4")
        self.textoDias1_4 = QtWidgets.QLabel(self.pageVaziaDias_4)
        self.textoDias1_4.setGeometry(QtCore.QRect(-5, 37, 231, 41))
        self.textoDias1_4.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"background:none;")
        self.textoDias1_4.setAlignment(QtCore.Qt.AlignCenter)
        self.textoDias1_4.setObjectName("textoDias1_4")
        self.textoDias2_4 = QtWidgets.QLabel(self.pageVaziaDias_4)
        self.textoDias2_4.setGeometry(QtCore.QRect(-10, 67, 231, 41))
        self.textoDias2_4.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"background:none;")
        self.textoDias2_4.setAlignment(QtCore.Qt.AlignCenter)
        self.textoDias2_4.setObjectName("textoDias2_4")
        self.stackedWidgetDias_4.addWidget(self.pageVaziaDias_4)
        self.label_68 = QtWidgets.QLabel(self.pageOneTick)
        self.label_68.setGeometry(QtCore.QRect(408, 126, 401, 41))
        self.label_68.setStyleSheet("font: 87 15pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"background:none;")
        self.label_68.setAlignment(QtCore.Qt.AlignCenter)
        self.label_68.setObjectName("label_68")
        self.widgetOpcoes = QtWidgets.QWidget(self.pageOneTick)
        self.widgetOpcoes.setGeometry(QtCore.QRect(218, 206, 781, 321))
        self.widgetOpcoes.setVisible(False)
        self.widgetOpcoes.setStyleSheet("background-color: rgb(128, 62, 226);\n"
"border:none;\n"
"border-radius:20%\n"
"")
        self.widgetOpcoes.setObjectName("widgetOpcoes")
        self.label_69 = QtWidgets.QLabel(self.widgetOpcoes)
        self.label_69.setGeometry(QtCore.QRect(50, 20, 201, 41))
        self.label_69.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"background:none;")
        self.label_69.setAlignment(QtCore.Qt.AlignCenter)
        self.label_69.setObjectName("label_69")
        self.botaoFechar_6 = QtWidgets.QPushButton(self.widgetOpcoes)
        self.botaoFechar_6.setGeometry(QtCore.QRect(710, 14, 50, 24))
        self.botaoFechar_6.setMinimumSize(QtCore.QSize(50, 0))
        self.botaoFechar_6.clicked.connect(self.abrirConfiguracoes)
        self.botaoFechar_6.setCursor(Qt.PointingHandCursor)
        self.botaoFechar_6.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(145, 70, 255);\n"
"    border-radius:10px;\n"
"    \n"
"    font:87 10pt \"Arial Black\";\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(166, 68, 255);\n"
"borderr-radius: 10px rgb(70, 70, 70);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(145, 70, 255);\n"
"color: (145, 70, 255);\n"
"}")
        self.botaoFechar_6.setObjectName("botaoFechar_6")
        self.label_70 = QtWidgets.QLabel(self.widgetOpcoes)
        self.label_70.setGeometry(QtCore.QRect(31, 60, 501, 21))
        self.label_70.setStyleSheet("font: 87 7pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"background:none;")
        self.label_70.setAlignment(QtCore.Qt.AlignCenter)
        self.label_70.setObjectName("label_70")
        self.widgetAddVariaveis_15 = QtWidgets.QWidget(self.widgetOpcoes)
        self.widgetAddVariaveis_15.setGeometry(QtCore.QRect(30, 30, 21, 21))
        self.widgetAddVariaveis_15.setStyleSheet("background-color: rgb(65, 31, 115);\n"
"border-radius:10%\n"
"")
        self.widgetAddVariaveis_15.setObjectName("widgetAddVariaveis_15")
        self.pushButton_17 = QtWidgets.QPushButton(self.widgetOpcoes)
        self.pushButton_17.setGeometry(QtCore.QRect(30, 90, 81, 41))
        self.pushButton_17.clicked.connect(self.resetarRotinasBotao)
        self.pushButton_17.setCursor(Qt.PointingHandCursor)
        self.pushButton_17.setStyleSheet("\n"
"QPushButton{\n"
"    \n"
"    \n"
"    image: url(:/pics/24x24/cil-reload.png);\n"
"    \n"
"    background-color: rgb(145, 70, 255);\n"
"    border:none;\n"
"    border-radius:15%;\n"
"    padding: 5px;\n"
"    color:white;\n"
"    font:87 23pt \"Arial Black\";\n"
"    color: rgb(0, 170, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"\n"
"background-color: ;\n"
"    background-color: rgb(137, 66, 243);\n"
"borderr-radius: 10px rgb(70, 70, 70);\n"
"}\n"
"QPushButton:pressed {\n"
"\n"
"background-color: rgbrgb(170, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.pushButton_17.setText("")
        self.pushButton_17.setObjectName("pushButton_17")
        self.label_71 = QtWidgets.QLabel(self.widgetOpcoes)
        self.label_71.setGeometry(QtCore.QRect(30, 180, 521, 21))
        self.label_71.setStyleSheet("font: 87 7pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"background:none;")
        self.label_71.setAlignment(QtCore.Qt.AlignCenter)
        self.label_71.setObjectName("label_71")
        self.label_72 = QtWidgets.QLabel(self.widgetOpcoes)
        self.label_72.setGeometry(QtCore.QRect(10, 140, 201, 41))
        self.label_72.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"background:none;")
        self.label_72.setAlignment(QtCore.Qt.AlignCenter)
        self.label_72.setObjectName("label_72")
        self.widgetAddVariaveis_16 = QtWidgets.QWidget(self.widgetOpcoes)
        self.widgetAddVariaveis_16.setGeometry(QtCore.QRect(29, 150, 21, 21))
        self.widgetAddVariaveis_16.setStyleSheet("background-color: rgb(65, 31, 115);\n"
"border-radius:10%\n"
"")
        self.widgetAddVariaveis_16.setObjectName("widgetAddVariaveis_16")
        self.pushButton_18 = QtWidgets.QPushButton(self.widgetOpcoes)
        self.pushButton_18.setGeometry(QtCore.QRect(30, 210, 81, 41))
        self.pushButton_18.clicked.connect(self.deslogar)
        self.pushButton_18.setCursor(Qt.PointingHandCursor)
        self.pushButton_18.setStyleSheet("\n"
"QPushButton{\n"
"    \n"
"    \n"
"    image: url(:/pics/24x24/cil-description.png);\n"
"    \n"
"    background-color: rgb(145, 70, 255);\n"
"    border:none;\n"
"    border-radius:15%;\n"
"    padding: 5px;\n"
"    color:white;\n"
"    font:87 23pt \"Arial Black\";\n"
"    color: rgb(0, 170, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"\n"
"background-color: ;\n"
"    background-color: rgb(137, 66, 243);\n"
"borderr-radius: 10px rgb(70, 70, 70);\n"
"}\n"
"QPushButton:pressed {\n"
"\n"
"background-color: rgbrgb(170, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.pushButton_18.setText("")
        self.pushButton_18.setObjectName("pushButton_18")
        self.widgetRotinasMensais = QtWidgets.QWidget(self.pageOneTick)
        self.widgetRotinasMensais.setGeometry(QtCore.QRect(318, 456, 241, 221))
        self.widgetRotinasMensais.setStyleSheet("background-color: rgb(79, 38, 140);\n"
"border-radius:40%\n"
"")
        self.widgetRotinasMensais.setObjectName("widgetRotinasMensais")
        self.botaoMensais_4 = QtWidgets.QPushButton(self.widgetRotinasMensais)
        self.botaoMensais_4.setGeometry(QtCore.QRect(0, 150, 241, 71))
        self.botaoMensais_4.clicked.connect(self.cliqueMensais)
        self.botaoMensais_4.setStyleSheet("\n"
"\n"
"\n"
"QPushButton{\n"
"    \n"
"background-color: rgb(128, 62, 226);\n"
"border: 1px solid #4a4a4a;\n"
"border-top-right-radius: 0%;\n"
"border-top-left-radius: 0%;\n"
"border-bottom-right-radius: 40%;\n"
"border-bottom-left-radius: 40%;\n"
"font: 87 10pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"\n"
"background-color: rgb(135, 65, 239);\n"
"borderr-radius: 10px rgb(70, 70, 70);\n"
"}\n"
"QPushButton:pressed {\n"
"\n"
"background-color: rgbrgb(170, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"")
        self.botaoMensais_4.setObjectName("botaoMensais_4")
        self.stackedWidgetMensais_4 = QtWidgets.QStackedWidget(self.widgetRotinasMensais)
        self.stackedWidgetMensais_4.setGeometry(QtCore.QRect(10, 10, 221, 131))
        self.stackedWidgetMensais_4.setObjectName("stackedWidgetMensais_4")
        self.pageMensagensMensais_4 = QtWidgets.QWidget()
        self.pageMensagensMensais_4.setObjectName("pageMensagensMensais_4")
        self.mensagemEnvMensais_4 = QtWidgets.QWidget(self.pageMensagensMensais_4)
        self.mensagemEnvMensais_4.setGeometry(QtCore.QRect(14, 7, 201, 51))
        self.mensagemEnvMensais_4.setStyleSheet("background-color: rgb(0, 176, 141);\n"
"border-radius:20%\n"
"")
        self.mensagemEnvMensais_4.setObjectName("mensagemEnvMensais_4")
        self.textoHorarioMensais1_4 = QtWidgets.QLabel(self.mensagemEnvMensais_4)
        self.textoHorarioMensais1_4.setGeometry(QtCore.QRect(127, 28, 51, 21))
        self.textoHorarioMensais1_4.setStyleSheet("font: 87 6pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"background:none;")
        self.textoHorarioMensais1_4.setAlignment(QtCore.Qt.AlignCenter)
        self.textoHorarioMensais1_4.setObjectName("textoHorarioMensais1_4")
        self.label_37 = QtWidgets.QLabel(self.mensagemEnvMensais_4)
        self.label_37.setGeometry(QtCore.QRect(170, 30, 20, 16))
        self.label_37.setStyleSheet("image: url(:/pics/20x20/cil-check.png);\n"
"background:none;")
        self.label_37.setText("")
        self.label_37.setAlignment(QtCore.Qt.AlignCenter)
        self.label_37.setObjectName("label_37")
        self.textoMsgFaltandoMensais_4 = QtWidgets.QLabel(self.mensagemEnvMensais_4)
        self.textoMsgFaltandoMensais_4.setGeometry(QtCore.QRect(10, 10, 181, 21))
        self.textoMsgFaltandoMensais_4.setStyleSheet("font: 87 6pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"background:none;")
        self.textoMsgFaltandoMensais_4.setAlignment(QtCore.Qt.AlignCenter)
        self.textoMsgFaltandoMensais_4.setObjectName("textoMsgFaltandoMensais_4")
        self.mensagemRecMensais_4 = QtWidgets.QWidget(self.pageMensagensMensais_4)
        self.mensagemRecMensais_4.setGeometry(QtCore.QRect(10, 70, 191, 51))
        self.mensagemRecMensais_4.setStyleSheet("background-color: rgb(177, 189, 208);\n"
"border-radius:20%\n"
"")
        self.mensagemRecMensais_4.setObjectName("mensagemRecMensais_4")
        self.label_38 = QtWidgets.QLabel(self.mensagemRecMensais_4)
        self.label_38.setGeometry(QtCore.QRect(10, 30, 20, 16))
        self.label_38.setStyleSheet("image: url(:/pics/20x20/cil-x-circle.png);\n"
"background:none;")
        self.label_38.setText("")
        self.label_38.setAlignment(QtCore.Qt.AlignCenter)
        self.label_38.setObjectName("label_38")
        self.textoHorarioMensais2_4 = QtWidgets.QLabel(self.mensagemRecMensais_4)
        self.textoHorarioMensais2_4.setGeometry(QtCore.QRect(22, 26, 51, 21))
        self.textoHorarioMensais2_4.setStyleSheet("font: 87 6pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"background:none;")
        self.textoHorarioMensais2_4.setAlignment(QtCore.Qt.AlignCenter)
        self.textoHorarioMensais2_4.setObjectName("textoHorarioMensais2_4")
        self.textoMsgEnviadasMensais_4 = QtWidgets.QLabel(self.mensagemRecMensais_4)
        self.textoMsgEnviadasMensais_4.setGeometry(QtCore.QRect(2, 8, 181, 21))
        self.textoMsgEnviadasMensais_4.setStyleSheet("font: 87 6pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"background:none;")
        self.textoMsgEnviadasMensais_4.setAlignment(QtCore.Qt.AlignCenter)
        self.textoMsgEnviadasMensais_4.setObjectName("textoMsgEnviadasMensais_4")
        self.stackedWidgetMensais_4.addWidget(self.pageMensagensMensais_4)
        self.pageVazia_7 = QtWidgets.QWidget()
        self.pageVazia_7.setObjectName("pageVazia_7")
        self.textoMensais1_4 = QtWidgets.QLabel(self.pageVazia_7)
        self.textoMensais1_4.setGeometry(QtCore.QRect(-5, 37, 231, 41))
        self.textoMensais1_4.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"background:none;")
        self.textoMensais1_4.setAlignment(QtCore.Qt.AlignCenter)
        self.textoMensais1_4.setObjectName("textoMensais1_4")
        self.textoMensais2_4 = QtWidgets.QLabel(self.pageVazia_7)
        self.textoMensais2_4.setGeometry(QtCore.QRect(-10, 67, 231, 41))
        self.textoMensais2_4.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"background:none;")
        self.textoMensais2_4.setAlignment(QtCore.Qt.AlignCenter)
        self.textoMensais2_4.setObjectName("textoMensais2_4")
        self.stackedWidgetMensais_4.addWidget(self.pageVazia_7)
        self.widgetRotinasNormais = QtWidgets.QWidget(self.pageOneTick)
        self.widgetRotinasNormais.setGeometry(QtCore.QRect(478, 206, 241, 221))
        self.widgetRotinasNormais.setStyleSheet("background-color: rgb(79, 38, 140);\n"
"border-radius:40%\n"
"")
        self.widgetRotinasNormais.setObjectName("widgetRotinasNormais")
        self.botaoNormais_4 = QtWidgets.QPushButton(self.widgetRotinasNormais)
        self.botaoNormais_4.setGeometry(QtCore.QRect(0, 150, 241, 71))
        self.botaoNormais_4.clicked.connect(self.cliqueNormais)
        self.botaoNormais_4.setStyleSheet("\n"
"\n"
"\n"
"QPushButton{\n"
"    \n"
"background-color: rgb(128, 62, 226);\n"
"border: 1px solid #4a4a4a;\n"
"border-top-right-radius: 0%;\n"
"border-top-left-radius: 0%;\n"
"border-bottom-right-radius: 40%;\n"
"border-bottom-left-radius: 40%;\n"
"font: 87 10pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"\n"
"background-color: rgb(135, 65, 239);\n"
"borderr-radius: 10px rgb(70, 70, 70);\n"
"}\n"
"QPushButton:pressed {\n"
"\n"
"background-color: rgbrgb(170, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"")
        self.botaoNormais_4.setObjectName("botaoNormais_4")
        self.stackedWidgetNormais_4 = QtWidgets.QStackedWidget(self.widgetRotinasNormais)
        self.stackedWidgetNormais_4.setGeometry(QtCore.QRect(10, 10, 221, 131))
        self.stackedWidgetNormais_4.setObjectName("stackedWidgetNormais_4")
        self.pageMensagensNormais_4 = QtWidgets.QWidget()
        self.pageMensagensNormais_4.setObjectName("pageMensagensNormais_4")
        self.mensagemEnvNormais_4 = QtWidgets.QWidget(self.pageMensagensNormais_4)
        self.mensagemEnvNormais_4.setGeometry(QtCore.QRect(14, 7, 201, 51))
        self.mensagemEnvNormais_4.setStyleSheet("background-color: rgb(0, 176, 141);\n"
"border-radius:20%\n"
"")
        self.mensagemEnvNormais_4.setObjectName("mensagemEnvNormais_4")
        self.textoHorarioNormais1_4 = QtWidgets.QLabel(self.mensagemEnvNormais_4)
        self.textoHorarioNormais1_4.setGeometry(QtCore.QRect(127, 28, 51, 21))
        self.textoHorarioNormais1_4.setStyleSheet("font: 87 6pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"background:none;")
        self.textoHorarioNormais1_4.setAlignment(QtCore.Qt.AlignCenter)
        self.textoHorarioNormais1_4.setObjectName("textoHorarioNormais1_4")
        self.label_75 = QtWidgets.QLabel(self.mensagemEnvNormais_4)
        self.label_75.setGeometry(QtCore.QRect(170, 30, 20, 16))
        self.label_75.setStyleSheet("image: url(:/pics/20x20/cil-check.png);\n"
"background:none;")
        self.label_75.setText("")
        self.label_75.setAlignment(QtCore.Qt.AlignCenter)
        self.label_75.setObjectName("label_75")
        self.textoMsgFaltandoNormais_4 = QtWidgets.QLabel(self.mensagemEnvNormais_4)
        self.textoMsgFaltandoNormais_4.setGeometry(QtCore.QRect(10, 10, 181, 21))
        self.textoMsgFaltandoNormais_4.setStyleSheet("font: 87 6pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"background:none;")
        self.textoMsgFaltandoNormais_4.setAlignment(QtCore.Qt.AlignCenter)
        self.textoMsgFaltandoNormais_4.setObjectName("textoMsgFaltandoNormais_4")
        self.stackedWidgetNormais_4.addWidget(self.pageMensagensNormais_4)
        self.pageVaziaNormais_4 = QtWidgets.QWidget()
        self.pageVaziaNormais_4.setObjectName("pageVaziaNormais_4")
        self.textoNormais1_4 = QtWidgets.QLabel(self.pageVaziaNormais_4)
        self.textoNormais1_4.setGeometry(QtCore.QRect(-5, 37, 231, 41))
        self.textoNormais1_4.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"background:none;")
        self.textoNormais1_4.setAlignment(QtCore.Qt.AlignCenter)
        self.textoNormais1_4.setObjectName("textoNormais1_4")
        self.textoNormais2_4 = QtWidgets.QLabel(self.pageVaziaNormais_4)
        self.textoNormais2_4.setGeometry(QtCore.QRect(-10, 67, 231, 41))
        self.textoNormais2_4.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"background:none;")
        self.textoNormais2_4.setAlignment(QtCore.Qt.AlignCenter)
        self.textoNormais2_4.setObjectName("textoNormais2_4")
        self.stackedWidgetNormais_4.addWidget(self.pageVaziaNormais_4)
        self.botaoCriarRotina = QtWidgets.QPushButton(self.pageOneTick)
        self.botaoCriarRotina.setGeometry(QtCore.QRect(568, 676, 61, 61))
        self.botaoCriarRotina.clicked.connect(self.mostrarPopup)
        self.botaoCriarRotina.setCursor(Qt.PointingHandCursor)
        self.botaoCriarRotina.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(0, 170, 0);\n"
"    border-radius:30%;\n"
"    padding: 5px;\n"
"    color:white;\n"
"    font:87 23pt \"Arial Black\";\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"\n"
"background-color: rgb(0, 207, 0);\n"
"borderr-radius: 10px rgb(70, 70, 70);\n"
"}\n"
"QPushButton:pressed {\n"
"\n"
"background-color: rgb(0, 104, 0);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.botaoCriarRotina.setObjectName("botaoCriarRotina")
        self.widgetRotinasSemanais = QtWidgets.QWidget(self.pageOneTick)
        self.widgetRotinasSemanais.setGeometry(QtCore.QRect(798, 206, 241, 221))
        self.widgetRotinasSemanais.setStyleSheet("background-color: rgb(79, 38, 140);\n"
"border-radius:40%\n"
"")
        self.widgetRotinasSemanais.setObjectName("widgetRotinasSemanais")
        self.botaoSemanais_4 = QtWidgets.QPushButton(self.widgetRotinasSemanais)
        self.botaoSemanais_4.setGeometry(QtCore.QRect(0, 150, 241, 71))
        self.botaoSemanais_4.clicked.connect(self.cliqueSemanais)
        self.botaoSemanais_4.setStyleSheet("\n"
"\n"
"\n"
"QPushButton{\n"
"    \n"
"background-color: rgb(128, 62, 226);\n"
"border: 1px solid #4a4a4a;\n"
"border-top-right-radius: 0%;\n"
"border-top-left-radius: 0%;\n"
"border-bottom-right-radius: 40%;\n"
"border-bottom-left-radius: 40%;\n"
"font: 87 10pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"\n"
"background-color: rgb(135, 65, 239);\n"
"borderr-radius: 10px rgb(70, 70, 70);\n"
"}\n"
"QPushButton:pressed {\n"
"\n"
"background-color: rgbrgb(170, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"")
        self.botaoSemanais_4.setObjectName("botaoSemanais_4")
        self.stackedWidgetSemanais_4 = QtWidgets.QStackedWidget(self.widgetRotinasSemanais)
        self.stackedWidgetSemanais_4.setGeometry(QtCore.QRect(10, 10, 221, 131))
        self.stackedWidgetSemanais_4.setObjectName("stackedWidgetSemanais_4")
        self.pageMensagensSemanais_4 = QtWidgets.QWidget()
        self.pageMensagensSemanais_4.setObjectName("pageMensagensSemanais_4")
        self.mensagemEnvSemanais_4 = QtWidgets.QWidget(self.pageMensagensSemanais_4)
        self.mensagemEnvSemanais_4.setGeometry(QtCore.QRect(14, 7, 201, 51))
        self.mensagemEnvSemanais_4.setStyleSheet("background-color: rgb(0, 176, 141);\n"
"border-radius:20%\n"
"")
        self.mensagemEnvSemanais_4.setObjectName("mensagemEnvSemanais_4")
        self.textoHorarioSemanais1_4 = QtWidgets.QLabel(self.mensagemEnvSemanais_4)
        self.textoHorarioSemanais1_4.setGeometry(QtCore.QRect(127, 28, 51, 21))
        self.textoHorarioSemanais1_4.setStyleSheet("font: 87 6pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"background:none;")
        self.textoHorarioSemanais1_4.setAlignment(QtCore.Qt.AlignCenter)
        self.textoHorarioSemanais1_4.setObjectName("textoHorarioSemanais1_4")
        self.label_77 = QtWidgets.QLabel(self.mensagemEnvSemanais_4)
        self.label_77.setGeometry(QtCore.QRect(170, 30, 20, 16))
        self.label_77.setStyleSheet("image: url(:/pics/20x20/cil-check.png);\n"
"background:none;")
        self.label_77.setText("")
        self.label_77.setAlignment(QtCore.Qt.AlignCenter)
        self.label_77.setObjectName("label_77")
        self.textoMsgFaltandoSemanais_4 = QtWidgets.QLabel(self.mensagemEnvSemanais_4)
        self.textoMsgFaltandoSemanais_4.setGeometry(QtCore.QRect(10, 10, 181, 21))
        self.textoMsgFaltandoSemanais_4.setStyleSheet("font: 87 6pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"background:none;")
        self.textoMsgFaltandoSemanais_4.setAlignment(QtCore.Qt.AlignCenter)
        self.textoMsgFaltandoSemanais_4.setObjectName("textoMsgFaltandoSemanais_4")
        self.mensagemRecSemanais_4 = QtWidgets.QWidget(self.pageMensagensSemanais_4)
        self.mensagemRecSemanais_4.setGeometry(QtCore.QRect(10, 70, 191, 51))
        self.mensagemRecSemanais_4.setStyleSheet("background-color: rgb(177, 189, 208);\n"
"border-radius:20%\n"
"")
        self.mensagemRecSemanais_4.setObjectName("mensagemRecSemanais_4")
        self.label_78 = QtWidgets.QLabel(self.mensagemRecSemanais_4)
        self.label_78.setGeometry(QtCore.QRect(10, 30, 20, 16))
        self.label_78.setStyleSheet("image: url(:/pics/20x20/cil-x-circle.png);\n"
"background:none;")
        self.label_78.setText("")
        self.label_78.setAlignment(QtCore.Qt.AlignCenter)
        self.label_78.setObjectName("label_78")
        self.textoMsgEnviadasSemanais2_4 = QtWidgets.QLabel(self.mensagemRecSemanais_4)
        self.textoMsgEnviadasSemanais2_4.setGeometry(QtCore.QRect(22, 26, 51, 21))
        self.textoMsgEnviadasSemanais2_4.setStyleSheet("font: 87 6pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"background:none;")
        self.textoMsgEnviadasSemanais2_4.setAlignment(QtCore.Qt.AlignCenter)
        self.textoMsgEnviadasSemanais2_4.setObjectName("textoMsgEnviadasSemanais2_4")
        self.textoMsgEnviadasSemanais_4 = QtWidgets.QLabel(self.mensagemRecSemanais_4)
        self.textoMsgEnviadasSemanais_4.setGeometry(QtCore.QRect(2, 8, 181, 21))
        self.textoMsgEnviadasSemanais_4.setStyleSheet("font: 87 6pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"background:none;")
        self.textoMsgEnviadasSemanais_4.setAlignment(QtCore.Qt.AlignCenter)
        self.textoMsgEnviadasSemanais_4.setObjectName("textoMsgEnviadasSemanais_4")
        self.stackedWidgetSemanais_4.addWidget(self.pageMensagensSemanais_4)
        self.pageVaziaSemanais_4 = QtWidgets.QWidget()
        self.pageVaziaSemanais_4.setObjectName("pageVaziaSemanais_4")
        self.textoSemanais1_4 = QtWidgets.QLabel(self.pageVaziaSemanais_4)
        self.textoSemanais1_4.setGeometry(QtCore.QRect(-5, 37, 231, 41))
        self.textoSemanais1_4.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"background:none;")
        self.textoSemanais1_4.setAlignment(QtCore.Qt.AlignCenter)
        self.textoSemanais1_4.setObjectName("textoSemanais1_4")
        self.textoSemanais2_4 = QtWidgets.QLabel(self.pageVaziaSemanais_4)
        self.textoSemanais2_4.setGeometry(QtCore.QRect(-10, 67, 231, 41))
        self.textoSemanais2_4.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"background:none;")
        self.textoSemanais2_4.setAlignment(QtCore.Qt.AlignCenter)
        self.textoSemanais2_4.setObjectName("textoSemanais2_4")
        self.stackedWidgetSemanais_4.addWidget(self.pageVaziaSemanais_4)
        self.widgetTab = QtWidgets.QWidget(self.pageOneTick)
        self.widgetTab.setGeometry(QtCore.QRect(-10, 0, 1201, 101))
        self.widgetTab.setStyleSheet("background-color:  rgb(145, 70, 255);\n"
"border: 1px solid #4a4a4a;\n"
"\n"
"border-bottom-right-radius: 20%;\n"
"border-bottom-left-radius: 20%;\n"
"\n"
"")
        self.widgetTab.setObjectName("widgetTab")
        self.label_79 = QtWidgets.QLabel(self.widgetTab)
        self.label_79.setGeometry(QtCore.QRect(20, 20, 101, 101))
        self.label_79.setStyleSheet("image: url(:/pics/OneTickLogoQT2.png);\n"
"border:none;\n"
"background:none;")
        self.label_79.setText("")
        self.label_79.setObjectName("label_79")
        self.widgetAddVariaveis_17 = QtWidgets.QWidget(self.widgetTab)
        self.widgetAddVariaveis_17.setGeometry(QtCore.QRect(560, 24, 541, 61))
        self.widgetAddVariaveis_17.setStyleSheet("background-color: rgb(128, 62, 226);\n"
"border:none;\n"
"border-radius:20%\n"
"")
        self.widgetAddVariaveis_17.setObjectName("widgetAddVariaveis_17")
        self.widgetStatusWhatsapp_4 = QtWidgets.QWidget(self.widgetAddVariaveis_17)
        self.widgetStatusWhatsapp_4.setGeometry(QtCore.QRect(40, 15, 31, 31))
        self.widgetStatusWhatsapp_4.setStyleSheet(f"background-color:{extrairLogin()[2]};\n"
"border-radius:15%\n"
"")
        self.widgetStatusWhatsapp_4.setObjectName("widgetStatusWhatsapp_4")
        self.label_80 = QtWidgets.QLabel(self.widgetAddVariaveis_17)
        self.label_80.setGeometry(QtCore.QRect(78, 10, 201, 41))
        self.label_80.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"background:none;")
        self.label_80.setAlignment(QtCore.Qt.AlignCenter)
        self.label_80.setObjectName("label_80")
        self.label_81 = QtWidgets.QLabel(self.widgetAddVariaveis_17)
        self.label_81.setGeometry(QtCore.QRect(295, 13, 161, 21))
        self.label_81.setStyleSheet("font: 87 7pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"background:none;")
        self.label_81.setAlignment(QtCore.Qt.AlignCenter)
        self.label_81.setObjectName("label_81")
        self.textoUltimaVerificacao_4 = QtWidgets.QLabel(self.widgetAddVariaveis_17)
        self.textoUltimaVerificacao_4.setGeometry(QtCore.QRect(302, 31, 141, 21))
        self.textoUltimaVerificacao_4.setStyleSheet("font: 87 7pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"background:none;")
        self.textoUltimaVerificacao_4.setAlignment(QtCore.Qt.AlignCenter)
        self.textoUltimaVerificacao_4.setObjectName("textoUltimaVerificacao_4")
        self.botaoAtualizar_4 = QtWidgets.QPushButton(self.widgetTab)
        self.botaoAtualizar_4.setGeometry(QtCore.QRect(490, 34, 51, 41))
        self.botaoAtualizar_4.clicked.connect(self.verificarWhatsapp)
        self.botaoAtualizar_4.setCursor(Qt.PointingHandCursor)
        self.botaoAtualizar_4.setStyleSheet("\n"
"QPushButton{\n"
"    \n"
"    \n"
"    image: url(:/pics/24x24/cil-reload.png);\n"
"    \n"
"    background-color: rgb(128, 62, 226);\n"
"    border:none;\n"
"    border-radius:15%;\n"
"    padding: 5px;\n"
"    color:white;\n"
"    font:87 23pt \"Arial Black\";\n"
"    color: rgb(0, 170, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"\n"
"background-color: ;\n"
"    background-color: rgb(137, 66, 243);\n"
"borderr-radius: 10px rgb(70, 70, 70);\n"
"}\n"
"QPushButton:pressed {\n"
"\n"
"background-color: rgbrgb(170, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.botaoAtualizar_4.setText("")
        self.botaoAtualizar_4.setObjectName("botaoAtualizar_4")
        self.botaoFechar = QtWidgets.QPushButton(self.widgetTab)
        self.botaoFechar.setGeometry(QtCore.QRect(1110, 34, 51, 41))
        self.botaoFechar.clicked.connect(QtWidgets.qApp.quit)
        self.botaoFechar.setCursor(Qt.PointingHandCursor)
        self.botaoFechar.setStyleSheet("\n"
"QPushButton{\n"
"    \n"
"    \n"
"    image: url(:/pics/20x20/cil-x-circle.png);\n"
"    background-color: rgb(128, 62, 226);\n"
"    border:none;\n"
"    border-radius:15%;\n"
"    padding: 5px;\n"
"    color:white;\n"
"    font:87 23pt \"Arial Black\";\n"
"    color: rgb(0, 170, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"\n"
"background-color: ;\n"
"    background-color: rgb(137, 66, 243);\n"
"borderr-radius: 10px rgb(70, 70, 70);\n"
"}\n"
"QPushButton:pressed {\n"
"\n"
"background-color: rgbrgb(170, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.botaoFechar.setText("")
        self.botaoFechar.setObjectName("botaoFechar")
        self.botaoOpcoes_4 = QtWidgets.QPushButton(self.widgetTab)
        self.botaoOpcoes_4.setGeometry(QtCore.QRect(250, 35, 51, 41))
        self.botaoOpcoes_4.clicked.connect(self.abrirConfiguracoes)
        self.botaoOpcoes_4.setCursor(Qt.PointingHandCursor)
        self.botaoOpcoes_4.setStyleSheet("\n"
"QPushButton{\n"
"    \n"
"    \n"
"    ;\n"
"    image: url(:/pics/24x24/cil-options.png);\n"
"    \n"
"    background-color: rgb(128, 62, 226);\n"
"    border:none;\n"
"    border-radius:15%;\n"
"    padding: 5px;\n"
"    color:white;\n"
"    font:87 23pt \"Arial Black\";\n"
"    color: rgb(0, 170, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"\n"
"background-color: ;\n"
"    background-color: rgb(137, 66, 243);\n"
"borderr-radius: 10px rgb(70, 70, 70);\n"
"}\n"
"QPushButton:pressed {\n"
"\n"
"background-color: rgbrgb(170, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.botaoOpcoes_4.setText("")
        self.botaoOpcoes_4.setObjectName("botaoOpcoes_4")
        self.label_82 = QtWidgets.QLabel(self.widgetTab)
        self.label_82.setGeometry(QtCore.QRect(70, 33, 191, 41))
        self.label_82.setStyleSheet("font: 24pt \"Bahnschrift Condensed\";\n"
"color: rgb(255, 255, 255);\n"
"background:none;\n"
"border:None;")
        self.label_82.setAlignment(QtCore.Qt.AlignCenter)
        self.label_82.setObjectName("label_82")
        self.widgetErro = QtWidgets.QWidget(self.pageOneTick)
        self.widgetErro.setEnabled(True)
        self.widgetErro.setVisible(False)
        self.widgetErro.setGeometry(QtCore.QRect(360, 260, 461, 241))
        self.widgetErro.setStyleSheet("background-color: rgb(53, 53, 53);\n"
"border:2px solid rgb(0, 0, 0);\n"
"border-radius: 30%;")
        self.widgetErro.setObjectName("widgetErro")
        self.frame_conterImagem = QtWidgets.QFrame(self.widgetErro)
        self.frame_conterImagem.setGeometry(QtCore.QRect(10, 10, 440, 221))
        self.frame_conterImagem.setStyleSheet("border:none;")
        self.frame_conterImagem.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_conterImagem.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_conterImagem.setObjectName("frame_conterImagem")
        self.img_alerta = QtWidgets.QLabel(self.frame_conterImagem)
        self.img_alerta.setGeometry(QtCore.QRect(-40, -140, 511, 441))
        self.img_alerta.setStyleSheet("background: url(:/imagemAlerta/24x24/3800505.png);\n"
"\n"
"border: none;\n"
"opacity: 0.5;\n"
"")
        self.img_alerta.setText("")
        self.img_alerta.setTextFormat(QtCore.Qt.AutoText)
        self.img_alerta.setScaledContents(False)
        self.img_alerta.setObjectName("img_alerta")
        self.tituloAlerta = QtWidgets.QLabel(self.frame_conterImagem)
        self.tituloAlerta.setGeometry(QtCore.QRect(0, 0, 441, 51))
        self.tituloAlerta.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tituloAlerta.setStyleSheet("background:none;\n"
"font: 87 16pt \"Arial Black\";\n"
"color:rgb(255, 255, 255)")
        self.tituloAlerta.setAlignment(QtCore.Qt.AlignCenter)
        self.tituloAlerta.setObjectName("tituloAlerta")
        self.textoAlerta = QtWidgets.QLabel(self.frame_conterImagem)
        self.textoAlerta.setGeometry(QtCore.QRect(0, 50, 441, 121))
        self.textoAlerta.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textoAlerta.setStyleSheet("background:none;\n"
"font: 87 10pt \"Arial Black\";\n"
"color:rgb(255, 255, 255)")
        self.textoAlerta.setAlignment(QtCore.Qt.AlignCenter)
        self.textoAlerta.setObjectName("textoAlerta")
        self.botaoFecharErro = QtWidgets.QPushButton(self.frame_conterImagem)
        self.botaoFecharErro.setGeometry(QtCore.QRect(171, 180, 91, 31))
        self.botaoFecharErro.clicked.connect(self.__popupErro)
        self.botaoFecharErro.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:10px;\n"
"    \n"
"    font:87 10pt \"Arial Black\";\n"
"    color: rgb(51, 51, 51);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(229, 229, 229);\n"
"borderr-radius: 10px rgb(70, 70, 70);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(145, 70, 255);\n"
"color: (145, 70, 255);\n"
"}")
        self.botaoFecharErro.setObjectName("botaoFecharErro")
        self.widgetRotinasDiarias = QtWidgets.QWidget(self.pageOneTick)
        self.widgetRotinasDiarias.setGeometry(QtCore.QRect(163, 206, 241, 221))
        self.widgetRotinasDiarias.setStyleSheet("background-color: rgb(79, 38, 140);\n"
"border-radius:40%\n"
"")
        self.widgetRotinasDiarias.setObjectName("widgetRotinasDiarias")
        self.botaoDiarias_4 = QtWidgets.QPushButton(self.widgetRotinasDiarias)
        self.botaoDiarias_4.setGeometry(QtCore.QRect(0, 150, 241, 71))
        self.botaoDiarias_4.clicked.connect(self.cliqueDiaria)
        self.botaoDiarias_4.setStyleSheet("\n"
"\n"
"\n"
"QPushButton{\n"
"    \n"
"background-color: rgb(128, 62, 226);\n"
"border: 1px solid #4a4a4a;\n"
"border-top-right-radius: 0%;\n"
"border-top-left-radius: 0%;\n"
"border-bottom-right-radius: 40%;\n"
"border-bottom-left-radius: 40%;\n"
"font: 87 10pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"\n"
"background-color: rgb(135, 65, 239);\n"
"borderr-radius: 10px rgb(70, 70, 70);\n"
"}\n"
"QPushButton:pressed {\n"
"\n"
"background-color: rgbrgb(170, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"")
        self.botaoDiarias_4.setObjectName("botaoDiarias_4")
        self.stackedWidgetDiarias_4 = QtWidgets.QStackedWidget(self.widgetRotinasDiarias)
        self.stackedWidgetDiarias_4.setGeometry(QtCore.QRect(10, 10, 221, 131))
        self.stackedWidgetDiarias_4.setObjectName("stackedWidgetDiarias_4")
        self.pageMensagensDiarias_4 = QtWidgets.QWidget()
        self.pageMensagensDiarias_4.setObjectName("pageMensagensDiarias_4")
        self.mensagemEnvDiarias_4 = QtWidgets.QWidget(self.pageMensagensDiarias_4)
        self.mensagemEnvDiarias_4.setGeometry(QtCore.QRect(14, 7, 201, 51))
        self.mensagemEnvDiarias_4.setStyleSheet("background-color: rgb(0, 176, 141);\n"
"border-radius:20%\n"
"")
        self.mensagemEnvDiarias_4.setObjectName("mensagemEnvDiarias_4")
        self.textoHorarioDiarias1_4 = QtWidgets.QLabel(self.mensagemEnvDiarias_4)
        self.textoHorarioDiarias1_4.setGeometry(QtCore.QRect(127, 28, 51, 21))
        self.textoHorarioDiarias1_4.setStyleSheet("font: 87 6pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"background:none;")
        self.textoHorarioDiarias1_4.setAlignment(QtCore.Qt.AlignCenter)
        self.textoHorarioDiarias1_4.setObjectName("textoHorarioDiarias1_4")
        self.label_83 = QtWidgets.QLabel(self.mensagemEnvDiarias_4)
        self.label_83.setGeometry(QtCore.QRect(170, 30, 20, 16))
        self.label_83.setStyleSheet("image: url(:/pics/20x20/cil-check.png);\n"
"background:none;")
        self.label_83.setText("")
        self.label_83.setAlignment(QtCore.Qt.AlignCenter)
        self.label_83.setObjectName("label_83")
        self.textoMsgFaltandoDiarias_4 = QtWidgets.QLabel(self.mensagemEnvDiarias_4)
        self.textoMsgFaltandoDiarias_4.setGeometry(QtCore.QRect(10, 10, 181, 21))
        self.textoMsgFaltandoDiarias_4.setStyleSheet("font: 87 6pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"background:none;")
        self.textoMsgFaltandoDiarias_4.setAlignment(QtCore.Qt.AlignCenter)
        self.textoMsgFaltandoDiarias_4.setObjectName("textoMsgFaltandoDiarias_4")
        self.mensagemRecDiarias_4 = QtWidgets.QWidget(self.pageMensagensDiarias_4)
        self.mensagemRecDiarias_4.setGeometry(QtCore.QRect(10, 70, 191, 51))
        self.mensagemRecDiarias_4.setStyleSheet("background-color: rgb(177, 189, 208);\n"
"border-radius:20%\n"
"")
        self.mensagemRecDiarias_4.setObjectName("mensagemRecDiarias_4")
        self.label_84 = QtWidgets.QLabel(self.mensagemRecDiarias_4)
        self.label_84.setGeometry(QtCore.QRect(10, 30, 20, 16))
        self.label_84.setStyleSheet("image: url(:/pics/20x20/cil-x-circle.png);\n"
"background:none;")
        self.label_84.setText("")
        self.label_84.setAlignment(QtCore.Qt.AlignCenter)
        self.label_84.setObjectName("label_84")
        self.textoHorarioDiarias2_4 = QtWidgets.QLabel(self.mensagemRecDiarias_4)
        self.textoHorarioDiarias2_4.setGeometry(QtCore.QRect(22, 26, 51, 21))
        self.textoHorarioDiarias2_4.setStyleSheet("font: 87 6pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"background:none;")
        self.textoHorarioDiarias2_4.setAlignment(QtCore.Qt.AlignCenter)
        self.textoHorarioDiarias2_4.setObjectName("textoHorarioDiarias2_4")
        self.textoMsgEnviadasDiaria_4 = QtWidgets.QLabel(self.mensagemRecDiarias_4)
        self.textoMsgEnviadasDiaria_4.setGeometry(QtCore.QRect(2, 8, 181, 21))
        self.textoMsgEnviadasDiaria_4.setStyleSheet("font: 87 6pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"background:none;")
        self.textoMsgEnviadasDiaria_4.setAlignment(QtCore.Qt.AlignCenter)
        self.textoMsgEnviadasDiaria_4.setObjectName("textoMsgEnviadasDiaria_4")
        self.stackedWidgetDiarias_4.addWidget(self.pageMensagensDiarias_4)
        self.pageVaziaDiarias_4 = QtWidgets.QWidget()
        self.pageVaziaDiarias_4.setObjectName("pageVaziaDiarias_4")
        self.textoDiarias1_4 = QtWidgets.QLabel(self.pageVaziaDiarias_4)
        self.textoDiarias1_4.setGeometry(QtCore.QRect(-5, 37, 231, 41))
        self.textoDiarias1_4.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"background:none;")
        self.textoDiarias1_4.setAlignment(QtCore.Qt.AlignCenter)
        self.textoDiarias1_4.setObjectName("textoDiarias1_4")
        self.textoDiarias2_4 = QtWidgets.QLabel(self.pageVaziaDiarias_4)
        self.textoDiarias2_4.setGeometry(QtCore.QRect(-10, 67, 231, 41))
        self.textoDiarias2_4.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"background:none;")
        self.textoDiarias2_4.setAlignment(QtCore.Qt.AlignCenter)
        self.textoDiarias2_4.setObjectName("textoDiarias2_4")
        self.stackedWidgetDiarias_4.addWidget(self.pageVaziaDiarias_4)
        self.widgetAbrirMensagens = QtWidgets.QWidget(self.pageOneTick)
        self.widgetAbrirMensagens.setGeometry(QtCore.QRect(308, 206, 601, 311))
        self.widgetAbrirMensagens.setVisible(False)
        self.widgetAbrirMensagens.setStyleSheet("background-color: rgb(128, 62, 226);\n"
"border:none;\n"
"border-radius:20%\n"
"")
        self.widgetAbrirMensagens.setObjectName("widgetAbrirMensagens")
        self.botaoFecharListaMensagens_4 = QtWidgets.QPushButton(self.widgetAbrirMensagens)
        self.botaoFecharListaMensagens_4.setGeometry(QtCore.QRect(530, 10, 50, 24))
        self.botaoFecharListaMensagens_4.setMinimumSize(QtCore.QSize(50, 0))
        self.botaoFecharListaMensagens_4.clicked.connect(self.abrirMensagens)
        self.botaoFecharListaMensagens_4.setCursor(Qt.PointingHandCursor)
        self.botaoFecharListaMensagens_4.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(145, 70, 255);\n"
"    border-radius:10px;\n"
"    \n"
"    font:87 10pt \"Arial Black\";\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(166, 68, 255);\n"
"borderr-radius: 10px rgb(70, 70, 70);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(145, 70, 255);\n"
"color: (145, 70, 255);\n"
"}")
        self.botaoFecharListaMensagens_4.setObjectName("botaoFecharListaMensagens_4")
        self.listaMensagensDeRotinas_4 = QtWidgets.QListWidget(self.widgetAbrirMensagens)
        self.listaMensagensDeRotinas_4.setGeometry(QtCore.QRect(40, 60, 411, 211))
        self.listaMensagensDeRotinas_4.clicked.connect(self.mostrarBotaoExcluir)
        self.listaMensagensDeRotinas_4.setCursor(Qt.PointingHandCursor)
        self.listaMensagensDeRotinas_4.setStyleSheet("QListWidget\n"
"{\n"
"border : 3px solid rgb(255,255,255);\n"
"border-radius:12%;\n"
"color:white;\n"
"padding:10px 20px;\n"
"}\n"
"QListView::item:hover\n"
"{\n"
"background: rgb(166, 104, 197);\n"
"color: white;\n"
"}\n"
" QListView::item:selected\n"
"{\n"
"border : 2px solid rgb(166, 104, 197);\n"
"background:rgb(85, 0, 127)\n"
"}")
        self.listaMensagensDeRotinas_4.setObjectName("listaMensagensDeRotinas_4")
        self.botaoExcluir_4 = QtWidgets.QPushButton(self.widgetAbrirMensagens)
        self.botaoExcluir_4.setGeometry(QtCore.QRect(470, 110, 101, 101))
        self.botaoExcluir_4.setMinimumSize(QtCore.QSize(50, 0))
        self.botaoExcluir_4.setVisible(False)
        self.botaoExcluir_4.clicked.connect(self.excluirMensagem)
        self.botaoExcluir_4.setCursor(Qt.PointingHandCursor)
        self.botaoExcluir_4.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(145, 70, 255);\n"
"    border-radius:10px;\n"
"    \n"
"    font:87 10pt \"Arial Black\";\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(166, 68, 255);\n"
"borderr-radius: 10px rgb(70, 70, 70);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(145, 70, 255);\n"
"color: (145, 70, 255);\n"
"}")
        self.botaoExcluir_4.setObjectName("botaoExcluir_4")
        self.label_85 = QtWidgets.QLabel(self.widgetAbrirMensagens)
        self.label_85.setGeometry(QtCore.QRect(100, 10, 401, 41))
        self.label_85.setStyleSheet("font: 87 15pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"background:none;")
        self.label_85.setAlignment(QtCore.Qt.AlignCenter)
        self.label_85.setObjectName("label_85")
        self.botaoAtualizarRotinas = QtWidgets.QPushButton(self.pageOneTick)
        self.botaoAtualizarRotinas.setGeometry(QtCore.QRect(60, 210, 51, 41))
        self.botaoAtualizarRotinas.clicked.connect(self.verificarSeHaMensagensParaExibir)
        self.botaoAtualizarRotinas.setCursor(Qt.PointingHandCursor)
        self.botaoAtualizarRotinas.setStyleSheet("\n"
 "QPushButton{\n"
 "    \n"
 "    \n"
 "    image: url(:/pics/24x24/cil-reload.png);\n"
 "    \n"
 "    background-color: rgb(128, 62, 226);\n"
 "    border:none;\n"
 "    border-radius:15%;\n"
 "    padding: 5px;\n"
 "    color:white;\n"
 "    font:87 23pt \"Arial Black\";\n"
 "    color: rgb(0, 170, 0);\n"
 "}\n"
 "\n"
 "QPushButton:hover {\n"
 "\n"
 "background-color: ;\n"
 "    background-color: rgb(137, 66, 243);\n"
 "borderr-radius: 10px rgb(70, 70, 70);\n"
 "}\n"
 "QPushButton:pressed {\n"
 "\n"
 "background-color: rgbrgb(170, 0, 255);\n"
 "color: rgb(255, 255, 255);\n"
 "\n"
 "}")
        self.botaoAtualizarRotinas.setText("")
        self.botaoAtualizarRotinas.setObjectName("botaoAtualizarRotinas")
        self.botaoAtualizarRotinas.raise_()
        self.label_85.raise_()
        self.botaoFecharListaMensagens_4.raise_()
        self.listaMensagensDeRotinas_4.raise_()
        self.botaoExcluir_4.raise_()
        self.widgetRotinasDeDias.raise_()
        self.label_68.raise_()
        self.widgetRotinasMensais.raise_()
        self.widgetRotinasNormais.raise_()
        self.botaoCriarRotina.raise_()
        self.widgetRotinasSemanais.raise_()
        self.widgetTab.raise_()
        self.widgetRotinasDiarias.raise_()
        self.widgetOpcoes.raise_()
        self.widgetAbrirMensagens.raise_()
        self.widgetErro.raise_()
        self.stackedWidget.addWidget(self.pageOneTick)
        MainWindow.setCentralWidget(self.centralwidget)

        MainWindow.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=3, yOffset=3,
                                                                           color=QtGui.QColor(0, 0, 0, 100)))


        self.widgetOpcoes.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=3, yOffset=3,
                                                                           color=QtGui.QColor(0, 0, 0, 100)))


        self.widgetAbrirMensagens.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=3, yOffset=3,
                                                                                color=QtGui.QColor(0, 0, 0, 100)))


        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(extrairLogin()[0])
        self.stackedWidgetDias_4.setCurrentIndex(1)
        self.stackedWidgetMensais_4.setCurrentIndex(1)
        self.stackedWidgetNormais_4.setCurrentIndex(1)
        self.stackedWidgetSemanais_4.setCurrentIndex(1)
        self.stackedWidgetDiarias_4.setCurrentIndex(1)
        self.verificarSeHaMensagensParaExibir()

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("OneTick", "OneTick"))
        MainWindow.setWindowIcon(QtGui.QIcon('OneTickLogo.png'))
        self.label_87.setText(_translate("MainWindow", "Seja bem vindo(a) ao OneTick"))
        self.botaoComecar.setText(_translate("MainWindow", "COMEÇAR"))
        self.label_90.setText(_translate("MainWindow", "Clique aqui para o aplicativo reconhecer seu Whatsapp"))
        self.botaoDias_4.setText(_translate("MainWindow", "ROTINAS DE DIAS"))
        self.textoHorarioDias1_4.setText(_translate("MainWindow", "12:20"))
        self.textoMsgFaltandoDias_4.setText(_translate("MainWindow", "X MENSAGENS FALTANDO"))
        self.textoHorarioDias2_4.setText(_translate("MainWindow", "12:20"))
        self.textoMsgEnviadasDias_4.setText(_translate("MainWindow", "X MENSAGENS JÁ FORAM"))
        self.textoDias1_4.setText(_translate("MainWindow", "NENHUMA MENSAGEM"))
        self.textoDias2_4.setText(_translate("MainWindow", "AGENDADA"))
        self.label_68.setText(_translate("MainWindow", "ACOMPANHE SUAS ROTINAS"))
        self.label_69.setText(_translate("MainWindow", "RESETAR ROTINAS:"))
        self.botaoFechar_6.setText(_translate("MainWindow", "x"))
        self.label_70.setText(_translate("MainWindow", "APERTE ABAIXO PARA RESETAR TODAS AS ROTINAS E VOLTAR AO PADRÃO"))
        self.label_71.setText(_translate("MainWindow", "CLIQUE NO BOTÃO ABAIXO PARA RESETAR TODAS AS ROTINAS E DESOLGAR"))
        self.label_72.setText(_translate("MainWindow", "DESLOGAR"))
        self.botaoMensais_4.setText(_translate("MainWindow", "ROTINAS MENSAIS"))
        self.textoHorarioMensais1_4.setText(_translate("MainWindow", "12:20"))
        self.textoMsgFaltandoMensais_4.setText(_translate("MainWindow", "X MENSAGENS FALTANDO"))
        self.textoHorarioMensais2_4.setText(_translate("MainWindow", "12:20"))
        self.textoMsgEnviadasMensais_4.setText(_translate("MainWindow", "X MENSAGENS JÁ FORAM"))
        self.textoMensais1_4.setText(_translate("MainWindow", "NENHUMA MENSAGEM"))
        self.textoMensais2_4.setText(_translate("MainWindow", "AGENDADA"))
        self.botaoNormais_4.setText(_translate("MainWindow", "ROTINAS NORMAIS"))
        self.textoHorarioNormais1_4.setText(_translate("MainWindow", "12:20"))
        self.textoMsgFaltandoNormais_4.setText(_translate("MainWindow", "X MENSAGENS FALTANDO"))
        self.textoNormais1_4.setText(_translate("MainWindow", "NENHUMA MENSAGEM"))
        self.textoNormais2_4.setText(_translate("MainWindow", "AGENDADA"))
        self.botaoCriarRotina.setText(_translate("MainWindow", "+"))
        self.botaoSemanais_4.setText(_translate("MainWindow", "ROTINAS SEMANAIS"))
        self.textoHorarioSemanais1_4.setText(_translate("MainWindow", "12:20"))
        self.textoMsgFaltandoSemanais_4.setText(_translate("MainWindow", "X MENSAGENS FALTANDO"))
        self.textoMsgEnviadasSemanais2_4.setText(_translate("MainWindow", "12:20"))
        self.textoMsgEnviadasSemanais_4.setText(_translate("MainWindow", "X MENSAGENS JÁ FORAM"))
        self.textoSemanais1_4.setText(_translate("MainWindow", "NENHUMA MENSAGEM"))
        self.textoSemanais2_4.setText(_translate("MainWindow", "AGENDADA"))
        self.label_80.setText(_translate("MainWindow", "STATUS WHATSAPP"))
        self.label_81.setText(_translate("MainWindow", "ÚLTIMA VERIFICAÇÃO:"))
        self.textoUltimaVerificacao_4.setText(_translate("MainWindow", extrairLogin()[1]))
        self.label_82.setText(_translate("MainWindow", "ONETICK"))
        self.botaoDiarias_4.setText(_translate("MainWindow", "ROTINAS DIÁRIAS"))
        self.textoHorarioDiarias1_4.setText(_translate("MainWindow", "12:20"))
        self.textoMsgFaltandoDiarias_4.setText(_translate("MainWindow", "X MENSAGENS FALTANDO"))
        self.textoHorarioDiarias2_4.setText(_translate("MainWindow", "12:20"))
        self.textoMsgEnviadasDiaria_4.setText(_translate("MainWindow", "X MENSAGENS JÁ FORAM"))
        self.textoDiarias1_4.setText(_translate("MainWindow", "NENHUMA MENSAGEM"))
        self.textoDiarias2_4.setText(_translate("MainWindow", "AGENDADA"))
        self.botaoFecharListaMensagens_4.setText(_translate("MainWindow", "x"))
        self.botaoExcluir_4.setText(_translate("MainWindow", "EXCLUIR"))
        self.label_85.setText(_translate("MainWindow", "MENSAGENS"))
        self.tituloAlerta.setText(_translate("Form", "Titulo"))
        self.textoAlerta.setText(_translate("Form", "Conteudo"))
        self.botaoFecharErro.setText(_translate("Form", "Fechar"))




# DEF QUE ABRE MENSAGENS VINDO DO BANCO DE DADOS
    def abrirMensagens(self):
        conexao = sqlite3.connect(rf'{self.localContent}')
        cursor = conexao.cursor()
        atualizarDados(cursor)

        if self.widgetAbrirMensagens.isVisible():
            self.widgetAbrirMensagens.setVisible(False)
        else:
            self.widgetAbrirMensagens.setVisible(True)


        conexao.commit()
        cursor.close()
        conexao.close()



#DEF PARA ABRIR POPUP DE CONFIGURAÇÕES
    def abrirConfiguracoes(self):

        if self.widgetOpcoes.isVisible():
            self.widgetOpcoes.setVisible(False)
        else:
            self.widgetOpcoes.setVisible(True)
            self.widgetOpcoes.raise_()






#DEF PARA DESLOGAR DO ONETICK
    def deslogar(self):
        conexao = sqlite3.connect(rf'{self.localContent}')
        cursor = conexao.cursor()

        apagarTodasRotinas(cursor)
        atualizarLogin(cursor, 0)


        conexao.commit()
        cursor.close()
        conexao.close()

        QtWidgets.qApp.quit()



#DEF PARA RESETAR ROTINAS
    def resetarRotinasBotao(self):
        conexao = sqlite3.connect(rf'{self.localContent}')
        cursor = conexao.cursor()

        apagarTodasRotinas(cursor)


        conexao.commit()
        cursor.close()
        conexao.close()

        self.verificarSeHaMensagensParaExibir()


#DEF PARA SALVAR PATH DE ONDE ESTÁ AS PATHS
    def InformacoesEPath(self):

        Interface = f'{os.getcwd()}'


        conexao = sqlite3.connect(rf'{self.localContent}')
        cursor = conexao.cursor()




        cursor.execute('DELETE FROM Informacoes')
        cursor.execute('INSERT INTO Informacoes (local)'
        'VALUES (?)', (Interface, ))



        conexao.commit()
        cursor.close()
        conexao.close()










#DEF PARA VERIFICAR SE WHATSAPP ESTÁ LOGADO
    def verificarWhatsapp(self):
            try:
                    close = subprocess.run("taskkill /im chrome.exe /f", shell=True, stderr=True)
                    print(close.stderr)
                    self.options = webdriver.ChromeOptions()
                    self.options.add_experimental_option("excludeSwitches", ['enable-automation'])
                    service = Service()
                    service.creationflags = CREATE_NO_WINDOW
                    self.options.add_argument(f'user-data-dir={os.path.expanduser("~")}\\AppData\\Local\\Google\\Chrome\\User Data')
                    self.driver = webdriver.Chrome(options=self.options, service=service)
                    sleep(1)
                    if close.returncode == 0:
                            sleep(1)
                            hotkey('ctrl', 'shift', 't')

                    self.driver.get("https://web.whatsapp.com/")

                    esperar = WebDriverWait(driver=self.driver, timeout=50).until(
                    EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="app"]/div/div/div[3]/header/div[1]/div/div/span')))

                    conexao = sqlite3.connect(rf'{self.localContent}')
                    cursor = conexao.cursor()

                    atualizarLogin(cursor, 1)

                    conexao.commit()
                    cursor.close()
                    conexao.close()
                    sleep(2)

                    if self.stackedWidget.currentIndex() == 0:
                        self.stackedWidget.setCurrentIndex(extrairLogin()[0])


                    self.widgetStatusWhatsapp_4.setStyleSheet(f"background-color:{extrairLogin()[2]};\n"
                    "border-radius:15%\n"
                    "")
                    self.textoUltimaVerificacao_4.setText(extrairLogin()[1])


                    sleep(2)

                    self.driver.close()
            except:

                  self.driver.close()


                  conexao = sqlite3.connect(rf'{self.localContent}')
                  cursor = conexao.cursor()

                  if self.stackedWidget.currentIndex() == 1:
                      atualizarLogin(cursor, 2)
                  else:
                      atualizarLogin(cursor, 0)

                  self.widgetStatusWhatsapp_4.setStyleSheet(f"background-color:{extrairLogin()[2]};\n"
                                                            "border-radius:15%\n"
                                                            "")
                  self.textoUltimaVerificacao_4.setText(extrairLogin()[1])

                  conexao.commit()
                  cursor.close()
                  conexao.close()
                  sleep(2)

#DEF PARA MOSTRAR BOTAO EXCLUR
    def mostrarBotaoExcluir(self):
        self.botaoExcluir_4.setVisible(True)

#DEF PARA MOSTRAR O POPUP DE ADICIONAR ROTINAS
    def mostrarPopup(self):
        self.popup = QtWidgets.QMainWindow()
        self.popupAdd = Ui_Form()
        self.popupAdd.setupUi(self.popup)
        self.popup.show()


#DEF ATUALIZAR CASO TENHA MENSAGENS NOVAS CADASTRADAS OU SE OUTRAS JÁ FORAM EXECUTADAS
    def verificarSeHaMensagensParaExibir(self):

        conexao = sqlite3.connect(rf'{self.localContent}')
        cursor = conexao.cursor()
        try:
            if extrairMensagensEnvio(cursor):
                mensagensPassadas(cursor)
                if extrairMensagensEnvio(cursor):
                    self.stackedWidgetNormais_4.setCurrentIndex(0)
                    msgsFaltantes = 0
                    for i in range(0, len(extrairMensagensEnvio(cursor))):
                        if extrairMensagensEnvio(cursor)[i][10] == 'PENDENTE':
                            msgsFaltantes += 1

                    self.textoHorarioNormais1_4.setText(extrairMensagensEnvio(cursor)[0][1])
                    self.textoMsgFaltandoNormais_4.setText(f'{msgsFaltantes} MENSAGENS FALTANDO')
                else:
                    self.stackedWidgetNormais_4.setCurrentIndex(1)

            else:
                self.stackedWidgetNormais_4.setCurrentIndex(1)



            if extrairMensagensDiaria(cursor):
                self.stackedWidgetDiarias_4.setCurrentIndex(0)

                if extrairMensagensDiaria(cursor):
                    msgsFaltantes = 0
                    msgsTotais = len(extrairMensagensDiaria(cursor))
                    for i in range(0, len(extrairMensagensDiaria(cursor))):
                        if extrairMensagensDiaria(cursor)[i][10] == 'PENDENTE':
                            msgsFaltantes += 1

                    msgsEnviadas = msgsTotais - msgsFaltantes

                    self.textoHorarioDiarias1_4.setText(extrairMensagensDiaria(cursor)[0][1])
                    self.textoHorarioDiarias2_4.setText(extrairMensagensDiaria(cursor)[0][1])
                    self.textoMsgFaltandoDiarias_4.setText(f'{msgsFaltantes} MENSAGENS FALTANDO')
                    self.textoMsgEnviadasDiaria_4.setText(f'{msgsEnviadas} MENSAGENS JÁ FORAM')
            else:
                self.stackedWidgetDiarias_4.setCurrentIndex(1)



            if extrairMensagensMensal(cursor):
                self.stackedWidgetMensais_4.setCurrentIndex(0)

                if extrairMensagensMensal(cursor):
                    msgsFaltantes = 0
                    msgsTotais = len(extrairMensagensMensal(cursor))
                    for i in range(0, len(extrairMensagensMensal(cursor))):
                        if extrairMensagensMensal(cursor)[i][10] == 'PENDENTE':
                            msgsFaltantes += 1

                    msgsEnviadas = msgsTotais - msgsFaltantes
                    self.textoHorarioMensais1_4.setText(extrairMensagensMensal(cursor)[0][1])
                    self.textoHorarioMensais2_4.setText(extrairMensagensMensal(cursor)[0][1])
                    self.textoMsgFaltandoMensais_4.setText(f'{msgsFaltantes} MENSAGENS FALTANDO')
                    self.textoMsgEnviadasMensais_4.setText(f'{msgsEnviadas} MENSAGENS JÁ FORAM')

            else:
                self.stackedWidgetMensais_4.setCurrentIndex(1)


            if extrairMensagensSemanal(cursor):
                self.stackedWidgetSemanais_4.setCurrentIndex(0)
                if extrairMensagensSemanal(cursor):
                    msgsFaltantes = 0
                    msgsTotais = len(extrairMensagensSemanal(cursor))
                    for i in range(0, len(extrairMensagensSemanal(cursor))):
                        if extrairMensagensSemanal(cursor)[i][10] == 'PENDENTE':
                            msgsFaltantes += 1

                    msgsEnviadas = msgsTotais - msgsFaltantes
                    self.textoHorarioSemanais1_4.setText(extrairMensagensSemanal(cursor)[0][1])
                    self.textoMsgEnviadasSemanais2_4.setText(extrairMensagensSemanal(cursor)[0][1])
                    self.textoMsgFaltandoSemanais_4.setText(f'{msgsFaltantes} MENSAGENS FALTANDO')
                    self.textoMsgEnviadasSemanais_4.setText(f'{msgsEnviadas} MENSAGENS JÁ FORAM')
            else:
                self.stackedWidgetSemanais_4.setCurrentIndex(1)






            if extrairMensagensPersonalizada(cursor):
                self.stackedWidgetDias_4.setCurrentIndex(0)
                if extrairMensagensPersonalizada(cursor):
                    msgsFaltantes = 0
                    msgsTotais = len(extrairMensagensPersonalizada(cursor))
                    for i in range(0, len(extrairMensagensPersonalizada(cursor))):
                        if extrairMensagensPersonalizada(cursor)[i][10] == 'PENDENTE':
                            msgsFaltantes += 1

                    msgsEnviadas = msgsTotais - msgsFaltantes
                    self.textoHorarioDias1_4.setText(extrairMensagensPersonalizada(cursor)[0][1])
                    self.textoHorarioDias2_4.setText(extrairMensagensPersonalizada(cursor)[0][1])
                    self.textoMsgFaltandoDias_4.setText(f'{msgsFaltantes} MENSAGENS FALTANDO')
                    self.textoMsgEnviadasDias_4.setText(f'{msgsEnviadas} MENSAGENS JÁ FORAM')
            else:
                self.stackedWidgetDias_4.setCurrentIndex(1)
        except:
            pass



        conexao.commit()
        cursor.close()
        conexao.close()

        self.widgetStatusWhatsapp_4.setStyleSheet(f"background-color:{extrairLogin()[2]};\n"
                                                  "border-radius:15%\n"
                                                  "")
        self.textoUltimaVerificacao_4.setText(extrairLogin()[1])


#DEF PARA ABRIR POPUP DE MENSAGENS DE DIARIA
    def cliqueDiaria(self):
        self.abrirMensagens()
        conexao = sqlite3.connect(rf'{self.localContent}')
        cursor = conexao.cursor()

        self.listaMensagensDeRotinas_4.clear()

        msgs = extrairMensagensDiaria(cursor)

        for i in msgs:
            self.listaMensagensDeRotinas_4.addItem(i[8])



        conexao.commit()
        cursor.close()
        conexao.close()


#DEF PARA ABRIR POPUP DE MENSAGENS DE SEMANAIS
    def cliqueSemanais(self):
        self.abrirMensagens()
        conexao = sqlite3.connect(rf'{self.localContent}')
        cursor = conexao.cursor()

        self.listaMensagensDeRotinas_4.clear()

        msgs = extrairMensagensSemanal(cursor)

        for i in msgs:
            self.listaMensagensDeRotinas_4.addItem(i[8])

        conexao.commit()
        cursor.close()
        conexao.close()



#DEF PARA ABRIR POPUP DE MENSAGENS DE NORMAIS
    def cliqueNormais(self):
        self.abrirMensagens()
        conexao = sqlite3.connect(rf'{self.localContent}')
        cursor = conexao.cursor()

        self.listaMensagensDeRotinas_4.clear()

        msgs = extrairMensagensEnvio(cursor)

        for i in msgs:
            self.listaMensagensDeRotinas_4.addItem(i[8])

        conexao.commit()
        cursor.close()
        conexao.close()




#DEF PARA ABRIR POPUP DE MENSAGENS DE MENSAIS
    def cliqueMensais(self):
        self.abrirMensagens()
        conexao = sqlite3.connect(rf'{self.localContent}')
        cursor = conexao.cursor()

        self.listaMensagensDeRotinas_4.clear()

        msgs = extrairMensagensMensal(cursor)

        for i in msgs:
            self.listaMensagensDeRotinas_4.addItem(i[8])

        conexao.commit()
        cursor.close()
        conexao.close()




#DEF PARA ABRIR POPUP DE MENSAGENS DE DIAS DA SEMANA
    def cliqueDeDias(self):
        self.abrirMensagens()
        conexao = sqlite3.connect(rf'{self.localContent}')
        cursor = conexao.cursor()

        self.listaMensagensDeRotinas_4.clear()

        msgs = extrairMensagensPersonalizada(cursor)

        for i in msgs:
            self.listaMensagensDeRotinas_4.addItem(i[8])

        conexao.commit()
        cursor.close()
        conexao.close()


#DEF PARA EXIBIR POPUP DE ERRO
    def __popupErro(self, titulo='Erro', conteudo='Erro'):
        try:
            self.tituloAlerta.setText(titulo)
            self.textoAlerta.setText(conteudo)
            self.widgetErro.setVisible(True)

        except:
            self.widgetErro.setVisible(False)



#DEF PARA EXCLUIR ROTINA DE MENSAGEM
    def excluirMensagem(self):


        conexao = sqlite3.connect(rf'{self.localContent}')
        cursor = conexao.cursor()
        try:
            if self.listaMensagensDeRotinas_4.count() != 0:
                item = self.listaMensagensDeRotinas_4.currentItem().text()
                itemQ = self.listaMensagensDeRotinas_4.currentItem()
                cursor.execute('DELETE FROM Mensagens WHERE nome_rotina = ?', (item, ))
                self.listaMensagensDeRotinas_4.takeItem(self.listaMensagensDeRotinas_4.indexFromItem(itemQ).row())
                atualizarRotinasInterface(cursor)
            else:
                self.__popupErro('Erro ao deletar', 'Selecione um item para deletar')
        except:
            self.__popupErro('Erro ao deletar', 'Selecione um item para deletar')


        conexao.commit()
        cursor.close()
        conexao.close()

        conexao = sqlite3.connect(rf'{self.localContent}')
        cursor = conexao.cursor()

        apagarRotinasInterface(cursor)

        conexao.commit()
        cursor.close()
        conexao.close()

        self.verificarSeHaMensagensParaExibir()

        self.botaoExcluir_4.setVisible(False)





if __name__=="__main__":
        app = QtWidgets.QApplication(sys.argv)
        Principal = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(Principal)
        Principal.show()
        sys.exit(app.exec_())

