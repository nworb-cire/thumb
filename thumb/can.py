import board
from adafruit_mcp2515 import MCP2515 as CAN, Message
from digitalio import DigitalInOut

MESSAGE_ADDRESS = 452


class CruiseState:
  OFF = 0
  ACTIVE = 1
  FAULTED = 3
  STANDSTILL = 4


def extract_cruise_state(message: bytes):
    if len(message) != 8:
        raise Exception(f"Invalid message length for data {message}")
    return (message[1] & 0b11100000) >> 5


def get_can_bus():
    cs = DigitalInOut(board.CAN_CS)
    cs.switch_to_output()
    spi = board.SPI()
    can_bus = CAN(
        spi, cs, loopback=False, silent=True
    )  # use loopback to test without another device

    return can_bus