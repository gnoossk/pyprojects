from tkinter import *
from ball import *
import time



window = Tk()

WIDTH = 500
HEIGHT = 500

canvas = Canvas(window, width = WIDTH, height = 500)
canvas.pack()

volley_ball = Ball(canvas,0,0,100,5,5,'white')
tennis_ball = Ball(canvas,0,0,50,8,4,'yellow')
my_ball = Ball(canvas,1,0,125,11,10,'red')
while True:
   volley_ball.move()
   tennis_ball.move()
   my_ball.move()
   window.update()
   time.sleep(0.01)


window.mainloop()




