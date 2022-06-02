"""
Python Inheritance:
------------------
Inheritance allows us to define a class
that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.


# single inheritance
 -> class will is derived from single base class

"""
# base
# keep common code for all child classes
# person

# student
# employee


# define base class
class Base:
    def method1(self):
        print("Method #1 is invoking from base class")

    def method3(self):
        print("Method #3 is invoking from base class")
    def method2(self):
        print("base class logic")

class Mychild(Base):

    def method2(self):
        out = super().method2()
        print("method #2 is invoking from my child class")



obj = Mychild()
obj.method2()

obj.method2()

# MRO - method resolution order



# multiple inheritance

class A:
    def method1(self):
        print("method1 from A")

class B:
    def method3(self):
        print("method2 from B")

class C(B, A):

    def method4(self):
        print("method4 from C")

    # def method1(self):
    #     print("From C ****$$$$$$$$$*********************")

class D(C):
    pass

print(D.__mro__)

obj = C()
obj.method1()
obj.method3()
obj.method4()
print("&&&&&&&&&&&&&&&&&&&&&&&&&&")
objd = D()
objd.method1()
objd.method3()