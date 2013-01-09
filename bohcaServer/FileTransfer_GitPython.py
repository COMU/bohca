import os, sys, logging
from git import *

current_path = os.environ["HOME"]
repo = Repo(current_path+"/bohca")
assert repo.bare == False

select_repo = str(raw_input("Enter repo name:"))

repo_register_file = open("/home/kancer/bohca/.git/config","r")
dizi = repo_register_file.readlines()

#check repo is empty or full
def repo_is_empty():
        direc_inc = os.listdir("/home/kancer/"+select_repo)
        print direc_inc
        if direc_inc == " ":
                return True
        else:
                return False

#check repo is created in the past
if  '[remote "'+select_repo+'"]\n' in dizi:
	if repo_is_empty() == True:    # if repo which created in the past is empty
		logging.basicConfig(format='%(message)s', level=logging.DEBUG)
                logging.info("this repo have been created.")
                choose = str(raw_input("if you want create new repo enter(C/c) or you can pass"))
                if choose == "C" | choose == "c":
                	select_repo = str(raw_input("Enter repo name:"))
			flag = repo_is_empty() # if user choose repo which created in the past, it is false for this program so we must check it.
			if flag == True:  # if repo is empty
				test_remote = repo.create_remote(select_repo,'https://github.com/COMU/bohca.git') # create repo
			else:
				logging.basicConfig(format='%(message)s', level=logging.DEBUG)
                		logging.info("this repo have been created. you must choose another repo name!")
				#burada tekrar basa donup yeni bir depo sectirmesi gerekiyor

                cloned_repo = repo.clone("/home/kancer/"+select_repo)
        else:
        	logging.basicConfig(format='%(message)s', level=logging.DEBUG)
                logging.info("this repo is not empty. please select another repo!")
                #select_repo = str(raw_input("Enter repo name:"))
		#burada tekrar depo sectirip deponun var olup olmadigi kontrol edilmeli
else:
	logging.basicConfig(format='%(message)s', level=logging.DEBUG)
        logging.info("the name of repo is "+"'"+select_repo+"'"+" is created")
        test_remote = repo.create_remote(select_repo,'https://github.com/COMU/bohca.git') # create repo
        cloned_repo = repo.clone("/home/kancer/"+select_repo)   #clone da hata olusuyor nedeeeennnnn.........

def exit_program():
        print "exit the program"
        print "Good Bye"
        sys.exit()

while True:

	commit_message = raw_input("Enter your commit message: ")
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
		exit_program()
        else:
        	logging.warn('Please specify the file name!')
