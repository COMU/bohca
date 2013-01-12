import glob
import sys
import os
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
import pynotify
from watchdog.events import FileSystemEventHandler

class MyEventHandler(FileSystemEventHandler):

    def catch_all_handler(self, event):
        logging.debug(event)
        
    def on_moved(self, event):
        self.catch_all_handler(event)
       
    def on_created(self, event):
        self.catch_all_handler(event)
    def on_deleted(self, event):
        self.catch_all_handler(event)
    def on_modified(self, event):
        self.catch_all_handler(event)
        notification = event.src_path
        pynotify.init("uyari")
        msg = pynotify.Notification(notification)
        msg.show()

def main():
  logging.basicConfig(level=logging.DEBUG)
                     #format='%(asctime)s - %(message)s',
                      #     datefmt='%Y-%m-%d %H:%M:%S')

 
#logging.basicConfig(level=logging.INFO)
  path="/home/mehtap/Desktop/bohca/"
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

