import turtle
import sys
import multiprocessing
from multiprocessing import Process, Pipe
import asyncio

from frontend import Game
from frontend import front_end
from frontend import send_game_status
from frontend import parent1
from frontend import parent2
from frontend import child1
from frontend import child2






def main():
    my_game = Game()
    winner="./Graphics/win.gif"
    loser= "./Graphics/lose.gif"
    no_Img= "0"
    
    multiprocessing.set_start_method('spawn')
    left_player = Process(target=front_end, args=(child1, ['w', 's']))
    right_player = Process(target=front_end, args=(child2, ['Up', 'Down']))
    left_player.start()
    right_player.start()

    while True:
        if parent1.poll():
            is_up = parent1.recv()
            press = 'w' if is_up else 's'
            my_game.paddle_move(press)
        if parent2.poll():
            is_up = parent2.recv()
            press = 'Up' if is_up else 'Down'
            my_game.paddle_move(press)
        my_game.ball_move()
       
        if(my_game.winner!=0):
            if(my_game.winner==1):
                    send_game_status(my_game.ball_x, my_game.ball_y,
                                     my_game.left_paddle_x, my_game.left_paddle_y,
                                     my_game.right_paddle_x, my_game.right_paddle_y,
                                     my_game.left_score, my_game.right_score, winner, loser)
            elif(my_game.winner==2):
                    send_game_status(my_game.ball_x, my_game.ball_y,
                                     my_game.left_paddle_x, my_game.left_paddle_y,
                                     my_game.right_paddle_x, my_game.right_paddle_y,
                                     my_game.left_score, my_game.right_score, loser, winner)
           
        send_game_status(my_game.ball_x, my_game.ball_y,
                                 my_game.left_paddle_x, my_game.left_paddle_y,
                                 my_game.right_paddle_x, my_game.right_paddle_y,
                                 my_game.left_score, my_game.right_score, no_Img, no_Img)



if __name__ == '__main__':
    sys.exit(main())