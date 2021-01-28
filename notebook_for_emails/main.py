'''The simplest notebook for a emails in the console'''
import shelve


while True:
    try:
        db = shelve.open('db')
        name = input('Enter name: ')
        email = input('Enter email: ')

        if name == '`' or email == '`':
            print('App is closing... bye!')
            break
        else:
            pass

        db[name] = email

        for key in db:
            print(key, '=>', db[key])

        db.close()
    except:
        print('Some error')
