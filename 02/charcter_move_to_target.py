from pico2d import *
from random import *
from math import *

def hand_event():
    global Loop
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            Loop = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            Loop = False

def move(x1,y1,tx2,ty2):
    global x,y,dir
    global tx,ty
    if (x1 == tx2 and y1 == ty2):
        chage_target_pos()
    if(x1 < tx2):
        x += 1
        dir = 1
    if (x1 > tx2):
        x -= 1
        dir = 0
    if (y1 < ty2):
        y += 1
    if (y1 > ty2):
        y -= 1


def chage_target_pos():
    global tx,ty
    tx, ty = randrange(0, 800), randrange(0, 600)

open_canvas(800,600)

target = load_image('hand_arrow.png')
character = load_image('animation_sheet.png')

Loop = True
x,y,frame,dir = 0,0,0,1
tx,ty = randrange(0,800),randrange(0,600)
while(Loop):
    clear_canvas()
    character.clip_draw(frame*100,100 * dir,100,100,x,y)
    target.draw(tx,ty)
    move(x,y,tx,ty)

    update_canvas()

    hand_event()
    frame = (frame + 1) % 8
    delay(0.01)

close_canvas()