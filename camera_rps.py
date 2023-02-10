import cv2
from keras.models import load_model
import numpy as np
import time

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
            return prediction

        elif round(t2-t1) == i:

            i  += 1
            print(round(t2-t1))

if __name__ == '__main__':
    
    print(get_prediction())
