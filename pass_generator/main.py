from all_symbols import *
import random
import re

#password_length = int(input('Введите количество символов пароля: '))
password_length = 7
new_password = ''


i = 0
for symbol in printable:
    while i < password_length:
        symbol = random.randint(0, len(printable))
        new_password += printable[symbol - 1]
        i += 1

print(new_password)