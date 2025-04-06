'''############# Day11 ################ 18/03/25'''


# --> unordered(set do not have a defined order), do not allow duplicate values.
# --> appears in a different order every time so cannot be referred to by index or key.
# --> created by placing all the elements inside curly braces{},separated by comma, or by using built-in set() class/functions.
# --> it can have any number of elements and they may be of different types(int,float,tuple,string.etc).but set cannot have mutable elements like lists, sets or dict as its elements.

# set_1 = {}      # this empty dict.
# set_1 = {1, }       # this is set.
# set_1 = set()           # this is emptyset.

# set_1 = {1,2,3,4,"vasu","charishma","sameul","krishna","sridevi","pavani",5.7}
# print(set_1)

'''############# METHODS ################ '''
'''# add()'''
# set_1.add("python")       # the element can add at any index.
# print(set_1)
'''# clear()'''
# set_1.clear()
# print(set_1)                #returns empty set() function.
'''# copy()'''
# set_2 = set_1.copy()
# print(set_2)
'''# pop()'''
# obj = set_1.pop()         #randomly any element will pop.
# print(obj)            #real time : games, lottory tickets
'''# remove()'''
# obj = set_1.remove("sridevi")
# print(set_1)
'''# update()'''
# set_2 = {"python","english","mytask"}
# set_1.update(set_2)
# print(set_1)            # here set_2 is adding into set_1
# print(set_2)            #remains same.

'''############# OPERATIONS ################ '''
# set_1 = {1,2,3,4,5,6}
# set_2 = {5,6,7,8,9,10}
'''# union()'''                   #returns a set containing the union of sets.
# print(set_1.union(set_2))
'''# difference()'''              #returns a set containing the difference between two or more sets.
# print(set_1.difference(set_2))          # results set_1 exclude elements present in set_2
'''# intersection()'''            #returns aset, that is the intersection of two or more sets.
# print(set_1.intersection(set_2))        #prints common elements
'''# isdisjoin()'''               #returns whether two sets have a intersection or not result in boolean value.
# print(set_1.isdisjoint(set_2))          #here we have two elements in common. so o/p is false/
# set_1 = {1,2,3,4,5,6}
# set_2 = {1,2,3}
'''# issubset()'''                #returns whether another set contains this set or not.
# print(set_1.issubset(set_2))          # here all set_1 elements are not present in set_2.so o/p is false.
# print(set_2.issubset(set_1))           # here all set_2 elements are present in set_1.so o/p is true.
'''# issuperset()'''              #returns whether this set contains another set or not.(primary set)
# print(set_1.issuperset(set_2))          # here set_2 should be part of set_1. so o/p is true.
# print(set_2.issuperset(set_1))          # here set_1 should be part of set_2. so o/p is false.
'''# symmetric_differenece()'''   #returns a set with the symmetric differences of two sets.
# print(set_1.symmetric_difference(set_2))            #opp. to intersection.
'''# frozenset()'''             # 
# set_1 = {1,2,3,4,5}
# set_1.add("vasu")
# print(set_1)
# set_2 = frozenset(set_1)            #set_2 contains set_1 elements only.
# set_2.add("vasu")                   # frozenset -cannot perform modifictionas-immutable set.
# print(set_2)                          # operations can perform like union.etc


''' #######  frozenset task #########'''
# set_1 = {1,2,3,4,5}
# set_2 = {5,6,7,8,9,10}
# frozenset(set_2)
'''# union()'''  
# print(set_1.union(set_2))
'''# difference()'''             
# print(set_1.difference(set_2)) 
'''# intersection()'''  
# print(set_1.intersection(set_2))
'''# isdisjoin()'''          
# print(set_1.isdisjoint(set_2))       
# set_1 = {1,2,3,4,5,6}
# set_2 = {1,2,3}
'''# issubset()'''               
# print(set_1.issubset(set_2))         
# print(set_2.issubset(set_1))       
'''# issuperset()'''          
# print(set_1.issuperset(set_2))        
# print(set_2.issuperset(set_1))       
'''# symmetric_differenece()'''  
# print(set_1.symmetric_difference(set_2))            





'''############# QUIZ ################ '''
# 1.o/p:
# my_set = {1,2,3,4,5}
# print(len(my_set))      #o/p:5
# 2.method is used to add an element to a set:
# add()
# 3. method use to find the elements that are common in both sets:
# set1 = {1,2,3,4,5}
# set2 = {4,5,6,7,8}
# print(set1.intersection(set2))
# 4.sets in python:
# sets are mutable.

'''############# task and exercise ################ '''
# 1.set intersection: o/p : {4,5}
# set1 = {1,2,3,4,5}
# set2 = {4,5,6,7,8}
# print(set1.intersection(set2))
# 2.set union:
# print(set1.union(set2))     #{1, 2, 3, 4, 5, 6, 7, 8}
# 3.set difference:
# print(set1.difference(set2))        #{1, 2, 3}
# 4.set symmetric diff:
# print(set1.symmetric_difference(set2))     # {1, 2, 3, 6, 7, 8}
# 5.membership test:
# print(4 in set1)            #True


