# From: https://www.youtube.com/watch?v=nzhBtG_cLfw
# Title: My Octatonic Musical Mouse! (Python Music Short #9)

from scamp import *
from scamp_extensions.pitch import Scale

s = Session()

# last_position = (0, 0)

# def mouse_move_listener(x, y):
#     global last_position
#     dx, dy = x - last_position[0], y - last_position[1]
#     last_position = (x, y)
#     print(dx, dy)

scale = Scale.pentatonic(60)
bassoon = s.new_part("bassoon")

countdown = 0.1
last_position = (0, 0)

def get_note_pitch(lower_note_pitch, top_note_pitch, percent):
    return lower_note_pitch + top_note_pitch * percent

def mouse_move_listener(x, y):
    global countdown, last_position
    dx, dy = x - last_position[0], y - last_position[1]
    last_position = (x, y)
    countdown -= (dx ** 2 + dy ** 2) ** 0.5  # Pythagoras and "** 0.5" it's the same as ** 1/2 (inverse square root)
    if countdown < 0:
        note_pitch = get_note_pitch(lower_note_pitch=34, top_note_pitch=40, percent=(1 - y))
        bassoon.play_note(scale.round(note_pitch), x, 0.1, blocking=False)
        countdown = 0.1


s.register_mouse_listener(on_move=mouse_move_listener, relative_coordinates=True)
s.wait_forever()