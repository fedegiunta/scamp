# From: https://www.youtube.com/watch?v=asDucFElSno
# Title: Shaping algorithmic music over time! (Python Music Short #11) 

from scamp import *
from scamp_extensions.utilities import TimeVaryingParameter
import random


def build_chord(interval_options,
                num_notes,
                pitch_center,
                round_transposition=True):
    
    chord = [0]
    while len(chord) < num_notes:
        chord.append(chord[-1] + random.choice(interval_options))
    
    transposition = pitch_center - sum(chord) / len(chord)
    if round_transposition:
        transposition = round(transposition)
    return [p + transposition for p in chord]


s = Session()

organ = s.new_part("church organ")

#                                      first value  
#                                       |  next values
#                                       v  v                  repetitions in beats
num_notes = TimeVaryingParameter(      [4,    1,    1,   10], [30, 30, 40])
pitch_center = TimeVaryingParameter(   [60,   90,   40],      [50, 50])
note_length = TimeVaryingParameter(    [0.25, 0.05, 2],       [70, 30] )
staccato_chance = TimeVaryingParameter([1,    0.5,  1,   0],  [30, 30, 40])

while s.beat() < 100:
    organ.play_chord(
        build_chord([2, 5, 10], num_notes(), pitch_center() + random.randint(-4, 4)),
        0.8,
        note_length(),
        "staccato" if random.random() < staccato_chance() else None
    )