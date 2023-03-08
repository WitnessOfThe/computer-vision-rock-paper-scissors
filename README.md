
# Computer Vision Rock-Paper-Scissors (RPS) 

Educational project.  Here we utilise trained a computer vision model using [Teachable-Machine](https://teachablemachine.withgoogle.com/). The model detects whether the user shows Rock, Paper, or Scissors to the camera, so the user can leverage that output to play an RPS game with the computer. We access model through TenserFlow API

## Milestone 2

While completing the task in Milestone 2, we trained a model to separate four different objects from the images received from the webcam. Now the model can distinguish hand shown Rock, Paper, scissors and nothing (just the face of the user). Then we uploaded this model using "Kerras" and "TensorFlow". Finally, we placed the model file into the main git repo.  For this model to perform better, there is a need to train the model with more people. Now we need to be able to work with this model in code.

## Milestone 4

In order to create a virtual environment for our simulations, we use miniconda. For the current project, we created a different environment and installed additional packages that allow us to manipulate web cameras and read trained models. The list of all necessary packages to run this project is saved in requirements.txt.

In the "manual_rps.py", we implemented the manual "Rock, Paper, Scissors" game. The game is constructed by using three separate functions. The first function is to determine what the is user's choice in the current scenario using While True statements were prohibited. Also, it is assumed that the user is cooperating. The second function picks the random item over the "Rock, Paper, Scissors" set. Finally, the third function is designed to compare the human and computer guesses and choose a winner. When a user wins, we print, "You win! And when the computer wins ""You lost". In the case, when user and computer provide the same answer we print "It's a tie!". The judging is implemented by using if-elif-else statements.

## Milestone 5

The final version of the program ("camera_rps_Finall.py") implements the classic "Rock, Paper, Scissors" game of the user vs computer. The user's choice is taken from the webcam image and classified using a trained beforehand model. The game is implemented by using the class "RockPaperScissors". To handle a camera and communicate with the user, we used the "cv2" package. Here, we construct our program in a way, that allows a user to see his image in real-time and be able to know if the mode reconstructed his gest in the right way.

![f_1](https://user-images.githubusercontent.com/33790455/218197101-1c437d0b-096c-4dc9-aab4-20f9317a9958.PNG)
![f_2](https://user-images.githubusercontent.com/33790455/218197120-798d905e-4adf-4317-960b-5e8106a839cf.PNG)
![f_3](https://user-images.githubusercontent.com/33790455/218197125-19f7856e-4f0a-41c1-a6dd-eb73641c91d3.PNG)


