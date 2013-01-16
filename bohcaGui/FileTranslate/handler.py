import os, sys, logging
from git import *
 
class GitHandler:
	
	def __init__(self):
		
		current_path = os.environ['HOME'] # working directory is gotten and current_path value was assigned. 
		 
		self.repo = Repo(current_path+'/bohca') # we have repo so we can use this command. but if we haven't repo we must use other repo command.
		assert self.repo.bare == False

		#self.origin = self.repo.remotes.origin  	
		self.index = self.repo.index # to use repo's index.

	def push_file(self, file_name, commit_message="gonderildi"):

		#file and commit message is pushed here
		
		self.index.add([file_name])  # we must add files to pushing files. So we add local repository (index) .
		new_commit = self.index.commit(commit_message) # after we add files in index, we must enter commit message. 
			
		o = self.repo.remotes.origin # we get remote which is origin.
		o.fetch() # fetch, pull and push from and to the remote
		o.pull()
		o.push()
		
		print "exit the program .Good Bye!"
		sys.exit()		

if __name__ == "__main__":
	git_handler = GitHandler()
