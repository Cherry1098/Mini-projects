'''############# Day16 ################ 25/03/25'''

'''FILE HANDLING'''
# --> File operations such as opening a file, reading from it, writing into it, closing it, renaming a file, deleting a file and various file methods.

'''modes of files:'''
# mode 'r': open an existing for read operation.
# mode 'a': open a existing file for append operations. it wont override existing data.(add,insert).it works as append operation.it wont truckate. old data wont lost.
# mode 'w': open an existing file for write operations. if the file already contains some data then it will be overridden but if the file is not present then it creates the file as well.


'''file methods:'''
'read()' #: returns the file content from existing file only.
# file = open("demo.txt",mode='r')       # in open open function we will pass arguments.
# read_data = file.read()
# print(read_data)
# file.close()          #when file is open , it must close. in between we can perform many operations.
# o/p:
# welcome to python life
# we started new python classes
# training starts from today

'readline()'#: read single line.
# file = open("demo.txt",mode='r')     
# read_data = file.readline()     #only one line will read and that too first line.
# print(read_data)                # if we want to read a particular line. then using looping conecpt we have to built a code.
# file.close()  

'readlines()' #: the content present in file will convert into list of substrings.
# file = open("demo.txt",mode='r')     
# read_data = file.readlines()   
# print(read_data)               
# file.close()  

'write()' # : 
# mode:a--> data wont loss.
# file = open("demo.txt",mode='a')     
# write_data = file.write("\nthis is new technology")             # data will add in last and it append to existing data.          
# file.close() 

# mode:w --> data will update or overrited. entire existing data will truckate.
# file = open("demo.txt",mode='w')     
# write_data = file.write("we are updating the text this month")             # data will add in last and it append to existing data.          
# file.close() 

'writelines()'
# mode:w --> data will update or overrited. entire existing data will truckate.
# voter_id = ['123\n','456\n']
# file = open("demo.txt",mode='w')     
# write_data = file.writelines(voter_id)             # data will add in last and it append to existing data.          
# file.close() 

# mode:a --> data will update or overrited. entire existing data will truckate.
# voter_id = ['123\n','456\n']
# file = open("demo.txt",mode='a')    
# file.write("\n")  
# write_data = file.writelines(voter_id)             # data will add in last and it append to existing data.          
# file.close()

'creating new file' # with some data. use only mode='w'
# file = open("string.txt",mode = 'w')
# write_data = file.write("welcome to pythonlife")
# file.close()

'creating new file' # with some data. alternate mode='a'
# file = open("string.txt",mode = 'a')
# write_data = file.write("welcome to pythonlife")
# file.close()

'seek()' '&' 'tell()'
# mode : w+
# file = open("demo2.txt",mode = 'w+')
# write_data = file.write("pythonlife")
# print(file.tell())          # tell() tells where the cursor is present.
# file.seek(0)
# read_data = file.read()
# print(read_data)            #empty. because the cursor is in ending index.
# file.close()

'To handle the file present in some other working directery using w+,a+,r+'
# -->copy the path of the file from properties. filename.extension should mention.
# voter_id = ['124376667','38842765','54446962']
# 'mode = w+'
# file = open("C:\\Users\\chari\\OneDrive\\Desktop\\python_new.txt", mode= 'w+')       #  if file is not present , it will create new and can perform operations.
# write_data = file.writelines(voter_id)                                                # it can perform all operations like create new file, wrtie on it, read the file and truncate the file. but cannot perform append
# 'mode = r+'
# file = open("C:\\Users\\chari\\OneDrive\\Desktop\\python_new.txt", mode= 'r+')          # r+ works on existing file only. i cannot create file or truncate.but append the data.
# 'mode = a+'
# file = open("C:\\Users\\chari\\OneDrive\\Desktop\\python_new.txt", mode= 'a+')          #  a+ works as r+ but can create new file but no truncate
# write_data = file.writelines(f"\n {item}" for item in voter_id) 
# print("length:",end="")       
# print(file.tell())          #here entering into next line or spaces also will count as 1
# file.seek(0) 
# read_data = file.read()
# print(read_data)
# file.close()


'using python programming delete the file and rename the file name'
'rename:'
# import os
# old_name = "demo.txt"
# new_name = "sample1.txt"
# os.rename(old_name,new_name)

'delete:'
# import os
# file_name = "python_new.txt"
# if os.path.exists("C:\\Users\\chari\\OneDrive\\Desktop\\python_new.txt"):
#     os.remove("C:\\Users\\chari\\OneDrive\\Desktop\\python_new.txt")
#     print(f"File '{file_name}' deleted successfully.")
# else:
#     print(f"File '{file_name}' not found.")


'creating csv file with in same folder'
# import csv      #built-in module
# csv_file = "students.csv" 
# data = [["id","place","grade"],
#         ["123","pavan","A+"],
#         ["1234","pavan1","A"],
#         ["12345","pavan2","B+"]
#         ]
# file = open(csv_file,mode='w+',newline="")
# write = csv.writer(file)
# write.writerows(data)
# file.close()


'project:' # audio book reader: pdf-mp3
# hint: extract third party modules
# pypdf-->used to extract the data.
# gtts--> google text to search
# when where want to install third party module, we have create a virtual environment . then activate then depenedencies module are install through pip tool. then use import module
#when we want to use the modules for different projects as global , some glitches happened. to over come use virtual environment.
# install--> through pip installation
# import pypdf
# import gtts






























