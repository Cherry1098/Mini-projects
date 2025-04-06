'''############# Day 5 ################ 10/03/25'''

'''#################### CONTROL STATEMENTS ##################'''
# 1. Conditional statement
# 2. iterative statement
# 3. transfer / jumping statement


'''#################### CONDITIONAL STATEMENT #################'''
# --->if
# --->elif
# --->else
# --->nested if else


'''################## IF CONDITION ################'''
# --> it takes a condition and evaluate to either true or false.
# --> if the condition is true, then the true blocks of code.
# syntax : 
# if condition :
#     statement 1
#     statement 2
#     statement n
# eg.
# number = 6
# if number > 5 :
#     print (number * number)    #calculate square.


'''################## ELSE CONDITION ################'''
# --> when the condition if statment is false, the alternative block of if statement is excuted.
# syntax :
# if condition :
#     statement 1
# else :
#     statement 2

# eg.
# age = 35                 # eligible--->true block 
# age = 16                 # not eligible--->alternate block
# if age >=  18 :          # giving condition
#     print(f"you are eligible {age}")
# else :
#     print(f"you are not eligible {age}")

# eg.
# user_name = input ("enter the username")
# pass_word = input ("enter the password")
# if user_name == "YERRAM" and pass_word == "1098" :
#     print("login successful")
# else :
#     print("invalid login details")



'''################## ELIF CONDITION ################'''
# --> for multi condition one after another, this is useful when you need to check multiple conditions.
# --> if condition fulfills, then excute that code.
# syntax :
# if condition 1:
#     statement 1
# elif condition 2:
#     statement 2
# elif condition 3:
#     statement 3
# else :
#      statement 4

# eg. 
# GRADING SYSTEM:
# marks = int(input("enter your marks"))
# if marks >=90 and marks <= 100 :
#     print (f"Grade A and marks {marks}")
# elif marks >=80 :
#     print (f"Grade B and marks {marks}")
# elif marks >=70 :
#     print (f"Grade c and marks {marks}")
# elif marks>=35 :
#     print (f"Just passed and marks {marks}")
# elif marks >= 0 and marks <=34 :
#     print (f"Failed and marks {marks}")
# else :
#     print ("enter valid number")




'''################## NESTED IF ELSE CONDITION ################'''
# --> using if statement inside another if statement.
# useful in making series of decisions.
# syntax :
# if condition1 :
#     statement 1
#   if condition2 :
#     statement 2
#   else :
#     statement 3
# else :
#   statment 4
# eg.
# user_name = input ("enter the username")       #
# pass_word = input ("enter the password")
# if user_name == "YERRAM" :
#   if pass_word == "1098" :
#     print("login successful")
#   else :
#     print("invalid password")
# else :
#   print("invalid username")




'''################## SHORT HAND IF AND SHORT HAND IF ELSE CONDITION ################'''
# --> if there is only one if condition and one else condition, then only use this.
# syntax :
# result : value_if_true if conditon else value_if_value.

# eg.
# age = int(input("enter your age : "))
# print(f"you are eligible to vote") if age>=18 else print(f"you are not eligible")

# eg. display the entered number is even or odd
# num = int(input(" enter the number : "))
# print("the number is even") if num%2 == 0 else print("the number is odd")



'''########## QUIZ QUESTIONS ##########'''
# 1.Indentation is crucial in python to define the scope of a code block.
# 2.
# x= int(input("enter the number :"))
# if x > 5 :
#     print("greater than 5")
# else :
#     print("5 or less")
# 3. in "if elif else" statement , how many conditions we can checked.--->multiple
# 4. what is purpose of else statement in python..--->to provide alternative block of code  when the if statement is false.
# 5. it allows more complex conditional logic then nested if statment is used.


'''########## EXERCISES ##########'''
''' 1.Vowel checker:'''
# print the entered letter is vowel or consonant.
# vowels = str(input("enter the letter :"))
# if vowels == "a" or vowels == "e" or vowels == "i" or vowels == "o" or vowels == "u" :
# if vowels in "aeiouAEIOU" :
#   print("the letter is vowel")
# else :
#   print("the letter is consonant")


''' 2.Age Group Classifications:'''
# child:0-12, teenagers:13-17, adult:18-64, senior:65 and above
# age = int(input("enter your age : "))
# if age >= 65 :
#     print("Status : Senior")
# elif age >=18 and age <=64 :
#     print("Status : Adult")
# elif age >=13 and age <=17 :
#     print("Status : Teenager")
# elif age >=0 and age<=12 :
#     print("Status : Child")
# else :
#     print("please enter correct number")
    
''' 3.Number Classifer:'''
# print the entered number is +ve or -ve or 0 :
# num =  int(input("enter the number :"))
# if num > 0 :
#     print("the number is positive")
# elif num == 0 :
#     print("the number is zero")
# elif num < 0 :
#     print("the number is negative")
# else :
#     print("please enter integer number only")

''' 4. Leap Year Checker :'''
# year = int(input("enter the year : "))
# if year%100 == 0 and year%400 == 0 :
#     print("entered year is leap year")
# elif year%4 == 0 :
#     print("entered year is leap year")
# else :
#     print("entered year is not leap year")


''' 5.calculator :'''
# num_1 = int(input("enter the first number : "))
# num_2 = int(input("enter the second number : "))
# operator = input("enter the operator : ")
# if operator == "+":
#     print(num_1+num_2)
# elif operator == "-":
#     print(num_1-num_2)
# elif operator == "/":
#     print(int(num_1/num_2))
# elif operator == "*":
#     print(num_1*num_2)
# else:
#     print("please enter valid operator")

''' 6. short hand if :'''
# num = int(input("enter the number : "))
# print("the number is even") if num%2 == 0 else print("the number is odd")

''' 7.Discount calculator :'''
# discount_percentage = int(input("enter the discount given : "))
# original_price = int (input("enter original price : "))
# final_price = original_price-(original_price/discount_percentage)
# print(final_price)


''' 8.BMI Calculator:'''
# weight = float(input("enter the weight value (KG) :"))
# height = float(input("enter the height value (cm) :"))
# BMI = weight / ( height * height )*10000
# print(BMI)
