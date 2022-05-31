"""
Class examples
"""

"""
----
class
initilizer(__init__())
object/instance
---
variables
 --> class variables
 --> instance variables

methods:
  --> instance methods(self methods)
  --> class methods(cls methods)
  --> static methods(no self or cls )
  --> properties
---------------------
inheritance(reuse)
  --> parent/super class
  --> child/ derived class
  --> overwriting
  --> overloading
  --> super()
"""



"""
What is class?

--> class is nothing but a blueprint which contains member variables and member functions

How do you define class in python?
--> by using class keyword
    ex:
        class MyClass:
            pass
            
        note: class name should follow below naming stanrd
              class myClass:  # wrong way of defining name
                  pass

"""


# define class
class MyClass:

    def __init__(self, name, location):
        print("Init function invoked")
        self.name = name
        self.loc = location

    def print_hello(self):
        print("Hello", self.name)

    def say_good_bye(self):
        print("Good bye.", self.name)

    def print_location(self):
        print(self.loc)


# create instance of the class

obj = MyClass("Vamsi", "HYD")  # python will create object in memory and store reference obj variable
# print(obj)
# print(dir(obj))

obj.print_hello()
obj.say_good_bye()
obj.print_location()


praven_obj = MyClass("Praveen", "Pune")
praven_obj.print_hello()
praven_obj.print_location()


print("-------------------------------")
for name, loc in [("praveen", "Pune"), ("kiran", "HYD")]:
    obj = MyClass(name, loc)
    obj.say_good_bye()
    obj.print_location()
    obj.print_hello()




# Student example

"""
variables:
student_id
name
dob
address
marks
-----

actions:
-------
get_student_grade

get_student_name and student id
"""

class Student:
    def __init__(self, student_id, name, dob, address, marks):
        self.id = student_id
        self.name = name
        self.dob = dob
        self.address = address
        self.marks = marks

    def get_grade(self):
        if self.marks >= 90:
            print("A grade")
        elif self.marks >= 75:
            print("B grade")
        else:
            print("C grade")

    def get_student_identity(self):
        return {'student_id': self.id, 'student_name': self.name}



# create instance
vamsi = Student(student_id="AB123", name="Vamsi",
                dob='10-03-1995', address="Ameerpet, hyd", marks=95)

vamsi.get_grade()


praveen = Student(student_id="AB124", name="praveen",
                dob='10-03-1996', address="panjagutta, hyd", marks=60)

praveen.get_grade()













