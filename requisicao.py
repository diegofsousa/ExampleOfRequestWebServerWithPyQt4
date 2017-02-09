#coding: utf-8

import json
import requests
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from threading import Thread, current_thread

class Th(Thread):
	def __init__ (self, container):
		Thread.__init__(self)
		self.container = container

	def run(self):
		base = None
		try:
			while True:
				r = requests.get('https://salty-inlet-77176.herokuapp.com/consultar/')
				if r.status_code == 200:
				    reddit_data = json.loads(r.content)
				    if reddit_data != base:
				    	if reddit_data == True:
							self.container.setPixmap(QPixmap('imagens/lampada.png').scaled(QSize(200,250)))
							self.container.setAlignment(Qt.AlignCenter)
				    	else:
							self.container.setPixmap(QPixmap('imagens/lampada.png').scaled(QSize(200,250)))
							self.container.setAlignment(Qt.AlignCenter)

		except KeyboardInterrupt:
			print "Ação cancelada pelo usuário"

	
