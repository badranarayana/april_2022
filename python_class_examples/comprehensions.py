"""
"""
"""
comprehension:
-------------
it is an process of creating iterable object from existing iterables by applying some conditions 
in single line syntax

1) list comprehension 
2) dict comprehension
3) tuple comprehension/generator expression

"""

# list comprehension
# list comprehension is an process of creating new list from existing iterable by applying some conditions
# in single line
"""
syntax:
------

out = [<expression> <loops> [<conditions>]]
"""

# write a program to find all even number by using list comprehension

data = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

even_numbers = [i for i in data if i % 2 == 0]
print(even_numbers)


# write a program to convert all strings to title case?
data = ['badra', 'srinu', 'ramu']
out = [name.title() for name in data]
print(out)

# out = []
# for name in data:
#     out.append(name.title())
# print(out)


# list comprehension always returns the list

companies = ['wipro', 'capgemini', 'tcs', 'oracle', 'infosys']

blocked_companies = ['capgemini', 'oracle']

out = [company for company in companies if company in blocked_companies]
print(out)


# write a program to multiply every item in list by 3
out = [i * 3 for i in range(1, 10)]
print(out)



# 2 dict comprehension:
"""
is  a process of creating new dict from existing iterable object by applying some conditions or modification

syntax:
{<expression> <loops> [<conditions>] }

note: condition is optional in comprehensions

"""

data = [1, 2, 3, 4, 5]
# {0:1, 1:2, 2:3, 3:4, 4:5}

out = {index:val for index, val in enumerate(data)} # dict
print(out)

# set comprehension

data = [1,2,2,2,3,3,3,44,4,444]
out = {i for i in data} # set
print(out)

# write a program to swap key an values?

data = {'a': 1, 'b': 2, "c": 3}

# {1: 'a', 2:'b', 3:'c'}

out = {val: key for key, val in data.items()}
print(out)


# 3 generator expression or tuple comprehension
#----------------------------------------------
"""
tuple comprehension used create generator object in single line expression

syntax:
------

out = (<expression>  <loops> [<conditions>])

what is the return data type tuple comprehension?
--> it returns the generator object.


"""

out = (i for i in range(5))

print(next(out))
print(next(out))
print(next(out))
print(next(out))
print(next(out))
#print(next(out))

out = [i for i in range(5)]
print(out)






