# Pong_Game
Pong Game using a multiprocessing approach that enables two players to play against each other - with each of them having his/her own window for the game on the same device.
Using an OOP design and pipe for processes communication, the game is divided into three main processes.

- First the parent process:
--> Runs the backend of the game by creating an instance of class Game. 
--> Controls the ball and the paddles’ motion and the score’s calculation.
--> Spawns two child processes.

- Second 2 child processes:
--> Considered as the frontend or drawer of the program.
--> Sending the player's moves through the pipe to the backend.
--> Recieving the game state from the backend to be shown through the graphical interface.

How to run the game:
- You need to have the final version of Python 3

- You need to install turtle library in your machine. If you use linux, you can simply put 
  the following command in the terminal for installing it: sudo apt install python3-tk

- Then, just put the command "python3 main.py"

- Finally, you are getting started to play the game with two displays:

    - The Left Player "You can see the title Left Player for simplicity" plays with "w" and "s"
    - The right Player plays with "Up" and "Down"

    - The priority comes to the one getting the highest score (4 for now: you can change it in the code)
    - After finishing the game, you will know who is the winner and who is the loser.
    - Click on the display after being showed whether you are the winner or the loser.
    - You will leave the game 
