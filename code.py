#  CircuitPython v. 3 code for Circuit Playground Express.
#  It cycles through some spooky lights, and will ghoulishly
#  laugh at anyone foolish enough to touch it. That is, 
#  provided you've used a wire (alligator clips work well) to
#  go from pin A1 on the CPX with the other end embedded deep
#  in the pumpkin's flesh.
#  Sound file "deep_evil_laugh.wav" is also in this repo.

import time
from adafruit_circuitplayground.express import cpx
cpx.adjust_touch_threshold(200)
 
def detectTouch():
    if cpx.touch_A1:
        print("Touched A1!")
        cpx.play_file("deep_evil_laugh.wav")
 
def yellowToOrange():
    red = 95
    green = 150
    cpx.pixels.fill((0, 0, 0))
    cpx.pixels.brightness = 1.0
    for x in range(100, 256, 5):
        red += 5
        cpx.pixels.fill((red, 150, 0))
        print(red, 150, 0)
        detectTouch()
    for x in range(155, 0, -5):
        green -= 5
        cpx.pixels.fill((red, x, 0))
        print(red, green, 0)
        detectTouch()
    # red = 255
    # green = 0
    print(red, green)
    for x in range(50, 100, 5):
        red -= 5
        green += 5
        cpx.pixels.fill((red, green, 0))
        print(red, green, 0)
        detectTouch()
 
def pulseOrange():
    cpx.pixels.brightness = 0
    cpx.pixels.fill((255, 50, 0))
    for x in range(0, 101):
        cpx.pixels.brightness = x / 100
        detectTouch()
    for x in range(100, -1, -1):
        cpx.pixels.brightness = x / 100
        detectTouch()
 
while True:
    yellowToOrange()
    pulseOrange()
    time.sleep(0.1)
