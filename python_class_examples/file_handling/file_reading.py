"""
File handling:

--> reading data from file in computer
--> write data to file in computer

"""

file_path = 'G:\Suman_IT_Python_2021\python_april_9_10\student details.txt'

# open
file_obj = open(file_path)

# print content
print(file_obj.read())


# close
file_obj.close()



print("---------------------------------------")
# read another file

file_path2 = 'F:\sample_file.txt'

# open()
file_obj = open(file_path2)

# print the content
print(file_obj.read())

# close
file_obj.close()


