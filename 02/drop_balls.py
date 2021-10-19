from pico2d import *

def handle_event():
    global Loop
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            Loop = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            Loop = False

open_canvas()
Loop = True
while Loop:
    clear_canvas()
    handle_event()
    update_canvas()
close_canvas()