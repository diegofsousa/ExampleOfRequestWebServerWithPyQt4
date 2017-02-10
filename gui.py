# -*- coding: iso-8859-1 -*-

import sys, os, subprocess
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from threading import Thread, current_thread
from requisicao import Th, Interruptor

class interface(QDialog):
	"""Interface gráfica para melhor usabilidade da aplicação"""
	def __init__(self, parent=None):
		super(interface, self).__init__(parent)	
		self.setWindowTitle('Interruptor remoto DjArduino')
		self.label = QLabel("Estado de conexao: Desativado")
		self.label.setAlignment(Qt.AlignCenter)
		self.lbl_imagem = QLabel(self)


		th = Th()
		self.connect(th, SIGNAL("up()"), self.up)
		self.connect(th, SIGNAL("down()"), self.down)
		self.connect(th, SIGNAL("wait()"), self.wait)
		th.start()

		up_button = QPushButton("Ligar")
		down_button = QPushButton("Desligar")

		hbox = QHBoxLayout()
		hbox.addWidget(up_button)
		hbox.addWidget(down_button)

		vbox = QVBoxLayout(self)
		vbox.addWidget(self.label)
		vbox.addWidget(self.lbl_imagem)
		vbox.addLayout(hbox)


		
		
		self.instanciaInt = Interruptor()

		self.connect(down_button, SIGNAL("clicked()"), self.desliga)
		self.connect(up_button, SIGNAL("clicked()"), self.liga)

		self.setLayout(vbox)
		self.setGeometry(500,500, 430,130)

	def down(self):
		self.lbl_imagem.setPixmap(QPixmap('imagens/lampadaapagada.png').scaled(QSize(200,250)))
		self.lbl_imagem.setAlignment(Qt.AlignCenter)

	def up(self):
		self.lbl_imagem.setPixmap(QPixmap('imagens/lampada.png').scaled(QSize(200,250)))
		self.lbl_imagem.setAlignment(Qt.AlignCenter)

	def wait(self):
		self.label.setText("Estado de conexao: CONECTADO")
		self.label.setAlignment(Qt.AlignCenter)

	def liga(self):
		self.lbl_imagem.setText("Aguarde...")
		print("ligou")
		self.instanciaInt.liga()

	def desliga(self):
		self.lbl_imagem.setText("Aguarde...")
		print("desligou")
		self.instanciaInt.desliga()

app = QApplication(sys.argv)
dlg = interface()
dlg.exec_()