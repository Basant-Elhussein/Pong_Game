import turtle
import sys
import multiprocessing
from multiprocessing import Process, Pipe
import asyncio

class Game:
    def __init__(self):
        self.ball_x = 0
        self.ball_y = 0
        self.ball_dx = 1
        self.ball_dy = -1
        self.left_paddle_x = -275
        self.left_paddle_y = 0
        self.right_paddle_x = 270
        self.right_paddle_y = 0
        self.left_score = 0
        self.right_score = 0
        self.winner = 0

    def paddle_move(self, press):
        if press == 'Up':
            self.right_paddle_y = min(240, self.right_paddle_y + 20)
        elif press == 'Down':
            self.right_paddle_y = max(-240, self.right_paddle_y - 20)
        elif press == 'w':
            self.left_paddle_y = min(240, self.left_paddle_y + 20)
        elif press == 's':
            self.left_paddle_y = max(-240, self.left_paddle_y - 20)

    def ball_move(self):

        #Inside the boundries
        self.ball_x += self.ball_dx
        self.ball_y+=self.ball_dy

        #Edges
        if(self.ball_y>290):
            self.ball_y=290
            self.ball_dy*=-1
        if(self.ball_y<-290):
            self.ball_y=-290
            self.ball_dy*=-1

        #Collision with the Paddle
        #Right Paddle
        if( self.ball_x > 250
           and self.ball_x < 260
           and self.ball_y < self.right_paddle_y + 80
           and self.ball_y > self.right_paddle_y - 80
        ):
            self.ball_x = 250
            self.ball_dx *=-1
       
        #Left Paddle
        if( self.ball_x < -250
           and self.ball_x > -260
           and self.ball_y < self.left_paddle_y + 80
           and self.ball_y > self.left_paddle_y - 80
        ):
            self.ball_x = -250
            self.ball_dx *=-1
       
        #Score Update
        if self.ball_x>=290:
            self.left_score+=1
            self.ball_x=0
            self.ball_y=0
            self.ball_dx = -1
       
        if self.ball_x<=-290:
            self.right_score+=1
            self.ball_x=0
            self.ball_y=0
            self.ball_dx = 1
       
        if self.left_score==4:
            self.winner = 1
       
        elif self.right_score==4:
            self.winner = 2
           

