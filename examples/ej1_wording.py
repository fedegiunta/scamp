# From: https://www.youtube.com/watch?v=9Lk4gBBWMqw
# Title: Text to MUSIC!?!? (Python Music Short #1)

from scamp import *

s = Session()

piano = s.new_part("piano")

text = "hola soy fede giunta"

for char in text:
    if char == " ":
        wait(0.2)
    elif char.isalnum():
        piano.play_note(ord(char) - 20, 0.5, 0.06)
    else:
        wait(0.2)
        piano.play_note(ord(char), 0.8, 0.06)
        wait(0.2)
