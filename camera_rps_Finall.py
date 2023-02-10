import cv2
from   keras.models import load_model
import numpy as np
import time
import random
import msvcrt as m
class RockPaperScissors:

    def __init__(self):

        ## internal game variables

        self.user_wins       = 0
        self.rounds_played   = 0
        self.computer_choice = ["None"]
        self.user_choice     = ["None"]

        ## Model Upload

        self.model = load_model('keras_model.h5')

        ## Video Capture and Data Storage variable
        
        self.prediction = [np.array([1,1,1])]
        self.data       = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        self.cap        = cv2.VideoCapture(0)
        ret, frame      = self.cap.read()
        self.frame      = frame
        self.clean_frame= frame
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
        else:

            return 'None'

    def get_prediction(self):

        # Frame resizing to be comparable with the model ones
        resized_frame    = cv2.resize(self.clean_frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np         = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        self.data[0]     = normalized_image
        self.prediction  = self.model.predict(self.data)

        return self.prediction

    def clean_up(self):

        self.cap.release()
        cv2.destroyAllWindows()

    def show_hud(self,time_dif):

        cv2.putText(self.frame,'Coundown: '+str(round(time_dif)),(50,50),self.font, 1, (200,255,155), 2, cv2.LINE_AA)
        cv2.putText(self.frame,'Round: '+str((self.rounds_played+1)),(50,100),self.font, 1, (200,255,155), 2, cv2.LINE_AA)
        cv2.putText(self.frame,'User won: '+str((self.user_wins)),(50,150),self.font, 1, (200,255,155), 2, cv2.LINE_AA)

    def show_round_results_info(self):

        cv2.putText(self.frame,'Computer: '+self.computer_choice,(300,50),self.font, 1, (200,255,155), 2, cv2.LINE_AA)
        cv2.putText(self.frame,'User: '+self.user_choice,(300,100),self.font, 1, (200,255,155), 2, cv2.LINE_AA)
        cv2.putText(self.frame,'Press "c" to continue',(150,400),self.font, 1, (200,255,155), 2, cv2.LINE_AA)
        cv2.imshow('frame', self.frame)

        while True:
            if cv2.waitKey(0) & 0xFF == ord('c'):
                break
 
    def show_game_over(self):

        cv2.putText(self.frame,'Game Over',(225,300),self.font, 1, (200,255,155), 2, cv2.LINE_AA)
        cv2.putText(self.frame,'To exit press "q"',(160,400),self.font, 1, (200,255,155), 2, cv2.LINE_AA)
        cv2.imshow('frame', self.frame)

        while True:
            if cv2.waitKey(0) & 0xFF == ord('q'):
                break

    def play(self): 

        t1  = time.time()
        i   = 1

        while True:

            t2 = time.time()
            ret, self.clean_frame = self.cap.read()
            self.frame = self.clean_frame

            self.show_hud(t2-t1)

            if (t2 - t1) >= 3.5:

                self.user_wins += self.get_winner()
                self.rounds_played += 1
                self.show_round_results_info()
                t1  = time.time()

            elif self.rounds_played == 5 or self.user_wins == 3:
                self.show_game_over()
                break

            cv2.imshow('frame', self.frame)
            cv2.waitKey(1)  
                      
        self.clean_up()

if __name__ == '__main__':
    
    game = RockPaperScissors()
    game.play()
    
