import game_framework
from pico2d import *
import game_world
import random

PIXEL_PER_METER = (10.0 / 0.3)
FLY_SPEED_KMPH = 20.0
FLY_SPEED_MPM = (FLY_SPEED_KMPH * 1000.0 / 60.0)
FLY_SPEED_MPS = (FLY_SPEED_MPM / 60.0)
FLY_SPEED_PPS = (FLY_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14

# 새는 10픽셀당 30cm 기준으로 20km의 속도로 비행한다.
# 새의 크기는 100x100을 10픽셀당 30cm의 크기를 기준으로 계산한다. 새의 크기 3M x 3M = 9m^2

class Bird:
    def __init__(self):
        self.x, self.y = random.randint(200,1000),random.randint(200,400)
        # Boy is only once created, so instance image loading is fine
        self.image = load_image('bird100x100x14.png')
        self.dir = 1
        self.velocity = 0
        self.frame = 0

    def get_bb(self):
        return self.x - 50,self.y - 50,self.x + 50,self.y + 50

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        self.x += self.dir * FLY_SPEED_PPS * game_framework.frame_time

        if ((self.x + 50) >= 1600):
            self.dir = -1
        elif ((self.x - 50 <= 0)):
            self.dir = 1


    def draw(self):
        if self.dir == 1:
            self.image.clip_composite_draw(int(self.frame) * 100, 0, 100, 100, 0, '', self.x,self.y - 25,100, 100)
        elif self.dir == -1:
            self.image.clip_composite_draw(int(self.frame) * 100, 0, 100, 100, 0, 'h', self.x, self.y - 25,100, 100)
       #self.image.clip_draw(int(self.frame) * 100, 0, 100, 100, self.x, self.y)
        #draw_rectangle(*self.get_bb())


    def handle_event(self, event):
        pass