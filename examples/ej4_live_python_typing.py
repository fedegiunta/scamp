# From: https://www.youtube.com/watch?v=1Y9MxI-azWQ
# Title: Live music typing! (Python Music Short #4)

from scamp import *

s = Session()

piano = s.new_part("piano")


def keyboard_listener(key, code):
    if len(key) == 1: 
        if key.isalnum():
            piano.play_note(ord(key) - 20, 0.5, 0.06, blocking=False)
        else:
            piano.play_note(ord(key), 1.0, 0.06, blocking=False)


s.register_keyboard_listener(keyboard_listener)
s.wait_forever()
