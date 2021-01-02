"""Pig Latin"""
# Согласные
consonants = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's',
              't', 'v', 'w', 'x', 'y', 'z')

# Гласные
vowels = ('a', 'e', 'i', 'o', 'u')

while True:
    string = input("Enter a word: ")

    for item in consonants:
        if item == string[0]:
            string = string[1:] + item + "ay"
        else:
            string += "way"

    print("{}".format(string))
    try_again = input("\n\nWill you try again? Enter for continue, N for exit\n")

    if try_again.lower() == "n":
        break
