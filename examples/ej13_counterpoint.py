# From: https://www.youtube.com/watch?v=TYNaA97HkeY
# Title: Algorithmic Counterpoint! (Python Music Short #13)

from scamp import *

playback_settings.recording_file_path = "counterpoint.wav"
s = Session()

voice = s.new_part("choir aah")
s.start_transcribing()

def is_consonant(p1, p2):
    if abs(p1 - p2) % 12 in [0, 3, 4, 7, 8, 9]:
        return True
    else:
        return False

cantus_firmus = [60, 63, 62, 67, 65, 64, 67, 69]
counterpoint = [76]

i = 0

while i < len(cantus_firmus):
    # play the current chord
    voice.play_chord([cantus_firmus[i], counterpoint[i]], 1.0, 1.0)
    if i + 1 >= len(cantus_firmus):
        # last note; no need to figure out the next counterpoint note
        break
    # otherwise, figure out the next counterpoint note
    for motion_option in [1, 2, -1, -2, 3, -3, 4, -4]:
        if cantus_firmus[i + 1] > cantus_firmus[i]:
            # cantus firmus is going up, so prioritize going down
            motion_option *= -1
        if is_consonant(cantus_firmus[i + 1], counterpoint[i] + motion_option):
            counterpoint.append(counterpoint[i] + motion_option)
            break
    else:
        raise RuntimeError("Could not find acceptable motion!")
    i += 1

print(f"Cantus firmus: {cantus_firmus}")
print(f"Counterpoint: {counterpoint}")
s.stop_transcribing().to_score().show()
