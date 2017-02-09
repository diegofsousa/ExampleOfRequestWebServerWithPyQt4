# -*- coding: iso-8859-1 -*-

import sys, os, subprocess
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from threading import Thread, current_thread
from requisicao import Th

class interface(QDialog):
	"""docstring for interface"""
	def __init__(self, parent=None):
		super(interface, self).__init__(parent)	
		self.setWindowTitle('Interruptor remoto DjArduino')
		label = QLabel("Estado de conexao: ATIVO")
		label.setAlignment(Qt.AlignCenter)
		self.lbl_imagem = QLabel(self)
		self.
		#self.lbl_imagem.setPixmap(QPixmap('imagens/lampada.png').scaled(QSize(200,250)))
		#self.lbl_imagem.setAlignment(Qt.AlignCenter)

		th = Th(self.lbl_imagem)
		th.start()

		up_button = QPushButton("Ligar")
		down_button = QPushButton("Desligar")

		hbox = QHBoxLayout()
		hbox.addWidget(up_button)
		hbox.addWidget(down_button)

		vbox = QVBoxLayout(self)
		vbox.addWidget(label)
		vbox.addWidget(self.lbl_imagem)
		vbox.addLayout(hbox)


		self.setLayout(vbox)

		self.connect(down_button, SIGNAL("clicked()"), self.down)
		self.connect(up_button, SIGNAL("clicked()"), self.up)

		self.setGeometry(500,500, 430,130)

	def down(self):
		self.lbl_imagem.setPixmap(QPixmap('imagens/lampadaapagada.png').scaled(QSize(200,250)))
	def up(self):
		self.lbl_imagem.setPixmap(QPixmap('imagens/lampada.png').scaled(QSize(200,250)))

app = QApplication(sys.argv)
dlg = interface()
dlg.exec_()