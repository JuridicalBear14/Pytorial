
dots = "."  #A string to keep the dots in

print("How many rows do you want?")

rows = int(input())  #Takes input form the user (cast to a number)

for i in range(rows):  #Adds one dot to the string and prints the new string out, then loops for [input] times
    print(dots)
    dots = dots + "."