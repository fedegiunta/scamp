# FROM: https://www.youtube.com/watch?v=Dwa_RDl-Sro
# Title: Musical Nested For Loops!! (Python Music Short #3)

from scamp import *
from scamp_extensions.pitch import Scale

s = Session()
s.tempo = 120
violin = s.new_part("violin")

d_minor = Scale.natural_minor(62)

while True:
    for n in range(3):
        for m in range(3):
            for l in range(3):
                for k in range(3):
                    violin.play_note(d_minor[k + l + m + n], 0.8, 0.25)