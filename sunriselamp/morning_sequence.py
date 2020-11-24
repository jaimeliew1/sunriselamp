import time

# import numpy as np # numpy isn't correctly configured on the raspberrypi
import math
import board
import neopixel


pixel_pin = board.D18
num_pixels = 24
MAX_BRIGHTNESS = 0.7

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=neopixel.RGB
)


def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // (num_pixels * 4)) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)


def run():
    t_start = time.time()
    for i in range(283):

        dt = time.time() - t_start
        print(dt)
        brightness = MAX_BRIGHTNESS * math.sin(dt / 7200 * math.pi)
        pixels.brightness = brightness
        rainbow_cycle(0.1)


if __name__ == "__main__":
    run()
