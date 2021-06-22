
vowels = ["a", "e", "i", "o", "u"]  #A list of all vowels (so we cna use a loop)

print("Please input sentence")

sentence = input().lower()  #Takes the user input, makes it lower case for simplicity

for i in range(len(vowels)):  #Replaces all instances of vowels item "i" in sentence with blank, repeats for each vowel
    sentence = sentence.replace(vowels[i], "")

print(sentence)