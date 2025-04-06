'''############# MINI PROJECT 1 ################ 17/03/25'''

dict = {"user1":"user1@123",
         "user2":"user2@123",
         "user3":"user3@123",
         "user4":"user4@123",
         "USERID1": [12,45,67],      #case sensitive, user1 and USER1 are not same.
        (1,2): "charishma",          #keys can be tuple, number or string.
        (4,5):{1:"hyd"},
        1:"string"}
# dict = {}
while True:
    print("\nDictionary management system")
    print("1.Add a word")
    print("2.Search for word")
    print("3.Display all words")
    print("4.Update Meaning")
    print("5.Delete word")
    print("6.exit")
    
    choice = input("enter your choice : ")
    
    if choice == "1": #Add a word
        word = input("enter the word :").lower()
        meaning = input("enter the meaning : ").lower()
        dict[word] = meaning
        print("word added successfully")

    elif choice == "2": #Search for word
        while True:  
            word = input("Enter the word to search: ").lower()
            if word in dict:  # Check if the word exists in the dictionary
                print("Meaning:", dict[word])
                break  # Exit the loop if a valid word is found
            else:
                print("Word not found in the dictionary. Please enter a correct word.")

    elif choice == "3":  #Display all words
        if dict:
            print("Words and their meanings:")
            for word, meaning in dict.items():
                print(f"{word}: {meaning}")
        else:
            print("the dict is empty")         


    elif choice == "4":     #Update Meaning
        while True:  # Infinite loop to keep asking for input
            word = input("Enter the word to update meaning: ").lower()
            if word in dict:  # Check if the word exists in the dictionary
                meaning = input("enter the meaning to update :")
                dict[word]=meaning
                print(dict)
                break  # Exit the loop if a valid word is found
            else:
                print("Word not found in the dictionary. Please enter a correct word.")
            
    elif choice == "5":     #Delete word
        while True:  # Infinite loop to keep asking for input
            word = input("Enter the word to get deleted: ").lower()
            if word in dict:  # Check if the word exists in the dictionary
                dict.pop(word)
                print("Word deleted successfully!")
                print(dict)
                break  # Exit the loop if a valid word is found
            else:
                print("Word not found in the dictionary. Please enter a correct word.") 

    elif choice == '6':
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please enter a valid option.")

















