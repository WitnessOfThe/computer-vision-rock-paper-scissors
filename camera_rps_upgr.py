import cv2
from   keras.models import load_model
import numpy as np
import time
import random

class RockPaperScissors:

    def __init__(self):

        ## internal game variables

        self.user_wins       = 0
        self.rounds_played   = 0
        self.computer_choice = []
        self.user_choice     = []

        ## Model Upload

        self.model = load_model('keras_model.h5')

        ## Video Capture and Data Storage variable
        
        self.prediction = [np.array([1,1,1])]
        self.data       = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        self.cap        = cv2.VideoCapture(0)
        self.font       = cv2.FONT_HERSHEY_SIMPLEX

    def get_winner(self):
    #    print(computer_choice)

        self.computer_choice = self.get_computer_choice.__func__() 
        self.user_choice     = self.get_user_choice()

        if self.computer_choice == 'Rock' and self.user_choice == 'Scissors':

            print("You lost")
            return 0

        elif self.computer_choice == 'Rock' and self.user_choice == 'Paper':

            print("You won!")
            return 1

        elif self.computer_choice == 'Scissors' and self.user_choice == 'Paper':

            print("You lost")
            return 0

        elif self.computer_choice == 'Scissors' and self.user_choice == 'Rock':

            print("You won!")
            return 1

        elif self.computer_choice == 'Paper' and self.user_choice == 'Rock':

            print("You lost")
            return 0

        elif self.computer_choice == 'Paper' and self.user_choice == 'Scissors':

            print("You won!")
            return 1

        elif self.computer_choice == self.user_choice:

            print("It is a tie!")      
            return 0

        else:

            print("Fail to recognize!")      
            return 0

    def get_computer_choice():

        return random.choice(['Rock', 'Paper','Scissors']) 

    def get_user_choice(self):

        self.prediction = self.get_prediction()

        if self.prediction[0][0] > 0.8:

            return 'Scissors'

        elif self.prediction[0][1] > 0.8:

            return 'Paper'

        elif self.prediction[0][2] > 0.8:

            return 'Rock'

    def get_prediction(self):

        t1  = time.time()
        i   = 1

        while True:

            t2 = time.time()

            ret, frame = self.cap.read()

            cv2.putText(frame,str(round(t2-t1)),(50,50),self.font, 1, (200,255,155), 2, cv2.LINE_AA)
            cv2.imshow('frame', frame)
            cv2.waitKey(1)

            if round(t2 - t1) >= 3:

                resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
                image_np      = np.array(resized_frame)

                normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    
                self.data[0]    = normalized_image
                self.prediction = self.model.predict(self.data)

                return self.prediction

    def clean_up(self):

        self.cap.release()
        cv2.destroyAllWindows()

    def play(self): 

        while True:

            
            if self.user_wins == 3:

                print('User Won!')
                break

            elif self.rounds_played == 5:

                print('Game Over!')
                break

            else:

               self.user_wins += self.get_winner()
               print(self.computer_choice)
               print(self.user_choice)

            self.rounds_played += 1

        self.clean_up()

if __name__ == '__main__':
    
    game = RockPaperScissors()
    game.play()
    
