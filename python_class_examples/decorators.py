"""
Decorators:
"""
"""
Decorators in python:
--------------------

A decorator takes in a function, adds some functionality and returns it

--> used to add some extra functionality to existing objects without modifying source code.

syntax:

def outer_func(func):
    def inner_func(*args, **kwargs):
        out = func()
        return out
    return inner_func
"""


# lets assume we have to print all arguments of the function while calling?
# decorator is an function which takes function as argument
# and add some extra behaviour to existing object and return the function object


def log_arguments(func):
    def inner_function(*args, **kwargs):
        print(f"**** $$$$$$ {func.__name__}  --> Arguments: {args} and {kwargs}")
        out = func(*args, **kwargs)  # sub(20, 30)
        return out
    return inner_function



@log_arguments
def add(a, b):
    #print("arguments: ", a, b)
    return a + b

@log_arguments
def sub(a, b):
    #print("arguments: ", a, b)
    return a - b

@log_arguments
def div(a, b):
    #print("arguments: ", a, b)
    return a/b

@log_arguments
def my_func(a, b, c):
    #print(a, b, c)
    return a + b + c


@log_arguments
def get_college_details(college_name):
    return {"college_name": "CBIT"}


print(add(10, 20))
print(sub(20, 30))
print(div(20, 40))
print(my_func(20,30, 40))


print(get_college_details("CBIT"))


# What exactly decorator does in python?
"""
1) Decorator is used to 
add some extra functionality to the object without modifying the source code of object
"""


# lets write some real time use case for decorator

# bank example
bank_accounts = {
    '1234': {"name": "Badra", 'balance': 4000},
    '1235': {"name": "kiran", 'balance': 14000},
    '1236': {"name": "vamsi", 'balance': 500000},

}

# min = 1000

def min_balance_check(func):
    def check_min_balance(*args, **kwargs):
        print(f"input details: {args}, {kwargs}")
        from_account = kwargs.get('from_account')
        from_account_details = bank_accounts.get(from_account)
        balance = from_account_details['balance']
        requested_amount = kwargs.get('amount')
        remaining_balance = balance - requested_amount
        if remaining_balance < 1000:
            raise ValueError("Please maintain min balance, transaction failed.")
        print("Validations passed ....")
        return func(*args, **kwargs)
    return check_min_balance


def check_open_account_min_balance(func):
    def check(*args, **kwargs):
        deposit_amount = kwargs.get('deposit_amount')
        kyc_verified = kwargs.get('kyc_verified')
        if not kyc_verified:
            raise ValueError("Kyc verification required to open account")
        if deposit_amount < 1000:
            raise ValueError("At least deposit min balance to open an new account")
        return func(*args, *kwargs)
    return check

@min_balance_check
def transfer_amount(from_account='', to_account='', amount=None):
    account_details = bank_accounts[from_account]
    print("Connecting to gateway and transfer amount ")
    print("Transaction success")

@check_open_account_min_balance
def open_account(kyc_verified=False, deposit_amount=None):
    print("opening account")
    print("Done...")

#transfer_amount(from_account='1234', to_account='1235', amount=5500)

open_account(kyc_verified=True, deposit_amount=1000)

















