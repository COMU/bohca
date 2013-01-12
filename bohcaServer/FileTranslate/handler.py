import os, sys, logging
from git import *
 
class GitHandler:
	
	def __init__(self):
		current_path = os.environ["HOME"] 
		self.file_path = current_path+"/bohca" # file is created in this path 
		repo = Repo(current_path+"/bohca")
		assert repo.bare == False
		
		self.file_name = raw_input("Enter the file name:")

		self.origin = repo.remotes.origin  #	
	
	# to exit the program
	def exit_program(self):
        	print "exit the program"
        	print "Good Bye"
        	sys.exit()

	def push_file(self, commit_message = "the file which is changed"):
		if self.file_name:
			#check file is created or not
			try:
				f = open(self.file_path+ self.file_name, "r")
				logging.warn('file was found')
				f.close()  #file is closed
				
				logging.basicConfig(format='%(message)s %(filename)s', level=logging.DEBUG)
			except IOError:
				logging.warn('file was not found')
				f = open(self.file_path+self.file_name, "w")
				f.close()

				logging.basicConfig(format='%(message)s %(filename)s', level=logging.DEBUG)

			#file and commit message is pushed here
		
			self.origin.push(self.file_name)
			self.origin.push(self.commit_message)
		else:
			logging.warn('please specify the file name!')

	
if __name__ == "__main__":
	git_handler = GitHandler()
	git_handler.push_file()
	git_handler.exit_program()
