from pico2d import *
import math

speed = 10
chmove = True
check = 0
def move(dir,x,y,chmove,check):
    if dir == 0:
        x = x+speed
        if check == 1 and x >= 400:
            check = 0
            chmove = False
            return chmove, dir, x, y, check
        if x >= 780 :
            dir = 1
    elif dir == 1:
        y = y+speed
        if y >= 560 :
            dir = 2
    elif dir == 2:
        x = x-speed
        if x <= 10 :
            x = 10
            dir = 3
    elif dir == 3:
        y = y-speed
        if y <= 90 :
            y = 90
            dir = 0
            check = 1

    return chmove,dir,x,y,check

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

Loop = True
x = 400
y = 90
dir = 0
t = 17

while (Loop):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    if chmove == True :
        chmove,dir,x,y,check = move(dir,x,y,chmove,check)
    if chmove == False:
        x = 400 + 210 * math.cos(t)
        y = 300 + 210 * math.sin(t)
        t = t + 0.1
        if t >= float(24) :
           x,y,t,dir,chmove,check = 400,90,17,0,True,0


    delay(0.01)

close_canvas()
