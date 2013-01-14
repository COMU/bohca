import os, sys, logging
from git import *

current_path = os.environ["HOME"]
repo = Repo(current_path+"/bohca")
assert repo.bare == False

#check repo is empty or full
def remote_is_empty():
        direc_inc = os.listdir(current_path+"/"+select_remote)
        print direc_inc
        if direc_inc == " ":
                return True
        else:
                return False
# to exit the program
def exit_program():
        print "exit the program"
        print "Good Bye"
        sys.exit()

def choose_file():

        file_name = raw_input("Enter the file name:")
        commit_message = raw_input("Enter your commit message: ")
        if file_name:
                #check file is done or not
                try:
                        f = open(current_path+"/bohca/"+file_name, "r")
                        logging.warn('file was found')
			f.close()
			
                        logging.basicConfig(format='%(message)s %(filename)s', level=logging.DEBUG)
                        path = os.path.abspath(file_name)
                        flag = os.path.isfile(path)
                        if flag == True:
                                logging.warn('file has been had')

                except IOError:
                         logging.warn('file not found')
                         f =  open(current_path+"/bohca/"+file_name, "w")
			 f.close()

                         logging.basicConfig(format='%(message)s %(filename)s', level=logging.DEBUG)
                         logging.info('created new file the name of '+"'"+file_name+"'")
		
                index = repo.index
                file_add = index.add([file_name])
		
		origin =repo.remotes.origin
		origin.push(file_name)
    		origin.push(commit_message)

        else:
                logging.warn('Please specify the file name!')

while True:
	select_remote = str(raw_input("Enter remote name:"))
	
	# we must check remote name.
	if select_remote == " " or select_remote == "":
		choose_file() #we will choose file that we want to commit it.
		break
	repo_register_file = open(current_path+"/bohca/.git/config","r")
	dizi = repo_register_file.readlines()
	#check repo is created in the past
	if  '[remote "'+select_remote+'"]\n' in dizi:
        	if remote_is_empty() == True:    # if repo which created in the past is empty
                	logging.basicConfig(format='%(message)s', level=logging.DEBUG)
                	logging.info("this repo have been created.")
                	choose = str(raw_input("if you want create new remote enter(C/c) or you can pass"))
                	if choose == "C" | choose == "c":
                        	select_remote = str(raw_input("Enter remote name:"))
                        	flag = remote_is_empty() # if user choose repo which created in the past, it is false for this program so we must check it.
                        	if flag == True:  # if repo is empty
                               		test_remote = repo.create_remote(select_remote,'git@github.com:COMU/bohca.git') # create repo
                        	else:
                                	logging.basicConfig(format='%(message)s', level=logging.DEBUG)
                                	logging.info("this repo have been created. you must choose another repo name!")
                                	continue
			
                	cloned_repo = repo.clone(current_path+"/"+select_remote)
        	else:
                	logging.basicConfig(format='%(message)s', level=logging.DEBUG)
                	logging.info("this repo is not empty. please select another repo!")
                	continue
	else:
        	logging.basicConfig(format='%(message)s', level=logging.DEBUG)
        	logging.info("the name of repo is "+"'"+select_remote+"'"+" is created")
        	test_remote = repo.create_remote(select_remote,'git@github.com:COMU/bohca.git') # create repo   

exit_program()
