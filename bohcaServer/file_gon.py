import socket
print "Sunucuya gondermek icin bir yazi giriniz : " 
yazi = raw_input()
s = socket.socket() 
sunucu = "localhost" 
port = 8888
s.connect((sunucu, port))
s.send(yazi)
veri = s.recv(1024)
s.close() 
print veri
if __name__ == "__main__":

  main()
