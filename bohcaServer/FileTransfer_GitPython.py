import os, sys
from git import *


repo = Repo("/home/kancer/bohca/git-python")
assert repo.bare == False

#test_remote = repo.create_remote('depo','git@github.com:COMU/bohca.git') # create repo

def exit_program():
        print "exit the program"
        print "Good Bye"
        sys.exit()

while True:

	commit_message = raw_input("Enter your commit message: ")

	choose = str(raw_input("If you want choose a file from your PC, you enter (B/b): "))
	if choose == 'B' or choose == 'b':

		#bilgisayrda goz at ciksin..
		print "deneme"

		os.system("xdg-open /home/kancer/bohca")

	elif choose != 'B' or choose != 'b':
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

	

		index = repo.index
		file_add = index.add([file_name])
		new_commit = index.commit(commit_message)
		file_add.push()
		new_commit.push()
	
		devel = repo.remotes.devel # get default remote by name
		ref = devel.refs
		d = devel.name #emin degilim
		d.fetch()
		d.pull()
		d.push()

		print "references: %s" %ref

#sistemden dosya secme olsun.
#repolar nerede olusuyor bak.
