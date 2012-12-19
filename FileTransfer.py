import sys, os
from pygit2 import init_repository, Signature, Commit, Repository

bare = False
repo = init_repository('test',bare)

author = Signature('Kancer Ezeroglu','ezeroglukancer@gmail.com')
committer = Signature('Kancer Ezeroglu','ezeroglukancer@gmail.com')
tree = repo.TreeBuilder().write()
repo.create_commit('refs/heads/master',author,committer,'my first commit',tree,[])


def exit_program():
	print "exit the program"
	print "Good Bye"
	sys.exit()
while True:
	file_name = raw_input("Enter the file name:")
	if file_name:
		try:
			f = open(file_name, "r")
			print "file was found"
                       
			#dosyanin var olup olmadiginin kontrolu gereksiz gibi.

			path = os.path.abspath(file_name)
			flag = os.path.isfile(path)
			if flag == True:
				print "file has been had"

        	except IOError:
           		 print "file not found"
			 open(file_name, "w")	
			 print "created new file the name of %s" %file_name

        	exit_program()

	else:
       		 print "Please specify the file name!"

#file_name.close()
#file_name.read()
#dosya silmek : import os os.remove(file_name) os.rename("file.txt","file2.txt")
#dosyanin yolunu veriyor os.path.abspath("test.txt")
#os.path.basename() tam tersi islem yapiyor
#os.path.isfile("yol") bu da verilen yolun bir dosya olup olmadigini

