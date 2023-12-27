# From: https://www.youtube.com/watch?v=_AngwYvzjkA
# Title: Random Walk Music! (Python Music Short #2)

from scamp import *
import random

s = Session()

cello = s.new_part("cello")

pitch = 55

while True:
    cello.play_note(pitch, 0.8, 0.25)
    pitch += random.choice([-1, 1])