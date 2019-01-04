#-*-coding: utf-8-*-
from socket import *
from cryptography.fernet import Fernet as fern
from sys import argv
from optparse import OptionParser as op
from platform import python_version as pv
from platform import platform as p
from os import system
from threading import Thread

class Character:
	def __init__(self):
		pass
class Server:
	def __init__(self, host, port , lisent, key):
		if str(pv())[0] == "3":
			raw_input = input
		if str(p())[0] == "W":
			clear = "cls"
		else:
			clear = "clear"
		self.f = fern(key)
		self.l = lisent
		self.sock = socket(AF_INET, SOCK_STREAM)
		try:
			self.sock.bind((host, port))
		except Exception as e:
			print(e)
			exit()
		self.sock.listen(self.l)
		self.sock.settimeout(0.0)
		self.conns = {}
		w = Thread(target=self.wait)
		w.daemon = True
		w.start()
		h = Thread(target=self.heartoall)
		h.daemon = True
		h.start()
		c = ""
		costum_clear = clear
		while c != "exit":
			c = raw_input(">")
			
			if c == costum_clear:
				system(clear)
			elif c[:17] == "set costume clear":
				costum_clear = c[18:]
		self.sock.shutdown(1)
		self.sock.close()


	def wait(self):
		while True:
			while len(self.conns) < self.l:
				try:
					conn, addr = self.sock.accept()
					conns[conn] = Character()
				except:
					pass
	def heartoall(self):
		while True:
			for client in self.conns:
				try:
					msj = client.recv(1024)
				except:
					pass
				else:
					process(msj, client)
	def process(self, m, c):
		cmd = self.f.decrypt(m)
		cmd = cmd.decode()
		print(cmd)

if __name__ == '__main__':
	opts = op("Usage: %prog [options] [values]")
	opts.add_option("-H","--host",dest="host",help="Set server's host. (default value = 127.0.0.1) (type = string)",default="127.0.0.1", type="string")
	opts.add_option("-p","--port",dest="port",help="Set server's port. (default value = 5000) (type = int)", default=5000, type="int")
	opts.add_option("-k","--key",dest="key",help="Set cryptography key. (default value = M2fg-uTtmo5BNeMoq4U1OfVmgAomY2897J4eYct4jII=) (type = string)", default="M2fg-uTtmo5BNeMoq4U1OfVmgAomY2897J4eYct4jII=", type="string")
	opts.add_option("-l","--listen",dest="listen",help="Set how many players can be connected at the same time. (default value = 2) (type = int)", default=2, type="int")
	(o, argv) = opts.parse_args()
	o.key = o.key.encode()
	s = Server(o.host, o.port, o.listen, o.key)