"""
Modules and packages in python
------------------------------

what is module?
--> module is nothing but file with extension .py, every python file is an module.

what is package?
--> package is nothing collection modules or sub packages and having some name space


Note: to write modular code , easily maintain and readable


college:

employees --> package name


students --> package name


college
  __init__.py
  -- employees
      __init__.py
      --> a.py
      --> b.py
      --> c.py
  -- student
      __init__.py
      --> student.py
      --> exam.py
  -- transport
      __init__.py
      --> bus.py
      --> routes.py
      --> fee.py
  -- admin
      __init__.py
      --> fee.py
      --> onboarding


built - in modules:
------------------

1) os
2) sys
3) json
4) request
5) datetime
6) yaml
7) numpy and pandas


OS Module in Python with Examples


* The OS module in Python provides functions for interacting with the operating system.
* OS comes under Python’s standard utility modules.
* This module provides a portable way of using operating system-dependent functionality.
 The *os* and *os.path* modules include many functions to interact with the file system.

"""
import os
# it is an built -in module

folder_name = "TestDir"

# create folder using os module
#os.mkdir(folder_name)

# nested dirs
my_path = 'photos\myphotos\Test123\A\B'
#os.makedirs(my_path, exist_ok=True)


#my_path = 'photos\myphotos\Test123\A'
# delete dirs
#os.rmdir(my_path)

my_path = "photos"
import shutil

shutil.rmtree(my_path, ignore_errors=True)



# how do we check given path is file or dir?
path = 'TestDir/abc.txt'

if os.path.isdir(path):
    print("Path is the folder path")

if os.path.isfile(path):
    print("path is the file path")


my_file_path = 'TestDir/abc.txt'
# how do we check file exists in path?
if os.path.exists(my_file_path):
    print("Path is valid")

# copying data from one folder to another folder?
source = 'TestDir'
destination = 'MyDir/rr/ee'

# lets create this dir if not exits
# if not os.path.exists(destination):
#     os.mkdir(destination)

#shutil.copytree(source, destination)




# how do we join two paths

dir_name = "TestDir"
file_name = "abc.txt"
file_path = os.path.join(dir_name, file_name)
print(file_path)












