'''############# Day10 ################ 17/03/25'''

#--> enclosed a comma-separated list of key-value using curly braces.
#--> mutable datatype(changable), add or remove items from the dict has been created.
#--> duplicate keys are not allowed.
#--> dict are used to store data values in form of key:value.
#--> values can be any type. while keys must be immutable like number, tuple and strings.
#--> keys are case sensitive.
#--> ordered o/p.
#--> eg. users data, product quantity, etc.
# syntax: {key1:value, key2:value}
# dict_1 = {}       #empty dict.
# 

# users = {"user1":"user1@123",
#          "user2":"user2@123",
#          "user3":"user3@123",
#          "user4":"user4@123",
#          "USERID1": [12,45,67],      #case sensitive, user1 and USER1 are not same.
#         (1,2): "charishma",          #keys can be tuple, number or string.
#         (4,5):{1:"hyd"},
#         1:"string"}
# print(users)



'''***########### DICT METHODS ############'''
"# CLEAR()"
#print(users.clear())
"# COPY()"
# user_updated = users.copy()
# print(user_updated)
"# GET()"
# print(users.get((1,2)))         # use round braces only.
# print(users.get((1,3)))         #if key is not present it shows as none.
# print(users.get[(1,2)])         # why im not able excute. the key is present in the given dict.
"# POP() "          #removing the entire element(k:v)
# users.pop("user2")
# print(users)
# new = users.pop("user2")
# print(new)              #here storing the popped value.
"# ITEMS() "          # returns a list containing in tuple format with each key value pair.
# print(users.items())        # like [('user1', 'user1@123'), ('user2', 'user2@123'), ('user3', 'user3@123'), ('user4', 'user4@123'), ('USERID1', [12, 45, 67]), ((1, 2), 'charishma'), ((4, 5), {1: 'hyd'}), (1, 'string')]
"# KEYS()  "       #it returns a list containing only keys
# print(users.keys())          # dict_keys(['user1', 'user2', 'user3', 'user4', 'USERID1', (1, 2), (4, 5), 1])
"# VALUES()  "        #it returns a list containing only values.
# print(users.values())           #dict_values(['user1@123', 'user2@123', 'user3@123', 'user4@123', [12, 45, 67], 'charishma', {1: 'hyd'}, 'string'])
"# UPDATE()"
'''# WAY1:'''
# new = {"user2":6839}            #if key is present , the value get updated.
# users.update(new)
# print(users)
# new = {"user7":6839}            #if key is not present , key:value will be added as new.
# users.update(new)
# print(users)
'''# WAY2:'''
# users.update({"user3":9376})            #directly printing with updated value.
# print(users)
"# ADD()"# add using [ ] for the key as shown
# users[13]=[23,45,67]     # here 13 key is not present so it is getting added.
# print(users)
# users[1]=[23,45,67]         # here 1 key is present so the value is getting updated.
# print(users)
# eg:
# dict_1 = {}
# user_name = input("enter the username : ")
# pass_word = input("enter the password : ")
# dict_1[user_name]=pass_word
# print(dict_1)


'''################ QUIZ #################'''
# 1.print o/p:
# my_dict = {'a':1,'b':2,'c':3}
# print(len(my_dict))         # o/p : 3
# 2. method used to add new key:value pair to a dict:
# update()
# 3.access the avlye associated with key 'age'?: both results 39.
# my_dict = {"name":"python","age":39,"city":"hyd"}
# print(my_dict["age"])         # here we know age key is present so using []
# print(my_dict.get("age"))              #here if we dont know age key is present or not then use .get()
# 4. if you try to access a key that doesn't exist in the dict using square braclets:
# it raises a key error.
# 5. returns a list  of all the keys in a dict:
# print(my_dict.keys())
# 6. returns a list  of all the values in a dict:
# print(my_dict.values())


''' ######### TASK ##############'''
# task1:add new key-value pair :
# my_dict = {"name":"python","age":39}
# my_dict["city"]="hyd"
# print(my_dict)
# task2: code to acces and print the value associated with key 'price':
# product_info = {"name":"laptop","brand":"dell","price":1200}
# print(product_info["price"])
# task3: remove the key-value pair with key 'city':
# my_dict = {"name":"python","age":39,"city":"hyd"}
# my_dict.pop("city")
# print(my_dict)
# task4:print only keys:
# my_dict = {"name":"python","age":39,"city":"hyd"}
# print(my_dict.keys())
# task5: print values:
# print(my_dict.values())


'''####### EXERCISE ##########'''
# 1. updates a dictionary with new key-value pair:
# my_dict = {"name":"python","age":39,"city":"hyd"}
# key = input("enter the key :")
# value = input("enter the value :")
# my_dict[key]=value
# print(my_dict)
# 2.access and print a the value associated with specified key in a dict:
# my_dict = {"name":"python","age":39,"city":"hyd"}
# print(my_dict["age"])
# 3.removes a key_value pair from a dict:
# my_dict = {"name":"python","age":39,"city":"hyd"}
# my_dict.pop("city")
# print(my_dict)
# task4:print only keys:
# my_dict = {"name":"python","age":39,"city":"hyd"}
# print(my_dict.keys())
# task5: print values:
# print(my_dict.values())











