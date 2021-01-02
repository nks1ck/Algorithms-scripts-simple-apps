"""Pig Latin"""
# Согласные
consonants = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's',
              't', 'v', 'w', 'x', 'y', 'z')

# Гласные
vowels = ('a', 'e', 'i', 'o', 'u')

string = input("Enter a word: ")

for item in consonants:
    if item == string[0]:
        string = string[1:] + item + "ay"
        print(string)
        break

for var in vowels:
    if var == string[0]:
        string += "way"
        print(string)
        break
