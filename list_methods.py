'''############# Day8 ################ 13/03/25'''
# -->mutable.
# -->collection of various data types.
# -->we can perform various operations on list such as individuals elements, slicing,appending and More.
# my_list = [10,20,30,40,53.6,60,70,"vasu",[3,4,5],{5,6,9},{"name":"cherry"},80]
# print(my_list[-2:-5:-1])      #[start:stop:step]
# []                            #empty list

'''############## INDEXING ################'''
'''-ve index'''      #-10,-9,-8,-7,-6,-5,-4,-3,-2,-1
'''element list'''   # 11, 3,-4, 6,90,23, 5,25,16,15
'''+ve index'''      # 0 , 1, 2, 3, 4, 5, 6, 7, 8, 9

     #   -8:-7:-6:-5:-4:-3:-2:-1          #index position
# list_1 =[10,20,30,40,50,60,70,80]     # here i want to access the element 4.index postion(0,1,2,3,4,5)
     #   0 : 1: 2: 3: 4: 5: 6: 7          #index position
'''+ve index'''  #in syntax we use []
# print(list_1[3])          # o/p will be 4.
'''-ve index'''
# print(list_1[-4])            # o/p will be 3


'''############## SLICING ################'''# in syntax we use [s:s:s]-->default[start takes as 0:stop(n-1):step as 1]
# -->extract a portion or a sub sequence of elemets from a sequence like list tuple sets or string.
# -->syntax: sequence(start,stop,step)
# print(list_1[2:4])    


''' +ve forward -------------------->'''
# print(list_1[4:7])    #[50,60,70]
''' -ve forward -------------------->'''
# print(list_1[-4:-1])    #[50,60,70]

''' +ve backward <-------------------'''
# print(list_1[6:3:-1])     #[70,60,50]
''' -ve backward <-------------------'''
# print(list_1[-2:-5:-1])     #[70,60,50]

'''############## SKIPPING ################'''
# print(list_1[::4])     #[10,20,30,40,60,70,80]


'''############## LIST METHODS ################''' #-->.methodname(arg)
# -->append()-->appending only one element .
# -->extend()-->extending with another list or group of elements.
# -->copy()-->returns the copy of existing list.
# -->clear()-->remove all elements from the existing list.
# -->count()-->returns no. of elements in the list.
# -->index()-->returns the index of first occurant element.
# -->remove()-->remove first occurrent element in the list.
# -->pop()--> remove the element using index.
# -->insert()-->adding element at particular index.
# -->reverse()-->it reverse the elements in the list.
# -->sort()--> can sort in dec or ascend
# list_1 =[10,20,30,40,50,60,70,80]
'''APPEND'''
# list_1.append(9)   # it will append only one and append in last index.
# print(list_1)
'''EXTEND''' # .extend([])
# list_1.extend([[8,9],4,"vasu"])   # we can extend with many arg and add in last only.
# print(list_1)    
'''COPY''' 
# new_list = list_1.copy()    #storing same list into another variable.
# print(new_list)
# new_list.append("vasu")
# print(list_1)
# print(new_list)              # here we are appending the str into new list. it wont effct to original list.
'''CLEAR'''
# list_1.clear()
# print(list_1)              #clear all the elements in the list.
'''COUNT'''
# print(list_1.count(50))          #it gives count of how many 50's are present in the list.
'''INDEX'''
# print(list_1.index(50))          # i want index for value 50. so o/p will 4 now.
                                 # if we have more than value "50". then the first occurence 50's index will be the o/p.
'''REMOVE'''
# list_1.remove(50)                #the required first element will be removed. once it remove we cannot store or return into the list again.
# print(list_1)                    # if we have same element like 50 more than 1, then we have use for loop condition.
'''POP''' #-->(enter the index value)
# num = list_1.pop(4)      #4 is index value. and the value under index 4 is storing in num variable.
# print(list_1)
'''INSERT''' #-->two arguments(index,element)
# list_1.insert(2,"vasu")            #we can insert the value at any index.
# print(list_1) 
'''REVERSE'''
# list_1.reverse()            #it reverse the elements.
# print(list_1)
'''SORT'''
# list_1.sort(reverse = True)             #it sorts the values in decending order.
# print(list_1)
# list_1.sort(reverse = False)             #it sorts the values in ascending order.
# print(list_1)
'''LEN'''
# print(len(list_1))   # count of elements in the list.



'''############## NESTED LIST ################'''
# -->list in list.
# matrix =[[1,2,3],[4,5,6],[7,8,9]]
# print(matrix[2][2])    #o/p:9  #([index of list_req in whole list][index of the element of list_req ])



'''############### LIST COMPREHENSIVE #############'''
# -->provide a easy way to create a list.
# syntax: [expression for item in iterable]
# empty_list = []
# for i in range(45):
#     result = i ** 2    #print(result)   # for this, i want o/p into list. # to achieve this, create empty list and append the o/p into empty list.
#     empty_list.append(result)
# print(empty_list)

#above thing i want in one single line.
# print([i**2 for i in range(5)])

'''using if condition''' 
# empty_list = []
# for i in range(10):
#     if i%2 ==0 :
#         empty_list.append(i)
# print(empty_list)
# print([i for i in range(10) if i%2 == 0])   #o/p : [0, 2, 4, 6, 8]...to achieve proper o/p here we are using if condition.
# print([i%2==0 for i in range(10)])    #o/p :[True, False, True, False, True, False, True, False, True, False]

'''eg.'''
# emp_details = ["charishma","vasu","sreenu","sreenu","srinivas","kiran","kiran","sreenu","kiran","charishma","vasu","srinivas"]
'''remove'''#: removing by using element.
# # empty_list_1 = []
# for i in emp_details :
#     if i =="sreenu":
#         emp_details.remove(i)
# print(emp_details)                 #here first sreenu is removed. but i want to remove all sreenu occurance in the list.
# empty_list_1 = []
# for i in emp_details :
#     if i !="sreenu":
#         empty_list_1.append(i)
# print(empty_list_1)            # here total all sreenu occurence are removed.
#above code in list comprehence:
# print([i for i in emp_details if i !="sreenu"])

'''index'''#: here i want a list with index values of "sreenu" occurence.
# sreenu_index = []
# for i in range(len(emp_details)):
#     if emp_details[i] == "sreenu":
#         sreenu_index.append(i)
# print(sreenu_index)
# print([i for i in range(len(emp_details)) if emp_details[i] == "sreenu"] )


''' ################ QUIZ ##################'''
# 1.
# my_list = [10,20,30,40,50]
# print(my_list[1:4])    #o/p :[20,30,40]
# 2. extend is used to add multiple elements to end of the list.
# 3. 
# fruits = ["apple","banana","cherry"]
# i want to remove banana from the list.
# fruits.remove("banana")
# print(fruits)
# 4. len function return the no of elements in the list.
# 5.list of even number from 0-10:
# print([x for x in range(11) if x%2 == 0])


''' ################ TASK ##################'''
# 1.reverse list:
# my_list = [10,20,30,40,50,11]
# my_list.reverse()               #using list method
# print(my_list)
# print(my_list[6::-1])        # +ve backward
# print(my_list[:-7:-1])      # -ve backward

# 2.common elements:  o/p:[4,5]
# empty_list = []
# list1 = [1,2,3,4,5]
# list2 = [4,5,6,7,8]
# for i in list1:
#     if i in list2:
#        empty_list.append(i)
# print(empty_list)


# 3.unique elements:
# original_list = [1,2,2,3,4,4,5]
# set_conv = set(original_list)
# list_conv = list(set_conv)
# print(list_conv)              # using set conv.
# unique_elements = []
# for i in original_list:
#     if i not in unique_elements:
#         unique_elements.append(i)
# print(unique_elements)           #using for loop and membership statement.

# 4.remove duplicates:
# duplicate_list = [1,2,2,3,4,4,5]
# set_conv = set(duplicate_list)
# list_conv = list(set_conv)
# print(list_conv)                # using set conv.
# duplicates_removed_elements = []
# for i in duplicate_list:
#     if i not in duplicates_removed_elements:
#         duplicates_removed_elements.append(i)
# print(duplicates_removed_elements)         #using for loop and membership statement ,duplicates are removed.

'''############ EXERCISE ############'''
# 1.concatenate two list:
# list_1 = [1,2,3,4,5]
# list_2 = [6,7,8,9,10]
# print(list_1+list_2)

# 2.repeats a list three times and print:
# list_1 = [1,2,3,4,5]
# three_times = list_1*3
# print(three_times)

# 3.list removal even indicates: o/p :[2,4]
# list_1 = [1,2,3,4,5]
# #         0,1,2,3,4......>index position.
# no_even_index = []
# for i in range(1,len(list_1)):
#          if i%2 == 0:
#               no_even_index.append(i)
# print(no_even_index)

# 4.list insertion:
# my_list = [1,2,3,4,5,6,7]
# for i in reversed([10,11,12]):
#     my_list.insert(0,i)
# print(my_list)









