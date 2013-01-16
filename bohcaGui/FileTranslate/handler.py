import os, sys, logging
from git import *
 
class GitHandler:
	
	def __init__(self):
		
		current_path = os.environ['HOME'] 
		 
		self.repo = Repo(current_path+'/bohca')
		assert self.repo.bare == False
		self.origin = self.repo.remotes.origin  	
		self.index = self.repo.index

	def push_file(self, file_name, commit_message="gonderildi"):

		#file and commit message is pushed here
		
		self.index.add([file_name])
		new_commit = self.index.commit(commit_message)
			
		o = self.repo.remotes.origin
		o.fetch()
		o.pull()
		o.push()
		
		print "exit the program .Good Bye!"
		sys.exit()		

if __name__ == "__main__":
	git_handler = GitHandler()
