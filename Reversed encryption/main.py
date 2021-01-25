text = input("Enter a text: ")


def reverse(txt):
    encrypted = ''
    i = len(txt) - 1
    while i >= 0:
        encrypted += txt[i]
        i -= 1

    print(encrypted)        

reverse(text)