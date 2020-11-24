import numpy as np
import board
import neopixel
import time

pixel_pin = board.D18
NUM_PIXELS = 24
WAIT = 0.5

pixels = neopixel.NeoPixel(
    pixel_pin, NUM_PIXELS, brightness=0.2, auto_write=False, pixel_order=neopixel.RGB
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


def rainbow_cycle(wait, brightness_range=[1, 1]):
    for j in range(255):
        brightness = np.interp(j, [0, 255], brightness_range)
        for i in range(NUM_PIXELS):
            pixel_index = (i * 256 // (NUM_PIXELS * 4)) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.brightness = brightness
        pixels.show()
        time.sleep(wait)


def off():
    for pixel in pixels:
        pixel = (0, 0, 0)
    pixels.show()


def set(angle):
    r, g, b = wheel(angle)
    pixels.brightness = 0.5
    for i in range(NUM_PIXELS):
        pixels[i] = (r, g, b)
        pixels.show()


def test():
    rainbow_cycle(0.001, brightness_range=[0, 1])
    rainbow_cycle(0.001, brightness_range=[1, 0])
    off()
