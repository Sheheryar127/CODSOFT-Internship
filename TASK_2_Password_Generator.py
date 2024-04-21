#A password generator is a useful tool that generates strong and random passwords for users. This project aims to create a password generator application using Python, allowing users to specify the length and complexity of the password.
#User Input: Prompt the user to specify the desired length of the password.
#Generate Password: Use a combination of random characters to generate a password of the specified length.
#Display the Password: Print the generated password on the screen.

#Import the module

import string
import random

#Take the length of the password as an input
Pass_Length = int(input("Enter the length of the password : "))

print("""----- Choose the Character set for the password from :
      1. Digits.
      2. Letters.
      3. Special Characters.
      4. Exit """)

#Create the empty string
Character_List = []

#Getting Character set for the password
while(True):
    #Take the number as an input
    Pass_Choice = int(input("Pick the number : "))

    if Pass_Choice == 1:
        #Adding letters to the Special Characters
        Character_List += string.ascii_letters

    elif Pass_Choice == 2:
        #Adding letters to the Special Characters
        Character_List += string.digits
    
    elif Pass_Choice == 3:
        #Adding letters to the Special Characters
        Character_List += string.punctuation
    
    elif Pass_Choice == 4:
        print("Exit")
        break

    else:
        print("Enter the Valid Option.")

#Create The Empty List by the name of password

Password = []

for i in range(Pass_Length):

    #Store the Random values in random character
    Random_Choice = random.choice(Character_List)

    #Append a random character to the password
    Password.append(Random_Choice)

#Printing Password as a string
print("The Random Password is : " + "".join(Password))