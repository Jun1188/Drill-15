from tokenize import group


world = [[], [], []]  # 0: 배경, 1: 오브젝트, 2: UI
collision_pairs = {} #딕셔너리 전역 선언


def add_oject(o, depth=1):
    world[depth].append(o)

def add_objects(ol, depth=1):
    world[depth] += ol

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o) #월드에서는 삭제하지만, 오브젝트는 삭제하지 않음
            return

def update():
    for layer in world:
        for o in layer[:]:
            o.update()

def render():
    for layer in world:
        for o in layer[:]:
            o.draw()
def add_collision_pair(group, a, b):
    if group not in collision_pairs:
        print(f'Added new group {group}')
        collision_pairs[group] = [ [], [] ] #전역 딕셔너리 a, b 리스트로 초기화
     #전역 딕셔너리 등록
    if a:
        collision_pairs[group][0].append(a)
    if b:
        collision_pairs[group][1].append(b)



def collide(a, b):# a b 충돌 검사
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def handle_collisions():
    for group, pairs in collision_pairs.items():
        for a in pairs[0]:
            for b in pairs[1]:
                if collide(a, b):
                    a.handle_collision(group, b)#충돌 객체에 충돌 처리 위임
                    b.handle_collision(group, a)#마찬가지

def remove_collision_object(o):
    for pairs in collision_pairs.values(): #모든 리스트(충돌 페어)에 대해 충돌된 페어는 삭제
        if o in pairs[0]:
            pairs[0].remove(o)
        if o in pairs[1]:
            pairs[1].remove(o)  

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            remove_collision_object(o)
            return        


def clear():
    for layer in world:
        layer.clear()
