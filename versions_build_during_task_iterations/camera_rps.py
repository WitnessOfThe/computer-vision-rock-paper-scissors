import cv2
from keras.models import load_model
import numpy as np
import time
import random
    
def get_winner(computer_choice,user_choice):
#    print(computer_choice)
    if computer_choice == 'Rock' and user_choice == 'Scissors':

        print("You lost")
        return 0

    elif computer_choice == 'Rock' and user_choice == 'Paper':

        print("You won!")
        return 1

    elif computer_choice == 'Scissors' and user_choice == 'Paper':

        print("You lost")
        return 0

    elif computer_choice == 'Scissors' and user_choice == 'Rock':

        print("You won!")
        return 1

    elif computer_choice == 'Paper' and user_choice == 'Rock':

        print("You lost")
        return 0

    elif computer_choice == 'Paper' and user_choice == 'Scissors':

        print("You won!")
        return 1

    elif computer_choice == user_choice:

        print("It is a tie!")      
        return 0

def get_prediction():

    t1  = time.time()
    i   = 1
    while True:

        t2 = time.time()

        if round(t2 - t1) > 3:

            model = load_model('keras_model.h5')
            cap = cv2.VideoCapture(0)
            data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data)
            cv2.imshow('frame', frame)
            cap.release()
            cv2.destroyAllWindows() 
            return list(prediction)

        elif round(t2-t1) == i:

            i  += 1
            print(round(t2-t1))

def get_computer_choice():

    return random.choice(['Rock', 'Paper','Scissors']) 

def get_user_choice():

    prediction = get_prediction()
    print(prediction)

    if prediction[0][0] > 0.8:

        return 'Scissors'

    elif prediction[0][1] > 0.8:

        return 'Paper'

    elif prediction[0][2] > 0.8:

        return 'Rock'

def play(): 

    user_wins      = 0
    rounds_played  = 0

    while True:

        
        if user_wins == 3:

            print('User Won!')
            break

        elif rounds_played == 5:

            print('Game Over!')
            break

        else:

            user_wins += get_winner(get_computer_choice(),get_user_choice())

        rounds_played += 1


                

if __name__ == '__main__':
    
    play()
