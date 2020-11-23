import board
import neopixel


pixel_pin = board.D18
num_pixels = 24


pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=neopixel.RGB
)


for pixel in pixels:
    pixel = (0, 0, 0)
pixels.show()
