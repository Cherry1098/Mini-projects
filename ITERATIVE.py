'''############# Day6 ################ 11/03/25'''

'''################ ITERATIVE STATEMENT ####################'''
# --> iterative statement is also known as looping statement.
# --> mainly they are two types.. for and while loop.


'''################ FOR LOOP ####################'''
# --> iterate over a sequence like list tuple sets dict string. and excute block of code.
# syntax:
# for variables in sequence :
    # code to be excuted.
# eg.
# employee_data = ["cherry" , "reddy" , "venky", "swathi"]
# for item in employee_data :
#     print(f"{item} are invited to the party ")

# for i in "pythonlife" :
#     print (i)


# fruits = ["apple","banana","cherry"]
# for item in fruits :
#     print(item)



'''################ RANGE() ####################'''
# -->to generate sequence of numbers.
# syntax : -->range(stop), range(start,stop), range(start,stop,step)
# eg:
# for i in range(5) :      # stop--->value is taken as n-1.
#     print(i)
# for i in range(0,10) :     #if user want 10 then range shoudl stop at 11.
#     print(i)
# for i in range(10,18,2):        #here step=2. 
#     print(i)


# for i in range(1,11):
#     print(f"2 * {i} = {i*2}")


# for i in range(1,11) :
#     print(f"8 * {i} = {i*8}")


'''##### table chart #####'''
# num =  int(input("enter the table num : "))     
# for i in range(1,11) :
#     print(f"{num} * {i} = {i*num}")




'''################ NESTED FOR LOOP ####################'''
# ---> for in for loop.
# syntax:
# for var in seq:
#     for var in seq :
# eg:
# for i in range(5):      #outer for loop
#     for j in range(5):    #inner for loop
#         print(i,j)


''' 1-5 tables '''
# for i in range(1,6):
#     for j in range(1,11):
#         print(f"{i} * {j} = {i*j}")
#     print("--"*15)


'''user input table:'''
# num_1 = int(input("enter the starting table :"))
# num_2 = int(input("enter the ending table :"))
# for i in range(num_1,num_2+1):
#     for j in range(1,11):
#         print(f"{i} * {j} = {i*j}")
#     print("--"*15)


'''################ WHILE LOOP ####################'''
# ---> code will excute untill the statment is false.
# ---> manually we can stop the excute by ctrl+c.
# ---> implict we can stop the excute by writing break.
# sytax:
# while condition :
#     code to be excuted.
# eg.
# while True :                  # t should be in caps.
#     print("pythonlife")       # to stop ctrl+c.
# while True :
#     print("pythonlife")
#     break                       # by writing break here it stops to excute.
# age = 35
# while age>=18 :
#     print("you are eligible")            # to stop ctrl+c.




# count = 0
# while count<=4:
#     print(count)
#     count +=1                 explict by writing this statement.



# while True:
#     user_name = input ("enter the username")
#     pass_word = input ("enter the password")
#     if user_name == "YERRAM" and pass_word == "1098" :
#       print("login successful")
#       break
#     else :
#       print("invalid login details")


'''################ NESTED WHILE LOOP ####################'''
# --->while in while loop.
# syntax:
# while outer_condition :
#     outer loop Code
#     while inner_condition :
#         inner loop Code


# x = 0
# while x < 3:
#     y = 0
#     while y < 2 :
#         print(x, y)
#         y +=1
#     x +=1
    


'''################ QUIZ QUESTIONS ####################'''
# 1.purpose of for loop-->to repeatedly excute a block of code for each element in a sequence.
# 2.iterate over a range of number in a for loop-->using range()
# 3.while loop stop excuting when the loop conditon becase false.
# 4.while loop sytac look like---> while condition:




'''################ CODING EXERCISE ####################'''

''' 1.sum of squares from 1-5 using for loop'''
# sum_of_squares = 0
# for i in range(1, 6) :
#     sum_of_squares += (i*i)
# print(f"The sum of squares from 1 to 5 is:", sum_of_squares)


''' 2.use while loop to print a countdown from 5 to 1 '''
# count = 5
# while count > 0:
#     print(count)
#     count -= 1


''' 3.multiplication table with nested for loop'''
# num_1 = int(input("enter the starting table :"))
# num_2 = int(input("enter the ending table :"))
# for i in range(1,num_2+1):
#     for j in range(1,11):
#         print(f"{i} * {j} = {i*j}")
#     print("--"*15)


''' 4.sum of all even numbers between 0 and 10 inclusion'''
# sum = 0
# for i in range(0,11,2) :
#     sum += i
# print(sum)


''' 5.sum of all numbers from 1 to given numbers'''
# num = int(input("enter the number : "))
# sum = 0
# for i in range(1,num+1) :
#     sum += i
# print(sum)


''' 6.display numbers from a list using a loop'''
# num = ["1","4","7","9","25"]
# for i in num :
#     print(i) 


''' 7.display numbers from -10 to -1 using a loop'''
# for i in range(-10,-1+1) :
#     print(i)


''' 8. print if sum of the numbers less than 100. break and print the sum is exceeded 100 '''
# sum = 0
# numbers = [25,30,20,40,15,25]
# for i in numbers:
#     sum += i
#     if(sum>100):
#         # break
#         print("sum is exceeded 100")
#         break
#     print(sum)











