
print("Input a number!")
number = input()  #Gets user input and stores it in number

remainder = number % 7
#Gives the remainder of number divided by 7

if (remainder == 0):  #If the remainder is 0 that means it divided cleanly
    print("It is divisible!")
else:  #If it's anything else it means 7 doesn't evenly go into our number
    print("It's not divisible!")