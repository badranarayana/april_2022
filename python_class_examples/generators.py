"""
Generators in python

"""
"""
--> generator functions are a special kind of function that return a lazy iterator
 by using yield keyword.

--> we use generators when dealing with large data sets
"""

"""
Example 1: Reading Large Files

A common use case of generators is to work with data streams or large files, 
like CSV files. These text files separate data into columns by using commas.
 This format is a common way to share data. Now, 
 what if you want to count the number of rows in a CSV file? 
 The code block below shows one way of counting those rows:


csv_gen = csv_reader("some_csv.txt")
row_count = 0

for row in csv_gen:
    row_count += 1

print(f"Row count is {row_count}")

def csv_reader(file_name):
    file = open(file_name)
    result = file.read().split("\n")
    return result

--> file.read().split() loads everything into memory at once, 
    causing the MemoryError.


--> Write the same function in generator function

def csv_reader(file_name):
    for row in open(file_name, "r"):
        yield row

--> write same functionality with generator expression (also called a generator comprehension
csv_gen = (row for row in open(file_name))

In this version, you open the file, iterate through it, and yield a row.
 This code should produce the output, with no memory errors:


Example 2: Generating an Infinite Sequence
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

note: next() function is used to get next value from generator object
"""

# generator expression (also called a generator comprehension
# Building Generators With Generator Expressions
"""
generator expressions allow you to quickly create 
a generator object in just a few lines of code. 

Note: They’re also useful in the same cases where list comprehensions are used

example:
------

(<expression> <loop> <condition>)

example:
-------
nums_squared_gc = (num**2 for num in range(5))

"""


def my_sequence(num):
    print("First statement")
    start = 0
    while start <= num:
        print("Inside while loop")
        yield start
        start += 1

    print("Last statement")

obj = my_sequence(5)
print(obj)
# next()
print(next(obj))
print(next(obj))


#  example

def infinate_sequence():
    print("first line")
    start = 0
    while True:
        yield  start
        print("after yield")
        start += 1

obj = infinate_sequence()
print("---------------------------")
#print(next(obj))
print("Hello")
#print(next(obj))
#print(next(obj))
print("how are you")

#print(next(obj))

print(next(obj))
print(next(obj))



def praveen():
    yield "Hi Vamsi"
    yield "I am fine, how are you doing"


def vamsi():
    yield "Hi Praveen, How are you!"
    yield "I am doing good, whats up"


praven_msg = praveen()
vamsi_msg = vamsi()

print(next(praven_msg))
print(next(vamsi_msg))
print(next(praven_msg))
print(next(vamsi_msg))

# StopIteration error
print(next(vamsi_msg))






