import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit
from PyQt5 import QtCore
from CodigoTCC import Mensagem


class Janela(QMainWindow):
    def __init__(self):
        super().__init__()

        self.topo = 100
        self.esquerda = 100
        self.largura = 800
        self.altura = 700
        self.titulo = 'Janela'
        self.setStyleSheet("background-color: #69AABB ;border : 1px solid #0E6176; border-radius: 5px")

        self.contato = QLineEdit(self)
        self.contato.setStyleSheet('QLineEdit {background-color: #FFFFFF}')
        self.contato.move(265, 200)
        self.contato.resize(300, 40)

        self.mensagem = QLineEdit(self)
        self.mensagem.setStyleSheet('QLineEdit {background-color: #FFFFFF}')
        self.mensagem.move(265, 300)
        self.mensagem.resize(300, 40)

        self.qnt = QLineEdit(self)
        self.qnt.setStyleSheet('QLineEdit {background-color: #FFFFFF}')
        self.qnt.move(265, 400)
        self.qnt.resize(300, 40)

        botao = QPushButton('Enviar Mensagem', self)
        botao.move(350, 600)
        botao.resize(100, 50)
        botao.setStyleSheet('QPushButton {background-color: #9DCCD8}')
        botao.clicked.connect(self.MandarMensagem)

        titulo = QLabel(self)
        titulo.setText("Agende o envio de suas mensagens!")
        titulo.move(170, 50)
        titulo.resize(500, 50)
        titulo.setStyleSheet(
            'QLabel {font: 25px; font-weight: 800 ;color: #FFFFFF;font-family: Courier, monospace; border: none}')
        titulo.setAlignment(QtCore.Qt.AlignCenter)

        label1 = QLabel(self)
        label1.setText("Contato:")
        label1.move(285, 150)
        label1.resize(100, 30)
        label1.setStyleSheet(
            'QLabel {font: 15px; font-family: Courier, monospace; background-color: #a2c0ff; border-radius: 5px; '
            'border: 1px}')
        label1.setAlignment(QtCore.Qt.AlignCenter)

        label2 = QLabel(self)
        label2.setText("Mensagem:")
        label2.move(285, 250)
        label2.resize(100, 30)
        label2.setStyleSheet(
            'QLabel {font: 15px;font-family: Courier, monospace; background-color: #a2c0ff; border-radius: 5px; '
            'border: 1px}')
        label2.setAlignment(QtCore.Qt.AlignCenter)


        label4 = QLabel(self)
        label4.setText("Quantidade de envio:")
        label4.move(285, 350)
        label4.resize(220, 30)
        label4.setStyleSheet(
            'QLabel {font: 15px;font-family: Courier, monospace; background-color: #a2c0ff; border-radius: 5px; '
            'border: 1px}')
        label4.setAlignment(QtCore.Qt.AlignCenter)

        self.CarregarJanela()

    def CarregarJanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

    def MandarMensagem(self):
        NMsg = Mensagem('11', '00')
        NMsg.enviar(self.mensagem.text(), int(self.qnt.text()), int(self.contato.text()))
        # print(self.contato.text())
        print(self.mensagem.text())




aplicacao = QApplication(sys.argv)
j = Janela()
sys.exit(aplicacao.exec())