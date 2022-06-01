
"""
Variables in class

two types of variables:
1) class variables
2) instance variables
"""

# class variables
# class variables share the same state to the all instances of the class


# instance variables state will vary from one instance to another instance of class(self variables)


class Student:
    # class variables
    school_name = "Zphs school"




obj1 = Student()
obj2 = Student()
obj3 = Student()

print(obj1.school_name)
print(obj2.school_name)
print(obj3.school_name)

# lets update school name with class name
Student.school_name = "Private school"

print(obj1.school_name)
print(obj2.school_name)
print(obj3.school_name)


# lets try to update school name with instance not with clas
# note : only that particular school name get affected
obj1.school_name = "Instance update school"


print(obj1.school_name)
print(obj2.school_name)
print(obj3.school_name)


# Note: class variables shares the same state to all instance of the class
#      2) any changes to class variables with class name reference , then affect the all objects.
#      3) any changes to class variables with instance reference,
#         then that change will affect on that instance

# db connection, headers





# Example on instance variables:
# data is dynamic in instance variables(self variables)

class Department:
    # class variables
    company = "Wipro"
    def __init__(self, name, id, manager):
        # instance variables
        self.__name = name # private variables
        self.__id = id   # private variables
        self.manager = manager # public variable

    def get_dept_id(self):
        return self.__id


# note: instance variables can't access with class name reference,
#       but class variables can access with instance reference

dept1 = Department(name="IT", id='666', manager="AV rao")
# print(dept1.manager)
# print(dept1.id)
dept2 = Department(name="Hardware", id='667', manager="AV rao1")
# print(dept2.manager)
# print(dept2.id)
dept2.manager = "Kiran"
print(dept2.manager)
print(dept2.get_dept_id())

print(dept1.manager)
print(dept1.get_dept_id())




# private variables: private variables can be defined with __ prefix,
# these variables can access only within class



