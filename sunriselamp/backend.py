import board
import neopixel
import time

pixel_pin = board.D18
num_pixels = 24
WAIT = 0.5

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=neopixel.RGB
)


def off():
    for pixel in pixels:
        pixel = (0, 0, 0)
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
