import time
import numpy as np

import board
import neopixel
from pathlib import Path
from sunriselamp.backend import wheel, off

PIXEL_PIN = board.D18
NUM_PIXELS = 24
MAX_BRIGHTNESS = 0.9
WAIT = 0.01
T_END = 2 * 60 * 60

this_dir = Path(__file__).parent
sequence_table = np.loadtxt(this_dir / "sunrise_sequence.txt", delimiter=",")
brightness_table = np.loadtxt(this_dir / "brightness_sequence.txt", delimiter=",")


def get_brightness(dt_norm):
    return np.interp(dt_norm, brightness_table[:, 0], brightness_table[:, 1])


def get_hue(dt_norm):
    pos = np.interp(dt_norm, sequence_table[:, 0], sequence_table[:, 1])
    return wheel(pos)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(NUM_PIXELS):
            pixel_index = (i * 256 // (NUM_PIXELS * 4)) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)


def run():
    pixels = neopixel.NeoPixel(
        PIXEL_PIN,
        NUM_PIXELS,
        brightness=0.2,
        auto_write=False,
        pixel_order=neopixel.RGB,
    )

    t_start = time.time()
    dt = time.time() - t_start
    while dt < T_END:
        dt_norm = dt / T_END
        print(dt_norm)
        pixels.brightness = MAX_BRIGHTNESS * get_brightness(dt_norm)
        hue = get_hue(dt_norm)

        for i in range(NUM_PIXELS):
            pixels[i] = hue
        pixels.show()
        time.sleep(WAIT)
        dt = time.time() - t_start

    off()


if __name__ == "__main__":
    run()
