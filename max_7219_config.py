#ESP32-Mini
from machine import Pin, SPI
import max7219

from config import device
if device == "rp2040-zero":
    print(f"Using {device} config")
    cs=Pin(7)
    sck=Pin(4)
    mosi=Pin(6)
    spi_bus=1
else:
    print(f"Using defaul esp32-mini config")
    cs=Pin(1)
    sck=Pin(2)
    mosi=Pin(3)
    spi_bus=0

spi = SPI(spi_bus, baudrate=10000000, polarity=1, phase=0, sck=sck, mosi=mosi)

NUM_MATRICES = 4    # Set to the total number of 8x8 matrices
DISPLAY_WIDTH = NUM_MATRICES * 8 # 4 modules * 8 pixels/module = 32 pixels wide

# --- SPI and Display Initialization ---
display = max7219.Matrix8x8(spi, cs, NUM_MATRICES)

