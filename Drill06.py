import random
import math
import sys
from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1024, 840
open_canvas(TUK_WIDTH, TUK_HEIGHT)

tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

# 초기 위치 설정
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
handX, handY = x, y
def handle_events():
    global running, handX, handY
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            handX, handY = event.x, TUK_HEIGHT - event.y

def rand_mouse():
    pass

running = True
frame = 0

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    hand.draw(handX, handY)

    if handX - x >= 0:
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
    else:
        character.clip_composite_draw(frame * 100, 100, 100, 100, 0, 'h', x, y, 100, 100)

    move_x = (handX - x) / 30.0
    move_y = (handY - y) / 30.0
    x += move_x
    y += move_y

    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    delay(0.05)

close_canvas()
sys.exit()
