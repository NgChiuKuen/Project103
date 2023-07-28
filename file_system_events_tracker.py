import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:\Users\rebec\Downloads>"

class FileEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"Event: {event.event_type} - File: {event.src_path}")

    def on_modified(self, event):
        print(f"Event: {event.event_type} - File: {event.src_path}")

    def on_moved(self, event):
        print(f"Event: {event.event_type} - File: {event.src_path}")

    def on_deleted(self, event):
        print(f"Event: {event.event_type} - File: {event.src_path}")


if __name__ == "__main__":

    observer = Observer()
    observer.schedule(FileEventHandler(), from_dir, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()