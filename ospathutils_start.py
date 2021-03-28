#
# Example file for working with os.path module
#
import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
  file = "textfile.txt"
  # Print the name of the OS
  print(os.name)
  
  # Check for item existence and type
  print("Item exists: " + str(path.exists(file)))
  print("Itme is a file: " + str(path.isfile(file)))
  print("Item is a directory " + str(path.isdir(file)))
  
  # Work with file paths
  print("Item path: " + str(path.realpath(file)))
  print("Item path and name: " + str(path.split(path.realpath(file))))
  
  # Get the modification time
  t = time.ctime(path.getmtime(file))
  print(t)
  print(datetime.datetime.fromtimestamp(path.getmtime(file)))
  
  # Calculate how long ago the item was modified
  td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime(file))
  print("It has been " + str(td) + " since the file was modified")
  print("Or, " + str(td.total_seconds()) + " seconds")
  
if __name__ == "__main__":
  main()
