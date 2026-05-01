
# MINI PROGECT IN PYTHON :- GUESS THE TARGET(RANDOM) NUMBER 

'''import random
target= random.randint(1,100)

while True:
    userChoice=int(input("Guess the target OR Quit(Q): "))
    if(userChoice=="Q"):
        break
    userChoice=int(userChoice)
    if( userChoice==target):
        print("success :corect guess!!")
        break
    elif( userChoice<target):
        print("your no was too small. Take a bigger guess...")
    else:
         print("your no was too big. Take a smaller guess...")

print("____GAME OVER____")   '''

# MINI PROGECT IN PYTHON :- GUESS THE TARGET(RANDOM) PASSWORD GENERATOR.

import random
import string
pass_len=10
charValues= string.ascii_letters + string.digits +string.punctuation
   # list comprehension[function for i in range(n)]
passWord= "".join([random.choice(charValues)for i in range(pass_len)])

'''passWord=""
for i in range(pass_len):
    passWord+= random.choice(charValues)'''

print("YOUR RANDOM PASSWORD IS :-", passWord)
  