# From: https://www.youtube.com/watch?v=IXPmVEc3AuI
# Title: Isorhythmic Music in Python! (Python Music Short #12)

from scamp import *
from itertools import cycle


# for x in [2, 7, 4]:
#     print(x)
#     wait(0.5)
# 
# for x in cycle([2, 7, 4]):
#     print(x)
#     wait(0.5)
    
# Using differnt sets with different lenghts (out of phase)    
# for x, y in zip(cycle([2, 7, 4]), cycle([30, 20, 10, 100, 200])):
#     print(x, y)
#     wait(0.5)


s = Session(tempo=90)

# oboe = s.new_part("oboe")
# 
# for pitch, dur in zip(cycle([69, 72, 71, 64, 66, None, 62]),
#                       cycle([1.0, 0.5, 0.75, 0.25, 1.0])):
#     oboe.play_note(pitch, 0.7, dur)
    


def do_isorhythm(inst, color, talea, voluminor=(1.0,)):
    for pitch, volume, dur, in zip(cycle(color), cycle(voluminor), cycle(talea)):
        inst.play_note(pitch, volume, dur)
    
    
s = Session(tempo=90)

oboe = s.new_part("oboe")
clarinet = s.new_part("clarinet")

fork(do_isorhythm, args=(oboe, [69, 72, 71, 64, 66, None, 62],
                        [1.0, 0.5, 0.75, 0.25, 1.0], [0.5, 0.7, 0.3]))
fork(do_isorhythm, args=(clarinet, [76, 78, 77, 79, None],
                        [2.0, 0.5, 1.0], [0.3, 0.5, 0.4, 0.6, 0.9, 0.6, 0.4]))
wait_forever()
