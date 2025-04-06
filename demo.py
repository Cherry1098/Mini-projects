'''############# Day1 ################ 05/03/25'''

'''Task1'''   #---> completed
#print("Hello Welcome to PythonLife")  #Task2 Completed


''' The python standard library contains the exact sytax, semantics, and tokens of python. 
It contains built-in modules that provide access to basic system functionality like I/O and some other core modules.
 Most of the python Libraries are written in the C Programming language. 
 The python standard library consists of more than 200 core modules. 
 All these work together to make python a high-level programming language . 
 Python standard library plays a vert important role.
   Without it, the programmer can't have access to the functionalities of python.
     But Other than this, there are several other libraries in python that make a programmer's life easier.'''

# To comment the line , shortcut key is ctrl+?


'''############# Day2 ################ 06/03/25'''


# num_1 = 10 # given 10 for num1
# num_2 = 20 # given 20 for num2
# result = num_1 + num_2 # sum of num1 &num2
# print(result)

# single line comment , use #
# multi line comment, use " " or '''(double quotes or triple single quotes)

'''#VARIABLES:'''
#syntax---> varible = value (the value is store in var is a name given to memory location)
#rules----> 
# 1.must start with letter or underscores.
# 2.cannot start with number.
# 3.name can contains alpa-numeric and underscores.(starting cann0t be with no numeric)
# 4.case sensitive (name, Name, NAME are three different variable names)
# 5.resvered words(keywords) cannot be used.
# 6.special characters are not used for variables names(@$%^&+-/)
'eg.'
# user_id = 101042589  
# User_id = 101042589
# USER_ID = 101042589
# print(user_id)  # printing the value given to variable.
# print(id(user_id)) # printing the memory id for the variable.
# print(User_id)  # printing the value given to variable.
# print(id(User_id)) # printing the memory id for the variable.
# print(USER_ID)  # printing the value given to variable.
# print(id(USER_ID)) # printing the memory id for the variable.

'''#check ID's for all three variables--they are different'''

'''# variable cases:'''#---> all three cases give o/p but as a developer should approach .
# 1. camel case (user_Name = "Vasu")
# 2. snake case (user_name = "Anjali")------very best approach
# 3. pascal case (User_Name = "Reddy")


'''# PYTHON DATA TYPES : '''
# 1. Numeric---->1.Integer, 2.Float, 3.Complex Number.
# 2. Dictonaries.
# 3. Boolean.
# 4. Set.
# 5. Sequence Type---->1.String, 2.List, 3.Tuple.

'''# TYPE FUNCTION :'''
#To check what data type it is, then use type function type()

'''# INT:'''
# -->Stands for integer.
# -->represents wholenumbers without any decimal ponit.(---,-1,0,1,---)
# eg.
# x = 5
# print(x)
# print(id(x))
# print(type(x))

'''# FLOAT:'''
# -->Stands for decimal.
# -->represents all decimal numbers.(---,-0.1,0.0,0.1,---)
# eg.
# x = 4.5
# print(x)
# print(id(x))
# print(type(x))

'''# STR:'''
# -->Stands for string.
# -->represents a sequence of characters.
# -->strings are enclosed in single ('') or double("") or triple single quotes(''').
'# eg1.'
# sample_sentence = 'welcome to india'
# sample_sentence = "welcome to india"
# sample_sentence = '''welcome to india'''
# ******if single quotes are used in sentence like 8'o clock, use double quotes.
# if single and double are used in sentence, then use triple single quotes.
'# eg2.'
#he said "Jhon has cycle" and he goes to ride at 8'o clock daily.
'# eg3. '
# user_height = "5.7"
# print(type(user_height))   (here datatype will be str)





'''################ TYPE CONVERSIONS:################'''

'# 1.Int-->Float:'
# eg.
# num = 35 #her DT is integer
# float_conv = float(num)  #using float function to convert integer to float DT.
# print(float_conv)
# print(type(float_conv))

'# 2.Float-->int:'
# eg.
# num = 35.6 #her DT is Float
# int_conv = int(num)  #using int function to convert float to int DT.
# print(int_conv)
# print(type(int_conv))

'# 3.int-->str:'
# eg.
# num = 35 #her DT is int
# str_conv = str(num)  #using str function to convert int to str DT.
# print(str_conv)
# print(type(str_conv))

'# 4.str-->int:'
# eg.
# num = "35" #her DT is str
# int_conv = int(num)  #using int function to convert str to int DT.
# print(int_conv)
# print(type(int_conv))

'# 5.str-->Float:'
# --> if the string contains float or int value, then only it converts.
# eg.
# num = "35" #her DT is str
# float_conv = float(num)  #using float function to convert float to str DT.
# print(float_conv)
# print(type(float_conv))



'# INPUT FUNCTION :'
# ---> To enter the values manually, then use input function" #input().
#input function default datatype is str. so use conversion to perform any operations.
# eg.
# num_1 = int(input ("enter the number1 :"))   #here user can enter values in number1.
# num_2 = int(input ("enter the number2 :"))   #here user can enter values in number2.
# print (num_1+num_2) # here if conversion function is not used , o/p will be concat. if num1=5 and num2=15 then result will be 515.
# num_1 = input ("enter the number1 :")  #here user can enter values in number1.
# num_2 = input ("enter the number2 :")   #here user can enter values in number2.
# print (num_1+num_2)  # here if conversion function is not used , o/p will be concat. if num1=5.6 and num2=15.5 then result will be 5.615.5.



'''############### TYPE CONVERSION :###############'''

'# 1. Implicit type---->'# Auto
# eg.
# num_1 = 10 #int
# num_2 = 5.7 #float
# result = num_1 + num_2
# print(result)   # auto convert, no need to use conversion.
# print(type(result))

'# 2. Explicit type---->' #Manually we are using conversion function to convert.
# eg.
# num_1 = int(input ("enter the number1 :"))   #here we should know the values of number1 are int and using int conversion.
# num_2 = int(input ("enter the number2 :"))   #here we should know the values of number2 are int and using int conversion.
# print (num_1+num_2)  # here if conversion function is not used , o/p will be concat. if num1=5 and num2=15 then result will be 515.



