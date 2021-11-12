# file for the intro, story

# import modules

import time
import os

# begin story

os.system("clear")
print('Hey...')
time.sleep(1)
input('\nPress enter to continue\n> ')
os.system("clear")

print('You were in a terrible accident...')
time.sleep(1)
print('\nThe hospital staff weren\'t sure if you were going to recover.')
time.sleep(1)
input('\nPress enter to continue\n> ')
os.system("clear")

print('Do you remember who you are.?')
time.sleep(1)
user_name = input('\nEnter your name\n> ')
os.system("clear")

print('I\'m glad to hear it, ' + user_name + '.')
time.sleep(1)
print('\nNot everybody was so lucky.\n')
time.sleep(1)
answers1 = ['What happened?', 'Where\'s my bag?']
print('Choose your response:')
n = 0
for i in answers1:
    n += 1
    print(n, i)
time.sleep(1)
answer = input('\n> ')
os.system("clear")
if answer == '1':
    print('You don\'t remember?!\nI suppose that\'s just as well.')
    time.sleep(1)
    print('There was an explosion while you were on your way to the City Hall to collect your inheritance.')
    time.sleep(1)
    input('\nPress enter to continue\n> ')
    os.system("clear")
    print('YOU SUDDENLY REMEMBER')
