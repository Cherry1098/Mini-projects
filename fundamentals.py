'''############# Day3 ################ 07/03/25'''

'# DATA STRUCTURES :'
# --> Two types.
'--> 1. Mutable : (LSD--list,sets,dict)'
# once you create any datatype and you modify and it refers to same address 
'--> 2. inmutable : (NTS--numeric,Tuple,string)'
# once you create any datatype and you try to modifiy and it refers to diff address(it creates a new address).
# first created address cannot be modified.

'# LIST : [ ]'
# --> a list is a mutable, ordered sequence of elements.
# --> elements acn be of different data types.
# --> lists are defined using square brackets '[]'.
# eg.
# my_list = [1,2,3,"apple",3.5]
# print(my_list)
# print(type(my_list))
# my_list.append("banana")     # here the value will be append to above list.
# print(my_list)               # here in print function we write variable name given to the list.
# #my_list.append([1,2,3.5],(1,2,3))  # here we cannot append more than 1 argument. the o/p will be error.
# my_list.append([1,2,3.5])    # here we can append the list into the list. simillary way we can append tuple into list.
# print(my_list)

'# TUPLE : ( )'
# --> A tuple is an immutable, ordered sequence of elements.
# --> similar to list but cannot be modified once created.
# --> Tuples are defined using parentheis '( )'.
# eg.
# Tuple_1 = (1,2,3.5,"jai sri ram",[1,2,3,4.5])
# print(Tuple_1)
# print(type(Tuple_1))
# Tuple_1.append("sai ram")
# print(Tuple_1)       # here the o/p will be error, because Tuples cannot be modified.

'# SETS : { }'
# --> A set ia an unordered collection of unique elements.(no duplicate)
# --> a set is an mutable data type.but elements in it should be inmutable.
# --> sets are defined using curly braces { }, elements seperated by comma.
# eg1.
# my_set ={1,2,3,4,5}
# print(my_set)
# print(type(my_set))
# # eg2.
# # # my_set = {1,2.5,{1,2,6},[4,5,6.7],"sri ram",(3,5,8.5)}   #here sets,lists are seen within sets. so error comes.
# # eg3.
# my_set = {1,2.5,"sri ram",(3,5,8.5)}
# print(my_set)
# print(type(my_set))
# # eg4.
# my_set = {1, 2, 3, 4, 3, 2, 1}
# print(my_set)   # o/p will be {1,2,3,4}---> because sets wont allow duplicates.
# # eg5.
# my_set = set(['Python', 'Java', 'C', 'C++'])
# print(my_set)   #we can convert list into sets but cannot use lists within sets.
# # eg6.
# my_set.add(40)
# print('Updated Set:', my_set)    #use add( ) function to add single element.
# # eg7.
# my_set.update([50, 60, 70])
# print('Updated Set:', my_set)    #use update( ) function to add or update more than one elements.


'# COMPLEX DATATYPES :'
# --> In python, a complex data type is used to represent complex numbers.
# --> a complex numbers consists of a realpart and imaginary part.
# --> written in form a+bj.
# --> a is real part(int of float) and b is imaginary part(int of float).
# eg1.
# sample = 4+5j
# print(sample)
# print(type(sample))
# where we can use this data type:--> in scientific computing, singal processing, AC circuits.
# eg2.
# sample_1 = 2-3j
# print(sample+sample_1)


'# DICTIONARIES :'
# --> a dictionary is an ordered collection of key-value pairs.
# --> keys must be unique within dictionary and values cane be any data type with duplicates.
# --> dictionary are defined using curely braces { } and colons :
# # eg1.
# my_dict = {"name" :"John" , "age" : 25 , "city" : "Newyork"}
# print(type(my_dict))
# print(my_dict)
# # eg2.
# my_dict = {"name" : "pavan" , 1 : 123 , 3 : [1,2,3] , (1,2) : 5.7 , 5 : {1,2,3} , 4 :(1,2)}
# print(my_dict)
# print(type(my_dict))


'# BOOLEAN : '
# --> boolean datatype value will be True and False..
# --> True = 1 (truth the value) and False = 0 (false the value)
# eg1.
# sample = bool(0)
# print(sample)     #o/p is false
# # eg2.
# sample = True
# print(sample)     #o/p is true


'#### f-string : #### STRING FORMAT #### '
# num_1 = int(input("enter the number1 : "))      #here taken one variable and assign a value by using = operator.
# num_2 = int(input("enter the number2 : "))
# result = num_1 + num_2       # here performed addition operation by using + operator.
# print(f"adding {num_1} and {num_2} by using operator + and the output is {result}")


'''Exercise 1 :'''
# sample_data = [1,2,3,4,5,1,2,3,4,"vasu","vasu","kumar","raju","priyanka"]
# conversion = list(set(sample_data))    #explicit conversion
# print(conversion)
# print(type(conversion))   #i want o/p datatype to be in same list. so i again converted set into list.


'''' Exercise 2 :'''''

'######list-->tuple :'
# sample_data = [1,2.5,"vasu","vasu",4.5,2.5,]
# conversion = tuple(set(sample_data))   #by using sets , we can remove duplicates
# conversion = tuple(sample_data)
# print(conversion)
'####### list-->sets :'
# sample_data = [1,2.5,"vasu","vasu",4.5,2.5,]
# conversion = set(sample_data)             #by using sets , we can remove duplicates
# print(conversion)
'####### sets-->list :'
# sample_data = {1,2.5,"vasu","vasu",4.5,2.5,}     #in this set , we have duplicates.but while print it removes duplicates.
# conversion = list(sample_data)      # list conversion, the values are in ordered now.
# print(conversion)
'####### sets-->tuple :'
# sample_data = {1,2.5,"vasu","vasu",4.5,2.5,}     #in this set , we have duplicates.but while print it removes duplicates.
# conversion = tuple(sample_data)      # tuple conversion, the values are in ordered now.
# print(conversion)
'####### sets-->list :'
# sample_data = {1,2.5,"vasu","vasu",4.5,2.5,}     #in this set , we have duplicates.but while print it removes duplicates.
# conversion = tuple(sample_data)      # tuple conversion, the values are in ordered now but cannot be modify.
# print(conversion)
'####### tuple--> list :'
# sample_data = [1,2.5,"vasu","vasu",4.5,2.5,]     #in this , we have duplicates.but while print it removes duplicates.
# conversion = list(sample_data)          # list conversion, the values are in ordered now with duplicates.
# conversion = list(set(sample_data))     # list and set conversions , the values are in ordered now without duplicates.
# print(conversion)
'####### tuple--> dict :'
# sample_data = [1,2.5,"vasu","vasu",4.5,2.5,]     #in this , we have duplicates.but while print it removes duplicates.
# conversion = dict(sample_data)           #but when converting into dict, this conversion throws an error
# print(conversion)
'####### dict-->all different data types :'
# sample = True                   #observations 
# conversion = tuple(sample)      #error
# conversion = list(sample)       #error
# conversion = set(sample)        #error  
# conversion = int(sample)        #o/p----->1
# conversion = float(sample)      #o/p----->1.0
# conversion = str(sample)        #o/p------>True
# conversion = complex(sample)    #o/p----->1+0j
# conversion = (sample) 
# print(conversion)    
'####### int-->all different data types  :'
# num = 35 #her DT is integer
# conversion = list(str(num))     #using str and then list function , then o/p is ['3','5']
# conversion = list(num)          #using list function to convert integer to list DT, it throws an error.single interger or float will not be listed.
# conversion = set(str(num))      #using str and then set function , then o/p is {'3','5'}
# conversion = str(num)           #using str function , then o/p is 35
# conversion = set(num)           #using set function ,  it throws an error.single interger or float will not be listed.
# conversion = tuple(num)         #using tuple function ,  it throws an error.single interger or float will not be form tuple.
# conversion = tuple(str(num))    #using str and then tuple function , then o/p is ('3', '5')
# conversion = dict(num)          #using dict function ,  it throws an error.single interger or float will not be form dict.it requries key and values.
# conversion = dict(str(num))     #using dict or any function ,  it throws an error.single interger or float will not be form dict.it requries key and values.
# conversion = bool(num)          #using bool function ,  what ever the value <> 0  then o/p true. if the value is eual to 0, then its false.
#conversion = complex(num)        #using complex function, it convert to complex..o/p -->(35+0j)
# print(conversion)
# print(type(conversion))
'####### float-->all different data types  :'
# num = 35.8 #her DT is float
# conversion = list(str(num))     #using str and then list function , then o/p is ['3', '5', '.', '8']
# conversion = list(num)          #using list function to convert integer to list DT, it throws an error.single interger or float will not be listed.
# conversion = set(str(num))      #using str and then set function , then o/p is {'5', '8', '.', '3'}
# conversion = str(num)           #using str function , then o/p is 35.8
# conversion = set(num)           #using set function ,  it throws an error.single interger or float will not be listed.
# conversion = tuple(num)         #using tuple function ,  it throws an error.single interger or float will not be form tuple.
# conversion = tuple(str(num))    #using str and then tuple function , then o/p is ('3', '5', '.', '8')
# conversion = dict(num)          #using dict function ,  it throws an error.single interger or float will not be form dict.it requries key and values.
# conversion = dict(str(num))     #using dict or any function ,  it throws an error.single interger or float will not be form dict.it requries key and values.
# conversion = bool(num)          #using bool function ,  what ever the value <> 0  then o/p true. if the value is eual to 0, then its false.
# conversion = complex(num)        #using complex function, it convert to complex..o/p -->(35.8+0j)
# print(conversion)
# print(type(conversion))
'####### str-->all different data types  :'
# text = " my name is charishma "  #her DT is str
# conversion = list(text)          #using list function to convert into list. here is o/p['m', 'y', ' ', 'n', 'a', 'm', 'e', ' ', 'i', 's', ' ', 'c', 'h', 'a', 'r', 'i', 's', 'h', 'm', 'a'].
# conversion = set(text)           #using set function ,  {'c', ' ', 'n', 'i', 'y', 'r', 'a', 'm', 'e', 's', 'h'}
# conversion = tuple(text)         #using tuple function ,here it wont remove duplicates ('m', 'y', ' ', 'n', 'a', 'm', 'e', ' ', 'i', 's', ' ', 'c', 'h', 'a', 'r', 'i', 's', 'h', 'm', 'a')
# conversion = dict(text)          #using dict function ,  it throws an error.single interger or float will not be form dict.it requries key and values.
# conversion = bool(text)          #using bool function ,  what ever the value <> 0  then o/p true. if the value is eual to 0, then its false.
# conversion = complex(text)        #using complex function, error.
# print(conversion)
# print(type(conversion))
'####### list-->all different data types  :'
# list_1 = ["1","2.5","4","4","ram naidu",("3","4.5","pinky"),"1"]
# conversion = int(list_1)         # list can't convert into integer.even though only int or float values are present in list, we cannot convert it.
# conversion = float(list_1)       # list can't convert into float.even though only int or float values are present in list, we cannot convert it.
# conversion = str(list_1)         #it convert whole value into str value. o/p is [1, 2.5, 4, 4, 'ram naidu', (3, 4.5, 'pinky'), 1]
# conversion = set(list_1)        #it converts into set.it removes duplicates. o/p {1, 2.5, 'ram naidu', 4, (3, 4.5, 'pinky')}
# conversion = tuple(list_1)      #it converts into tuple. o/p (1, 2.5, 4, 4, 'ram naidu', (3, 4.5, 'pinky'), 1)
# conversion = dict(list_1)       # it doesn't have key and values..so throwing an error.
# conversion = bool(list_1)        # True..why it is true.
# conversion = complex(list_1)      # unable to convert into int or float. so we cannot convert into complex too.
# print(conversion)
# print(type(conversion))
'####### set-->all different data types  :'
# set_1 = {1,2.5,4,4,"ram naidu",(3,4.5,"pinky"),1}
# conversion = int(set_1)         # set can't convert into integer.even though only int or float values are present in list, we cannot convert it.
# conversion = float(set_1)       # list can't convert into float.even though only int or float values are present in list, we cannot convert it.
# conversion = str(set_1)         #it convert whole value into str value. o/p is {1, 2.5, 4, 'ram naidu', (3, 4.5, 'pinky')}
# conversion = list(set_1)        #it converts into list.it removes duplicates. because the variable value is given in set data type. so o/p [(3, 4.5, 'pinky'), 1, 2.5, 4, 'ram naidu']
# conversion = tuple(set_1)      #it converts into tuple.it removes duplicates. because the variable value is given in set data type.o/p (1, 2.5, 4, 'ram naidu', (3, 4.5, 'pinky'))
# conversion = dict(set_1)       # it doesn't have key and values..so throwing an error.
# conversion = bool(set_1)        # True..why it is true.
# conversion = complex(set_1)      # unable to convert into int or float. so we cannot convert into complex too.
# print(conversion)
# print(type(conversion))


'''#####################  EXERCISES ##################'''

# 1. print statement:
# write a program that prints a pattern using multiple statments.
# name = input("enter your name :")
# age = int(input(" enter your age :"))
# country = input(" enter the country you are from : ")
# hobby = input("enter your the hobby you like most : ")
# print(f"Hi. My name is {name} , age {age} from {country} and the hobby i like most is {hobby} ")

# 2.comments: giving one example from above.
# sample_data = [1,2.5,"vasu","vasu",4.5,2.5,]     #in this , we have duplicates.but while print it removes duplicates.
# conversion = list(sample_data)          # list conversion, the values are in ordered now with duplicates.
# conversion = list(set(sample_data))     # list and set conversions , the values are in ordered now without duplicates.
# print(conversion)

# # 3.string operations :
# num = int(input("35"))    # string as input(35)
# print(type(num))

# 4.concatenate strings :
# first_name = input("enter the first name : ")
# middle_name = input("enter the middle name :")
# last_name = input("enter the last name : ")
# result = (first_name+" "+middle_name+" "+last_name)
# print(result)


# 5.type conversion :
# age = int(input("enter your age : "))
# print(age + 5)


# 6.calculator :
# num_1 = int(input("enter the first number : "))
# num_2 = int(input("enter the second number : "))
#     print(num_1+num_2)
#     print(num_1-num_2)
#     print(int(num_1/num_2))
#     print(num_1*num_2)
























