import os, sys, logging
from git import *


 
class GitHandler:
	
	def __init__(self):
		current_path = os.environ['HOME'] 
		 
		repo = Repo(current_path+'/BOHCA/bohca')
		assert repo.bare == False
		

		self.origin = repo.remotes.origin  	
	
	# to exit the program
	def exit_program(self):
        	print "exit the program"
        	print "Good Bye"
        	sys.exit()

	def push_file(self, file_path, commit_message="gonderildi"):

		#file and commit message is pushed here
		
		self.origin.push(file_path)
		self.origin.push(commit_message)

	
if __name__ == "__main__":
	git_handler = GitHandler()
        
        	
