import os, sys, logging
from git import *
 
repo = Repo("/home/kancer/bohca/")
assert repo.bare == False

select_repo = str(raw_input("Enter repo name:"))
depo_register_file = open("/home/kancer/bohca/.git/config","r")
dizi = depo_register_file.readlines()

if  '[remote "'+select_repo+'"]\n' in dizi:
	logging.basicConfig(format='%(message)s', level=logging.DEBUG)
	logging.info("this repo have been created. if you want create new repo, you must enter new repo name!")
else:
	test_remote = repo.create_remote(select_repo,'git@github.com:COMU/bohca.git') # create repo

def exit_program():
        print "exit the program"
        print "Good Bye"
        sys.exit()

while True:

	commit_message = raw_input("Enter your commit message: ")
	#choose = str(raw_input("If you want choose a file from your PC, you enter (B/b): "))
        
	file_name = raw_input("Enter the file name:")
        if file_name:
		#dosyanin var olup olmadiginin kontrolu
        	try:
                	f = open(file_name, "r")
                        logging.warn('file was found')
                        
			logging.basicConfig(format='%(message)s %(filename)s', level=logging.DEBUG)
                        path = os.path.abspath(file_name)
                        flag = os.path.isfile(path)
                        if flag == True:
                                logging.warn('file has been had')

                except IOError:
                         logging.warn('file not found')
                         open(file_name, "w")
								
			 logging.basicConfig(format='%(message)s %(filename)s', level=logging.DEBUG)
		 	 logging.info('created new file the name of '+"'"+file_name+"'")
			 exit_program()

		index = select_repo.index
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
	
        else:
        	logging.warn('Please specify the file name!')
