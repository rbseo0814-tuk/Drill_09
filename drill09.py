from pico2d import *

WIDTH, HEIGHT = 1280, 1024


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False


open_canvas(WIDTH, HEIGHT)

running = True

while running:
    clear_canvas()
    update_canvas()
    handle_events()
    delay(0.05)

close_canvas()
