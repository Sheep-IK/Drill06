from pico2d import *


TUK_WIDTH, TUK_HEIGHT = 1024, 840
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
mouse = load_image('hand_arrow.png')


def handle_events():
    global running
    global mouseX, mouseY, goalX, goalY
    global ck
    ck = False
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            goalX, goalY = event.x, TUK_HEIGHT - 1 - event.y
            ck = True


running = True
frame = 0
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
mouseX, mouseY = x, y
ck = False
goalX, goalY = x,y


while running:
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    handle_events()
    if ck:
        mouse.clip_draw(0, 0, 50, 52, goalX, goalY)

    if ck and (goalX + 5 < x or goalX - 5 > x or goalY + 5 < y or goalY - 5 > y):
        if goalX - x >= 0:
            character.clip_draw(frame * 100, 100, 100, 100, x, y)
        elif goalX - x < 0:
            character.clip_composite_draw(frame * 100, 100, 100, 100, 0, 'h', x, y, 100, 100)
        x += (goalX - x) / 60.0
        y += (goalX - y) / 60.0


    update_canvas()
    frame = (frame + 1) % 8
    delay(0.05)

close_canvas()




