'''############# Day4 ################ 08/03/25'''

'''############# OPERATORS ################ '''

# 1. arithmetic operators.
# 2. assignment operators.
# 3. comparsion operators and logical operators.
# 4.identity operators.
# 5. membership operators and o/p.
# 6. o/p formatting.(f=string)


'''############# ARITHMETIC OPERATORS ################ '''
# --> AO are used for mathematical operations.
# 1.addition(+)
# 2.subtraction(-)
# 3.multiplecation(*)
# 4.division(/)
# 5.modules(%)
# 6.exponentiational(**)
# 7.floor division(//)


'''############# OPERATORS ################ '''
#symbol or keyword that performs an operation on one or more operands.

'''############# OPERAND ################ '''
#value or variable acted upon by an operator to produce a result.



'''############# 1.ADDITION (+) ################ '''
# age = 35     #age is operand
# print(age+5)      #+ is operator. age and 5 are operand.

# num_1 = 3     #num_1 is variable/operand
# num_2 = 5     #num_2 is variable/operand
# print(num_1 + num_2)     # here + is operator


'''############# 2.SUBTRACTION (-) ################ '''
# age = 35     #age is operand
# print(age-5)      #- is operator. age and 5 are operand.

# num_1 = 3     #num_1 is variable/operand
# num_2 = 5     #num_2 is variable/operand
# print(num_1 - num_2)     # here - is operator. we have to check num_1 is left operand, num_2 is right operand.


'''############# 3.MULTIPLICATIONS (-) ################ '''
# age = 35     #age is operand
# print(age*5)      #* is operator. age and 5 are operand.

# num_1 = 3     #num_1 is variable/operand
# num_2 = 5     #num_2 is variable/operand
# print(num_1 * num_2)     # here * is operator. 


'''############# 4.DIVISION (/) ################ '''
# division returns quotient in float value.
# age = 35     #age is operand
# print(age/5)      #/ is operator. age and 5 are operand.

# num_1 = 3     #num_1 is variable/operand
# num_2 = 5     #num_2 is variable/operand
# print(num_1 / num_2)     # here / is operator. we have to check num_1 is left operand, num_2 is right operand.


'''############# 5.EXPONENTIAL (**) ################ '''
# age = 35     #age is operand
# print(age**5)      #** is operator. age and 5 are operand.

# num_1 = 3     #num_1 is variable/operand
# num_2 = 5     #num_2 is variable/operand
# print(num_1 ** num_2)     # here ** is operator. we have to check which is base and which is exponent.


'''############# 6.MODULUS (%) ################ '''
# division returns reminder value.
# age = 35     #age is operand
# print(age%5)      #% is operator. age and 5 are operand.

# num_1 = 3     #num_1 is variable/operand
# num_2 = 5     #num_2 is variable/operand
# print(num_1 % num_2)     # here % is operator. we have to check which is base and which is exponent.


'''############# 7.FLOOR DIVISION (//) ################ '''
# division returns quotient in int value.
# age = 35     #age is operand
# print(age//5)      #// is operator. age and 5 are operand.

# num_1 = 3     #num_1 is variable/operand
# num_2 = 5     #num_2 is variable/operand
# print(num_1 // num_2)     # here // is operator. we have to check num_1 is left operand, num_2 is right operand.





'''############# COMPOUND ASSIGNMENT  OPERATORS ################ '''
# -->assignment operators are used to assign values to the variables .
# --> it acts are operator and provide value to the variable.
# eg.
# num_1 = 1    
# num_2 = 2    
# num_1 += 5      #+= is compund assignment operator
# num_2 -= 1      #-= is compund assignment operator
# num_1 *= 5      #*= is compund assignment operator
# num_2 /= 1      #/= is compund assignment operator
# print(num_1)
# print(num_2)




'''############# COMPARSION  OPERATORS ################ '''
# --> are used to compare the values and returns the result in boolen value i.e. TRUE or FALSE.
# cost_1 = int(input("enter the actual price : "))
# cost_2 = int(input("enter the purchased price : "))
# print(cost_1 == cost_2 )
# print(cost_1 != cost_2 )
# print(cost_1 < cost_2 )
# print(cost_1 > cost_2 )        
# print(cost_1 >= cost_2 )        # if any one statement is false , entire statement is false.
# print(cost_1 <= cost_2 )        # if any one statement is false , entire statement is false.
# eg.
# user_name = input("enter the username : ")
# pass_word = input("enter the password : ")
# print( user_name == "cherry" and pass_word == "1098")





'''############# LOGICAL OPERATORS ################ '''
# --> used to combine multiple conditions.
# -->1.AND , 2.OR , 3.NOT
''' statement A        statement B      AND       OR '''
   #     T                  T             T        T  
   #     T                  F             F        T
   #     F                  T             F        T
   #     F                  F             F        F
'''NOT'''
''' statement A            NOT'''   
   #     T                  T    
   #     F                  F   



'''############# IDENTITY OPERATORS ################ '''
# --> used to check if two variables refer to same object and returns value in boolean.
# --> is and isnot.
# eg.
# a = [1,2,3,4]
# b = a
# c = [1,2,3,4]
# print(a is b)       #o/p will true.
# print(id(a))
# print(id(b))
# print(id(c))
# print(c is b)         #o/p will false. 
# print(c is not b)     #o/p will true.


'''############# MEMBERSHIP OPERATORS ################ '''
# -->used to test whether a value is present in sequence.
# eg. the sequence can be list tuple or string.
# fruits = ["apple","banana","oranges","grapes"]
# print("guava" in fruits)    #checking guava in above list.--false
# print("guava" not in fruits)   #checking guava in above list.--true




'''############# O/P FORMATTING ################ '''
# -->easily insert the variable into string .
# -->you can perform calculations  or call functions directly within the string.
# eg.
# name = "john"
# age = 25
# print(f"my name is {name} and  age {age}")
# eg2.
# discount:
# product_cost = 10000
# discount = 5
# result = product_cost * (discount/100)
# product_cost -= result
# print(product_cost)



'''# quiz questions:'''
# 1.
# x = 15
# y = 4
# result = x//y
# print(result)
# 2.
# a = 7
# b = 3
# c =a % b
# print(c)    #  prints the reminder
# 3.
# x = 4
# x *= 5    #(x = x * 5)
# print(x)
# 4.
# x = 5 < 3 or 2 == 2
# print(x)       #true
# 5.
# a = "true"
# b = "false"
# c = not a or b
# print(c)    # false.



'''#####################  EXERCISES ##################'''

'''1.area of rectangle :'''
# length = int(input("enter the length : "))
# width = int(input("enter the width : "))
# area = length * width
# print(area)


'''2.demonstrate imcrementing and decrementing a variable '''
# num = int(input("enter the number :"))
# num += 5
# num -= 5
# print(num)

'''3.convert temperature from celsius to fahrenheit '''
# c = int(input(" enter the temperature : "))
# f = (c * 9.5) + 32
# print(f)

'''4.simple interest '''
# p = int(input("enter the priciple amount : "))
# t = int(input("enter the time period : "))
# r = int(input("enter the rate of interest per annum :"))
# simple_interest = (p * t * r)/100
# print(simple_interest)


'''two strings and display the result'''
# text_1 = input("enter the first word :")
# text_2 = input("enter the second word :")
# print(text_1+" "+text_2)

'''distance from kilometers to miles'''
# kilometers = int(input("enter the kilometers covered :"))
# miles = 1.60934 * kilometers
# print(miles)



'''quiz questions'''
# 1.identity operators (is and is not) checks for memory address identity.
# 2.if x is y is true if x and y refer to the same object - identity operator.
# 3.sequence membership ---> (in and not in)membership operator.
# 4. not in ---> membership operator is used to check if a value is not present in a sequence.


'''###################CODING EXERCISE################'''
# 1.user input for theier name and age.
# name = input("enter your name :")
# age = int(input("enter your age : "))
# print(f"welcoming the {name} and  age {age}")


# 2.dictionary with information about a product 
# name = input("enter the name :")
# price = input("enter the price : ")
# quantity =  input("enter the quantity : ")
# print(f"{name} are very fresh and price is {price}rs per kg and i want {quantity}'kgs ")


# 3.check if the number 5 is the list and 15 is not in the list
# list = [1,3,5,7,35]
# print(5 in list)     #true
# print(15 not in list)     #true












