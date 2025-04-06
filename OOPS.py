'''############# Day14 & 15 ################ 21/03/25 & 24/03/25'''
# --> oops- object oriented programming.
# --> oops is a programming based on the concept of objects.
# --> the objects contains both data and code.
# --> data in the form of properties (often known as attributes) and code in the form of methods(actions objects can perform).

'types of oops : '
# 1.class
# 2.object
# 3.inheritance
# 4.polymorphism
# 5.encapsulation
# 6.abrtaction

'oops terminology:'
# --> attributes also known azs data member or variable.
# --> behaviour also known as member function or method


''' ########### class ##########'''
# --> class is defined with keyword class.
# --> the class is user-defined data structire that binds the data members and methods into single-unit.
# --> class is blueprint or code template for object creation.
# --> using a class, you can create as many objects as you want.

# class ex: mercedes,bmw,toyota etc.
# syntax: class Classname:          # class name can be anything.


# class greeting():             class- class keyword, greetings- classname.
    # print("hello world")          print- class body.


''' ############ self keyword ############'''
# --> self parameters is used to access current class methods and variables.
# --> it does not have to be named self, you can call it whatever you like, but it has to be first parameter of any function  in the class.



''' ############## object ###############'''
# --> an object is simply a collection of data(variables) and methods(functions) that act on those data.
# --> similary, a class is a blueprint for that object.
# --> the object is the instance of a class. 
# --> the process of creating an object can be called instantiation.
# --> there is no memory allocation untill we create its oject.
# --> the objector instance conatins real data or information.
# object examples: chair, bike, marker, pen , table, car etc.
# sytax :  objname = clasname()
# eg:
# class details():            #details- classname.
#     user_name = "harika"        #attritube
#     id = 1234                   #attribute
#     def user_info(self):            # self declaration is must. to access the attributes and variables.
#         #here without self, the result will be an error.
#         print(f"user_name is {self.user_name} this is basic info functionality ")            #till here it is called blue print.
# obj = details()
# print(obj.user_name)
# print(obj.id)
# obj.user_info()


# class details():            #details- classname.
#     user_name = "harika"       
#     id = 1234                   
#     def user_info(self):          
#         print(f"user_name is {self.user_name} this is basic info functionality ")  
#     def user_info_2 (self):
#         print("this is second info method")
#         self.user_info
#         print(self.user_name,self.id)
# obj = details()
# print(obj.user_name)
# print(obj.id)
# obj.user_info()
# obj.user_info_2()


# class mobile_phone():       #class definition
#     brand_name = "samsung"          #attributes
#     color = "white"          #attributes
#     storage = "128gb"          #attributes
#     def calling(self,mobile_name,):
#         print(f"making a phone call from" , mobile_name)
#     def browsing(self,mobile_name):
#         print(f"your are browsing from ", mobile_name)
#     def playing(self,mobile_name):
#         print(f"playing on mobile ", mobile_name)
# samsung = mobile_phone()
# samsung.calling("samsung")
# samsung.browsing("samsung")
# samsung.playing("samsung")
# vivo = mobile_phone()
# vivo.calling("vivo")
# vivo.browsing("vivo")
# vivo.playing("vivo")


''' ###########  __init__ #############'''
# --> __init__ method in oops is nothing but a special fucntion.
# --> special function are the functions that are used to enrich the class.
# --> these can be easily identified as they double underscores on either side.
# --> __init__ method is used to initialize the attributes. it is called a constructor in other programming languages.
# syntax:
# def __init_(self,attribute1,attribute2,......attributen)
    # self.attr1 = attr1
    # self.attr2 = attr2
    # .
    # .
    # .
    # self.attrn = attrn

# class car():
#     def __init__(self,bn,color,model,eng_v):
#         self.bn = bn
#         self.color = color
#         self.model = model
#         self.eng_v = eng_v
#     def driving(self):
#         print(f"you are driving {self.bn}")
#     def engine(self,a):
#         print(f"{self.eng_v} engine {a}",self.model)
# tata = car("tata","white","nexon","2025")
# tata.driving()
# tata.engine("500cc")
# maruti = car("maruthi","black","breeza","2024")
# maruti.driving()
# maruti.engine("1000cc")


" ############ inheritance ############ "
# --> inheritance allows us to define a class that inherits all the methods and properties from another class.
# --> parent class is the class being inherited from , also called base class.
# --> child class is the class that inherits from another class, also called derived class.
# types :
# 1. single inheritance
# 2.multilevel inheritance
# 3.hierarchical inheritance
# 4. multiple inheritance


# class mobile_phone():
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
#     def make_call(self,number):
#         print(f"calling {number} from {self.brand} and {self.model}")
#     def send_message(self,number,message):
#         print(f"sending{message} to {number} from {self.brand} and {self.model}")
# obj = mobile_phone("apple","apple15s")
# obj.make_call(12345)
# obj.send_message("234567","hello evryone")


'# 1. single inheritance:'
# upgrading with smart phone 
# class mobile_phone():
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
#     def make_call(self,number):
#         print(f"calling {number} from {self.brand} and {self.model}")
#     def send_message(self,number,message):
#         print(f"sending{message} to {number} from {self.brand} and {self.model}")
# class smart_phone(mobile_phone):
#     def browsing(self,browsing =None):
#         print(f"browsing {browsing} internet on {self.brand} {self.model}")
#     def app(self,app=None):
#         print(f"using {app} app on {self.brand} {self.model}.")
# apple = smart_phone("apple","iphone15s")
# apple.make_call(234556)
# apple.send_message(256783,"hello")
# apple.browsing("instagram")
# apple.app("facebook")


'# 2.multilevel inheritance:'
# class grandfather():
#     def output(self):
#         print('this is gf class')
# class father(grandfather):
#     def outputf(self):
#         print('this is father class')
# class child(father):
#     def outputc(self):
#         print('this is child class')
# obj = child()
# obj.output()
# obj.outputf()
# obj.outputc()


'# 3.hierarchical inheritance:'
# class a():
#     def output(self):
#         print('this is parent class')
# class b(a):
#     def output1(self):
#         print('this is child1 class')
# class c(a):
#     def output2(self):
#         print('this is child2 class')
# obj = b()
# obj.output()
# obj.output1()
# obj2 = c()
# obj2.output2()
# obj2.output()



'# 4. multiple inheritance:'
# class parent1():
#     def father(self):
#         print("this is father class")
# class parent2():
#     def mother(self):
#         print("this is mother class")
# class child(parent1,parent2):
#     def child(self):
#         print("this is child class")
# object = child()
# object.father()
# object.mother()





" ############ POLYMORPHISM ############ "
# --> implementing samething in diff. forms.
# --> the literal meaning of polymorphism is the condition of occurence in different forms.
# --> two types:
# 1. overloading--i.method overloading. ii.operator overloading.
# 2. method overriding.


' # Operator OL :'
# eg. +
# 1+2=3 added.
# "hi"+"world"="hi world"

' # Method OL :'
# --> method should be same.
# --> arguments must be diff.
# --> in the terms of length or type of arguments.
# --> to over come method OL, using default parameters we can achieve.
# eg.:
# class calculator ():
#     def add(self,a=None, b=None):
#         print(a,b)
#     def add(self,a=None,b=None,c=None):  #here  count of the arguments of above add is replacing with count 3 arguments.
#         print(a,b,c)
# obj = calculator()
# obj.add(10,10,10)
# obj.add(10,10)

' # Method OR :'
# -->method name should be same, arguments should be also same.
# eg.:
# class father():
#     def details(self,a):
#         print("this is base class",a)
# class child(father):
#     def details(self,a):
#         print("this is child class",a)          
#         super().details("200cr")
# obj = child()
# obj.details("100cr")        #base class is overwrited.

""" ############## KEY POINTS: ###############"""
# print-->the print the statement.
# return-->to exit/ end the execution.
# yield--> to repeat the multiple value in same function. if yield is present, the function is cal generator function.
# __init__--> to initial the arguments. and automatically takes the values from obj created.
# super()--> to access the parent functions.


''' ####### ENCAPSULATION: ######## '''
# --> mechanisam of wrapping the data (variables) and code acting on the data(methods) together as a single unit.
# using this, we can provide security to data.
# 1.public.--> access to outside world
# 2.protected.--> access to derived class.(inherit class only)
# 3.private.--> not accessible to outside.
# --> if you want to give any protection, mostly keep private data or protected in base class.

'public'
# class gfather():
#     def __init__(self,a):
#         self.a = a
#         print(a)
#     def sample(self):
#         print(self.a)
# class father(gfather):
#     def display(self):
#         print(self.a)
# obj = father("100cr")
# obj.display()
# obj.sample()



'protected:' # protected by using symbol'_'
# class gfather():
#     def __init__(self,a):
#         self._a = a
#         print(a)
#     def sample(self):
#         print(self._a)
# class father(gfather):
#     def display(self):
#         print(self._a)  # here single underscore gives data from gfather. because gfather is protected.
# obj = father("100cr")
# obj.display()
# obj.sample()

'private'   # private by using "__"
# class gfather():
#     def __init__(self,a):
#         self.__a = a
#         print(a)
#     def sample(self):
#         print(self.__a)
# class father(gfather):
#     def display(self):
#         print(self.__a)  # here if you give double underscore also u cannot access data from gfather. because gfather is in private.
# obj = father("100cr")
# obj.display()
# obj.sample()

''' ####### DATA ABSTRACTION : ######## '''
# --> hiding the implementation and hiding the code(unnecessary part) and showing the essential part.
# 1. abstract class.--> class which contains abstract methods .
# 2.abstract method.
# 3.concrete class.


'abstract method:'
# -->the method which is having only declaration but not the definition/ implementation / declaration (hiding)''
# --> object cannot create here.

'concrete class:'
# --> class which does not have abstract method.
# --> object can create only to concrete class only.
# --> to create abstract classes, you can use the abc module (abstract base class )


# from abc import ABC , abstractmethod
# class abstract_demo(ABC):
#     @abstractmethod
#     def display(self):
#         pass
#     @abstractmethod
#     def display2(self):
#         pass
# class demo(abstract_demo):
#     def display(self):
#         print("implemmenting in derived class")
#     def display2(self):
#         print("implementing in derived class display2")     # they are two abstractmethods in base class , so two functions calling in derived class also.
# obj = demo()
# obj.display()
# obj.display2()













