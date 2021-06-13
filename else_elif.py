if (False):
    print("This won't happen")  #This if statement is not true, so the first print doesn't happen, but it instead triggers the else statement

else:
    print("This will happen")


if (False):
    print("This won't happen again")  #This if statement is not true, so it checks the elif instead

elif (True):
    print("This will happen again")  #This prints because the elif is true

#OUTPUT-> This will happen
#OUTPUT-> This will happen again