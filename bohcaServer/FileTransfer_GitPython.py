import os, sys, logging
from git import *
 
repo = Repo("/home/kancer/bohca/")
assert repo.bare == False

select_repo = str(raw_input("Enter repo name:"))
test_remote = repo.create_remote(select_repo,'git@github.com:COMU/bohca.git') # create repo

current_index = os.getcwd
path = current_index + "/.git"
print(path)

os.chdir(path) #change working directory
file_config = open("config","r")

###############################
#while #eof kontrolü yap
#	file_config.readline()
	#depo ismini ara


def exit_program():
        print "exit the program"
        print "Good Bye"
        sys.exit()

while True:

	commit_message = raw_input("Enter your commit message: ")

	choose = str(raw_input("If you want choose a file from your PC, you enter (B/b): "))
	if choose == 'B' or choose == 'b':
		
		
		os.system("xdg-open /home/kancer/bohca")

	elif choose != 'B' or choose != 'b':
        	file_name = raw_input("Enter the file name:")
        	if file_name:
                	try:
                        	f = open(file_name, "r")
                        	logging.warn('file was found')
                        
				#dosyanin var olup olmadiginin kontrolu
                        	path = os.path.abspath(file_name)
                        	flag = os.path.isfile(path)
                        	if flag == True:
                                	logging.warn('file has been had')

                	except IOError:
                         	logging.warn('file not found')
                         	open(file_name, "w")
								
				logging.basicConfig(format='%(message)s %(filename)s', level=logging.DEBUG)
				
				logging.info('created new file the name of')
				
			

                	exit_program()

        	else:
                	 logging.warn('Please specify the file name!')

		

		index = repo.index
		file_add = index.add([file_name])
		new_commit = index.commit(commit_message)
		file_add.push(file_name)
		new_commit.push()
	
		devel = repo.remotes.devel # get default remote by name
		ref = devel.refs
		d = devel.name
		d.fetch()
		d.pull()
		d.push()

		print "references: %s" %ref
		
		file_name.close()
