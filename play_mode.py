from pico2d import *
import game_world
import game_framework
from boy import Boy
from grass import Grass
from ball import Ball
from zombie import Zombie
import random

boy = None
zombie = None

def handle_events():


    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)


def init():
    global boy
    global balls
    global grass
    global zombie
    zombie = [Zombie() for i in range(5)]
    for z in zombie:
        game_world.add_oject(z)

    boy = Boy()
    game_world.add_oject(boy)

    grass = Grass()
    game_world.add_oject(grass, 0)

    balls = [Ball(random.randint(100, 1700), 60 ,0) for i in range(30)]
    game_world.add_objects(balls, 1)

    #소년과 볼 사이 충돌 페어 등록
    game_world.add_collision_pair('boy:ball', boy, None)
    game_world.add_collision_pair('boy:zombie', boy, None)
    for ball in balls:
        game_world.add_collision_pair('boy:ball', None, ball)
    for z in zombie:
        game_world.add_collision_pair('boy:zombie', None, z)

def pause():
    boy.pause()


def resume():
    pass


def finish():
    global boy
    game_world.clear()
    boy = None


def update():
    game_world.update()
    game_world.handle_collisions()
    #볼 소년 충돌처리
    #for ball in balls[:]: #balls[:] - balls 리스트를 복사하여,
        #반복 중에 원본 리스트에서 요소를 제거해도 안전하게 반복 가능
        #if game_world.collide(boy, ball):
        #    print('소년 - 볼 충돌')
        #    boy.ball_count += 1
        #    game_world.remove_object(ball) #월드의 list에서는 삭제하지만, 
         #   #balls의 오브젝트 ball는 삭제하지 않음
         #   balls.remove(ball) #balls의 list에서도 삭제, 그러나 반복문이 balls면 null 참조로 위험하므로, 반복문은 balls[:]로 복사한 리스트에서 반복하도록 함
        #elif game_world.collide(ball, grass):
       #     print('잔디 - 볼 충돌')
        #    ball.stopped = True #바닥에 놓인 공으로 처리
def render():
    clear_canvas()
    game_world.render()
    update_canvas()









