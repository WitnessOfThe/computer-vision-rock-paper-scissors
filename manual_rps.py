import random

def get_computer_choice():

    return random.choice(['Rock', 'Paper','Scissors']) 

def get_user_choice():

#    while True:

    choice = input("Gimmi 'Rock', 'Paper' or 'Scissors' ")

 #       if choice in ['rock', 'paper','scissors']:

    return choice

  #      else:

   #         print('Try again, one from the list: "rock", "paper" or"scissors"')            
def get_winner(computer_choice,user_choice):
    print(computer_choice)
    if computer_choice == 'Rock' and user_choice == 'Scissors':

        print("You lost!")

    elif computer_choice == 'Rock' and user_choice == 'Paper':

        print("You won!")

    elif computer_choice == 'Scissors' and user_choice == 'Paper':

        print("You lost!")

    elif computer_choice == 'Scissors' and user_choice == 'Rock':

        print("You won!")

    elif computer_choice == 'Paper' and user_choice == 'Rock':

        print("You lost!")

    elif computer_choice == 'Paper' and user_choice == 'Scissors':

        print("You won!")

    else:#~ computer_choice == user_choice:

        print("It is a tie!")

if __name__ == '__main__':

#    print(get_computer_choice())
#    print(get_user_choice())   
     get_winner(get_computer_choice(),get_user_choice()) 