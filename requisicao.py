#coding: utf-8

import json
import requests
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from threading import Thread, current_thread

class Th(QThread):
	def __init__ (self):
		QThread.__init__(self)

	def run(self):
		base = None

		try:
			while True:
				r = requests.get('https://salty-inlet-77176.herokuapp.com/consultar/')

				if r.status_code == 200:
					
					reddit_data = json.loads(r.content)
					if reddit_data != base:
						base = reddit_data
						self.emit(SIGNAL("wait()"))
						print(reddit_data)
						if reddit_data == True:
							self.emit(SIGNAL("up()"))
						else:
							self.emit(SIGNAL("down()"))

		except KeyboardInterrupt:
			print "Ação cancelada pelo usuário"



class Interruptor:
	"""docstring for Interruptor"""
	
	def liga(self):
		a = requests.get('https://salty-inlet-77176.herokuapp.com/liga/')
		if a.status_code != 200:
			print("Erro")

	def desliga(self):
		a = requests.get('https://salty-inlet-77176.herokuapp.com/desliga/')
		if a.status_code != 200:
			print("Erro")
		
