from machine import Pin, SPI
import max7219
from config import device

# Device configuration dispatch table
DEVICE_CONFIGS = {
    "rp2040-zero": {
        "cs_pin": 7,
        "sck_pin": 4,
        "mosi_pin": 6,
        "spi_bus": 1
    },
    "esp32-mini": {  # default config
        "cs_pin": 1,
        "sck_pin": 2,
        "mosi_pin": 3,
        "spi_bus": 0
    }
}

# Get configuration, fallback to esp32-mini if device not found
config = DEVICE_CONFIGS.get(device, DEVICE_CONFIGS["esp32-mini"])
print(f"Using {device} config" if device in DEVICE_CONFIGS else f"Unknown device '{device}', using esp32-mini config")

# Initialize pins and SPI using dispatch table values
cs = Pin(config["cs_pin"])
sck = Pin(config["sck_pin"])
mosi = Pin(config["mosi_pin"])

spi = SPI(config["spi_bus"], baudrate=10000000, polarity=1, phase=0, sck=sck, mosi=mosi)

NUM_MATRICES = 4    # Set to the total number of 8x8 matrices
DISPLAY_WIDTH = NUM_MATRICES * 8 # 4 modules * 8 pixels/module = 32 pixels wide

# --- SPI and Display Initialization ---
display = max7219.Matrix8x8(spi, cs, NUM_MATRICES)
