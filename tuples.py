'''############# Day11 ################ 18/03/25'''

# -->inmutable datatypes
# -->same as list.
# -->once created a tuple,cannot modified.
# -->enclosed by ()
#--> ordered  and having index to each and evry element.
# -->pancard,aadhar,emp.id
# -->different datatype elements and allows duplicates.
# -->can assign tuple inside tuple.

# tuple_1 = ()        #empty tuple
# tuple_1 = (1,2,3,4)
# tuple_1 = tuple()       #tuple class

# tuple_1 = (1,2,3,"charishma","vasu",[1,2,3],(4,5,6.7),9.4,3,2,1)

'''############# METHODS ################ '''
"Indexing[S:S:S]"
# print(tuple_1[:6]) # print till index 5
"len()"
# print(len(tuple_1))     #count of elements
"count()"
# print(tuple_1.count(3))     # here how many 3 are present in tuple.
"index()"
# print(tuple_1.index(5))         # here element 5 is not present so o/p is error.
# print(tuple_1.index(3))         # here we have two 3's so first element 3 index will excute.


'''############# OPERATIONS ################ '''
# tuple_1 = (1,2,3)
# tuple_2 = ('a','b','c')
"concatenation : "
# print(tuple_1+tuple_2)
"repetition : "
# print(tuple_1*2)
"membership test"
# result = 3 in tuple_1
# print(result)
"all:"
# tuple_1 = ()
# print(all(tuple_1))        # here tuple doesnot contains 0 or false. so o/p is true


'''############# QUIZ ################ '''
# 1. all() function return when applied to an empty tuple:
# True.
# 2. creates a tuple:
# my_tuple = (1,2,3)
# 3.len() o/p: 3
# my_tuple = (1,2,3)
# print(len(my_tuple))
# 4.tuple in python:
# tuples use parenthesis( ) for declaration.


'''############# task and exercise ################ '''
# 1. create tuple : tuple containing three elements: your name, your age and your fav color. then print.
# name = input("enter your name : ")
# age = input("enter your age : ")
# fav_color = input("enter your fav color : ")
# print(f"my name is {name} and my age is {age}. my fav color is {fav_color}")
# 2.access tuple elements: tuple containing the days of the week.print third element.
# days = ('sunday','monday','tuesday','wednesday','thursday','friday','saturday')
# print(days[2])
# 3.tuple concatenation:
# tuple_1 = (1,3,5,7,9)
# tuple_2 = (0,2,4,6,8,10)
# print(tuple_1+tuple_2)          #  (1, 3, 5, 7, 9, 0, 2, 4, 6, 8, 10)
# 4.tuple unpacking:
# length = int(input("enter the length : "))
# width = int(input("enter the width :"))
# rectangle_dimensions = length,width
# print(rectangle_dimensions)
# area = length * width
# print(f"The area of the rectangle with length {length} and width {width} is: {area}")
# 5.check if an element exits:
# element_exists = input("enter the element to check : ").lower()
# if element_exists in days:
#     print(f"{element_exists} exists in the days.")
# else:
#     print(f"{element_exists} does not exist in the days.")