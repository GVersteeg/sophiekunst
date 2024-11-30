import board
import digitalio
from digitalio import DigitalInOut as DIO
import time
import neopixel
import random
import pwmio

# led = digitalio.DigitalInOut(board.D13)
# pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)
# led.direction = digitalio.Direction.OUTPUT


# pixel.brightness= 0.1



def start_shutdown_timer():
    # Stop after n time
    return ''

def get_brightness(value):
    if 0 <= value <= 1:
        return value * 65536
    else:
        return 65536
def perform_story(story):
    for step in story:
        # parse storybeat
        story[0].value = get_brightness(story[1])
        # If not the last step in the story, wait before lights turn on in next step location
        if len(step)==3:
            sleeptime = step[2]
            time.sleep(sleeptime)
        # If last step in the story, leave lights on for sleepmins minutes
        else:
            sleepmins = 30
            sleeptime = sleepmins*60
            time.sleep(sleeptime)
        return ''

class LightGroup:
    def __init__(self, name, pins):
        self.name = name
        self.pins = pins
        self.intensity = 0

        for pin in self.pins:
            pin.direction = digitalio.Direction.OUTPUT

    def __str__(self):
        return f"{self.name}, {self.pins}"

    def turn_on_all(self):
        for light in self.pins:
            # turn on the lights
            light.value = True

    def turn_off_all(self):
        for light in self.pins:
            # turn off the lights
            light.value = False


LP = LightGroup('lp', [DIO(board.D13)])
# D = LightGroup('d', [DIO(board.D12)])

# test_led = DIO(board.D4)
# test_led.direction = digitalio.Direction.OUTPUT
pwm = pwmio.PWMOut(board.D4, frequency=1000, duty_cycle=0)
#D.pins[0].brightness = 1

while True:
    # LP.turn_on_all()
    # LP.pins[0].value = True
    pwm.duty_cycle = 3000
    time.sleep(0.5)
    # LP.turn_off_all()
    # LP.pins[0].value = False
    # test_led.value = 0
    pwm.duty_cycle = 0
    time.sleep(0.5)

random_time = random.randrange(1,5,1)
random_internal = random.randrange(0.1, 4, 0.2)

LP_story = [
    # Pin name, set to brightness, (optionally) timer
    [D.pins[0], 1, 0.1],
    [LP.pins[0], 1]
]

RP_story = [
    # Pin name, set to brightness, (optionally) timer
    [D.pins[0], 1, 0.1],
    [RP.pins[0], 1]
]

L0_story = [
    # Pin name, set to brightness, (optionally) timer
    [D.pins[0], 1, 0.1],
    [L0.pins[0], 1]
]

R0_story = [
    # Pin name, set to brightness, (optionally) timer
    [D.pins[0], 1, 0.1],
    [R0.pins[0], 1]
]

L1_story = [
    # Pin name, set to brightness, (optional) timer
    [D.pins[0], 1, 0.1],
    [T1.pins[0], 1, random_time],
    [L1b.pins[0], 1, random_internal],
    [L1a.pins[0], 1]
]

R1_story = [
    # Pin name, set to brightness, (optional) timer
    [D.pins[0], 1, 0.1],
    [T1.pins[0], 1, random_time],
    [R1b.pins[0], 1, random_internal],
    [R1a.pins[0], 1]
]

L2_story = [
    # Pin name, set to brightness, (optional) timer
    [D.pins[0], 1, 0.1],
    [T1.pins[0], 1, random_time],
    [T2.pins[0], 1, random_time],
    [L2b.pins[0], 1, random_internal],
    [L2a.pins[0], 1]
]

R2_story = [
    # Pin name, set to brightness, (optional) timer
    [D.pins[0], 1, 0.1],
    [T1.pins[0], 1, random_time],
    [T2.pins[0], 1, random_time],
    [R2b.pins[0], 1, random_internal],
    [R2a.pins[0], 1]
]

all_stories = [LP_story, RP_story, L0_story, R0_story, L1_story, R1_story, L2_story, R2_story]
def storypicker():
    return random.choice(all_stories)
