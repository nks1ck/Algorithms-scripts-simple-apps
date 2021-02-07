from all_symbols import *

import sys
import random


while True:
    try:
        password_length = int(input('Enter the number of characters of the password (0 - To exit): '))

        new_password = ''

        symbols_counter = 0
        for symbol in printable:
            while symbols_counter < password_length:
                symbol = random.randint(0, len(printable))
                new_password += printable[symbol - 1]
                symbols_counter += 1

        print(new_password)

        if password_length == 0:
            break
    except:
        print('Error. Try it again!')