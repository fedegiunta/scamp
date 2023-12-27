# From: https://www.youtube.com/watch?v=RllMODKTA1I
# Title: Building Chords in Python! (Python Music Short #10)

from scamp import *
import random


def build_chord(interval_options,
                num_notes,
                pitch_center,
                round_transposition=True):
    # The chord its formed by incrementing intervals
    chord = [0]
    while len(chord) < num_notes:
        chord.append(chord[-1] + random.choice(interval_options))
    
    chord_center = sum(chord) / len(chord)
    transposition = pitch_center - chord_center
    if round_transposition:
        transposition = round(transposition)
        
    transposed_chord = [p + transposition for p in chord]
    print(f"* center: {pitch_center} - chord: {chord} - transposed chord: {transposed_chord}\n")
    return transposed_chord


s = Session()

organ = s.new_part("church organ")


while True:
    organ.play_chord(
        pitches=build_chord([3, 4, 5, 7], random.randint(3, 5), random.randint(40, 80)),
        volume=0.8,
        length=0.5,  # 1/2 notes
    )
    