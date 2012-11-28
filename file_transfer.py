from sys import exit
import socket

class ayar(object):

	def baglanti(self):
		s = socket.socket()
                sunucu = "127.0.0.1"
                port = 21
                deger= s.connect((sunucu,port))
		print "fonksiyondan donen deger: ",deger

		s.send(yazi)
                self.veri = s.recv(1024)
                s.close()
		return self.veri
 
class dosya(object):

	def __init__(self):
		self.number = 0
	def dosya_gon(self):
		print "sunucuya gondermek icin bir yazi giriniz: "
		yazi = raw_input()

		return 'ayar'	

		s = ayar()
		s.baglanti()

a = dosya()
a.dosya_gon()

#print a.veri

#file_trans = dosya("dosya_gon")		
