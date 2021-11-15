# file for the intro, story

# import modules

import time
import os

# begin story

os.system("clear")
a = input('(P)lay intro or (S)kip intro\n> ')
if a == 'p' or a == 'P':
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
    answer = input('\n> ')
    os.system("clear")
    if answer == '1':
        print('You don\'t remember?!')
        time.sleep(1)
        print('\nI suppose that\'s just as well.\n')
        time.sleep(1)
        print('There was an explosion while you were on your way to the City Hall to collect your inheritance now that you\'re 18.')
    if answer == '2':
        print('Your bag?\n')
        time.sleep(1)
        print('I believe it\'s right there on the chair beside you.\n')
        time.sleep(1)
        print('I hope you don\'t mind, but I looked inside as a security measure.\n')
        time.sleep(1)
        print('It looks like you have a letter from City Hall about some inheritance to collect now that you\'re 18.')
    time.sleep(1)
    answers2 = ['My inheritance?']
    print('\nChoose your response:')
    n = 0
    for i in answers2:
        n += 1
        print(n, i)
    input('\n> ')
    os.system("clear")
    print('Yeah, the word going around is that you had an uncle who recently passed away.\n')
    time.sleep(1)
    print('Rumor has it he left you some small fortune in the form of a ship, some units, and a note.')
    time.sleep(1)
    input('\nPress enter to continue\n> ')
    os.system("clear")
    print('How are you feeling?')
    time.sleep(1)
    answers3 = ['I feel alright. I should probably get going.', 'A little rough, but I have places to be.']
    print('\nChoose your response:')
    n = 0
    for i in answers3:
        n += 1
        print(n, i)
    answer = input('\n> ')
    os.system("clear")
    print('**You collect your bag and make your way to City Hall..**\n')
    time.sleep(1)
    print('**After being escorted through the proper channels, you collect a computer left to you by your uncle.**\n')
    time.sleep(1)
    input('\nPress enter to continue\n> ')
    os.system("clear")
    print('**You take the computer home and log on.**\n')
    time.sleep(1)
    print('**You log on to see a note on the desktop that has been left to you.**')
    time.sleep(1)
    input('\nPress enter to continue\n> ')
    os.system("clear")
    print('"Hey, ' + user_name + '. I know we were never very close, and for that I am sorry."\n')
    time.sleep(3)
    print('"I\'ve been sick for awhile now and I thought the least I could do is leave you what little I have left."\n')
    time.sleep(3)
    print('"I have a simple ship and a few units saved up from my adventuring days, and I know that you\'re about to be 18."\n')
    time.sleep(3)
    print('"That means you\'re about to be old enough to get your space permit, and start some adventuring of your own."\n')
    time.sleep(3)
    print('"I hope that you can forgive me for not being around,"\n')
    time.sleep(3)
    print('"and take these things to go make a name for yourself in the galaxy..."')
    time.sleep(3)
    input('\nPress enter to continue\n> ')
    os.system("clear")
    print('**And so you do.**\n')
    time.sleep(2)
    print('**You go and get your space permit,**\n')
    time.sleep(2)
    print('**and make your way to the hangar to lay eyes on your new ship for the first time.**\n')
    time.sleep(2)
    print('**It isn\'t anything fancy, but it\'ll do.**\n')
    time.sleep(2)
    print('**And so, with a heavy heart, and excitement for the adventure to come...**\n')
    time.sleep(2)
    print('**You set off...**')
    time.sleep(1)
    input('\nPress enter to continue\n> ')
else:
    os.system("clear")
    user_name = input('Enter your name\n> ')
os.system("clear")
start_of_game_items = ['100 gal of fuel', '1000 units (currency)', 'A desire to make money exploring the galaxy']
print('Game details:\n')
time.sleep(1)
print('What you start with...')
n = 0
for i in start_of_game_items:
    n += 1
    print(n, i)
print('\nGame rules:')
game_rules = ['You must try to acquire wealth by buying and selling resources across the galaxy.', 'Each planet has at least one unique resource.', 'Traveling requires fuel, and time.', 'The game will end once you reach 62 years of age.', 'You have a chance every time you travel to find a meteorite with a resource in it.']
n = 0
for i in game_rules:
    n += 1
    print(n, i)
print('\nWin conditions:')
win_con = ['Amass a total of 50,000 units']
n = 0
for i in win_con:
    n += 1
    print(n, i)
print('\nGood luck, ' + user_name + '!')
time.sleep(1)
input('\nPress enter to continue\n> ')
os.system("clear")
