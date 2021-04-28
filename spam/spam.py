from termcolor import colored
import subprocess
import time
import pyautogui
subprocess.call('', shell=True)

def SendMessage():
    time.sleep(2)
    # The message you want to send
    message = "1"
    # How many times do i send a message?
    iterations = 10

    for i in range(iterations):
        pass

    while iterations > 0:
        iterations -= 1

        pyautogui.typewrite(message.strip())
        pyautogui.press('enter')

    print('Done, high five')

def SendScript():
    time.sleep(2)
    with open('text.txt') as f:
        lines = f.readlines()
    for line in lines:
        pyautogui.typewrite(line.strip())
        pyautogui.press('enter')

    print('It was hard, but we did it, high five.')

print(colored('~'*50, 'red'))
print(colored('Welcome bro \(O V O)/', 'green'))
print(colored("Let's make fun of someone?", 'green'))
print(colored('~'*50, 'red'))


print(colored("\t[1] ===> Resend the same message (─__─)", 'magenta' ))
print(colored("\t[2] ===> Send titles from the script \(v _ v)/", 'magenta'))

print(colored('~'*50, 'red'))
print('\n')
option = input(colored('[Choose an option]==> ', 'cyan'))

if option == "1":
    SendMessage()
elif option == "2":
    SendScript()
else:
    print(colored('Choose a function! ¯\_(-_-)_/¯', 'red'))