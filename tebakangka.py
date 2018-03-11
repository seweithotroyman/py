# imported libraries go here

import random

# global variable go here

game_on = None
tebakkan = None
secret = None

# function for easy version

def difficulty_level_easy():
    global secret
    secret = int(random.randrange(0,100))
    while game_on:
        tebakkan = int(raw_input('Masukkan Tebakan angka. '))
        if tebakkan > secret:
            print('Salah bro! angka terlalu besar. Masukan angka yang lebih kecil!')
        elif tebakkan < secret:
            print('Salah bro! angka terlalu kecil. Masukan angka yang lebih besar!.')
        elif tebakkan == secret:
            print('Hore... boleh juga lo!')
            play_again()

# function for hard version

def difficulty_level_hard():
    global guesses
    global secret
    guesses = 3
    secret = int(random.randrange(0, 100))
    for i in range(guesses):
        tebakkan = int(raw_input('Masukkan Tebakan angka. '))
        if i == 2:
            print('Game over. Anda kurang beruntung!!.')
            play_again()
        elif tebakkan > secret:
            print('Salah bro! angka terlalu besar. Masukan angka yang lebih kecil!')
        elif tebakkan < secret:
            print('Salah bro! angka terlalu kecil. Masukan angka yang lebih besar!.')
        elif guess == secret:
            print('Hore... boleh juga lo!')
            play_again()

# function for start game

def start_game():
    global game_on
    game_on = True
    level = raw_input('Selamat datang. Pilih easy, hard, atau keluar. = ')
    if level == 'easy':
        difficulty_level_easy()
    elif level == 'hard':
        difficulty_level_hard()
    elif level == 'quit':
        game_on = False
    else:
        start_game()

def play_again():
    global game_on
    game_on = True
    play = raw_input('Main lagi? ya atau tidak. ')
    if play == 'ya':
        start_game()
    else:
        game_on = False
        print ('Dasar lemah!!, baru gitu aja udahan')

start_game()

# function to stop game

# function calls go here
