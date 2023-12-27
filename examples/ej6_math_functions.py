# From: https://www.youtube.com/watch?v=fB4qTzUjLaQ
# Title: Turning mathematical functions into music! (Python Music #6)

from scamp import *
from scamp_extensions.pitch import Scale
import math

s = Session()

melodic_minor = Scale.melodic_minor(62)

strings = s.new_part("strings")

while True:
    # raw_pitch = 80 + 10 * math.sin(s.beat())
    # raw_pitch = 80 + 10 * math.sin(s.beat() * 3) + 8 * math.sin(s.beat() * 5)
    # raw_pitch = 80 + math.tan(s.beat())
    raw_pitch = 80 + 10 * math.sin(100 / (0.1 + s.beat()))
    strings.play_note(melodic_minor.round(raw_pitch), 0.8, 0.05, "staccato")
