"""
File handling:

--> reading data from file in computer
--> write data to file in computer

"""

# file_path = 'G:\Suman_IT_Python_2021\python_april_9_10\student details.txt'
#
# # open
# file_obj = open(file_path)
#
# # print content
# print(file_obj.read())
#
#
# # close
# file_obj.close()
#
#
#
# print("---------------------------------------")
# # read another file
#
# file_path2 = 'F:\sample_file.txt'
#
# # open()
# file_obj = open(file_path2)
#
# # print the content
# print(file_obj.read())
#
# # close
# file_obj.close()



# what is file handling in python?
# it is the process of reading and writing files in computer through python programs

# file name --> location of the file where it is stored in computer

#how do you open file in python?
"""
python provides as function called open() to deal with files.

open(filepath, mode)


'r' --> read (you are opening file for only reading)

'w' --> used to write the content to the file, 
       file will be created if doesn't exits already
       note: it will always overwrite the existing content in file
       
 'a'  --> used to write the content to the file and it create file if doesn't exit

'rb' --> read binary (pdf, images)
'wb' --> write binary

"""

# 'w' --> it create file if doesn't exit

file_name = "data/friends.txt"

#file_obj = open(file_name, 'w')
#file_obj.write("content from pythonryrtrtr")
#file_obj.close()

# 'w' mode created the file in data folder
#  and wrote content to that newly created  file

# open file in 'a' mode and write some content
# file_obj = open(file_name, 'a')
# file_obj.write("new string in append mode")
# file_obj.close()


# open file in 'a' mode and check file creating or not ?
# file_name = 'data/locations.txt'
#
# file_obj = open(file_name, 'a')  # it create file as location.txt doesn't exit in data folder
# file_obj.write("I am from append mode \n")    # write content to newly crated file locations.txt
# file_obj.write("I am from append mode2 \n")
# file_obj.close()        # close the file


"""
# when will we use 'a' mode?  
# we use mode 'a' when we want to write content to the existing file
( 'a' mode won't overwrite the data)

"""


# write a program to read the entire content in file?
"""
location_path = 'data/locations.txt'

# lets open file in 'r'
file_obj = open(location_path, 'r')
content = file_obj.read()
file_obj.close()

print(content)
"""


# write a program to write the below lines in to file called locations
"""
locations = ['hyderabad', 'bangalore', 'vizag', 'pune', 'mumbai']

# step #1: open file 'a'
file_path = 'data/locations.txt'
file_obj = open(file_path, 'a')  # using 'a' mode , because locations.tx already has some content
for index, loc in enumerate(locations):
    file_obj.write(str(index) + '\t' + loc + '\n')

# close the file
file_obj.close()
"""


# write a program read content from file a and write to file b?
"""
source_file = 'data/friends.txt'

file_obj = open(source_file, 'r')

for index, line in enumerate(file_obj):
    if index == 0:
        print("Skipping header")
        continue
    location = line.split(",")[2].replace("\n", '')
    print(location)
    if location == 'hyderabad':
        file_hyd = 'data\hyderabad.txt'
        # a mode
        file_hyd = open(file_hyd, 'a')
        file_hyd.write(line)
        file_hyd.close()
    elif location == 'bangalore':
        file_bng = r'data\bangalore.txt'
        # a mode
        file_bng_obj = open(file_bng, 'a')
        file_bng_obj.write(line)
        file_bng_obj.close()

"""

# opening file in context manager

# note: context manager used to close the resource automatically once task completed

with open('data/friends.txt', 'r') as file_obj:

   # it reads entire content of file into memory and return as string
   print(file_obj.readlines())
   print(file_obj.read())
   for line in file_obj:
       pass




