"""
Exception Handling in python
"""
"""




"""


# built-in exception types
"""
ValueError
ZeroDivisionError
FileNotFoundError
KeyError
IndexError
NotImplemented

RuntimeError
AttributeError


raise --> used to raise exception 
raise <exception_object>


try:
    pass  # here we call code that may raise exceptions
except <exception class>:
    pass
finally:
    pass
    

"""

# how raise exceptions in python?

def add(a, b):
    if a <= 0:
        raise ValueError("a should be > 0")
    if b <= 0:
        raise ValueError("b should be > 0")

    if a > 10:
        raise RuntimeError("A should be less than 10")

    out = a + b
    print(out)


try:
    add(13, 1)
    print("completed")


except ValueError as error:
    print("Value error")
    print(error.args)
    print("Please pass valid values")
except RuntimeError as error:
    print("RUN time error")
    print(error.args)
except Exception as error:
    print("Exception block")
    print(error.args)

print("HHHHHHHHHHHHHHHHHHHH")


# data = {'a': 10}
#
# try:
#     print(data['a1'])
# except KeyError as error:
#     print("Key error: ", error.args)

# Exception is base class for all type of exception classes



# how to define your custom exception classes and use in code

class InvalidAccount(Exception):
    pass


def validateAccount(num):
    if num < 236:
        raise InvalidAccount("Account is invalid")

try:
    # call function that may raise exception here
    validateAccount(100)

except InvalidAccount as error:
    print(error.args)
except Exception as error:
    print("Exception")
    print(error.args)






class MinBalanceError(Exception):
    pass


def validate_min_balance(bal):
    if bal < 1000:
        raise MinBalanceError("Please maintain min balance")
    print("Balance is ok")

try:
    validate_min_balance(200)
    # close connection
except MinBalanceError as error:
    print(error.args)
finally:
    print("finally block")


# note
# raise keyword used to raise/throw the exception
# except block is used to handle exceptions those are thrown from try block

# finally will always executes irrespective of error or not,  generally we use finally for closing resourses
# like, db connection



