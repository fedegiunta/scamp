# From: https://www.youtube.com/watch?v=xk91z22Bnag
# Title: Bouncing Ball Physics Music?!?!? (Python Music Short #5)

from scamp import *

s = Session()

piano = s.new_part("piano")

pitch = 80
pitch_velocity = 0
pitch_acceleration = -98

while True:
    piano.play_note(pitch, 0.7, 0.05)
    pitch_velocity += pitch_acceleration * 0.05
    pitch += pitch_velocity * 0.05
    if pitch < 25:
        pitch_velocity *= -1
        