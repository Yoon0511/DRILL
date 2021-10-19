from pico2d import *
import  random

# Game object class here
class Ball:
    def __init__(self):
        self.type = random.randint(0,1)
        self.x,self.y = random.randint(100,700),599
        self.smallball = load_image('ball21x21.png')
        self.bigball = load_image('ball41x41.png')
        self.downspeed = random.randint(5,20)
        self.down = True

    def update(self):
        if self.down == True:
            self.y -= self.downspeed
            if self.type == 1:
                if self.y <= 75:
                    self.y = 75
                    self.down = False
            if self.type == 0:
                if self.y <= 65:
                    self.y = 65
                    self.down = False

    def draw(self):
        if self.type == 0:
            self.smallball.draw(self.x,self.y)
        elif self.type == 1:
            self.bigball.draw(self.x, self.y)

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400,30)

class Boy:
    def __init__(self):
        self.image = load_image('run_animation.png')
        self.x,self.y = random.randint(100,700),90
        self.frame = random.randint(0,7)

    def update(self):
        self.x += 5
        self.frame = (self.frame + 1) % 8

    def draw(self):
        self.image.clip_draw(self.frame * 100,0,100,100,self.x,self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
open_canvas(800,600)
grass = Grass()
#boy = Boy()
team = [Boy() for i in range(11)]
balls = [Ball() for i in range(20)]
running = True
# game main loop code
while running:
    handle_events()

    #update
    for boy in team:
        boy.update()
    for ball in balls:
        ball.update()
    #draw
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    for ball in balls:
        ball.draw()
    update_canvas()
    delay(0.05)
# finalization code