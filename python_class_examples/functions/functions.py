"""
"""
"""
Functions:
---------
--> function is nothing but a named block of reusable code, 
--> function can reused any where and any number of times


python provides two types of functions:

1) def function (normal function)
2) lambda function( anonymous function(no name to function)


1) syntax:

def <function_name>(arguments/parameters):
    -- statements

"""


# let define function to add two number and return value back to caller
def add(a, b): # a and b are arguments/parameters
    return a + b


# calling function
out = add(10, 20)
print(out)
print(add(30, 30))
print(add(40, 30))


def sub(a, b):
    return a - b


a=20
b = 30
print(sub(a, b))



# write a function to sum the elements of list


def cal_sum(data):
    sum_val = 0
    for val in data:
        sum_val += val
    return sum_val


out = cal_sum([1,2])
print("&&&&&&&&&&&&&&&&&&&&&&&&")
print(out)
out = cal_sum([1, 2, 3, 4, 10, 11, 22, 33])
print(out)


# note: return statement used to return the values from function
# by default python function return None value if no return statement in function

def myfunc():
    print("function is calling")
    return [1,2,2,2]

# call
out = myfunc()
print(out)



def add_fun(a, b, c): # a, b, c are positional required argments
    a = a
    b = b
    c = c
    return a + b + c

# how many arguments needs to pass here?

print(add_fun(10,11, 1))
print(add_fun(11, 12, 3))
print(add_fun(20, 13, 4))
print(add_fun(30, 14, 5))



# write a function to get the all keys value from dict

def get_values(keys, dict_obj):

    for key, val in dict_obj.items():
        if key in keys:
            print(val)




data = {'name': "Badra", 'age': 30, "location": "hyderabad"}

keys = ['age', 'name']

get_values(keys, data)




# arguments types
"""
parameters/arguments
-------------------
1) positional arguments
   --> these arguments needs to pass at any cost, 
   --> required arguments, order is matter while providing argument
2) arbitrary arguments(*args)
    --> allows to pass any number of positional arguments
    --> *args will be available as tuple object inside function
3) default arguments
   --> it uses the default value when we do not provide while calling function
   --> it uses provided value if we provide any while calling function
4) keyword arguments(**kwargs)
   --> allows to pass any number of keyword arguments while calling function
   --> kwargs are available as dict inside a function
"""

# Example on positional arguments

def math_add(a, b): # a and b are positional/ required arguments, mandetory argus
    print(a + b)

# calling function
math_add(30, 20)


# example of arbitrary arguments(*args)
def add_v2(a, b, *args):
    print(args)
    out = a + b

    for i in args:
        out += i
    print(out)

add_v2(10, 3,444,5,5)




# Example on default arguments

def get_country(country='india'):
    countries = {'india': {"county": "India", "iso_code": "IND"},
                 'USA': {'country': "USA", 'iso_code': "US"}}
    return countries.get(country)

print(get_country())



def discount(amount, per=2, **kwargs):
    print(kwargs)
    print(f"you will get {per} % of discount")

discount(1000, per=44, name='badra')




# Examples of **kwargs

def save_student_details(name, id, branch, college_name='CBIT', **kwargs):

    print("STUDENT DETAILS: ")
    print("Name: ",  name)
    print("id: ", id)
    print("branch: ", branch)
    print("college name: ", college_name)
    print("KWARGS: ", kwargs)
    # we connect with database and storing data
    print('Data save successfully')


# call function
save_student_details("Vamsi", "abcnn44", 'ECE',
                     college_name="JPNC",
                     home_location="Hyd",
                     bus_route="Via ameerpet")



# write a function to handle all type of arguments

def my_func(a, b, *args, location="Hyderabad", **kwargs):
    """
    :param a:  is positional argument
    :param b:  is positional argument
    :param args: is arbitrary positional argument
    :param location: is default argument
    :param kwargs: keyword arguments
    :return:
    """
    print(a)
    print(b)
    print(args)   # data type: tuple
    print(location)
    print(kwargs)  # data type dict

my_func(10, 20,30, 30, 44,33, 44, movie_name="KGF-2", time="2:30PM")
my_func(10, 20)



# What is the order of arguments in funtion?
# 1) positional, 2) arbitrary positional arguments, 3) default 4) kwargs










# write a function to find the even number using function?

def isEven(num):
    """
    This function return True if given value is even number else False
    :return: Bool
    """
    if not num:
        raise ValueError("Num is required field")

    if num % 2 == 0:
        return True
    else:
        return False

print(isEven(5))

# write a program to figure all even numbers between 2 to 100?
data = range(2, 101)

for num in data:
    if isEven(num):
        print(num)


# write a program to find the employees whose salary is less than 5000

data = [
    {'name': "Vinay", 'salary': 20000},
    {'name': "sandya", 'salary': 50000},
    {'name': "mahesh", 'salary': 120000},
    {'name': "kiran", 'salary': 500000},
]

def find_employees(employees, filter_val=50000, operation='min'):
    """
    This is the help doc of find employee
    :param employees:
    :param filter_val:
    :param operation:
    :return:
    """

    for employee in employees:
        salary = employee['salary']
        if operation == 'min':
            if salary <= filter_val:
                print(employee)
        elif operation == 'max':
            if salary > filter_val:
                print(employee)


find_employees(data, filter_val=20000, operation='max')
print(help(find_employees))



# write a program to find the states whose population is lessthan 50000

def find_state_less_population(database):
    for state in database:
        population = state['population']
        if population <= 50000:
            print(state)


database = [
    {'state_name': "TG", "population": 4000000000},
    {'state_name': "KA", "population": 5000000000},
    {'state_name': "AP", "population": 40000},
]

find_state_less_population(database)
















