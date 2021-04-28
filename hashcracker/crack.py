import hashlib


hash = input('[*] Хэш => ')
dict = input('[*] Путь до словаря => ')

def md5_brut(hash, dict):
    try:
        descript = open(dict, 'r', encoding='utf-8', errors='ignore')
    except:
        print('[*] Словарь не существует или файл не найден!')
        exit()


    for password in descript:
        filemd5 = hashlib.md5(password.encode().strip()).hexdigest()

        if(hash == filemd5):
            print(f"[*] Легко. Пароль => {password}")
            break
        else:
            print("[*] Ой..")


md5_brut(hash, dict)
