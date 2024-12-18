from time import sleep

import board
import digitalio


def get_led():
    led = digitalio.DigitalInOut(board.LED)
    led.direction = digitalio.Direction.OUTPUT
    return led


def flash(led: digitalio.DigitalInOut):
    led.value = True
    sleep(0.1)
    led.value = False
    sleep(0.1)
