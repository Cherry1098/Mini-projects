'''############# Day7 ################ 12/03/25'''

'''################ JUMPING/TRANSFER STATEMENT ####################'''
# --->1.break statement.
# --->2.continue statement.
# --->3.pass statement.


'''################ BREAK STATEMENT ####################'''
# -->once condition meets , i want to stop the looping then break is used to stop or break the loop and passes to next statement outside the loop.
# syntax:
# for item in iterable :
#     if condition :
#         break
# eg.
# employee_data = [11,22,33,44,55,66,77,88,99]
# for i in employee_data : 
#     if i ==44 :    #requriement: i want to check whether 44 is present in i
#         print(i)         # in this print o/p give what if condition is asked.
#         break
#     print(i)             #in this print o/p shows all iterations.
    # break
# print(i)                 # in this print 0/p print what is last iteration.



# eg.
# for i in range(10) :
#     if i ==5 :
#         print(i)
#     print(i)
# print(i)



'''################ CONTINUE STATEMENT ####################'''
# --> once condition statisfied, and u dont want to stop the loop and just skipping that iteration step, again it continue looping.
# syntax:
# for item in iterable :
#     if condition :
#         continue
#     # code here will bee skipped if the condition is met.

# for i in range(10):
#     if i == 5:
#         continue
#     print(i)
# print(i)

# range = ("ok","ok","defect","ok","ok","defect","ok")
# for i in range  :
#     if i == "defect" :
#         continue
    # print(i)
# print(i)

# voter_list = [11,22,18,25,65,85,5,4]
# for i in voter_list :
#     if i < 18:
#         continue
#     print(i)



'''################ PASS STATEMENT ####################'''
# -->is a null statement.
# -->meaning it does nothing.
# --> it hold the placeholder, where you need code.
# sytax:
# if conditon :
#     pass
# eg.
# for i in range(5):
#     #code to be excuted
#     pass    # holdin the palce holder. where you dont know what to print.


# age = 18
# if age<=18 :
#     block of code to be excuted
#     pass
# 
# for i in range(5):
#     pass
# print(i)


'''########### POINTS:###############'''
# -->indentation is critical for proper code structure in python.

'''########### QUIZ:###############'''
# break-->exit the loop immediately.
# continue-->to skip the rest of the current iteration and move to the next.
# pass-->acts as a null operation, doing nothing.

'''########### CODING EXERCISE:###############'''
# 1.using break in for loop:
# list of numbers as input
# number =[25,30,20,40,15,25,120]
# print sum of numbers. if the sum exceeds 100, stop adding numbers and print "sum exceeded 100"
# total_sum = 0
# for i in number:
#     total_sum += i
#     if total_sum < 100:
#         print(i)
# print("sum exceeded 100")

# 2.using continue in a for loop:
# numbers from 1-600.
# print only odd numbers, skipping the even ones using continue statement.
# for i in range(1,601,2):    #here we used step value.
#     print(i)
# for num in range(1, 601):   #here we used continue value.
#     if num % 2 == 0:
#         continue
#     print(num)


# 3.using pass in conditional statement:
# if number is even or odd. if it is even print even. if it is pass the stement..
# num = int(input("enter the number :"))
# if num %2 ==0 :
#     pass
#     print("even")


# 4. combining transfer statement:
# sum = ""
# words = ["hello","world","skip","python","break","code"]
# for i in words:
#     if i == "break":
#         break
#     elif i == "skip":
#         continue
#     print(i)









































































