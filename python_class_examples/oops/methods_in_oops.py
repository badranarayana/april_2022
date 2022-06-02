"""
Method/function

1) instance method
2) class method
3) static method

4) properties

"""

class Employee:
    company_name = "Wipro"
    location = "Hyderabad"
    def __init__(self, emp_id, name): # instance method
        self.emp_id = emp_id
        self.name = name

    def get_employee_details(self):
        return {'employee name': self.name, 'Employee no': self.emp_id}

    @classmethod
    def get_company_details(cls):
        return {'company_name': cls.company_name, 'location': cls.location}






obj = Employee(123, 'kiran')
out = obj.get_employee_details() # instance method, so that we can this method with instance
print(out)

# lets access instance variables
print(obj.emp_id)
print(obj.name)

# class method should call with only
out = Employee.get_company_details()
print(out)
out1 = obj.get_company_details()
# it is not best practice to call  class methods with instance reference
print(out1)


# What is instance method?
"""
by default every function/method is instance method in class and it takes self as argument

class Myclass:
    def method1(self):
        pass

obj = Myclass()
obj.method1()    
"""
# what is class method?
"""
class method can be defined by using @classmethod decorator
class method takes first argument as cls which refers to class name

class Myclass:
   @classmethod
   def mymethod(cls):
       pass

Myclass.mymethod()

# note: we no need to create object to access class methods
"""

# what is static method?
"""
We can define static method with @staticmethod decorator, but static method won't take self or cls as
default argument,

# static method can be call with class name as well as instance

"""


class Myclass:

    @staticmethod
    def calculate(num1, num2):
        return num1 + num2

    def my_func1(self):
        out = self.calculate(10, 20)
        return out

    @classmethod
    def my_func2(cls):
        out = cls.calculate(30, 40)
        return out


# class method
out = Myclass.my_func2()
print(out)

obj = Myclass()
out = obj.my_func1()

print(out)




# Write a class to read files and format data?


class FileReader:
    def __init__(self, file_path):
        self.data = self.read_data(file_path)

    @staticmethod
    def read_data(file_path):
        with open(file_path, 'r') as obj:
            return obj.readlines()

    def print_content(self):
        print(self.data)

    def print_last_line(self):
        print(self.data[-1])

    def get_line(self, line_num):
        if len(self.data) >= line_num:
            print(self.data[line_num - 1])
        else:
            print("No line found")

    def save_to_db(self):
        print("Connecting with db")
        for row in self.data:
            print("saving into db..", row)
            print("Done")



obj = FileReader('test_data.txt')
obj.save_to_db()
#obj.print_content()
#obj.print_last_line()
#obj.get_line(1)




#out = FileReader.read_data('test_data.txt')
#print(out)



"""
property in python:

Defining Properties in class:
-----------------------------
The @property decorator is a built-in decorator in Python for the property() function. 
Use @property decorator on any method in the class to use the method as a property.

You can use the following three decorators to define a property:

@property: Declares the method as a property.
@<property-name>.setter: Specifies the setter method for a property that sets the value to a property.
@<property-name>.deleter: Specifies the delete method as a property that deletes a property.


Get data
setting data
deleting data

"""


class Student:
    def __init__(self, name, age):
        self.__name = name # Private variables, only access in side class
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if new_age <= 100:
            self.__age = new_age
        else:
            raise ValueError("Age should be less than 100")

    @property
    def name(self):  # getter property
        print("Invoking getter name property")
        return self.__name

    @name.setter
    def name(self, name): # setting value
        print("Invoking Setter property")
        if name.startswith("a"):
            self.__name = name
        else:
            raise ValueError("name should starts with a only")

    @name.deleter
    def name(self):
         print("Delete property invoking")
         del self.__name

print("*******************************************************************")

obj = Student("Badra", 28)
print(obj.name)

obj.name = "aavi"
print(obj.name)

obj.age = 96
print(obj.age)


#del obj.name
#print(obj.name)

# What are the differences between class method and static method?
"""
   class method                                       static method
   ------------                                       -------------
   1) Declare method as class method with help        1) Declare method as static method with help of @staticmethod decorator
      of @classmethod decorator. 
   2) It can access class attributes,                 2) It can't access either class attributes or instance attributes
     but not instance atrributes
   3) it can call by using class name                 3) same 
       myclass.method()
       with object
        obj.method()
   4) class method take first argument as cls         4) no reference args like cls, self

   5) It can be used to create factory method that    5) can't create object as no access to class
      allows to create object of class and return


"""











