from pico2d import *

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
        self.ruler_image = load_image('ruler.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(400, 30)
        self.image.draw(1200, 30)
        self.ruler_image.draw(800, 350)
    def get_bb(self): #잔디의 충돌 영역을 계산하여 bb 좌표 리턴
        return 0, 0, 1600, 50


