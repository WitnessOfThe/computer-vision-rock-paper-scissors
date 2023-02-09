# Computer Vision RPS

# Milestone 2

While completing the task in Milestone 2, we trained a model to separate four different objects from the images received from the webcam. Now the model can distinguish hand shown Rock, Paper, scissors and nothing (just the face of the user). Then we uploaded this model using "Kerras" and "TensorFlow". Finally, we placed the model file into the main git repo.  For this model to perform better, there is a need to train the model with more people. Now we need to be able to work with this model in code.

# Milestone 4

In order to create a virtual environment for our simulations, we use miniconda. For the current project, we created a different environment and installed additional packages that allow us to manipulate web cameras and read trained models. The list of all necessary packages to run this project is saved in requirements.txt.

In the "manual_rps.py", we implemented the manual "Rock, Paper, Scissors" game. The game is constructed by using three separate functions. The first function is to determine what the is user's choice in the current scenario using While True statements were prohibited. Also, it is assumed that the user is cooperating. The second function picks the random item over the "Rock, Paper, Scissors" set. Finally, the third function is designed to compare the human and computer guesses and choose a winner. When a user wins, we print, "You win! And when the computer wins ""You lost". In the case, when user and computer provide the same answer we print "It's a tie!". The judging is implemented by using if-elif-else statements.