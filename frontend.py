import turtle
import sys
import multiprocessing
from multiprocessing import Process, Pipe
import asyncio

from backend import Game

           
class Ball:

    def __init__(self):
        self.Ball= turtle.Turtle()
        self.Ball.speed(0)
        self.Ball.shape("./Graphics/ball2.gif")
        self.Ball.penup()
        self.Ball.goto(0,0)

    def update(self, x,y):
        self.Ball.setx(x)
        self.Ball.sety(y)

class Paddle:
   
    def __init__(self, pic, posx, posy, shapeWidth, shapeLength):
        self.paddle = turtle.Turtle() # Create an object
        self.paddle.speed(0)
        self.paddle.shape("square")
        self.paddle.shape(pic)
        self.paddle.shapesize(stretch_wid=shapeWidth, stretch_len=shapeLength)
        self.paddle.penup()
        self.paddle.goto(posx,posy)

    def update(self, x, y):
        self.paddle.setx(x)
        self.paddle.sety(y)
   

class Score:
    def __init__(self, dim ):
        self.leftPlayerScore=0
        self.rightPlayerScore=0
        self.scoring = turtle.Turtle()
        self.scoring.speed(0)
        self.scoring.pencolor('red')
        self.scoring.penup()
        self.scoring.hideturtle()
        self.scoring.goto(0,dim)
        self.scoring.write("Left Player: 0           Right Player: 0", align="center", font=("Arial",20,"bold"))
   
    def update(self, left, right):
        self.leftPlayerScore= left
        self.rightPlayerScore= right
        self.scoring.clear()
        self.scoring.write("Left Player: {}           Right Player: {}".format(self.leftPlayerScore,self.rightPlayerScore), align="center", font=("Arial",20,"bold"))
   
   
        
        
class control_pipe:
    def __init__(self, pipe):
        # Defining The Pipe
        self.pipe = pipe
        # Creating Window
        self.win = turtle.Screen()
        self.win.title("Pong Game")
        self.win.bgcolor("black")
        self.win.setup(width = 600, height = 600)
        self.win.tracer(0)
        self.win.bgpic('./Graphics/background.gif')
        self.win.addshape("./Graphics/paddle51.gif")
        self.win.addshape("./Graphics/paddle52.gif")
        self.win.addshape("./Graphics/ball2.gif")
        # Instantiate The Score
        self.score = Score(260)

        # Instantiate The Ball
        self.ball = Ball()

        # Instantiate Paddles
        self.left_paddle = Paddle('./Graphics/paddle52.gif', -275, 0, 8, 1)
        self.right_paddle = Paddle('./Graphics/paddle51.gif', 270, 0, 8, 1)

    def move_up(self):
        self.pipe.send(1)


    def move_down(self):
        self.pipe.send(0)

    def render(self):
        self.ball.update(self.pipe.recv(),self.pipe.recv())
        self.left_paddle.update(self.pipe.recv(), self.pipe.recv())
        self.right_paddle.update(self.pipe.recv(), self.pipe.recv())
        self.score.update(self.pipe.recv(), self.pipe.recv())
        pic1 = self.pipe.recv()
        if(pic1!="0"):
            self.ball.update(0,0)
            self.win.clearscreen()
            self.win.bgpic(pic1)
            self.win.exitonclick()
        player = self.pipe.recv()

        if player == 'The Left Player' or player == 'The Right Player':
            self.win.title(player)
        
        


def front_end(pipe, keys):
   
    my_pipe = control_pipe(pipe)

    my_pipe.win.listen()
   
    # Push to pipe whenever a key pressed
    # Order of pushing: left score, right score
    my_pipe.win.onkeypress(my_pipe.move_up, keys[0])
    my_pipe.win.onkeypress(my_pipe.move_down, keys[1])

    while True:
        if pipe.poll():
            my_pipe.render()
        my_pipe.win.update()
       


parent1, child1 = Pipe()
parent2, child2 = Pipe()

def send_game_status(ball_x, ball_y, left_paddle_x, left_paddle_y,
                    right_paddle_x, right_paddle_y, left_score, right_score, pic1, pic2):
   
    #Left Player
    parent1.send(ball_x)
    parent1.send(ball_y)

    parent1.send(left_paddle_x)
    parent1.send(left_paddle_y)

    parent1.send(right_paddle_x)
    parent1.send(right_paddle_y)

    parent1.send(left_score)
    parent1.send(right_score)
   
    parent1.send(pic1)
    parent1.send('The Left Player')


    #Right Player
    parent2.send(ball_x)
    parent2.send(ball_y)

    parent2.send(left_paddle_x)
    parent2.send(left_paddle_y)

    parent2.send(right_paddle_x)
    parent2.send(right_paddle_y)

    parent2.send(left_score)
    parent2.send(right_score)

    parent2.send(pic2)

    parent2.send('The Right Player')



