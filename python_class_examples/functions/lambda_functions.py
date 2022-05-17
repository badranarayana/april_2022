"""

"""


"""
what is lambda function?
--> lambda is an anonymous function, we no need to give name while defining lambda function
--> we use lambda keyword to define lambda function
--> lambda function always returns the function object, not values like def function
--> lambda function is restricted to single line expression

syntax:
------


lambda arguments: <expression>



When will we use lambda function?
--> lambda functions mainly used for inline purpose and instantly 
   scenarios like sorting list, list comprehension, map, filter() functions

"""


my_func = lambda x, y: x + y
print(my_func)
print(my_func(3, 4))


def add(x, y):
    return x + y

print(add)
print(add(3, 4))


# write a program  sort the list by using key parameter in sorted function?
data = [
    {'name': "Badra", 'age': 26},
    {'name': "vamsi", 'age': 22},
    {'name': "praveen", 'age': 24},
    {'name': "mahesh", 'age': 29}
]

# asc
# [
#     {'name': "vamsi", 'age': 22},
#     {'name': "praveen", 'age': 24},
#     {'name': "Badra", 'age': 26},
#     {'name': "mahesh", 'age': 29}
# ]

# lets sort the list by employee age
out = sorted(data, key=lambda jj: jj['age'])
print(out)
# sort by name
out = sorted(data, key=lambda jj: jj['name'])
print(out)




# my_func = lambda x: x * 2
#
# for i in range(10):
#     print(lambda i: i * 2)





data = [(1, 3), (1, 2), (1, 10), (1, 5)]  #List of tuples

out = sorted(data, key=lambda x: x[1])  # key(x)
print(out)



def key_tuple(x):
    return x[1]

out = sorted(data, key=key_tuple)
print(out)


#

def calculate(func, a, b):
    return func(a, b)



def my_add(x, y):
    return x + y

def my_sub(x, y):
    return x - y

out = calculate(func=lambda a, b: a * b, a=10, b= 20)
print(out)

out = calculate(func=my_func, a=10, b= 20)
print(out)


out = calculate(func=my_sub, a=10, b= 20)
print(out)
out = calculate(func=lambda x, y: x - y, a=10, b= 20)
print(out)


# in python functions can be passed as argument to another function

# functional programming in python?
# map( function, iterable object)
# filter(function, iterable object)

# example on map()
# map() is built in function which takes first parameter as function and second as iterable object

# write a program to convert str into int in list?
data = ['1', '2', '3', '4']

# [1, 2, 3, 4]

# classical way using for loop

out = []
for i in data:
    num = int(i)
    out.append(num)
print(out)

# same thing using map()

out = map(lambda x: int(x), data)
print(list(out))

# write a program to convert all strings to upper case

names = ['ramu', 'ravi', 'raghu', 'badra']
out = map(lambda name: name.upper(), names)
print(list(out))


# filter(function, iterable)
out = filter(lambda name: name.startswith('r'), names)
print(list(out))


# even number program using filter

out = filter(lambda x: x % 2 == 0, range(1, 10))
print(list(out))



# difference between def function and lambda function?
"""
  def function                                lambda function
  ->def keyword used to define                -> lambda keyword used to define lambda 
         normal function                                     function
  -> we can give name to the def function     --> anonymous function(no name to function)
  -> return keyword used to return values     --> no return statement used to return the values
                                                  lambda return function object, 
  -> this functions can be reused any where   --> lambda functions mainly used for inline/instance purpose
     by just importing function name              ex: like sorting(), map(), reduce()
     


"""



# what is lambda function?
# lambda function is anonymous function, used for instance purpose
# we use lambda keyword to define function

# what is the main difference between normal(def) and lambda function?
# 1) def used to define normal function, and lambda keyword used to define lambda fun
# 2) def function can have name , but lambda we no need to give name
# 3) normal functions return values, but lambda return function object
# 4) lambda function syntax restricted single line, but in normal functions we write complex logics

from  functools import reduce

# sum of all numbers

data = [1, 2, 3, 4]
out = reduce(lambda x, y: x + y , data)
print(out)






# Home work
# write a program to find out all vowels in given string by using filter
