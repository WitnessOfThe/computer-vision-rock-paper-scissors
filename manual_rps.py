import random

def get_computer_choice():

    return random.choice(['rock', 'paper','scissors']) 

def get_user_choice():

#    while True:

    choice = input("Gimmi 'rock', 'paper' or 'scissors' ")

 #       if choice in ['rock', 'paper','scissors']:

    return choice

  #      else:

   #         print('Try again, one from the list: "rock", "paper" or"scissors"')            
def get_winner(computer_choice,user_choice):

    if computer_choice == 'rock' and user_choice == 'scissors':

        print("You lost")

    elif computer_choice == 'rock' and user_choice == 'paper':

        print("You won")

    elif computer_choice == 'scissors' and user_choice == 'paper':

        print("You lost")

    elif computer_choice == 'scissors' and user_choice == 'rock':

        print("You won")

    elif computer_choice == 'paper' and user_choice == 'rock':

        print("You lost")

    elif computer_choice == 'paper' and user_choice == 'scissors':

        print("You won")

    elif computer_choice == user_choice:

        print("It is a tie!")

if __name__ == '__main__':

#    print(get_computer_choice())
#    print(get_user_choice())   
     get_winner(get_computer_choice(),get_user_choice()) 