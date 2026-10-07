from pico2d import *

WIDTH, HEIGHT = 1280, 1024


def handle_events():
    global running, dir_x
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_RIGHT:
                dir_x += 1
            elif event.key == SDLK_LEFT:
                dir_x -= 1
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
            elif event.key == SDLK_LEFT:
                dir_x += 1


open_canvas(WIDTH, HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x, y = WIDTH // 2, HEIGHT // 2
frame = 0
dir_x = 0
face_dir = 1

while running:
    clear_canvas()
    tuk_ground.draw(WIDTH // 2, HEIGHT // 2)
    if dir_x != 0:
        action = 1 if face_dir == 1 else 0
    else:
        action = 3 if face_dir == 1 else 2
    character.clip_draw(frame * 100, action * 100, 100, 100, x, y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    if dir_x > 0:
        face_dir = 1
    elif dir_x < 0:
        face_dir = -1
    x += dir_x * 5
    delay(0.07)

close_canvas()
