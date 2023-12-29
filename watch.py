#!/usr/bin/python
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import time
import os

from timeit import default_timer as timer
from datetime import timedelta
import datetime


class Handler(FileSystemEventHandler):
    def __init__(self, time=datetime.datetime.now()):
        self.time = time

    def on_modified(self, event):
        time.sleep(3)
        print("\n")
        print("Output: ")
        print("\n")
        start = time.time()
        subprocess.run(["python", event.src_path])
        end = time.time()
        elapsed_time = end - start
        print("\n")
        print(
            f"Executed in {elapsed_time:.3f} seconds or {elapsed_time*1000:.2f} milliseconds"
        )


if __name__ == "__main__":
    event_handler = Handler()
    observer = Observer()
    observer.schedule(event_handler, path=".", recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(3)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
