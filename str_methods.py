'''############# Day9 ################ 14/03/25'''

# -->immutable datatypes.(once create, we cannot modify)
# -->you can execute modified data directely through print statment or we can store the modifies data into var, then print
# -->most common using data type.
# -->textable data type-->str data type is used.
# -->sequence of chara, enclose with ' ', " ",''' '''.


# single_quoted_str = 'hello word'
# double_quoted_str = "python class starts at 7'o clock daily"
# triple_single_quoted_str = '''Triple quotes allow he said, "triple" 8'o clock string to span multiple lines.'''
# #we can there is no single or double quotes, we can use triple single also.
# print(single_quoted_str)
# print(type(single_quoted_str))
# print(double_quoted_str)
# print(type(double_quoted_str))
# print(triple_single_quoted_str)
# print(type(triple_single_quoted_str))


# my_str ="python life"
# '''########## INDEXING ###########'''
# print(my_str[3])    #o/p-->h    +ve indexing concept.
# print(my_str[-3])   #o/p-->i    -ve indexing concept.

'''######## SLICING ############'''
# --> to extract portion of characters.
# syntax :var[S:S:S]
# print(my_str[2:6])           #o/p-->thon    +ve forward slicing concept.
# print(my_str[5:1:-1])           #o/p-->noht    +ve backward slicing concept.
# print(my_str[-9:-5:])           #o/p-->thon    -ve forward slicing concept.
# print(my_str[-6:-10:-1])           #o/p-->noht    -ve backward slicing concept.



'''############## STR METHODS ################''' #-->.methodname(arg)
# my_str =" python Lifef @ 8'o clock "

'''--> upper()''' #--->convert all characters in the str into upper cases
# print(my_str.upper())

'''--> lower()''' #--->convert all characters in the str into lower cases
# print(my_str.lower())

'''--> count()''' #--->returns no. of occurences of the specified sub-string.
# print(my_str.count("i"))     #here it counts both caps i and small i 

'''--> strip()''' #--->removes spaces only at starting and ending.
# print(len(my_str))              
# print(my_str.strip())               #here remove both sides spaces.
# print(len(my_str.strip()))
# print(my_str.lstrip())              #here remove left sides space.
# print(len(my_str.lstrip()))
# print(my_str.rstrip())              #here remove right sides space.
# print(len(my_str.rstrip()))

''' --> split()''' #---> split the string into a list based on separator.
# print(my_str.split( ))              # here separator i given as space.
# my_str =" python,Life,@8'o,clock "
# print(my_str.split( ))                  # here i dont find space so enter str is printed.
# print(my_str.split(","))                   # here using the separator is given in ","
# in real life mostly we use ","

''' --> replace()''' #-->it replace the new chars with old char in the str.
# print(my_str.replace("8","9"))            #python Life @ 9'o clock 
# print(my_str.replace("f","9"))              #python Li9e @ 8'o clock. where ever you find f , it repace with 9.
# print(my_str.replace("python","9"))         # 9 Lifef @ 8'o clock. where ever you find python , it repace with 9.

''' --> startswith() ''' #-->it checks the str is starts with given argument, then it print true. if not then false.
# print(my_str.startswith(" "))     # here space in thegiven str is started with.
# my_str ="python Lifef @ 8'o clock.text"
# print(my_str.startswith("python"))      #true
# print(my_str.startswith("p"))           #true

''' --> endswith() ''' #-->it checks the str is end with given argument, then it print true. if not then false.
# print(my_str.endswith(" "))     # here space in thegiven str is ends with.
# my_str ="python Lifef @ 8'o clock.text"
# print(my_str.endswith(".text"))      #true
# print(my_str.endswith("t"))           #true
# email_list = ["example1@gmail.com","example2@yahoo.com","example3@gmail.com","example4@hotmail.com","example5@outlook.com"]
# empty_list = []
# for i in email_list:
#     if i.endswith("@gmail.com"):
#         empty_list.append(i)
# print(empty_list)
# print([i for i in email_list if i.endswith("@gmail.com")])        # list comprehensive way. writing the code in one line.

''' --> find() ''' #-->need to pass char in arg.and result the index of the char.
# print(my_str.find("python"))
# print(my_str.find("fi"))     # here we have two f's. but print first char index only.
# print(my_str.find("w"))         #here w is not present in entire str. so it result as -1.

'''index()''' #-->need to pass char in arg.and result the index of the char.
# print(my_str.index("python"))
# print(my_str.index("f"))     # here we have two f's. but print first char index only.
# print(my_str.index("w"))         #here w is not present in entire str. so it result as error.

''' capitalize() ''' #-->first letter of the  entire str will capitalize.
# my_str ="python Lifef @ 8'o clock "
# print(my_str.capitalize())       #o/p : Python lifef @ 8'o clock 

''' title() ''' #-->first letter of the  entire str will capitalize.
# my_str = "welcome to pythonlife"         #here i want first letter of every str in entire should print in caps.
# print(my_str.title())                 # o/p : Welcome To Pythonlie

''' isapla()'''  #--> it checks entire str is consist of only aplabets.the print as boolean value. if you find any special char like space,@,$,' print as false.
# my_str = "welcome to pythonlife" 
# print(my_str.isalpha())     # here we have space..so printind as false.
# my_str = "pythonlife" 
# print(my_str.isalpha())         # Here we dont have any special char. so print as true.

''' isdigit()''' #--> it checks entire str is consist of only digits.the print as boolean value. if you find any special char like space,@,$,' print as false.
# my_str = "1234 567 8910" 
# print(my_str.isdigit())     # here we have space..so printind as false.
# my_str = "12345678910" 
# print(my_str.isdigit())         # Here we dont have any special char. so print as true.

''' any()'''   # --> it checks entire str contains alphabet or digits.
# my_str = "charishma1098"            #if both contains ,we have some methods.
# print(any(char.isalpha() for char in my_str)) 
# print(any(char.isdigit() for char in my_str)) 

''' join() ''' # --> joins the sub string of the list into single str.
# str_list = ["hello", "world","welcome","to","pythonlife"]
# print(" ".join(str_list))   

''' ############## QUIZ ################# '''
# 1.immutable-->python str.
# 2.last char-->my_string[-1]             # giving index of last char in neg indexing.
# 3.".upper()"-->used to convert a tring to uppercase.
# 4.".split()"--->splits a tring into a list of sub string.
# 5. ".startswith()"--->checks if string starts with a specific prifix.


''' ######### CODING EXERCISE ############'''
# 1. print the char at even indices:
# sentence = "Python is amazing"     # o/p : pto saaig
# final_output = [ ]
# for i in range(len(sentence)):
#     if i%2 == 0:
#         final_output.append(sentence[i])
# print("".join(final_output))

# 2. replace spaces with _:
# s = "Python is fun and powerful"    #o/p : Python_is_fun_and_powerful
# print(s.replace(" ","_"))

# 3.print in reverse order :
# s = "Python is amazing"             # o/p : gnizama si nohtyP
# print(s[::-1])

# 4.print first char of all sub string in caps:
# s = "python programming is fun"       # o/p : Python Programming Is Fun
# print(s.title())










