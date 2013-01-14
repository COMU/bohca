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
        
        file = event.src_path.split(".spx")
        
        if not pynotify.init("icon-summary-body"):
           sys.exit(1)
        msg = pynotify.Notification(
                         "Notification",
                         file[0] + "dosyanin ismi degisti",
                         "notification-message-im")
        msg.show()
    def on_created(self, event):
        self.catch_all_handler(event)
        file = event.src_path.split(".spx")

        if not pynotify.init("icon-summary-body"):
           sys.exit(1)
        msg = pynotify.Notification(
                         "Notification",
                         file[0] + " "+"isimli dosya yeni olusturuldu",
                         "notification-message-im")
        msg.show()

    def on_deleted(self, event):
        file = event.src_path.split(".spx")
        if not pynotify.init("icon-summary-bady"):
              sys.exit(1)
        msg = pynotify.Notification(
                         "Notification",
                         file[0] + "silindi",
                         "notification-message-im")
        msg.show() 
       

    def on_modified(self, event):
        self.catch_all_handler(event)

        
def main():
  logging.basicConfig(level=logging.DEBUG)
 
  path=os.getenv('HOME')+'/Bohca'
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

