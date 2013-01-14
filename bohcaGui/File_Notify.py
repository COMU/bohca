import sys
import os
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
import pynotify
from watchdog.events import FileSystemEventHandler
from FileTranslate.handler import *
#from messages import *
class MyEventHandler(FileSystemEventHandler):

    def __init__(self):
	self.git_handler = GitHandler()

    def catch_all_handler(self, event):
        logging.debug(event)

    def on_moved(self, event):
        self.catch_all_handler(event)
        
        f = event.src_path.split(".spx")
        
        if not pynotify.init("icon-summary-body"):
           sys.exit(1)
        msg = pynotify.Notification(
                         "Notification",
                         f[0] + "dosyanin ismi degisti",
                         "notification-message-im")
        msg.show()
    def on_created(self, event):
        self.catch_all_handler(event)
        #f = event.src_path.split(".spx")
        f = []
        
        f = event.src_path.split('/')
        
        dosya = f.pop()
        if dosya[0] != ".":
             
           if not pynotify.init("icon-summary-body"):
               sys.exit(1)
        
           msg = pynotify.Notification(
                         "Notification",
                         dosya + " "+"isimli dosya yeni olusturuldu",
                         "notification-message-im")
           msg.show()
           gonderilen = dosya
           print gonderilen 
	   self.git_handler.push_file(gonderilen)
           print "calisiyor"
           #self.git_handler.exit_program()
    def on_deleted(self, event):
        f = []

        f = event.src_path.split('/')

        dosya = f.pop()
        if dosya[0] != ".":

           if not pynotify.init("icon-summary-body"):
               sys.exit(1)

           msg = pynotify.Notification(
                         "Notification",
                         dosya + " "+"isimli dosya silindi",
                         "notification-message-im")
           msg.show()
           gonderilen = dosya


    def on_modified(self, event):
        self.catch_all_handler(event)

        
def main():
  logging.basicConfig(level=logging.DEBUG)
 
  path=os.getenv('HOME')+"/BOHCA/bohca"
  event_handler = MyEventHandler()
  observer = Observer()
  observer.schedule(event_handler, path, recursive=True)
  observer.start()

  try:
             while True:
                 time.sleep(1)
               # print "sleep"
  except KeyboardInterrupt:
            observer.stop()
            observer.join()
if __name__ == '__main__':
      main()

