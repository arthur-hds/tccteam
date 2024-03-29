#ONETICK POPUP ADD MENSAGEM

import os
from getVcf import returnVcf
import icons.imagesQt
from PyQt5 import QtCore, QtGui, QtWidgets
import sys, sqlite3
from PyQt5.QtCore import *
from datetime import date
import arrow
from bibliotecas import atualizarDados, resetarRotinas, extrairMensagens, atualizarRotinasInterface, extrairMensagensPersonalizada, extrairHorarios
import ast
from pyautogui import hotkey



class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(991, 759)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        self.InformacoesEPath()
        self.frame_7 = QtWidgets.QFrame(Form)
        self.frame_7.setGeometry(QtCore.QRect(10, 0, 981, 721))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.frame_principal = QtWidgets.QFrame(self.frame_7)
        self.frame_principal.setGeometry(QtCore.QRect(0, 0, 969, 716))
        self.frame_principal.setStyleSheet("background: rgb(145, 70, 255);")
        self.frame_principal.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_principal.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_principal.setLineWidth(1)
        self.frame_principal.setObjectName("frame_principal")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.frame_principal)
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.frame_esquerda_3 = QtWidgets.QFrame(self.frame_principal)
        self.frame_esquerda_3.setEnabled(True)
        self.frame_esquerda_3.setStyleSheet("QFrame{\n"
"    \n"
"    background-color: rgb(241, 231, 255);\n"
"}\n"
"QPushButton{\n"
"    \n"
"    background-color: rgb(218, 209, 230);\n"
"    border-top-right-radius:20px;\n"
"    border-top-left-radius:30px;\n"
"    border-bottom-left-radius: 30px;\n"
"    \n"
"    font:87 15pt \"Arial Black\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(215, 135, 255);\n"
"borderr-radius: 20px rgb(70, 70, 70);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(250, 230, 0);\n"
"border-radius: 20px rgb(255, 165, 24);\n"
"color: rgb(35, 35, 35);\n"
"}")
        self.frame_esquerda_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_esquerda_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_esquerda_3.setLineWidth(1)
        self.frame_esquerda_3.setObjectName("frame_esquerda_3")
        self.label_50 = QtWidgets.QLabel(self.frame_esquerda_3)
        self.label_50.setGeometry(QtCore.QRect(32, 100, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_50.setFont(font)
        self.label_50.setStyleSheet("font: 11pt \"Franklin Gothic Medium\";\n"
"color: rgb(0,0,0);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"\n")
        self.label_50.setObjectName("label_50")
        self.label_51 = QtWidgets.QLabel(self.frame_esquerda_3)
        self.label_51.setGeometry(QtCore.QRect(30, 350, 101, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_51.setFont(font)
        self.label_51.setStyleSheet("font: 11pt \"Franklin Gothic Medium\";\n"
"color: rgb(0,0,0);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_51.setObjectName("label_51")
        self.label_52 = QtWidgets.QLabel(self.frame_esquerda_3)
        self.label_52.setGeometry(QtCore.QRect(45, 590, 71, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_52.setFont(font)
        self.label_52.setStyleSheet("font: 11pt \"Franklin Gothic Medium\";\n"
"color: rgb(0,0,0);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_52.setObjectName("label_52")
        self.barraMomento_3 = QtWidgets.QProgressBar(self.frame_esquerda_3)
        self.barraMomento_3.setGeometry(QtCore.QRect(170, 0, 31, 721))
        self.barraMomento_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.barraMomento_3.setStyleSheet("QProgressBar::chunk {\n"
"    background-color: rgb(160, 64, 255);\n"
"    margin: 0.5px;\n"
"}")
        self.barraMomento_3.setProperty("value", 35)
        self.barraMomento_3.setTextVisible(False)
        self.barraMomento_3.setOrientation(QtCore.Qt.Vertical)
        self.barraMomento_3.setInvertedAppearance(True)
        self.barraMomento_3.setObjectName("barraMomento_3")
        self.horizontalLayout_19.addWidget(self.frame_esquerda_3)
        self.frame_conteudo_3 = QtWidgets.QFrame(self.frame_principal)
        self.frame_conteudo_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_conteudo_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_conteudo_3.setObjectName("frame_conteudo_3")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_conteudo_3)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.frame_14 = QtWidgets.QFrame(self.frame_conteudo_3)
        self.frame_14.setStyleSheet("")
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.widget_20 = QtWidgets.QWidget(self.frame_14)
        self.widget_20.setGeometry(QtCore.QRect(0, 0, 771, 81))
        self.widget_20.setStyleSheet("QWidget{\n"
"background-color: rgb(145, 70, 255);\n"
"}\n"
"QWidget{\n"
"    border-top-right-radius:40%\n"
"}")
        self.widget_20.setObjectName("widget_20")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.widget_20)
        self.horizontalLayout_20.setContentsMargins(15, 0, 0, 0)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_53 = QtWidgets.QLabel(self.widget_20)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_53.setFont(font)
        self.label_53.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_53.setObjectName("label_53")
        self.horizontalLayout_20.addWidget(self.label_53)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem)
        self.botaoFechar_3 = QtWidgets.QPushButton(self.widget_20)
        self.botaoFechar_3.setMinimumSize(QtCore.QSize(50, 0))
        self.botaoFechar_3.clicked.connect(self.fechar)
        self.botaoFechar_3.setCursor(Qt.PointingHandCursor)
        self.botaoFechar_3.setStyleSheet("QPushButton{\n"
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
        self.botaoFechar_3.setObjectName("botaoFechar_3")
        self.horizontalLayout_20.addWidget(self.botaoFechar_3)
        self.verticalLayout_14.addWidget(self.frame_14)
        self.frame_15 = QtWidgets.QFrame(self.frame_conteudo_3)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame_15)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.stackedWidget_3 = QtWidgets.QStackedWidget(self.frame_15)
        self.stackedWidget_3.setStyleSheet("QWidget{\n"
"    background-color: rgb(66, 59, 117)\n"
"\n"
"}\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"    border: 3px solid rgb(52, 59, 72);    \n"
"}\n"
"")
        self.stackedWidget_3.setObjectName("stackedWidget_3")
        self.page_9 = QtWidgets.QWidget()
        self.page_9.setObjectName("page_9")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.page_9)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.widget_21 = QtWidgets.QWidget(self.page_9)
        self.widget_21.setStyleSheet("QWidget{\n"
"background-color: rgb(145, 70, 255);\n"
"}\n"
"QWidget{\n"
"    border-bottom-right-radius:40%\n"
"}")
        self.widget_21.setObjectName("widget_21")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.widget_21)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_54 = QtWidgets.QLabel(self.widget_21)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_54.setFont(font)
        self.label_54.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_54.setAlignment(QtCore.Qt.AlignCenter)
        self.label_54.setObjectName("label_54")
        self.horizontalLayout_21.addWidget(self.label_54)
        self.verticalLayout_16.addWidget(self.widget_21)
        self.frame_16 = QtWidgets.QFrame(self.page_9)
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.label_55 = QtWidgets.QLabel(self.frame_16)
        self.label_55.setGeometry(QtCore.QRect(64, 40, 133, 49))
        self.label_55.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_55.setObjectName("label_55")
        self.caixaMensagens_3 = QtWidgets.QPlainTextEdit(self.frame_16)
        self.caixaMensagens_3.setGeometry(QtCore.QRect(60, 120, 561, 101))
        self.caixaMensagens_3.setMinimumSize(QtCore.QSize(350, 0))
        self.caixaMensagens_3.textChanged.connect(self.selecionarVariaveis)
        self.caixaMensagens_3.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"border:none;\n"
"color: rgb(255, 255, 255);\n"
"border-bottom:3px solid rgb(250, 250,250);\n"
"border-radius:5%;\n"
"padding-bottom:7px;\n"
"letter-spacing: 1px;\n"
"line-height: 1.1;\n")
        self.caixaMensagens_3.setObjectName("caixaMensagens_3")
        self.label_56 = QtWidgets.QLabel(self.frame_16)
        self.label_56.setGeometry(QtCore.QRect(70, 290, 231, 49))
        self.label_56.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_56.setObjectName("label_56")
        self.label_57 = QtWidgets.QLabel(self.frame_16)
        self.label_57.setGeometry(QtCore.QRect(70, 480, 371, 49))
        self.label_57.setStyleSheet("font: 7pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_57.setObjectName("label_57")
        self.listaMensagensSalvas_3 = QtWidgets.QListWidget(self.frame_16)
        self.listaMensagensSalvas_3.setGeometry(QtCore.QRect(70, 330, 561, 151))

        self.listaMensagensSalvas_3.clicked.connect(self.mostrarBotoesMensagens)
        self.listaMensagensSalvas_3.setStyleSheet("QListWidget\n"
"{\n"
"border : 3px solid rgb(255,255,255);\n"
"border-radius:12%;\n"
"color:white;\n"
"padding:10px 20px 20px;\n"
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
        self.listaMensagensSalvas_3.setObjectName("listaMensagensSalvas_3")
        self.botaoAddVariaveis_3 = QtWidgets.QPushButton(self.frame_16)
        self.botaoAddVariaveis_3.setGeometry(QtCore.QRect(60, 240, 121, 21))
        self.botaoAddVariaveis_3.clicked.connect(self.abrirPopupVariavel)
        self.botaoAddVariaveis_3.setCursor(Qt.PointingHandCursor)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(6)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.botaoAddVariaveis_3.setFont(font)
        self.botaoAddVariaveis_3.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(145, 70, 255);\n"
"    border-radius:10px;\n"
"    \n"
"    font:87 6pt \"Arial Black\";\n"
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
        self.botaoAddVariaveis_3.setObjectName("botaoAddVariaveis_3")
        self.botaoSalvar_3 = QtWidgets.QPushButton(self.frame_16)
        self.botaoSalvar_3.setGeometry(QtCore.QRect(630, 120, 111, 41))
        self.botaoSalvar_3.clicked.connect(self.salvar_msg)
        self.botaoSalvar_3.setCursor(Qt.PointingHandCursor)
        self.botaoSalvar_3.setStyleSheet("QPushButton{\n"
"    \n"
"    \n"
"    image: url(:/imagemAlerta/24x24/cil-paper-plane.png);\n"
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
        self.botaoSalvar_3.setText("")
        self.botaoSalvar_3.setObjectName("botaoSalvar_3")
        self.botaoAvan1_3 = QtWidgets.QPushButton(self.frame_16)
        self.botaoAvan1_3.setGeometry(QtCore.QRect(710, 510, 31, 31))
        self.botaoAvan1_3.clicked.connect(self.avancar)
        self.botaoAvan1_3.setCursor(Qt.PointingHandCursor)

        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.botaoAvan1_3.setFont(font)
        self.botaoAvan1_3.setStyleSheet("QPushButton{\n"
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
        self.botaoAvan1_3.setObjectName("botaoAvan1_3")
        self.listaVariaveis_3 = QtWidgets.QListWidget(self.frame_16)
        self.listaVariaveis_3.setGeometry(QtCore.QRect(200, 222, 331, 61))
        self.listaVariaveis_3.setVisible(False)
        self.listaVariaveis_3.doubleClicked.connect(self.cliqueDuploVariavel)
        self.listaVariaveis_3.setStyleSheet("QListWidget\n"
"{\n"
"background-color: rgb(58, 58, 58);\n"
"border-bottom: 3px solid rgb(255,255,255);\n"
"border-radius:3px;\n"
"color:white;\n"
"font: 87 8pt \"Arial Black\";\n"
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
        self.listaVariaveis_3.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.listaVariaveis_3.setObjectName("listaVariaveis_3")
        item = QtWidgets.QListWidgetItem()
        self.listaVariaveis_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listaVariaveis_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listaVariaveis_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listaVariaveis_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listaVariaveis_3.addItem(item)
        self.widgetAddVariaveis = QtWidgets.QWidget(self.frame_16)
        self.widgetAddVariaveis.setGeometry(QtCore.QRect(190, 240, 401, 71))
        self.widgetAddVariaveis.setVisible(False)
        self.widgetAddVariaveis.setStyleSheet("background-color: rgb(145, 70, 255);\n"
"border-radius:10%\n"
"")
        self.widgetAddVariaveis.setObjectName("widgetAddVariaveis")
        self.label_33 = QtWidgets.QLabel(self.widgetAddVariaveis)
        self.label_33.setGeometry(QtCore.QRect(20, -3, 64, 49))
        self.label_33.setStyleSheet("font: 7pt \"MS Shell Dlg 2\";\n"
"color: rgb(255,255,255);")
        self.label_33.setObjectName("label_33")
        self.caixaNomeVariavel = QtWidgets.QLineEdit(self.widgetAddVariaveis)
        self.caixaNomeVariavel.setGeometry(QtCore.QRect(64, 12, 111, 21))
        self.caixaNomeVariavel.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"font: 7pt \"MS Shell Dlg 2\";\n"
"border:none;\n"
"color: rgb(255, 255, 255);\n"
"border-bottom:3px solid rgb(250, 250,250);\n"
"border-radius:5%;\n"
"padding-bottom:7px;")
        self.caixaNomeVariavel.setText("")
        self.caixaNomeVariavel.setObjectName("caixaNomeVariavel")
        self.botaoAddVariavel = QtWidgets.QPushButton(self.widgetAddVariaveis)
        self.botaoAddVariavel.setGeometry(QtCore.QRect(140, 40, 131, 21))
        self.botaoAddVariavel.clicked.connect(self.salvarVariavel)
        self.botaoAddVariavel.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:10px;\n"
"    padding: 5px;\n"
"    color:white;\n"
"    font:87 6pt \"Arial Black\";\n"
"    color: rgb(145, 70, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(232, 232, 232);\n"
"borderr-radius: 10px rgb(70, 70, 70);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(145, 70, 255);\n"
"color: (145, 70, 255);\n"
"}")
        self.botaoAddVariavel.setObjectName("botaoAddVariavel")
        self.botaoFecharVariaveis = QtWidgets.QPushButton(self.widgetAddVariaveis)
        self.botaoFecharVariaveis.setGeometry(QtCore.QRect(370, 10, 21, 21))
        self.botaoFecharVariaveis.clicked.connect(self.abrirPopupVariavel)
        self.botaoFecharVariaveis.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:10px;\n"
"    padding: 5px;\n"
"    color:white;\n"
"    font:87 6pt \"Arial Black\";\n"
"    color: rgb(145, 70, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(232, 232, 232);\n"
"borderr-radius: 10px rgb(70, 70, 70);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(145, 70, 255);\n"
"color: (145, 70, 255);\n"
"}")
        self.botaoFecharVariaveis.setObjectName("botaoFecharVariaveis")
        self.label_34 = QtWidgets.QLabel(self.widgetAddVariaveis)
        self.label_34.setGeometry(QtCore.QRect(184, 10, 64, 21))
        self.label_34.setStyleSheet("font: 7pt \"MS Shell Dlg 2\";\n"
"color: rgb(255,255,255);")
        self.label_34.setObjectName("label_34")
        self.caixaConteudoVariavel = QtWidgets.QLineEdit(self.widgetAddVariaveis)
        self.caixaConteudoVariavel.setGeometry(QtCore.QRect(250, 12, 111, 21))
        self.caixaConteudoVariavel.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"font: 7pt \"MS Shell Dlg 2\";\n"
"border:none;\n"
"color: rgb(255, 255, 255);\n"
"border-bottom:3px solid rgb(250, 250,250);\n"
"border-radius:5%;\n"
"padding-bottom:7px;")
        self.caixaConteudoVariavel.setText("")
        self.caixaConteudoVariavel.setObjectName("caixaConteudoVariavel")
        self.botaoMensagemPraCima = QtWidgets.QPushButton(self.frame_16)
        self.botaoMensagemPraCima.setGeometry(QtCore.QRect(650, 350, 31, 41))
        self.botaoMensagemPraCima.setVisible(False)
        self.botaoMensagemPraCima.clicked.connect(self.moverItemPraCimaMensagens)
        self.botaoMensagemPraCima.setCursor(Qt.PointingHandCursor)
        self.botaoMensagemPraCima.setStyleSheet("QPushButton{\n"
"    background-color: rgb(145, 70, 255);\n"
"    \n"
"    image: url(:/imagemAlerta/24x24/cil-arrow-top.png);\n"
"    color:white;\n"
"    font:87 8pt \"Arial Black\";\n"
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
        self.botaoMensagemPraCima.setText("")
        self.botaoMensagemPraCima.setObjectName("botaoMensagemPraCima")
        self.botaoMensagemPraBaixo = QtWidgets.QPushButton(self.frame_16)
        self.botaoMensagemPraBaixo.setGeometry(QtCore.QRect(650, 413, 31, 41))
        self.botaoMensagemPraBaixo.setVisible(False)
        self.botaoMensagemPraBaixo.clicked.connect(self.moverItemPraBaixoMensagens)
        self.botaoMensagemPraBaixo.setCursor(Qt.PointingHandCursor)
        self.botaoMensagemPraBaixo.setStyleSheet("QPushButton{\n"
"    background-color: rgb(145, 70, 255);\n"
"    \n"
"    \n"
"    image: url(:/imagemAlerta/24x24/cil-arrow-bottom.png);\n"
"    color:white;\n"
"    font:87 8pt \"Arial Black\";\n"
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
        self.botaoMensagemPraBaixo.setText("")
        self.botaoMensagemPraBaixo.setObjectName("botaoMensagemPraBaixo")
        self.botaoMensagemApagar = QtWidgets.QPushButton(self.frame_16)
        self.botaoMensagemApagar.setVisible(False)
        self.botaoMensagemApagar.setGeometry(QtCore.QRect(693, 380, 41, 41))
        self.botaoMensagemApagar.clicked.connect(self.eliminarItemListaMensagens)
        self.botaoMensagemApagar.setCursor(Qt.PointingHandCursor)
        self.botaoMensagemApagar.setStyleSheet("QPushButton{\n"
"    background-color: rgb(145, 70, 255);\n"
"    \n"
"    \n"
"    image: url(:/imagemAlerta/24x24/cil-x.png);\n"
"    color:white;\n"
"    font:87 8pt \"Arial Black\";\n"
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
        self.botaoMensagemApagar.setText("")
        self.botaoMensagemApagar.setObjectName("botaoMensagemApagar")
        self.botaoAddConteudo_3 = QtWidgets.QPushButton(self.frame_16)
        self.botaoAddConteudo_3.setGeometry(QtCore.QRect(630, 170, 111, 41))
        self.botaoAddConteudo_3.clicked.connect(self.browseFileImage)
        self.botaoAddConteudo_3.setCursor(Qt.PointingHandCursor)
        self.botaoAddConteudo_3.setStyleSheet("QPushButton{\n"
"    background-color: rgb(145, 70, 255);\n"
"    \n"
"    \n"
"    \n"
"    image: url(:/imagemAlerta/24x24/cil-link-alt.png);\n"
"    color:white;\n"
"    font:87 8pt \"Arial Black\";\n"
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
        self.botaoAddConteudo_3.setText("")
        self.botaoAddConteudo_3.setObjectName("botaoAddConteudo_3")
        self.botaoInfo_4 = QtWidgets.QPushButton(self.frame_16)
        self.botaoInfo_4.setEnabled(False)
        self.botaoInfo_4.setGeometry(QtCore.QRect(15, 152, 31, 31))
        self.botaoInfo_4.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(161, 161, 161);\n"
"    border-radius:15px;\n"
"    \n"
"    padding: 5px;\n"
"    color:white;\n"
"    font:87 11pt \"Arial Black\";\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.botaoInfo_4.setObjectName("botaoInfo_4")
        self.verticalLayout_16.addWidget(self.frame_16)
        self.verticalLayout_16.setStretch(0, 1)
        self.verticalLayout_16.setStretch(1, 8)
        self.stackedWidget_3.addWidget(self.page_9)
        self.page_10 = QtWidgets.QWidget()
        self.page_10.setObjectName("page_10")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.page_10)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.widget_22 = QtWidgets.QWidget(self.page_10)
        self.widget_22.setStyleSheet("QWidget{\n"
"background-color: rgb(145, 70, 255);\n"
"}\n"
"QWidget{\n"
"    border-bottom-right-radius:40%\n"
"}")
        self.widget_22.setObjectName("widget_22")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.widget_22)
        self.horizontalLayout_22.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.label_58 = QtWidgets.QLabel(self.widget_22)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_58.setFont(font)
        self.label_58.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_58.setAlignment(QtCore.Qt.AlignCenter)
        self.label_58.setObjectName("label_58")
        self.horizontalLayout_22.addWidget(self.label_58)
        self.verticalLayout_17.addWidget(self.widget_22)
        self.frame_17 = QtWidgets.QFrame(self.page_10)
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.radioContato_3 = QtWidgets.QRadioButton(self.frame_17)
        self.radioContato_3.setChecked(True)
        self.radioContato_3.setGeometry(QtCore.QRect(50, 89, 95, 21))
        self.radioContato_3.clicked.connect(self.checkContato)
        self.radioContato_3.setCursor(Qt.PointingHandCursor)
        self.radioContato_3.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.radioContato_3.setObjectName("radioContato_3")
        self.botaoAddContato_3 = QtWidgets.QPushButton(self.frame_17)
        self.botaoAddContato_3.setGeometry(QtCore.QRect(50, 360, 131, 31))
        self.botaoAddContato_3.clicked.connect(self.abrirPopupContato)
        self.botaoAddContato_3.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(145, 70, 255);\n"
"    border-radius:10px;\n"
"    padding: 5px;\n"
"    color:white;\n"
"    font:87 8pt \"Arial Black\";\n"
"    font:87 6pt \"Arial Black\";\n"
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
        self.botaoAddContato_3.setObjectName("botaoAddContato_3")
        self.radioGrupo_3 = QtWidgets.QRadioButton(self.frame_17)
        self.radioGrupo_3.setGeometry(QtCore.QRect(170, 89, 95, 21))
        self.radioGrupo_3.setCursor(Qt.PointingHandCursor)
        self.radioGrupo_3.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.radioGrupo_3.setObjectName("radioGrupo_3")
        self.radioGrupo_3.clicked.connect(self.checkGrupo)
        self.label_60 = QtWidgets.QLabel(self.frame_17)
        self.label_60.setGeometry(QtCore.QRect(50, 49, 441, 29))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_60.setFont(font)
        self.label_60.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(250, 250, 250);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_60.setObjectName("label_60")
        self.listaContatos_3 = QtWidgets.QListWidget(self.frame_17)
        self.listaContatos_3.setGeometry(QtCore.QRect(50, 130, 651, 221))
        self.listaContatos_3.clicked.connect(self.salvarRemetentes)
        self.listaContatos_3.setCursor(Qt.PointingHandCursor)
        self.listaContatos_3.setStyleSheet("QListWidget\n"
"{\n"
"border : 3px solid rgb(255,255,255);\n"
"border-radius:12%;\n"
"color:white;\n"
"padding:10px 20px 20px;\n"                                           
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
        self.listaContatos_3.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.listaContatos_3.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listaContatos_3.setObjectName("listaContatos_3")
        self.__preencherContatos()
        self.listaRemetentesSelecionados = QtWidgets.QListWidget(self.frame_17)
        self.listaRemetentesSelecionados.setGeometry(QtCore.QRect(50, 400, 601, 101))
        self.listaRemetentesSelecionados.clicked.connect(self.mostrarBotoesRemetentes)
        self.listaRemetentesSelecionados.setCursor(Qt.PointingHandCursor)
        self.listaRemetentesSelecionados.setStyleSheet("QListWidget\n"
"{\n"
"border : 3px solid rgb(255,255,255);\n"
"border-radius:12%;\n"
"color:white;\n"
"padding:10px 20px 20px;\n"
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
        self.listaRemetentesSelecionados.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.listaRemetentesSelecionados.setObjectName("listaRemetentesSelecionados")
        self.botaoAvan2_3 = QtWidgets.QPushButton(self.frame_17)
        self.botaoAvan2_3.setGeometry(QtCore.QRect(710, 510, 31, 31))
        self.botaoAvan2_3.clicked.connect(self.avancar)
        self.botaoAvan2_3.setCursor(Qt.PointingHandCursor)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.botaoAvan2_3.setFont(font)
        self.botaoAvan2_3.setStyleSheet("QPushButton{\n"
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
        self.botaoAvan2_3.setObjectName("botaoAvan2_3")
        self.botaoRetro1_3 = QtWidgets.QPushButton(self.frame_17)
        self.botaoRetro1_3.setGeometry(QtCore.QRect(30, 510, 31, 31))
        self.botaoRetro1_3.clicked.connect(self.voltar)
        self.botaoRetro1_3.setCursor(Qt.PointingHandCursor)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.botaoRetro1_3.setFont(font)
        self.botaoRetro1_3.setStyleSheet("QPushButton{\n"
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
        self.botaoRetro1_3.setObjectName("botaoRetro1_3")
        self.botaoInfo_2 = QtWidgets.QPushButton(self.frame_17)
        self.botaoInfo_2.setEnabled(False)
        self.botaoInfo_2.setGeometry(QtCore.QRect(10, 220, 31, 31))
        self.botaoInfo_2.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(161, 161, 161);\n"
"    border-radius:15px;\n"
"    \n"
"    padding: 5px;\n"
"    color:white;\n"
"    font:87 11pt \"Arial Black\";\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.botaoInfo_2.setObjectName("botaoInfo_2")
        self.botaoInfo_3 = QtWidgets.QPushButton(self.frame_17)
        self.botaoInfo_3.setEnabled(False)
        self.botaoInfo_3.setGeometry(QtCore.QRect(10, 434, 31, 31))
        self.botaoInfo_3.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(161, 161, 161);\n"
"    border-radius:15px;\n"
"    \n"
"    padding: 5px;\n"
"    color:white;\n"
"    font:87 11pt \"Arial Black\";\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.botaoInfo_3.setObjectName("botaoInfo_3")
        self.botaoAddGrupo_4 = QtWidgets.QPushButton(self.frame_17)
        self.botaoAddGrupo_4.setGeometry(QtCore.QRect(50, 360, 131, 31))
        self.botaoAddGrupo_4.setVisible(False)
        self.botaoAddGrupo_4.clicked.connect(self.abrirPopupGrupo)
        self.botaoAddGrupo_4.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(145, 70, 255);\n"
"    border-radius:10px;\n"
"    padding: 5px;\n"
"    color:white;\n"
"    font:87 8pt \"Arial Black\";\n"
"    font:87 6pt \"Arial Black\";\n"
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
        self.botaoAddGrupo_4.setObjectName("botaoAddGrupo_4")
        self.botaoInfo_1 = QtWidgets.QPushButton(self.frame_17)
        self.botaoInfo_1.setEnabled(False)
        self.botaoInfo_1.setGeometry(QtCore.QRect(300, 49, 31, 31))
        self.botaoInfo_1.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(161, 161, 161);\n"
"    border-radius:15px;\n"
"    \n"
"    padding: 5px;\n"
"    color:white;\n"
"    font:87 11pt \"Arial Black\";\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.botaoInfo_1.setObjectName("botaoInfo_1")
        self.widgetAddContato = QtWidgets.QWidget(self.frame_17)
        self.widgetAddContato.setGeometry(QtCore.QRect(190, 370, 481, 71))
        self.widgetAddContato.setVisible(False)
        self.widgetAddContato.setStyleSheet("background-color: rgb(145, 70, 255);\n"
"border-radius:10%\n"
"")
        self.widgetAddContato.setObjectName("widgetAddContato")
        self.label_29 = QtWidgets.QLabel(self.widgetAddContato)
        self.label_29.setGeometry(QtCore.QRect(16, -3, 64, 49))
        self.label_29.setStyleSheet("font: 7pt \"MS Shell Dlg 2\";\n"
"color: rgb(255,255,255);")
        self.label_29.setObjectName("label_29")
        self.caixaNomeDoContatoPersonalizado_4 = QtWidgets.QLineEdit(self.widgetAddContato)
        self.caixaNomeDoContatoPersonalizado_4.setGeometry(QtCore.QRect(70, 12, 161, 21))
        self.caixaNomeDoContatoPersonalizado_4.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"font: 7pt \"MS Shell Dlg 2\";\n"
"border:none;\n"
"color: rgb(255, 255, 255);\n"
"border-bottom:3px solid rgb(250, 250,250);\n"
"border-radius:5%;\n"
"padding-bottom:7px;")
        self.caixaNomeDoContatoPersonalizado_4.setObjectName("caixaNomeDoContatoPersonalizado_4")
        self.label_31 = QtWidgets.QLabel(self.widgetAddContato)
        self.label_31.setGeometry(QtCore.QRect(240, -3, 64, 49))
        self.label_31.setStyleSheet("font: 7pt \"MS Shell Dlg 2\";\n"
"color: rgb(255,255,255);")
        self.label_31.setObjectName("label_31")
        self.caixaNomePersonalizado_4 = QtWidgets.QLineEdit(self.widgetAddContato)
        self.caixaNomePersonalizado_4.setGeometry(QtCore.QRect(290, 12, 161, 21))
        self.caixaNomePersonalizado_4.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"font: 7pt \"MS Shell Dlg 2\";\n"
"border:none;\n"
"color: rgb(255, 255, 255);\n"
"border-bottom:3px solid rgb(250, 250,250);\n"
"border-radius:5%;\n"
"padding-bottom:7px;\n"
"letter-spacing: 1px;\n"
"line-height: 1.1;\n"
"word-spacing: 10px;")
        self.caixaNomePersonalizado_4.setText("")
        self.caixaNomePersonalizado_4.setObjectName("caixaNomePersonalizado_4")
        self.botaoAddContato = QtWidgets.QPushButton(self.widgetAddContato)
        self.botaoAddContato.setGeometry(QtCore.QRect(178, 40, 131, 21))
        self.botaoAddContato.clicked.connect(self.criarContato)
        self.botaoAddContato.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:10px;\n"
"    padding: 5px;\n"
"    color:white;\n"
"    font:87 6pt \"Arial Black\";\n"
"    color: rgb(145, 70, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(232, 232, 232);\n"
"borderr-radius: 10px rgb(70, 70, 70);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(145, 70, 255);\n"
"color: (145, 70, 255);\n"
"}")
        self.botaoAddContato.setObjectName("botaoAddContato")
        self.botaoFecharAddContato = QtWidgets.QPushButton(self.widgetAddContato)
        self.botaoFecharAddContato.setGeometry(QtCore.QRect(450, 5, 21, 21))
        self.botaoFecharAddContato.clicked.connect(self.abrirPopupContato)
        self.botaoFecharAddContato.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:10px;\n"
"    padding: 5px;\n"
"    color:white;\n"
"    font:87 6pt \"Arial Black\";\n"
"    color: rgb(145, 70, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(232, 232, 232);\n"
"borderr-radius: 10px rgb(70, 70, 70);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(145, 70, 255);\n"
"color: (145, 70, 255);\n"
"}")
        self.botaoFecharAddContato.setObjectName("botaoFecharAddContato")
        self.botaoImportarVcf = QtWidgets.QPushButton(self.widgetAddContato)
        self.botaoImportarVcf.setGeometry(QtCore.QRect(370, 40, 81, 21))
        self.botaoImportarVcf.clicked.connect(self.__browseFileVcf)
        self.botaoImportarVcf.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:10px;\n"
"    padding: 5px;\n"
"    color:white;\n"
"    font:87 6pt \"Arial Black\";\n"
"    color: rgb(145, 70, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(232, 232, 232);\n"
"borderr-radius: 10px rgb(70, 70, 70);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(145, 70, 255);\n"
"color: (145, 70, 255);\n"
"}")
        self.botaoImportarVcf.setObjectName("botaoImportarVcf")
        self.widgetAddGrupo = QtWidgets.QWidget(self.frame_17)
        self.widgetAddGrupo.setGeometry(QtCore.QRect(190, 370, 261, 71))
        self.widgetAddGrupo.setVisible(False)
        self.widgetAddGrupo.setStyleSheet("background-color: rgb(145, 70, 255);\n"
"border-radius:10%\n"
"")
        self.widgetAddGrupo.setObjectName("widgetAddGrupo")
        self.label_32 = QtWidgets.QLabel(self.widgetAddGrupo)
        self.label_32.setGeometry(QtCore.QRect(20, -3, 64, 49))
        self.label_32.setStyleSheet("font: 7pt \"MS Shell Dlg 2\";\n"
"color: rgb(255,255,255);")
        self.label_32.setObjectName("label_32")
        self.caixaNumeroPersonalizado_5 = QtWidgets.QLineEdit(self.widgetAddGrupo)
        self.caixaNumeroPersonalizado_5.setGeometry(QtCore.QRect(64, 12, 161, 21))
        self.caixaNumeroPersonalizado_5.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"font: 7pt \"MS Shell Dlg 2\";\n"
"border:none;\n"
"color: rgb(255, 255, 255);\n"
"border-bottom:3px solid rgb(250, 250,250);\n"
"border-radius:5%;\n"
"padding-bottom:7px;\n"
"letter-spacing: 1px;\n"
"line-height: 1.1;\n"
"word-spacing: 10px;")
        self.caixaNumeroPersonalizado_5.setText("")
        self.caixaNumeroPersonalizado_5.setObjectName("caixaNumeroPersonalizado_5")
        self.botaoAddGrupo = QtWidgets.QPushButton(self.widgetAddGrupo)
        self.botaoAddGrupo.setGeometry(QtCore.QRect(67, 40, 131, 21))
        self.botaoAddGrupo.clicked.connect(self.criarGrupo)
        self.botaoAddGrupo.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:10px;\n"
"    padding: 5px;\n"
"    color:white;\n"
"    font:87 6pt \"Arial Black\";\n"
"    color: rgb(145, 70, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(232, 232, 232);\n"
"borderr-radius: 10px rgb(70, 70, 70);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(145, 70, 255);\n"
"color: (145, 70, 255);\n"
"}")
        self.botaoAddGrupo.setObjectName("botaoAddGrupo")
        self.botaoFecharAddGrupo_2 = QtWidgets.QPushButton(self.widgetAddGrupo)
        self.botaoFecharAddGrupo_2.setGeometry(QtCore.QRect(230, 6, 21, 21))
        self.botaoFecharAddGrupo_2.clicked.connect(self.abrirPopupGrupo)
        self.botaoFecharAddGrupo_2.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:10px;\n"
"    padding: 5px;\n"
"    color:white;\n"
"    font:87 6pt \"Arial Black\";\n"
"    color: rgb(145, 70, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(232, 232, 232);\n"
"borderr-radius: 10px rgb(70, 70, 70);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(145, 70, 255);\n"
"color: (145, 70, 255);\n"
"}")
        self.botaoFecharAddGrupo_2.setObjectName("botaoFecharAddGrupo_2")
        self.botaoRemetentePraBaixo_2 = QtWidgets.QPushButton(self.frame_17)
        self.botaoRemetentePraBaixo_2.setGeometry(QtCore.QRect(667, 453, 31, 41))
        self.botaoRemetentePraBaixo_2.setVisible(False)
        self.botaoRemetentePraBaixo_2.clicked.connect(self.moverItemPraBaixoRemetentes)
        self.botaoRemetentePraBaixo_2.setCursor(Qt.PointingHandCursor)
        self.botaoRemetentePraBaixo_2.setStyleSheet("QPushButton{\n"
"    background-color: rgb(145, 70, 255);\n"
"    \n"
"    \n"
"    image: url(:/imagemAlerta/24x24/cil-arrow-bottom.png);\n"
"    color:white;\n"
"    font:87 8pt \"Arial Black\";\n"
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
        self.botaoRemetentePraBaixo_2.setText("")
        self.botaoRemetentePraBaixo_2.setObjectName("botaoRemetentePraBaixo_2")
        self.botaoRemetentePraCima_2 = QtWidgets.QPushButton(self.frame_17)
        self.botaoRemetentePraCima_2.setGeometry(QtCore.QRect(667, 403, 31, 41))
        self.botaoRemetentePraCima_2.setVisible(False)
        self.botaoRemetentePraCima_2.clicked.connect(self.moverItemPraCimaRemetentes)
        self.botaoRemetentePraCima_2.setCursor(Qt.PointingHandCursor)
        self.botaoRemetentePraCima_2.setStyleSheet("QPushButton{\n"
"    background-color: rgb(145, 70, 255);\n"
"    \n"
"    image: url(:/imagemAlerta/24x24/cil-arrow-top.png);\n"
"    color:white;\n"
"    font:87 8pt \"Arial Black\";\n"
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
        self.botaoRemetentePraCima_2.setText("")
        self.botaoRemetentePraCima_2.setObjectName("botaoRemetentePraCima_2")
        self.caixaFiltrarRemetentes = QtWidgets.QLineEdit(self.frame_17)
        self.caixaFiltrarRemetentes.setGeometry(QtCore.QRect(430, 90, 181, 31))
        self.caixaFiltrarRemetentes.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"font: 9pt \"MS Shell Dlg 2\";\n"
"border:none;\n"
"color: rgb(255, 255, 255);\n"
"border-bottom:3px solid rgb(250, 250,250);\n"
"border-radius:5%;\n"
"padding-bottom:7px;\n"
"letter-spacing: 1px;\n"
"line-height: 1.1;\n"
"word-spacing: 10px;")
        self.caixaFiltrarRemetentes.setText("")
        self.caixaFiltrarRemetentes.setObjectName("caixaFiltrarRemetentes")
        self.botaoFiltrar = QtWidgets.QPushButton(self.frame_17)
        self.botaoFiltrar.setGeometry(QtCore.QRect(620, 80, 51, 41))
        self.botaoFiltrar.clicked.connect(self.filtrar)
        self.botaoFiltrar.setCursor(Qt.PointingHandCursor)
        self.botaoFiltrar.setStyleSheet("QPushButton{\n"
"    background-color: rgb(145, 70, 255);\n"
"    \n"
"    \n"
"    padding:10px;\n"
"    image: url(:/imagemAlerta/24x24/iconeLupaQT.png);\n"
"    color:white;\n"
"    font:87 8pt \"Arial Black\";\n"
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
        self.botaoFiltrar.setText("")
        self.botaoFiltrar.setObjectName("botaoFiltrar")
        self.verticalLayout_17.addWidget(self.frame_17)
        self.verticalLayout_17.setStretch(0, 1)
        self.verticalLayout_17.setStretch(1, 8)
        self.stackedWidget_3.addWidget(self.page_10)
        self.page_11 = QtWidgets.QWidget()
        self.page_11.setObjectName("page_11")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.page_11)
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.widget_23 = QtWidgets.QWidget(self.page_11)
        self.widget_23.setStyleSheet("QWidget{\n"
"background-color: rgb(145, 70, 255);\n"
"}\n"
"QWidget{\n"
"    border-bottom-right-radius:40%\n"
"}")
        self.widget_23.setObjectName("widget_23")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.widget_23)
        self.horizontalLayout_23.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.label_63 = QtWidgets.QLabel(self.widget_23)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_63.setFont(font)
        self.label_63.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_63.setAlignment(QtCore.Qt.AlignCenter)
        self.label_63.setObjectName("label_63")
        self.horizontalLayout_23.addWidget(self.label_63)
        self.verticalLayout_18.addWidget(self.widget_23)
        self.frame_18 = QtWidgets.QFrame(self.page_11)
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.label_65 = QtWidgets.QLabel(self.frame_18)
        self.label_65.setGeometry(QtCore.QRect(231, 58, 130, 24))
        self.label_65.setStyleSheet("font:87 10pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);")
        self.label_65.setObjectName("label_65")
        self.label_66 = QtWidgets.QLabel(self.frame_18)
        self.label_66.setGeometry(QtCore.QRect(266, 110, 75, 24))
        self.label_66.setStyleSheet("font:87 10pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);")
        self.label_66.setObjectName("label_66")
        self.comboTipoDeEnvio_3 = QtWidgets.QComboBox(self.frame_18)
        self.comboTipoDeEnvio_3.setGeometry(QtCore.QRect(370, 55, 149, 30))
        self.comboTipoDeEnvio_3.currentIndexChanged.connect(self.habilitarPersonalizadaECalendario)
        self.comboTipoDeEnvio_3.setCursor(Qt.PointingHandCursor)
        self.comboTipoDeEnvio_3.setStyleSheet("QComboBox{\n"
"    background-color: rgb(145, 70, 255);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgba(27, 29, 35, 0);\n"
"    padding: 5px;\n"
"    padding-left: 10px;\n"
"    color:white;\n"
"    font:87 8pt \"Arial Black\";\n"
"}\n"
"QComboBox:hover{\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px; \n"
"    border-left-width: 3px;\n"
"    border-left-color: rgba(39, 44, 54, 150);\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;    \n"
"    background-position: center;\n"
"    background-repeat: no-reperat;\n"
"    color:white;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"    background-color: rgb(27, 29, 35);\n"
"    padding: 10px;\n"
"    selection-background-color: rgb(39, 44, 54);\n"
"    color:white;\n"
"}")
        self.comboTipoDeEnvio_3.setEditable(False)
        self.comboTipoDeEnvio_3.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.comboTipoDeEnvio_3.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.comboTipoDeEnvio_3.setDuplicatesEnabled(False)
        self.comboTipoDeEnvio_3.setFrame(True)
        self.comboTipoDeEnvio_3.setObjectName("comboTipoDeEnvio_3")
        self.comboTipoDeEnvio_3.addItem("")
        self.comboTipoDeEnvio_3.addItem("")
        self.comboTipoDeEnvio_3.addItem("")
        self.comboTipoDeEnvio_3.addItem("")
        self.comboTipoDeEnvio_3.addItem("")
        self.botaoAvan3_3 = QtWidgets.QPushButton(self.frame_18)
        self.botaoAvan3_3.setGeometry(QtCore.QRect(710, 510, 31, 31))
        self.botaoAvan3_3.clicked.connect(self.avancar)
        self.botaoAvan3_3.setCursor(Qt.PointingHandCursor)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.botaoAvan3_3.setFont(font)
        self.botaoAvan3_3.setStyleSheet("QPushButton{\n"
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
        self.botaoAvan3_3.setObjectName("botaoAvan3_3")
        self.botaoRetro2_3 = QtWidgets.QPushButton(self.frame_18)
        self.botaoRetro2_3.setGeometry(QtCore.QRect(30, 510, 31, 31))
        self.botaoRetro2_3.setCursor(Qt.PointingHandCursor)
        self.botaoRetro2_3.clicked.connect(self.voltar)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.botaoRetro2_3.setFont(font)
        self.botaoRetro2_3.setStyleSheet("QPushButton{\n"
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
        self.botaoRetro2_3.setObjectName("botaoRetro2_3")
        self.spinBoxHora = QtWidgets.QSpinBox(self.frame_18)
        self.spinBoxHora.setGeometry(QtCore.QRect(350, 108, 61, 31))
        self.spinBoxHora.setStyleSheet("QSpinBox{\n"
"    background-color: rgb(145, 70, 255);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgba(27, 29, 35, 0);\n"
"    padding: 5px;\n"
"    padding-left: 10px;\n"
"    color:white;\n"
"    font:87 8pt \"Arial Black\";\n"
"}\n"
"QSpinBox:hover{\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QSpinBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px; \n"
"    border-left-width: 3px;\n"
"    border-left-color: rgba(39, 44, 54, 150);\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;    \n"
"    background-position: center;\n"
"    background-repeat: no-reperat;\n"
"    color:white;\n"
" }\n"
"QSpinBox QAbstractItemView {\n"
"    background-color: rgb(27, 29, 35);\n"
"    padding: 10px;\n"
"    selection-background-color: rgb(39, 44, 54);\n"
"    color:white;\n"
"}")
        self.spinBoxHora.setMaximum(23)
        self.spinBoxHora.setObjectName("spinBoxHora")
        self.spinBoxMinuto = QtWidgets.QSpinBox(self.frame_18)
        self.spinBoxMinuto.setGeometry(QtCore.QRect(430, 108, 61, 31))
        self.spinBoxMinuto.setStyleSheet("QSpinBox{\n"
"    background-color: rgb(145, 70, 255);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgba(27, 29, 35, 0);\n"
"    padding: 5px;\n"
"    padding-left: 10px;\n"
"    color:white;\n"
"    font:87 8pt \"Arial Black\";\n"
"}\n"
"QSpinBox:hover{\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QSpinBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px; \n"
"    border-left-width: 3px;\n"
"    border-left-color: rgba(39, 44, 54, 150);\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;    \n"
"    background-position: center;\n"
"    background-repeat: no-reperat;\n"
"    color:white;\n"
" }\n"
"QSpinBox QAbstractItemView {\n"
"    background-color: rgb(27, 29, 35);\n"
"    padding: 10px;\n"
"    selection-background-color: rgb(39, 44, 54);\n"
"    color:white;\n"
"}")
        self.spinBoxMinuto.setMaximum(59)
        self.spinBoxMinuto.setObjectName("spinBoxMinuto")
        self.label_69 = QtWidgets.QLabel(self.frame_18)
        self.label_69.setGeometry(QtCore.QRect(417, 109, 16, 24))
        self.label_69.setStyleSheet("font:87 10pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"background:none;")
        self.label_69.setObjectName("label_69")
        self.stackedWidgetDataEHora = QtWidgets.QStackedWidget(self.frame_18)
        self.stackedWidgetDataEHora.setGeometry(QtCore.QRect(30, 150, 711, 351))
        self.stackedWidgetDataEHora.setObjectName("stackedWidgetDataEHora")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.botaoAdicionarDiaCalendario = QtWidgets.QPushButton(self.page)
        self.botaoAdicionarDiaCalendario.setGeometry(QtCore.QRect(120, 310, 81, 31))
        self.botaoAdicionarDiaCalendario.clicked.connect(self.adicionarDiasCalendario)
        self.botaoAdicionarDiaCalendario.setCursor(Qt.PointingHandCursor)
        self.botaoAdicionarDiaCalendario.setStyleSheet("QPushButton{\n"
"    border: 0px;\n"
"    border-radius:10px;\n"
"    background-color: rgb(145, 70, 255);\n"
"    padding: 5px;\n"
"    color:white;\n"
"    font:87 8pt \"Arial Black\";\n"
"    font:87 6pt \"Arial Black\";\n"
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
        self.botaoAdicionarDiaCalendario.setObjectName("botaoAdicionarDiaCalendario")
        self.listaDiasSelecionados_3 = QtWidgets.QListWidget(self.page)
        self.listaDiasSelecionados_3.setGeometry(QtCore.QRect(370, 50, 341, 251))
        self.listaDiasSelecionados_3.doubleClicked.connect(self.eliminarItemListaCalendario)
        self.listaDiasSelecionados_3.setStyleSheet("QListWidget\n"
"{\n"
"border : 3px solid rgb(255,255,255);\n"
"border-radius:40%;\n"
"border:none;\n"
"color:white;\n"
"padding:10px 20px 20px;\n"
"background-color: rgb(97, 88, 132);\n"
"}\n"
"QListView::item:hover\n"
"{\n"
"background: rgb(166, 104, 197);\n"
"color: white;\n"
"}\n"
"QListView::item:selected\n"
"{\n"
"border : 2px solid rgb(166, 104, 197);\n"
"background:rgb(85, 0, 127)\n"
"}")
        self.listaDiasSelecionados_3.setObjectName("listaDiasSelecionados_3")
        self.label_64 = QtWidgets.QLabel(self.page)
        self.label_64.setGeometry(QtCore.QRect(450, 10, 171, 32))
        self.label_64.setStyleSheet("font:87 10pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"background:None;")
        self.label_64.setObjectName("label_64")
        self.calendario_3 = QtWidgets.QCalendarWidget(self.page)
        self.calendario_3.setGeometry(QtCore.QRect(0, 20, 351, 281))
        self.calendario_3.setDisabled(True)
        self.calendario_3.setMinimumDate(QtCore.QDate(int(date.today().year), int(date.today().month), int(date.today().day)))
        self.calendario_3.setCursor(Qt.PointingHandCursor)
        self.calendario_3.setStyleSheet("QCalendarWidget QToolButton {\n"
"    \n"
"      height: 30px;\n"
"      width: 110px;\n"
"      color: white;\n"
"      font-size: 20px;\n"
"      icon-size: 30px, 30px;\n"
"      background-color:rgb(145, 70, 255)\n"
"  }\n"
"\n"
"  QCalendarWidget QMenu {\n"
"    width: 150px;\n"
"      left: 20px;\n"
"      color: white;\n"
"      font-size: 10px;\n"
"      background-color: rgb(100, 100, 100);\n"
"      \n"
"  }\n"
"\n"
"  QCalendarWidget QSpinBox { \n"
"      width: 150px; \n"
"      font-size:24px; \n"
"      color: white; \n"
" \n"
"  }\n"
"  \n"
"QCalendarWidget QSpinBox::up-button {\n"
" subcontrol-origin: border;  subcontrol-position: top right;  width:65px;\n"
" }\n"
"\n"
"  QCalendarWidget QSpinBox::down-button {\n"
"subcontrol-origin: border; subcontrol-position: bottom right;  width:65px;\n"
"}\n"
"\n"
"  QCalendarWidget QSpinBox::up-arrow {\n"
" width:56px;  height:56px; \n"
"}\n"
"\n"
"  QCalendarWidget QSpinBox::down-arrow {\n"
" width:56px;  height:56px; \n"
"}  \n"
"\n"
"  QCalendarWidget QWidget {\n"
"    alternate-background-color: rgb(128, 128, 128);\n"
"    padding: 5px;\n"
"    padding-left: 10px;\n"
"    color:white;\n"
"    font:87 8pt \"Arial Black\";\n"
" }\n"
"\n"
"  QCalendarWidget QAbstractItemView:enabled \n"
"  {\n"
"      font-size:15px;  \n"
"      color: rgb(0, 0, 0);  \n"
"      background-color: white;  \n"
"      selection-background-color: rgb(64, 64, 64); \n"
"      selection-color: rgb(0, 255, 0); \n"
"  }\n"
"   \n"
"QCalendarWidget QWidget#qt_calendar_navigationbar\n"
"{ \n"
"  background-color:rgb(255, 255, 255)\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView:disabled \n"
"{ \n"
"color: rgb(231, 231, 231); \n"
"}\n"
"\n"
"")
        self.calendario_3.setFirstDayOfWeek(QtCore.Qt.Sunday)
        self.calendario_3.setGridVisible(False)
        self.calendario_3.setSelectionMode(QtWidgets.QCalendarWidget.SingleSelection)
        self.calendario_3.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.NoHorizontalHeader)
        self.calendario_3.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendario_3.setNavigationBarVisible(True)
        self.calendario_3.setDateEditEnabled(True)
        self.calendario_3.setObjectName("calendario_3")
        self.stackedWidgetDataEHora.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.widget_24 = QtWidgets.QWidget(self.page_2)
        self.widget_24.setGeometry(QtCore.QRect(40, 30, 621, 271))
        self.widget_24.setStyleSheet("QWidget{\n"
"    border: 3px solid;\n"
"    border-radius:40%;\n"
"    border-color: rgb(255, 255, 255);\n"
"}")
        self.widget_24.setObjectName("widget_24")
        self.label_67 = QtWidgets.QLabel(self.widget_24)
        self.label_67.setGeometry(QtCore.QRect(230, -10, 141, 31))
        self.label_67.setStyleSheet("font:87 10pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(255, 255, 255);\n"
"border-radius:20%;\n"
"")
        self.label_67.setAlignment(QtCore.Qt.AlignCenter)
        self.label_67.setObjectName("label_67")
        self.label_68 = QtWidgets.QLabel(self.widget_24)
        self.label_68.setGeometry(QtCore.QRect(88, 50, 151, 24))
        self.label_68.setStyleSheet("font:87 10pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"border:none;")
        self.label_68.setObjectName("label_68")
        self.botaoAdicionarDias_3 = QtWidgets.QPushButton(self.widget_24)
        self.botaoAdicionarDias_3.setGeometry(QtCore.QRect(108, 180, 81, 31))
        self.botaoAdicionarDias_3.clicked.connect(self.adicionarDiasPersonalizados)
        self.botaoAdicionarDias_3.setCursor(Qt.PointingHandCursor)
        self.botaoAdicionarDias_3.setStyleSheet("QPushButton{\n"
"    border: 0px;\n"
"    border-radius:10px;\n"
"    background-color: rgb(145, 70, 255);\n"
"    padding: 5px;\n"
"    color:white;\n"
"    font:87 8pt \"Arial Black\";\n"
"    font:87 6pt \"Arial Black\";\n"
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
        self.botaoAdicionarDias_3.setObjectName("botaoAdicionarDias_3")
        self.listaDiasPersonalizado_3 = QtWidgets.QListWidget(self.widget_24)
        self.listaDiasPersonalizado_3.setGeometry(QtCore.QRect(320, 40, 281, 201))
        self.listaDiasPersonalizado_3.doubleClicked.connect(self.eliminarItemListaPersonalizado)
        self.listaDiasPersonalizado_3.setStyleSheet("QListWidget\n"
"{\n"
"border : 3px solid rgb(255,255,255);\n"
"border-radius:40%;\n"
"border:none;\n"
"color:white;\n"
"background-color: rgb(97, 88, 132);\n"
"padding:10px 20px 20px;\n"
"}\n"
"QListView::item:hover\n"
"{\n"
"background: rgb(166, 104, 197);\n"
"color: white;\n"
"}\n"
"QListView::item:selected\n"
"{\n"
"border : 2px solid rgb(166, 104, 197);\n"
"background:rgb(85, 0, 127)\n"
"}")
        self.listaDiasPersonalizado_3.setObjectName("listaDiasPersonalizado_3")
        self.comboDias_3 = QtWidgets.QComboBox(self.widget_24)
        self.comboDias_3.setGeometry(QtCore.QRect(60, 110, 191, 31))
        self.comboDias_3.setCursor(Qt.PointingHandCursor)
        self.comboDias_3.setAcceptDrops(True)
        self.comboDias_3.setStyleSheet("QComboBox{\n"
"    background-color: rgb(145, 70, 255);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgba(27, 29, 35, 0);\n"
"    padding: 5px;\n"
"    padding-left: 10px;\n"
"    color:white;\n"
"    font:87 7pt \"Arial Black\";\n"
"}\n"
"QComboBox:hover{\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px; \n"
"    border-left-width: 3px;\n"
"    border-left-color: rgba(39, 44, 54, 150);\n"
"    border-left-style: solid;\n"
"    background-position: center;\n"
"    background-repeat: no-reperat;\n"
"    color:white;\n"
"\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"    background-color: rgb(27, 29, 35);\n"
"    padding: 10px;\n"
"    selection-background-color: rgb(39, 44, 54);\n"
"    color:white;\n"
"    border:none;\n"
"    border-radius:0px;\n"
"}\n"
"")
        self.comboDias_3.setEditable(False)
        self.comboDias_3.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.comboDias_3.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.comboDias_3.setDuplicatesEnabled(False)
        self.comboDias_3.setFrame(True)
        self.comboDias_3.setObjectName("comboDias_3")
        self.comboDias_3.addItem("")
        self.comboDias_3.addItem("")
        self.comboDias_3.addItem("")
        self.comboDias_3.addItem("")
        self.comboDias_3.addItem("")
        self.comboDias_3.addItem("")
        self.comboDias_3.addItem("")
        self.stackedWidgetDataEHora.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label = QtWidgets.QLabel(self.page_3)
        self.label.setGeometry(QtCore.QRect(200, 40, 321, 171))
        self.label.setStyleSheet("image: url(:/imagemAlerta/24x24/IconeRelogioQT.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.stackedWidgetDataEHora.addWidget(self.page_3)
        self.stackedWidgetDataEHora.raise_()
        self.label_65.raise_()
        self.label_66.raise_()
        self.comboTipoDeEnvio_3.raise_()
        self.botaoAvan3_3.raise_()
        self.botaoRetro2_3.raise_()
        self.spinBoxHora.raise_()
        self.spinBoxMinuto.raise_()
        self.label_69.raise_()
        self.verticalLayout_18.addWidget(self.frame_18)
        self.verticalLayout_18.setStretch(0, 1)
        self.verticalLayout_18.setStretch(1, 8)
        self.stackedWidget_3.addWidget(self.page_11)
        self.page_12 = QtWidgets.QWidget()
        self.page_12.setObjectName("page_12")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.page_12)
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.widget_25 = QtWidgets.QWidget(self.page_12)
        self.widget_25.setStyleSheet("QWidget{\n"
"background-color: rgb(145, 70, 255);\n"
"}\n"
"QWidget{\n"
"    border-bottom-right-radius:40%\n"
"}")
        self.widget_25.setObjectName("widget_25")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout(self.widget_25)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.label_70 = QtWidgets.QLabel(self.widget_25)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_70.setFont(font)
        self.label_70.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_70.setAlignment(QtCore.Qt.AlignCenter)
        self.label_70.setObjectName("label_70")
        self.horizontalLayout_24.addWidget(self.label_70)
        self.verticalLayout_19.addWidget(self.widget_25)
        self.frame_19 = QtWidgets.QFrame(self.page_12)
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.widget_26 = QtWidgets.QWidget(self.frame_19)
        self.widget_26.setGeometry(QtCore.QRect(0, 60, 531, 81))
        self.widget_26.setStyleSheet("background-color: rgb(145, 70, 255);\n"
"border-top-right-radius:30%;\n"
"border-bottom-right-radius:30%;\n"
"")
        self.widget_26.setObjectName("widget_26")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout(self.widget_26)
        self.horizontalLayout_25.setContentsMargins(1, 14, 16, 0)
        self.horizontalLayout_25.setSpacing(5)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        spacerItem1 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem1)
        self.label_71 = QtWidgets.QLabel(self.widget_26)
        self.label_71.setStyleSheet("    font:87 10pt \"Arial Black\";\n"
"    color: rgb(255, 255, 255);")
        self.label_71.setObjectName("label_71")
        self.horizontalLayout_25.addWidget(self.label_71)
        self.textoQntMsg_3 = QtWidgets.QLineEdit(self.widget_26)
        self.textoQntMsg_3.setStyleSheet("font:87 10pt \"Arial Black\";\n"
"color: rgba(255, 255, 255, 150);")
        self.textoQntMsg_3.setObjectName("textoQntMsg_3")
        self.textoQntMsg_3.setDisabled(True)
        self.horizontalLayout_25.addWidget(self.textoQntMsg_3)
        self.botaoConcluir_3 = QtWidgets.QPushButton(self.frame_19)
        self.botaoConcluir_3.setGeometry(QtCore.QRect(330, 470, 101, 31))
        self.botaoConcluir_3.setCursor(Qt.PointingHandCursor)
        self.botaoConcluir_3.clicked.connect(self.__gravar)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.botaoConcluir_3.setFont(font)
        self.botaoConcluir_3.setStyleSheet("QPushButton{\n"
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
        self.botaoConcluir_3.setObjectName("botaoConcluir_3")
        self.widget_27 = QtWidgets.QWidget(self.frame_19)
        self.widget_27.setGeometry(QtCore.QRect(0, 160, 531, 81))
        self.widget_27.setStyleSheet("background-color: rgb(145, 70, 255);\n"
"border-top-right-radius:30%;\n"
"border-bottom-right-radius:30%;\n"
"")
        self.widget_27.setObjectName("widget_27")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout(self.widget_27)
        self.horizontalLayout_26.setContentsMargins(1, 14, 16, 0)
        self.horizontalLayout_26.setSpacing(5)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        spacerItem2 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_26.addItem(spacerItem2)
        self.label_72 = QtWidgets.QLabel(self.widget_27)
        self.label_72.setStyleSheet("    font:87 10pt \"Arial Black\";\n"
"    color: rgb(255, 255, 255);")
        self.label_72.setObjectName("label_72")
        self.horizontalLayout_26.addWidget(self.label_72)
        self.textoQntDias_3 = QtWidgets.QLineEdit(self.widget_27)
        self.textoQntDias_3.setStyleSheet("font:87 10pt \"Arial Black\";\n"
"color: rgba(255, 255, 255, 150);")
        self.textoQntDias_3.setObjectName("textoQntDias_3")
        self.textoQntDias_3.setDisabled(True)
        self.horizontalLayout_26.addWidget(self.textoQntDias_3)
        self.widget_28 = QtWidgets.QWidget(self.frame_19)
        self.widget_28.setGeometry(QtCore.QRect(1, 260, 531, 81))
        self.widget_28.setStyleSheet("background-color: rgb(145, 70, 255);\n"
"border-top-right-radius:30%;\n"
"border-bottom-right-radius:30%;\n"
"")
        self.widget_28.setObjectName("widget_28")
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout(self.widget_28)
        self.horizontalLayout_27.setContentsMargins(1, 14, 16, 0)
        self.horizontalLayout_27.setSpacing(5)
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        spacerItem3 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_27.addItem(spacerItem3)
        self.label_73 = QtWidgets.QLabel(self.widget_28)
        self.label_73.setStyleSheet("    font:87 10pt \"Arial Black\";\n"
"    color: rgb(255, 255, 255);")
        self.label_73.setObjectName("label_73")
        self.horizontalLayout_27.addWidget(self.label_73)
        self.textoHorarioEnvio_3 = QtWidgets.QLineEdit(self.widget_28)
        self.textoHorarioEnvio_3.setStyleSheet("font:87 10pt \"Arial Black\";\n"
"color: rgba(255, 255, 255, 150);")
        self.textoHorarioEnvio_3.setObjectName("textoHorarioEnvio_3")
        self.textoHorarioEnvio_3.setDisabled(True)
        self.horizontalLayout_27.addWidget(self.textoHorarioEnvio_3)
        self.botaoRetro3_3 = QtWidgets.QPushButton(self.frame_19)
        self.botaoRetro3_3.setGeometry(QtCore.QRect(30, 510, 31, 31))
        self.botaoRetro3_3.clicked.connect(self.voltar)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.botaoRetro3_3.setFont(font)
        self.botaoRetro3_3.setStyleSheet("QPushButton{\n"
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
        self.botaoRetro3_3.setObjectName("botaoRetro3_3")
        self.caixaDigitarNomeRotina = QtWidgets.QLineEdit(self.frame_19)
        self.caixaDigitarNomeRotina.setGeometry(QtCore.QRect(20, 416, 281, 31))
        self.caixaDigitarNomeRotina.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"border:none;\n"
"color: rgb(255, 255, 255);\n"
"border-bottom:3px solid rgb(250, 250,250);\n"
"border-radius:5%;\n"
"padding-bottom:7px;\n"
"letter-spacing: 1px;\n"
"line-height: 1.1;\n"
"word-spacing: 10px;")
        self.caixaDigitarNomeRotina.setObjectName("caixaDigitarNomeRotina")
        self.label_74 = QtWidgets.QLabel(self.frame_19)
        self.label_74.setGeometry(QtCore.QRect(20, 360, 291, 56))
        self.label_74.setStyleSheet("    font:87 10pt \"Arial Black\";\n"
"    color: rgb(255, 255, 255);")
        self.label_74.setObjectName("label_74")
        self.label_75 = QtWidgets.QLabel(self.frame_19)
        self.label_75.setGeometry(QtCore.QRect(410, 345, 351, 56))
        self.label_75.setStyleSheet("    font:87 10pt \"Arial Black\";\n"
"    color: rgb(255, 255, 255);\n"
"background:none;")
        self.label_75.setObjectName("label_75")
        self.label_76 = QtWidgets.QLabel(self.frame_19)
        self.label_76.setGeometry(QtCore.QRect(416, 375, 331, 56))
        self.label_76.setStyleSheet("    font:87 10pt \"Arial Black\";\n"
"    color: rgb(255, 255, 255);\n"
"background:none;")
        self.label_76.setObjectName("label_76")
        self.radioNao = QtWidgets.QRadioButton(self.frame_19)
        self.radioNao.setGeometry(QtCore.QRect(590, 430, 95, 21))
        self.radioNao.setChecked(True)
        self.radioNao.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.radioNao.setObjectName("radioNao")
        self.radioSim = QtWidgets.QRadioButton(self.frame_19)
        self.radioSim.setGeometry(QtCore.QRect(500, 430, 95, 21))
        self.radioSim.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.radioSim.setObjectName("radioSim")
        self.verticalLayout_19.addWidget(self.frame_19)
        self.verticalLayout_19.setStretch(0, 1)
        self.verticalLayout_19.setStretch(1, 8)
        self.stackedWidget_3.addWidget(self.page_12)
        self.verticalLayout_15.addWidget(self.stackedWidget_3)
        self.verticalLayout_14.addWidget(self.frame_15)
        self.verticalLayout_14.setStretch(0, 1)
        self.verticalLayout_14.setStretch(1, 8)
        self.horizontalLayout_19.addWidget(self.frame_conteudo_3)
        self.horizontalLayout_19.setStretch(0, 2)
        self.horizontalLayout_19.setStretch(1, 8)
        self.widgetErro = QtWidgets.QWidget(Form)
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
        self.widgetSimNao = QtWidgets.QWidget(Form)
        self.widgetSimNao.setEnabled(True)
        self.widgetSimNao.setVisible(False)
        self.widgetSimNao.setGeometry(QtCore.QRect(360, 260, 461, 241))
        self.widgetSimNao.setStyleSheet("background-color: rgb(53, 53, 53);\n"
"border:2px solid rgb(0, 0, 0);\n"
"border-radius: 30%;")
        self.widgetSimNao.setObjectName("widgetSimNao")
        self.frame_conterImagem_4 = QtWidgets.QFrame(self.widgetSimNao)
        self.frame_conterImagem_4.setGeometry(QtCore.QRect(10, 10, 440, 221))
        self.frame_conterImagem_4.setStyleSheet("border:none;")
        self.frame_conterImagem_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_conterImagem_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_conterImagem_4.setObjectName("frame_conterImagem_4")
        self.img_alerta_4 = QtWidgets.QLabel(self.frame_conterImagem_4)
        self.img_alerta_4.setGeometry(QtCore.QRect(-40, -140, 511, 441))
        self.img_alerta_4.setStyleSheet("background: url(:/imagemAlerta/24x24/3800505.png);\n"
"\n"
"border: none;\n"
"opacity: 0.5;\n"
"")
        self.img_alerta_4.setText("")
        self.img_alerta_4.setTextFormat(QtCore.Qt.AutoText)
        self.img_alerta_4.setScaledContents(False)
        self.img_alerta_4.setObjectName("img_alerta_4")
        self.tituloAlerta_4 = QtWidgets.QLabel(self.frame_conterImagem_4)
        self.tituloAlerta_4.setGeometry(QtCore.QRect(0, 0, 441, 51))
        self.tituloAlerta_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tituloAlerta_4.setStyleSheet("background:none;\n"
"font: 87 16pt \"Arial Black\";\n"
"color:rgb(255, 255, 255)")
        self.tituloAlerta_4.setAlignment(QtCore.Qt.AlignCenter)
        self.tituloAlerta_4.setObjectName("tituloAlerta_4")
        self.textoAlerta_4 = QtWidgets.QLabel(self.frame_conterImagem_4)
        self.textoAlerta_4.setGeometry(QtCore.QRect(0, 50, 441, 121))
        self.textoAlerta_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textoAlerta_4.setStyleSheet("background:none;\n"
"font: 87 10pt \"Arial Black\";\n"
"color:rgb(255, 255, 255)")
        self.textoAlerta_4.setAlignment(QtCore.Qt.AlignCenter)
        self.textoAlerta_4.setObjectName("textoAlerta_4")
        self.botaoFecharSimNao = QtWidgets.QPushButton(self.frame_conterImagem_4)
        self.botaoFecharSimNao.setGeometry(QtCore.QRect(240, 180, 91, 31))
        self.botaoFecharSimNao.setStyleSheet("QPushButton{\n"
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
        self.botaoFecharSimNao.setObjectName("botaoFecharSimNao")
        self.botaoSimSimNao = QtWidgets.QPushButton(self.frame_conterImagem_4)
        self.botaoSimSimNao.setGeometry(QtCore.QRect(120, 180, 91, 31))
        self.botaoSimSimNao.clicked.connect(self.addVcf)
        self.botaoSimSimNao.setStyleSheet("QPushButton{\n"
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
        self.botaoSimSimNao.setObjectName("botaoSimSimNao")
        self.frame_7.raise_()
        self.widgetErro.raise_()
        self.widgetSimNao.raise_()


        self.mensagensNaoFormatadas = []
        self.listaMidias = []
        self.frame_7.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=3, yOffset=3,
                                                                           color=QtGui.QColor(0, 0, 0, 100)))

        self.retranslateUi(Form)
        self.stackedWidget_3.setCurrentIndex(0)
        self.stackedWidgetDataEHora.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Form)




    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Rotina", "Rotina"))
        Form.setWindowIcon(QtGui.QIcon('OneTickLogo.png'))
        self.label_50.setText(_translate("Form", "Mensagem"))
        self.label_51.setText(_translate("Form", "Destinatário"))
        self.label_52.setText(_translate("Form", "Horário"))
        self.label_53.setText(_translate("Form", "Agendar mensagem"))
        self.botaoFechar_3.setText(_translate("Form", "x"))
        self.label_54.setText(_translate("Form", "Configurando a mensagem"))
        self.label_55.setText(_translate("Form", "Mensagem:"))
        self.caixaMensagens_3.setPlaceholderText(_translate("Form", "Escreva aqui..."))
        self.label_56.setText(_translate("Form", "Ordem de envio:"))
        self.label_57.setText(_translate("Form", "* Selecione e mova de acordo com sua preferência de envio"))
        self.botaoAddVariaveis_3.setText(_translate("Form", "Adicionar Variáveis"))
        self.botaoAvan1_3.setText(_translate("Form", ">"))
        __sortingEnabled = self.listaVariaveis_3.isSortingEnabled()
        self.listaVariaveis_3.setSortingEnabled(False)
        item = self.listaVariaveis_3.item(0)
        item.setText(_translate("Form", "Nome do destinatário"))
        item = self.listaVariaveis_3.item(1)
        item.setText(_translate("Form", "Hora no envio da mensagem"))
        item = self.listaVariaveis_3.item(2)
        item.setText(_translate("Form", "Data no envio da mensagem"))
        item = self.listaVariaveis_3.item(3)
        item.setText(_translate("Form", "Hora Atual"))
        item = self.listaVariaveis_3.item(4)
        item.setText(_translate("Form", "Data Atual"))
        self.listaVariaveis_3.setSortingEnabled(__sortingEnabled)
        self.label_33.setText(_translate("Form", "Nome:"))
        self.caixaNomeVariavel.setPlaceholderText(_translate("Form", "Variável"))
        self.botaoAddVariavel.setText(_translate("Form", "Adicionar Variavel"))
        self.botaoFecharVariaveis.setText(_translate("Form", "X"))
        self.label_34.setText(_translate("Form", "Conteúdo:"))
        self.caixaConteudoVariavel.setPlaceholderText(_translate("Form", "Conteúdo"))
        self.botaoInfo_4.setToolTip(_translate("Form", "Digite \'/\' para acessar as variáveis especiais"))
        self.botaoInfo_4.setText(_translate("Form", "?"))
        self.label_58.setText(_translate("Form", "Configurando contatos"))
        self.radioContato_3.setText(_translate("Form", "Contato"))
        self.botaoAddContato_3.setText(_translate("Form", "Adicionar Contato"))
        self.radioGrupo_3.setText(_translate("Form", "Grupo"))
        self.label_60.setText(_translate("Form", "Selecione o tipo de destinatário:"))
        self.botaoAvan2_3.setText(_translate("Form", ">"))
        self.botaoRetro1_3.setText(_translate("Form", "<"))
        self.botaoInfo_2.setToolTip(_translate("Form", "Selecione os remetentes"))
        self.botaoInfo_2.setText(_translate("Form", "?"))
        self.botaoInfo_3.setToolTip(_translate("Form", "* Ordem de encaminhamento de mensagens"))
        self.botaoInfo_3.setText(_translate("Form", "?"))
        self.botaoAddGrupo_4.setText(_translate("Form", "Adicionar Grupo"))
        self.botaoInfo_1.setToolTip(_translate("Form", "*Selecione \"Contato\" para informar o número do remetente, ou, \"Grupo\" para informar o nome do grupo."))
        self.botaoInfo_1.setText(_translate("Form", "?"))
        self.label_29.setText(_translate("Form", "Número:"))
        self.caixaNomeDoContatoPersonalizado_4.setPlaceholderText(_translate("Form", "99 99 9999-9999"))
        self.label_31.setText(_translate("Form", "Nome:"))
        self.caixaNomePersonalizado_4.setPlaceholderText(_translate("Form", "Contato"))
        self.botaoAddContato.setText(_translate("Form", "Adicionar Contato"))
        self.botaoFecharAddContato.setText(_translate("Form", "X"))
        self.botaoImportarVcf.setText(_translate("Form", "Importar vcf"))
        self.label_32.setText(_translate("Form", "Nome:"))
        self.caixaNumeroPersonalizado_5.setPlaceholderText(_translate("Form", "Grupo"))
        self.botaoAddGrupo.setText(_translate("Form", "Adicionar Grupo"))
        self.botaoFecharAddGrupo_2.setText(_translate("Form", "X"))
        self.caixaFiltrarRemetentes.setPlaceholderText(_translate("Form", "Remetente"))
        self.label_63.setText(_translate("Form", "Configurando a data e hora"))
        self.label_65.setText(_translate("Form", "Tipo de Envio:"))
        self.label_66.setText(_translate("Form", "Horário:"))
        self.comboTipoDeEnvio_3.setCurrentText(_translate("Form", "Diária"))
        self.comboTipoDeEnvio_3.setItemText(0, _translate("Form", "Diária"))
        self.comboTipoDeEnvio_3.setItemText(1, _translate("Form", "Semanal"))
        self.comboTipoDeEnvio_3.setItemText(2, _translate("Form", "Mensal"))
        self.comboTipoDeEnvio_3.setItemText(3, _translate("Form", "Personalizada"))
        self.comboTipoDeEnvio_3.setItemText(4, _translate("Form", "Calendário"))
        self.botaoAvan3_3.setText(_translate("Form", ">"))
        self.botaoRetro2_3.setText(_translate("Form", "<"))
        self.label_69.setText(_translate("Form", ":"))
        self.botaoAdicionarDiaCalendario.setText(_translate("Form", "Adicionar"))
        self.label_64.setText(_translate("Form", "Dias selecionados:"))
        self.label_67.setText(_translate("Form", "Personalizado"))
        self.label_68.setText(_translate("Form", "Adicionar dias:"))
        self.botaoAdicionarDias_3.setText(_translate("Form", "Adicionar"))
        self.comboDias_3.setCurrentText(_translate("Form", "Domingo"))
        self.comboDias_3.setItemText(0, _translate("Form", "Domingo"))
        self.comboDias_3.setItemText(1, _translate("Form", "Sábado"))
        self.comboDias_3.setItemText(2, _translate("Form", "Segunda-feira"))
        self.comboDias_3.setItemText(3, _translate("Form", "Terça-feira"))
        self.comboDias_3.setItemText(4, _translate("Form", "Quarta-feira"))
        self.comboDias_3.setItemText(5, _translate("Form", "Quinta-feira"))
        self.comboDias_3.setItemText(6, _translate("Form", "Sexta-feira"))
        self.label_70.setText(_translate("Form", "Revisão"))
        self.label_71.setText(_translate("Form", "Quantidade de mensagens"))
        self.textoQntMsg_3.setText(_translate("Form", "Vezes"))
        self.textoQntMsg_3.setPlaceholderText(_translate("Form", "Nenhuma mensagem"))
        self.botaoConcluir_3.setText(_translate("Form", "Concluir"))
        self.label_72.setText(_translate("Form", "Quantidade de dias"))
        self.textoQntDias_3.setText(_translate("Form", "Vezes"))
        self.textoQntDias_3.setPlaceholderText(_translate("Form", "Nenhuma mensagem"))
        self.label_73.setText(_translate("Form", "Horário de envio"))
        self.textoHorarioEnvio_3.setText(_translate("Form", "Vezes"))
        self.textoHorarioEnvio_3.setPlaceholderText(_translate("Form", "Nenhuma mensagem"))
        self.botaoRetro3_3.setText(_translate("Form", "<"))
        self.caixaDigitarNomeRotina.setPlaceholderText(_translate("Form", "Nome"))
        self.label_74.setText(_translate("Form", "Escreva o nome da sua rotina:"))
        self.label_75.setText(_translate("Form", "Caso haja erro ao executar a rotina,"))
        self.label_76.setText(_translate("Form", "deseja adiar para o próximo dia?"))
        self.radioNao.setText(_translate("Form", "NÃO"))
        self.radioSim.setText(_translate("Form", "SIM"))
        self.tituloAlerta.setText(_translate("Form", "Titulo"))
        self.textoAlerta.setText(_translate("Form", "Conteudo"))
        self.botaoFecharErro.setText(_translate("Form", "Fechar"))
        self.tituloAlerta_4.setText(_translate("Form", "Titulo"))
        self.textoAlerta_4.setText(_translate("Form", "Conteudo"))
        self.botaoFecharSimNao.setText(_translate("Form", "Fechar"))
        self.botaoSimSimNao.setText(_translate("Form", "Sim"))


# PEGA AS INFORMAÇÕES DE PATH
    def InformacoesEPath(self):

        Interface = f'{os.getcwd()}'


        self.localContent = r'C:\Users\Usuario\PycharmProjects\Git\tccteam\TCC\localContent.db'
        self.InterfaceDB = r'C:\Users\Usuario\PycharmProjects\Git\tccteam\InterfaceDB.db'

        conexao = sqlite3.connect(rf'{self.localContent}')
        cursor = conexao.cursor()


# JANELA PARA BUSCAR VCF
    def __browseFileVcf(self):
        dir = os.getcwd()
        self.explorador = QtWidgets.QFileDialog.getOpenFileName(directory=dir, caption='OneTick Selecionar Imagem', filter="Vcard (*.vcf)")
        self.contatos = returnVcf(self.explorador[0])
        if self.contatos != 'ARQUIVO VCF ESTÁ COM PROBLEMA':
            self.__popupSimNao(titulo='Importar arquivo vcf', conteudo=f'Foram encontrados {len(self.contatos)} contatos\n Deseja importa-los?')
        self.abrirPopupContato()


#DEF PARA ADICIONAR OS CONTATOS DO VCF
    def addVcf(self):
        self.conexao = sqlite3.connect(rf'{self.InterfaceDB}')
        self.cursor = self.conexao.cursor()

        self.cursor.execute('DELETE FROM Contatos')

        self.NomesContatos = sorted(self.contatos)

        for i in self.NomesContatos:
            self.cursor.execute(f'INSERT INTO Contatos (nome, numero) VALUES(?, ?)', (i, self.contatos[i]))

            self.widgetSimNao.setVisible(False)


        self.conexao.commit()
        self.cursor.close()
        self.conexao.close()
        self.__preencherContatos()


#GRAVAR TODAS AS INFORMAÇÕES
    def __gravar(self):
        #MUDAR PATH
        self.conexao = sqlite3.connect(rf'{self.localContent}')
        self.cursor = self.conexao.cursor()

        mensagens = extrairMensagens(cursor=self.cursor)

        nomeValido = True
        try:
            for i in mensagens:


                if i[8] == self.caixaDigitarNomeRotina.text() or self.caixaDigitarNomeRotina.text() == '':
                    self.__popupErro('Erro ao definir nome', 'O nome da rotina é nulo\nou ja está em uso')
                    nomeValido = False
                    break
        except:
              pass


        if self.comboTipoDeEnvio_3.itemText(self.comboTipoDeEnvio_3.currentIndex()) == 'Calendário':
            if not self.__horarioPassado():
                return self.__popupErro('Erro ao salvar horário', 'O horário informado já passou')



        if nomeValido:

                dados = self.__coletarDados()
                mensagens = dados[0]
                horario = dados[1]
                dia = dados[2]
                remetente = dados[3]
                tipo_remetente = dados[4]
                contem_midia = dados[5]
                data_criada = dados[6]
                hora_criada = dados[7]
                nome_rotina = self.caixaDigitarNomeRotina.text()
                executar_erro = self.radioSim.isChecked()

                itemSelecionado = self.comboTipoDeEnvio_3.itemText(self.comboTipoDeEnvio_3.currentIndex())

                if itemSelecionado == 'Personalizada':
                    dia = 'Personalizada'
                    executar_erro = dados[2]








                if len(dia) > 1 and type(dia) is list:
                    count = 0
                    for i in dia:
                        count += 1
                        count2 = ''
                        if count == 1:
                            count2 = ''
                        else:
                            if count2 == '':
                                count2 = 0
                            else:
                                count2 += 1
                        count += 1
                        diaLista = [i]
                        self.cursor.execute(
                            'INSERT INTO Mensagens (mensagens, horario, dia, remetente, tipo_remetente, contem_midia, data_criada, hora_criada, nome_rotina, executar_erro)'
                            ' VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (
                            str(mensagens), horario, str(diaLista), str(remetente), tipo_remetente, contem_midia,
                            data_criada, hora_criada, str(nome_rotina)+str(count2), str(executar_erro),))

                else:
                    self.cursor.execute(
                    'INSERT INTO Mensagens (mensagens, horario, dia, remetente, tipo_remetente, contem_midia, data_criada, hora_criada, nome_rotina, executar_erro)'
                    ' VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (
                    str(mensagens), horario, str(dia), str(remetente), tipo_remetente,
                    contem_midia,
                    data_criada, hora_criada, str(nome_rotina), str(executar_erro),))






                atualizarDados(cursor=self.cursor)
                atualizarRotinasInterface(cursor=self.cursor)
                self.fechar()

                self.conexao.commit()
                self.cursor.close()
                self.conexao.close()




#PEGAR TODAS AS INFORMAÇÕES PASSADAS
    def __coletarDados(self):
        # self.tipo_Remetente
        # self.qntd_Mensagens
        # self.exploradorMidia
        # self.horario
        # self.mensagensFormatadas
        # self.Dias
        hora = self.spinBoxHora.text()
        minuto = self.spinBoxMinuto.text()
        if int(hora) < 10:
            hora = f'0{hora}'
        if int(minuto) < 10:
            minuto = f'0{minuto}'

        self.horario = f'{hora}:{minuto}'



        self.mensagensFormatadas = []
        itemSelecionado = self.comboTipoDeEnvio_3.itemText(self.comboTipoDeEnvio_3.currentIndex())
        numerosContatos = []
        nomesGrupos = []



        if itemSelecionado == 'Personalizada':
            self.Dias = []
            for i in range(0, self.listaDiasPersonalizado_3.count()):
                self.Dias.append(self.listaDiasPersonalizado_3.item(i).text())


        elif itemSelecionado == 'Calendário':
            self.Dias = []
            for i in range(0, self.listaDiasSelecionados_3.count()):
                self.Dias.append(self.listaDiasSelecionados_3.item(i).text())

        else:
            self.Dias = itemSelecionado


        if self.tipo_Remetente == 'Contato':

            for i in range(0, self.listaRemetentesSelecionados.count()):
                try:
                    numerosContatos.append(self.contatosENumeros[self.listaRemetentesSelecionados.item(i).text()])
                except:
                    numerosContatos.append(self.listaRemetentesSelecionados.item(i).text())

        elif self.tipo_Remetente == 'Grupo':
            for i in range(0, self.listaRemetentesSelecionados.count()):
                nomesGrupos.append(self.listaRemetentesSelecionados.item(i).text())


        #BOTAR VARIAVEIS
        for i in range(0, self.listaMensagensSalvas_3.count()):
                try:
                    msg = self.mensagensNaoFormatadas[i]

                    for j in range(0, self.listaVariaveis_3.count()):
                        variavel = self.listaVariaveis_3.item(j).text()

                        if f'({variavel})' in msg:
                            if variavel == 'Nome do destinatário':
                                msg = msg.replace(f'({variavel})', '(Nome do destinatário)')

                            elif variavel == 'Hora no envio da mensagem':
                                msg = msg.replace(f'({variavel})', self.horario)
                            elif variavel == 'Data no envio da mensagem':
                                msg = msg.replace(f'({variavel})', self.Dias)
                            else:
                                msg = msg.replace(f'({variavel})', self.variaveisEConteudos[variavel])


                    self.mensagensFormatadas.append(msg)

                except:
                    pass

        if not numerosContatos :
            self.remetente = nomesGrupos
        else:
            self.remetente = numerosContatos


        try:
            self.exploradorMidia
            for k in range(0, self.listaMensagensSalvas_3.count()):
                item = self.listaMensagensSalvas_3.item(k).text()
                if '...' not in item[len(item) - 3:]:
                    self.contem_midia = 'SIM'
        except:
            self.contem_midia = 'NÃO'


        atual = arrow.now()
        self.dia_atual_formatado = atual.now(tzinfo=atual.tzinfo).format('MM/DD')
        self.dia_atual = atual.now(tzinfo=atual.tzinfo).format('DD/MM')
        self.hora_atual = atual.now(tzinfo=atual.tzinfo).format('HH:mm')

        return self.mensagensFormatadas, self.horario, self.Dias, self.remetente, self.tipo_Remetente, self.contem_midia,\
               self.dia_atual, self.hora_atual




#POPUP PARA CONFIRMAR VCF
    def __popupSimNao(self, titulo='Janela de confirmação', conteudo=''):
        try:
            self.widgetSimNao.setVisible(True)
            self.tituloAlerta_4.setText(titulo)
            self.textoAlerta_4.setText(conteudo)
        except:
            self.widgetSimNao.setVisible(False)


#DEF PARA ACHAR PATH DA IMAGEM
    def browseFileImage(self):
        dir = os.getcwd()

        self.exploradorMidia = QtWidgets.QFileDialog.getOpenFileName(directory=dir, caption='OneTick Selecionar Imagem', filter="Images (*.png *.xpm *.jpg)")
        if self.exploradorMidia[0] != '':
            nomeArq = self.exploradorMidia[0].__str__().split('/')

            self.listaMidias.append(self.exploradorMidia[0])
            nomeArq = nomeArq[-1]

            self.mensagensNaoFormatadas.append(self.exploradorMidia[0])
            msg_curta = f'(MIDIA - {nomeArq})'
            self.listaMensagensSalvas_3.addItem(msg_curta)


#DEF PARA POPUPS DE ERRO
    def __popupErro(self, titulo='Erro', conteudo='Erro'):
        try:
            self.tituloAlerta.setText(titulo)
            self.textoAlerta.setText(conteudo)
            self.widgetErro.setVisible(True)

        except:
            self.widgetErro.setVisible(False)


# DEF PARA VER SE MENSAGEM JA PASSOU DO HORÁRIO
    def __horarioPassado(self):
       atual = arrow.now()
       self.dia_atual_formatado = atual.now(tzinfo=atual.tzinfo).format('MM/DD')
       self.hora_atual = atual.now(tzinfo=atual.tzinfo).format('HH:mm')
       for i in range(0, self.listaDiasSelecionados_3.count()):
           if self.listaDiasSelecionados_3.item(i).text() == self.dia_atual_formatado:

               if int(self.hora_atual[:2]) > int(self.spinBoxHora.text()):

                   self.__popupErro('Erro ao informar horário',
                   'O horário selecionado\n já passou para um dos dias')

                   return False
               elif int(self.hora_atual[:2]) == int(self.spinBoxHora.text()):
                   if int(self.hora_atual[3:]) >= int(self.spinBoxMinuto.text()):
                       self.__popupErro('Erro ao informar horário',
                       'O horário selecionado\n já passou para um dos dias')
                       return False
                   else:
                       return True
               else:
                   return True
           else:
               return True


#DEF PARA VERIFICAR SE INFORMAÇÕES PASSADAS EM CADA PÁGINA ESTÃO DENTRO DOS PARÂMETROS
    def __verificar(self):
        try:
            currentIndex = self.stackedWidget_3.currentIndex()
            self.qntd_Mensagens = self.listaMensagensSalvas_3.count()
            tipo_RemetenteCtt = self.radioContato_3.isChecked()
            tipo_RemetenteGpp = self.radioGrupo_3.isChecked()
            qntd_listaDias = self.listaDiasPersonalizado_3.count()
            qntd_listaDiasSelecionados = self.listaDiasSelecionados_3.count()

            # Caixa de mensagens
            if self.qntd_Mensagens == 0 and currentIndex == 0:
                self.__popupErro('Erro em mensagens', 'Nenhuma mensagem foi selecionada para envio')
                return False


            # Radios Contato e Grupo
            if tipo_RemetenteCtt is False and tipo_RemetenteGpp is False and currentIndex == 1:
                self.__popupErro('Erro em seleção', 'Nenhum tipo de envio foi selecionado')
                return False
            elif currentIndex == 1:
                if tipo_RemetenteGpp is True:
                    self.tipo_Remetente = 'Grupo'
                else:
                    self.tipo_Remetente = 'Contato'

                if self.listaRemetentesSelecionados.count() == 0:
                    self.__popupErro('Erro', 'Não há nenhum contato ou grupo selecionado para envio')

                    return False


            # Caixa Personalizada
            if qntd_listaDias == 0 and self.comboTipoDeEnvio_3.itemText(
                    self.comboTipoDeEnvio_3.currentIndex()) == 'Personalizada' and currentIndex == 2:

                    self.__popupErro('Erro de personalização', 'Os dias semanais não foram\n informados corretamente')
                    return False

            elif qntd_listaDiasSelecionados == 0 and self.comboTipoDeEnvio_3.itemText(
                    self.comboTipoDeEnvio_3.currentIndex()) == 'Calendário' and currentIndex == 2:

                    self.__popupErro('Erro de personalização', 'Os dias do calendário não foram\n informados corretamente')
                    return False



            #HORARIO JA PASSOU
            elif self.comboTipoDeEnvio_3.itemText(
            self.comboTipoDeEnvio_3.currentIndex()) == 'Calendário' and currentIndex == 2:
                if not self.__horarioPassado():
                    return False

            self.conexao = sqlite3.connect(rf'{self.localContent}')
            self.cursor = self.conexao.cursor()

            if currentIndex == 2:
                hora = self.spinBoxHora.text()
                minuto = self.spinBoxMinuto.text()

                if int(hora) < 10:
                    hora = f'0{hora}'
                if int(minuto) < 10:
                    minuto = f'0{minuto}'

                horarioStr = f'{hora}:{minuto}'
                for msg in extrairHorarios(self.cursor):
                    if horarioStr == msg:
                        self.__popupErro('Erro ao informar Horário', 'Já há outra rotina nesse tempo')
                        return False





            if extrairMensagensPersonalizada(self.cursor) and self.comboTipoDeEnvio_3.itemText(
                    self.comboTipoDeEnvio_3.currentIndex()) == 'Personalizada' and currentIndex == 2:
                    self.__popupErro('Erro ao salvar personalizada', 'Parece que já existe uma rotina criada')
                    self.conexao.commit()
                    self.cursor.close()
                    self.conexao.close()
                    return False
            else:
                self.conexao.commit()
                self.cursor.close()
                self.conexao.close()





            if currentIndex == 2:
                if self.comboTipoDeEnvio_3.itemText(self.comboTipoDeEnvio_3.currentIndex()) == 'Calendário':
                    self.radioNao.setVisible(True)
                    self.radioSim.setVisible(True)
                    self.label_75.setVisible(True)
                    self.label_76.setVisible(True)
                else:
                    self.radioNao.setVisible(False)
                    self.radioSim.setVisible(False)
                    self.label_75.setVisible(False)
                    self.label_76.setVisible(False)



                self.__coletarDados()
                self.textoQntMsg_3.setText(str(self.qntd_Mensagens))
                self.textoQntDias_3.setText(str(self.Dias))
                self.textoHorarioEnvio_3.setText(str(self.horario))
        except:
                return False


# DEF PARA VERIFICAR SE O NUMERO INSERIDO É VALIDO
    def __verificarNumero(self, num):
        num = str(num.replace(' ', '').replace('-', ''))
        if len(num) == 12 and num.isnumeric() is True:
            return True, num
        else:
            self.__popupErro('Erro ao verificar número', 'O padrão correto não foi digitado')
            return False


# DEF PARA ADICIONAR OS DIAS SELECIONADOS NO CALENDÁRIO
    def adicionarDiasCalendario(self):
        dia = self.calendario_3.selectedDate().day()
        mes = self.calendario_3.selectedDate().month()



        item = f'{mes}/{dia}'
        igual = False
        try:
            for i in range(0, self.listaDiasSelecionados_3.count()+1):
                if item == self.listaDiasSelecionados_3.item(i).text():
                    igual = True
                    self.__popupErro('Erro ao adicionar data', 'A data já está selecionada')
        except:
              pass
        if not igual:
            self.listaDiasSelecionados_3.addItem(item)



    def mostrarEmoji(self):
        hotkey('win', '.')



# DEF PARA ADICIONAR DIAS PERSONALIZADOS
    def adicionarDiasPersonalizados(self, item):
        if self.comboDias_3.count() != 0:
            dia = self.comboDias_3.itemText(self.comboDias_3.currentIndex())
            self.listaDiasPersonalizado_3.addItem(dia)
            self.comboDias_3.removeItem(self.comboDias_3.currentIndex())


# DEF PARA HABILITAR A OPCAO DE SELECIONAR DIAS PERSONALIZADOS E CALENDÁRIOS
    def habilitarPersonalizadaECalendario(self, item):
        if item == 3:
            self.stackedWidgetDataEHora.setCurrentIndex(1)
            self.widget_24.setDisabled(False)
            try:
                self.calendario_3.setDisabled(True)
                self.botaoAdicionarDiaCalendario.setDisabled(True)
            except:
                pass
        elif item == 4:
            self.stackedWidgetDataEHora.setCurrentIndex(0)

            try:
                self.widget_24.setDisabled(True)
            except:
                pass
            self.botaoAdicionarDiaCalendario.setDisabled(False)
            self.calendario_3.setDisabled(False)
        else:
            try:
                self.stackedWidgetDataEHora.setCurrentIndex(2)

                self.botaoAdicionarDiaCalendario.setDisabled(True)
                self.widget_24.setDisabled(True)
                self.calendario_3.setDisabled(True)
            except:
                pass






# DEF PARA ABRIR E FECHAR O POPUP DE ADICIONAR VARIÁVEL
    def abrirPopupVariavel(self):
        if self.widgetAddVariaveis.isVisible():
                self.widgetAddVariaveis.setVisible(False)
        else:
                self.widgetAddVariaveis.setVisible(True)


# DEF PARA PARA SALVAR A VARIÁVEL
    def salvarVariavel(self):
        self.conexao = sqlite3.connect(rf'{self.InterfaceDB}')
        self.cursor = self.conexao.cursor()

        if self.caixaNomeVariavel.text().strip() != "" and self.caixaConteudoVariavel.text().strip() != "":

            nome_variavel = self.caixaNomeVariavel.text().strip()
            conteudo = self.caixaConteudoVariavel.text().strip()
            try:
                self.cursor.execute(f'INSERT INTO Variaveis (encurtamento, conteudo) VALUES(?, ?)', (nome_variavel, conteudo))
            except:
                self.__popupErro('Erro na variável', 'Erro ao salvar os conteúdos\nCheque se o nome da variável já existe')
            self.abrirPopupVariavel()

        else:
            self.__popupErro('Erro nas informações', 'Nome da variável ou do conteúdo são nulos')

        self.conexao.commit()
        self.cursor.close()
        self.conexao.close()



# DEF PARA SALVAR O REMETENTE SELECIONADO
    def salvarRemetentes(self):
        self.listaRemetentesSelecionados.clear()
        itemsSelecionados = self.listaContatos_3.selectedItems()


        for i in range(0, len(itemsSelecionados)):
            self.listaRemetentesSelecionados.addItem(itemsSelecionados[i].text())

        if self.listaRemetentesSelecionados.count() == 0:
            self.mostrarBotoesRemetentes()



# DEF QUE CRIA O CONTATO DIGITADO
    def criarContato(self):
        num_add = self.caixaNomeDoContatoPersonalizado_4.text()
        nome_add = self.caixaNomePersonalizado_4.text().strip()
        if self.__verificarNumero(num_add) and nome_add != '':


            self.conexao = sqlite3.connect(rf'{self.InterfaceDB}')
            self.cursor = self.conexao.cursor()
            try:
                self.cursor.execute(f'INSERT INTO Contatos (nome, numero) VALUES(?, ?)', (nome_add, num_add))
                self.abrirPopupContato()
            except:
                pass

            self.conexao.commit()
            self.cursor.close()
            self.conexao.close()
            self.abrirPopupContato()
            self.checkContato()
        else:
            self.__popupErro('Erro ao criar contato', 'O nome não foi preenchido\nou o número está incorreto')


#DEF QUE CRIA O GRUPO DIGITADO
    def criarGrupo(self):
        self.conexao = sqlite3.connect(rf'{self.InterfaceDB}')
        self.cursor = self.conexao.cursor()
        grupo = self.caixaNumeroPersonalizado_5.text().strip()

        if grupo != '':
            self.cursor.execute(f'INSERT INTO Grupos (nome) VALUES(?)', (grupo, ))
        else:
            self.__popupErro('Erro ao criar grupo', 'O nome não foi preenchido')

        self.conexao.commit()
        self.cursor.close()
        self.conexao.close()
        self.abrirPopupGrupo()
        self.checkGrupo()


# DEF PARA O CLIQUE DUPLO DE VARIÁVEIS PERSONALIZADAS
    def cliqueDuploVariavel(self, item):

        variavel = '('+self.listaVariaveis_3.currentItem().text()+')'
        texto = self.caixaMensagens_3.toPlainText()
        if texto.count('/') > 1:
            textoFormatado = texto[:texto.find('/')+1].replace('/', variavel)
            texto = textoFormatado + texto[texto.find('/')+1:]
        else:
            texto = texto.replace('/', variavel)
            self.listaVariaveis_3.setVisible(False)

        self.caixaMensagens_3.clear()
        self.caixaMensagens_3.insertPlainText(texto)


#DEF PARA SELECIONAR VARIAVEIS
    def selecionarVariaveis(self):
        texto = self.caixaMensagens_3.toPlainText()
        if "/" in texto:
            self.__preencherVariaveis()
            self.listaVariaveis_3.setVisible(True)
        else:
            self.listaVariaveis_3.setVisible(False)


#DEF PARA AVANÇAR DE PÁGINAS
    def avancar(self):
        if self.__verificar() is not False:
                self.barraMomento_3.setValue(self.barraMomento_3.value() + 32)
                index = self.stackedWidget_3.currentIndex()
                self.stackedWidget_3.setCurrentIndex(index + 1)



#DEF PARA PREENCHER OS GRUPOS DO BANCO DE DADOS
    def __preencherGrupos(self):
        self.conexao = sqlite3.connect(rf'{self.InterfaceDB}')
        self.cursor = self.conexao.cursor()

        try:
            self.listaContatos_3.clear()
            self.cursor.execute('SELECT nome FROM Grupos')
            for elemento in self.cursor.fetchall():
                self.listaContatos_3.addItem(str(elemento[0]))
        except:
            self.__popupErro('Erro ao preencher Grupos', 'Erro ao importar grupos salvos')
        self.cursor.close()
        self.conexao.close()


#DEF PARA PREENCHER OS CONTATOS DO BANCO DE DADOS
    def __preencherContatos(self):
        self.conexao = sqlite3.connect(rf'{self.InterfaceDB}')
        self.cursor = self.conexao.cursor()

        try:
            self.listaContatos_3.clear()
            self.contatosENumeros = {}
            self.cursor.execute('SELECT * FROM Contatos ORDER BY nome ASC')
            for elemento in self.cursor.fetchall():
                self.contatosENumeros[elemento[0]] = elemento[1]
                self.listaContatos_3.addItem(elemento[0])
        except:
            self.__popupErro('Erro ao preencher contatos', 'Erro ao importar contatos salvos')

        self.cursor.close()
        self.conexao.close()


#DEF PARA PREENCHER VARIÁVEIS DO BANCO DE DADOS
    def __preencherVariaveis(self):

        self.conexao = sqlite3.connect(rf'{self.InterfaceDB}')
        self.cursor = self.conexao.cursor()
        try:
            self.variaveisEConteudos = {}
            self.listaVariaveis_3.clear()
            self.cursor.execute('SELECT * FROM Variaveis')
            for elemento in self.cursor.fetchall():
                self.variaveisEConteudos[elemento[0]] = elemento[1]
                self.listaVariaveis_3.addItem(elemento[0])
        except:
            self.__popupErro('Erro no importe', 'Erro importar variáveis')

        self.conexao.commit()
        self.cursor.close()
        self.conexao.close()




#DEF PARA ABRIR E FECHAR POPUPS DOS CONTATOS
    def abrirPopupContato(self):
        if self.widgetAddContato.isVisible():
            self.widgetAddContato.setVisible(False)
            self.caixaNomePersonalizado_4.clear()
            self.caixaNomeDoContatoPersonalizado_4.clear()
        else:
            self.widgetAddContato.setVisible(True)



#DEF PARA ABRIR E FECHAR POPUP DOS GRUPOS
    def abrirPopupGrupo(self):
        if self.widgetAddGrupo.isVisible():
            self.caixaNumeroPersonalizado_5.clear()
            self.widgetAddGrupo.setVisible(False)
        else:
            self.widgetAddGrupo.setVisible(True)





#DEF PARA MOSTRAR OS BOTOES DE ALTERNAR SEQUÊNCIA DE MENSAGENS
    def mostrarBotoesRemetentes(self):
        item = self.listaRemetentesSelecionados.currentItem()
        countList = self.listaRemetentesSelecionados.count()

        if countList > 1 and self.listaRemetentesSelecionados.indexFromItem(item).row() == 0:

            self.botaoRemetentePraCima_2.setVisible(False)
            self.botaoRemetentePraBaixo_2.setVisible(True)

        elif countList > 1 and self.listaRemetentesSelecionados.indexFromItem(item).row() == countList -1:

            self.botaoRemetentePraCima_2.setVisible(True)
            self.botaoRemetentePraBaixo_2.setVisible(False)

        elif countList > 1:

            self.botaoRemetentePraCima_2.setVisible(True)
            self.botaoRemetentePraBaixo_2.setVisible(True)

        else:
            self.botaoRemetentePraCima_2.setVisible(False)
            self.botaoRemetentePraBaixo_2.setVisible(False)



#DEF PARA MOVER ITEM PRA CIMA
    def moverItemPraCimaRemetentes(self):
        row = self.listaRemetentesSelecionados.currentRow()
        item = self.listaRemetentesSelecionados.takeItem(row)
        self.listaRemetentesSelecionados.insertItem(row - 1, item)


#DEF PARA MOVER ITEM PRA BAIXO
    def moverItemPraBaixoRemetentes(self):
        row = self.listaRemetentesSelecionados.currentRow()
        item = self.listaRemetentesSelecionados.takeItem(row)
        self.listaRemetentesSelecionados.insertItem(row + 1, item)



#DEF PARA MOSTRAR OS BOTÕES DAS MENSAGENS
    def mostrarBotoesMensagens(self):
        if self.listaMensagensSalvas_3.count() != 0:
            self.botaoMensagemApagar.setVisible(True)

            item = self.listaMensagensSalvas_3.currentItem()
            countList = self.listaMensagensSalvas_3.count()

            if countList > 1 and self.listaMensagensSalvas_3.indexFromItem(item).row() == 0:

                    self.botaoMensagemPraCima.setVisible(False)
                    self.botaoMensagemPraBaixo.setVisible(True)

            elif countList > 1 and self.listaMensagensSalvas_3.indexFromItem(item).row() == countList -1:

                    self.botaoMensagemPraCima.setVisible(True)
                    self.botaoMensagemPraBaixo.setVisible(False)

            elif countList > 1:

                    self.botaoMensagemPraCima.setVisible(True)
                    self.botaoMensagemPraBaixo.setVisible(True)

            else:
                    self.botaoMensagemPraCima.setVisible(False)
                    self.botaoMensagemPraBaixo.setVisible(False)
        else:
            self.botaoMensagemApagar.setVisible(False)




#DEF PARA MOVER MENSAGENS PRA CIMA
    def moverItemPraCimaMensagens(self):
        row = self.listaMensagensSalvas_3.currentRow()
        item = self.listaMensagensSalvas_3.takeItem(row)
        self.listaMensagensSalvas_3.insertItem(row - 1, item)
        self.__atualizarOrdemMensagens()


#DEF PARA MOVER MENSAGENS PRA BAIXO
    def moverItemPraBaixoMensagens(self):
        row = self.listaMensagensSalvas_3.currentRow()
        item = self.listaMensagensSalvas_3.takeItem(row)
        self.listaMensagensSalvas_3.insertItem(row + 1, item)
        self.__atualizarOrdemMensagens()



#DEF PARA ATUALIZAR A ORDEM DAS MENSAGENS CASO MUDE A SEQUÊNCIA
    def __atualizarOrdemMensagens(self):
        msgsBackup = list(self.mensagensNaoFormatadas)
        self.mensagensNaoFormatadas.clear()

        for i in range(0, self.listaMensagensSalvas_3.count()):
            mensagem = self.listaMensagensSalvas_3.item(i).text()
            if '...' in mensagem[len(mensagem) - 3:]:
                self.mensagensNaoFormatadas.append(mensagem[:len(mensagem) - 3])
            else:
                for j in msgsBackup:
                   if os.path.basename(j) in mensagem:
                      self.mensagensNaoFormatadas.append(j)
                      break


#DEF PARA ELIMINAR MENSAGEM CASO APAGUE
    def eliminarItemListaMensagens(self):
        item = self.listaMensagensSalvas_3.currentItem()
        self.listaMensagensSalvas_3.takeItem(self.listaMensagensSalvas_3.indexFromItem(item).row())
        self.__atualizarOrdemMensagens()
        self.mostrarBotoesMensagens()


#DEF PARA ELIMINAR CONTATO
    def eliminarItemListaContatos(self):
        item = self.listaContatos_3.currentItem()
        self.listaContatos_3.takeItem(self.listaContatos_3.indexFromItem(item).row())



#DEF PARA ELIMINAR DIA DA ROTINA PERSONALIZADA
    def eliminarItemListaPersonalizado(self):
            item = self.listaDiasPersonalizado_3.currentItem().text()

            self.comboDias_3.addItem(item)

            itemQ = self.listaDiasPersonalizado_3.currentItem()
            self.listaDiasPersonalizado_3.takeItem(self.listaDiasPersonalizado_3.indexFromItem(itemQ).row())


#DEF PARA ELIMINAR DIA DA LISTA DE CALENDÁRIO
    def eliminarItemListaCalendario(self):
        item = self.listaDiasSelecionados_3.currentItem()
        self.listaDiasSelecionados_3.takeItem(self.listaDiasSelecionados_3.indexFromItem(item).row())


#DEF PARA SALVAR MENSAGEM
    def salvar_msg(self):
        if self.caixaMensagens_3.toPlainText().strip() != '':
            msg = self.caixaMensagens_3.toPlainText()
            self.mensagensNaoFormatadas.append(msg)
            msg_format = msg+"..."
            self.listaMensagensSalvas_3.addItem(msg_format)
            self.caixaMensagens_3.clear()

        else:
            self.__popupErro('Erro ao salvar mensagem', 'A mensagem não possui informações')


#DEF PARA VOLTAR PAGINA
    def voltar(self):
        index = self.stackedWidget_3.currentIndex()
        self.stackedWidget_3.setCurrentIndex(index - 1)
        if index != 3:
                self.barraMomento_3.setValue(self.barraMomento_3.value() - 32)


#DEF DE FILTRO
    def filtrar(self):
        filtro = self.caixaFiltrarRemetentes.text()

        self.conexao = sqlite3.connect(rf'{self.InterfaceDB}')
        self.cursor = self.conexao.cursor()

        try:
            self.listaContatos_3.clear()
            if self.radioContato_3.isChecked():
                self.contatosENumeros = {}
                self.cursor.execute('SELECT * FROM Contatos ORDER BY nome ASC')
                for elemento in self.cursor.fetchall():
                    if elemento[0][:len(filtro)].upper() == filtro.upper():
                        self.contatosENumeros[elemento[0]] = elemento[1]
                        self.listaContatos_3.addItem(elemento[0])
            else:
                self.cursor.execute('SELECT * FROM Grupos ORDER BY nome ASC')
                for elemento in self.cursor.fetchall():
                    if elemento[0][:len(filtro)].upper() == filtro.upper():
                        self.listaContatos_3.addItem(elemento[0])
        except:
            self.__popupErro('Erro ao preencher contatos', 'Erro ao importar contatos salvos')

        self.cursor.close()
        self.conexao.close()





#DEF PARA MOSTRAR BOTOES DE GRUPOS
    def checkGrupo(self):
        self.botaoAddGrupo_4.setVisible(True)
        self.botaoAddContato_3.setVisible(False)
        self.widgetAddGrupo.setVisible(False)
        self.widgetAddContato.setVisible(False)
        self.listaRemetentesSelecionados.clear()
        self.__preencherGrupos()


#DEF PARA MOSTRAR BOTOES DE CONTATOS
    def checkContato(self):
        self.botaoAddGrupo_4.setVisible(False)
        self.botaoAddContato_3.setVisible(True)
        self.widgetAddGrupo.setVisible(False)
        self.widgetAddContato.setVisible(False)
        self.listaRemetentesSelecionados.clear()
        self.__preencherContatos()


#DEF PARA MINIMIZAR
    def minimizar(self):
        self.frame_7.showMinimized()

#DEF PARA FECHAR POPUP
    def fechar(self):
        self.frame_7.close()
        self.widgetErro.close()
        self.widgetSimNao.close()


import sys

if __name__=="__main__":
        app = QtWidgets.QApplication(sys.argv)
        Principal = QtWidgets.QMainWindow()
        ui = Ui_Form()
        ui.setupUi(Principal)
        Principal.show()
        sys.exit(app.exec_())
