import random

def get_computer_choice():

    return random.choice(['rock', 'paper','scissors']) 

def get_user_choice():

    while True:

        choice = input("Gimmi 'rock', 'paper' or 'scissors' ")

        if choice in ['rock', 'paper','scissors']:

            return choice

        else:

            print('Try again, one from the list: "rock", "paper" or"scissors"')            

if __name__ == '__main__':

    print(get_computer_choice())
    print(get_user_choice())    