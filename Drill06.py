import random
from pico2d import *


TUK_WIDTH, TUK_HEIGHT = 1024, 840
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
mouse = load_image('hand_arrow.png')

def handle_events():
    global running
    global mouseX
    global mouseY
    mouseX = TUK_WIDTH // 2
    mouseY = TUK_HEIGHT //2
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN:
            mouse.clip_draw(0, 0, 50, 52, x, y)


running = True
frame = 0
x, y = TUK_WIDTH // 2, TUK_HEIGHT //2
hide_cursor()



while running:
    copyX = x
    copyY = y
    while mouseX+5 < x or mouseX-5 > x or mouseY+5 < y or mouseY-5 > y:
        tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
        handle_events()
        if mouseX-copyX >= 0:
            character.clip_draw(frame * 100, 100, 100, 100, x, y)
        elif mouseX-copyY < 0:
            character.clip_composite_draw(frame * 100, 100, 100, 100, 0, 'h', x, y, 100, 100)
        x += (mouseX-copyX) / 60.0
        y += (mouseY-copyY) / 60.0
        update_canvas()
        handle_events()
        frame = (frame + 1) % 8
        delay(0.05)
        clear_canvas()

close_canvas()




