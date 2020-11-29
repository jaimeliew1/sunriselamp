import numpy as np
import board
import neopixel
import time
from sunriselamp.backend import wheel, off

pixel_pin = board.D18
NUM_PIXELS = 24
WAIT = 0.01
pixels = neopixel.NeoPixel(
    pixel_pin, NUM_PIXELS, brightness=0.2, auto_write=False, pixel_order=neopixel.RGB
)

FADE_T = 120
duration = 7200
color_f = 1 / 8  # Hz
ring_f = 1 / 10  # Hz
# FADE_T = 1.3
# duration = 3
# color_f = 1 / 8  # Hz
# ring_f = 1 / 1  # Hz


def PDF(x, sigma, mu):
    p = np.exp(-((np.log(x) - mu) ** 2) / (2 * sigma ** 2)) / (
        x * sigma * np.sqrt(2 * np.pi)
    )
    return p ** 2


kernel = lambda x: PDF(x, 0.7833936678835931, 2)


def fade(t, duration):
    if t < FADE_T:
        return t / FADE_T
    elif t > (duration - FADE_T):
        return 1 - (t - (duration - FADE_T)) / FADE_T
    else:
        return 1


def brightness_func(dt):
    pos = (np.arange(NUM_PIXELS) + dt * ring_f * NUM_PIXELS) % NUM_PIXELS
    b = kernel(pos)
    b /= max(b)
    b = np.nan_to_num(b)
    return b


def hue_func(dt):
    pos = (np.linspace(0, 255, NUM_PIXELS) + dt * color_f * 255) % 255
    return [wheel(x) for x in pos]


def run():
    t_start = time.time()
    dt = 0
    while dt < duration:

        t_norm = dt / duration

        hues = hue_func(dt)
        brightnesses = brightness_func(dt) * fade(dt, duration)

        for i, (hue, brightness) in enumerate(zip(hues, brightnesses)):
            pixels[i] = [int(h * brightness) for h in hue]

        pixels.brightness = 1
        pixels.show()
        time.sleep(WAIT)
        dt = time.time() - t_start

    off()


if __name__ == "__main__":
    run()
