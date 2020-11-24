import board
import neopixel
import time

pixel_pin = board.D18
num_pixels = 24
WAIT = 0.5

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


def off():
    for pixel in pixels:
        pixel = (0, 0, 0)
    pixels.show()


def set(angle):
    r, g, b = wheel(angle)
    pixels.brightness = 0.5
    for i in range(num_pixels):
        pixels[i] = (r, g, b)
        pixels.show()


def test():
    for i in range(num_pixels):
        pixels[i] = (255, 0, 0)
    pixels.show()
    time.sleep(WAIT)

    for i in range(num_pixels):
        pixels[i] = (0, 0, 0)
    pixels.show()
    time.sleep(WAIT)

    for i in range(num_pixels):
        pixels[i] = (0, 255, 0)
    pixels.show()
    time.sleep(WAIT)

    for i in range(num_pixels):
        pixels[i] = (0, 0, 0)
    pixels.show()
    time.sleep(WAIT)

    for i in range(num_pixels):
        pixels[i] = (0, 0, 255)
    pixels.show()
    time.sleep(WAIT)

    for i in range(num_pixels):
        pixels[i] = (0, 0, 0)
    pixels.show()
    time.sleep(WAIT)
