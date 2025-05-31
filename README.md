# MicroPython Scrolling Matrix Display for Acid Watcher Diet

This repository contains the MicroPython code and instructions to build a scrolling LED matrix display unit. It's designed to continuously display phrases related to Dr. Aviv's Acid Watcher Diet, providing a constant reminder of key principles. The physical unit can be built using 3D-printable parts for a neat, enclosed design.

---

## Hardware Assembly

This project utilizes common MAX7219 8x8 LED matrix modules. The enclosure design is based on an existing Thingiverse model.

### 3D Printed Parts

The structural components for the display unit can be 3D printed. The  `.stl` files are at this Thingiverse link:

* **[MAX7219 Enclosure by 'Andrewkuk'](https://www.thingiverse.com/thing:3154164/files)**

Download and print the parts, which typically include:
* `cover.stl`
* `body.stl`
  
### Required Components
| Component                       | Description                                                                                          | Link                                                                                                                                                                     |
| :------------------------------ | :--------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **RP2040-Zero** | Small microcontroller running MicroPython (suggested for its size)                                   | [Waveshare RP2040-Zero Wiki](https://www.waveshare.com/wiki/RP2040-Zero)                                                                                                  |
| **4 x MAX7219 8x8 LED Matrix Modules** | Ensure these are chained together                                                                    | [Amazon - MAX7219 Modules](https://www.amazon.com/dp/B0BXDKHZL6?ref_=ppx_hzsearch_conn_dt_b_fed_asin_title_1&th=1)                                                         |
| **Jumper Wires** | Female-to-female                                                                       |                                                                                                                                                                       |
| **USB-C Cable** | For power and programming                                                                            |                                                          


### Wiring Diagram

The ESP32-S3-BOX Lite has a limited number of "safe" and accessible GPIO pins for external SPI communication. Based on extensive testing, the following pinout for a **separate SPI bus (SPI2)** is recommended for the MAX7219 module, using safe and exposed GPIOs on the J2/J3 headers. The internal display (OLED) on your ESP32-S3-BOX uses `SPI(1)` internally.

**Connect the MAX7219 modules (chained together) to your ESP32-S3-BOX Lite as follows:**

* **MAX7219 DIN (Data In)** → **RP2040-Zero MOSI/Pin 3 ** 
* **MAX7219 CLK (Clock)** → **RP2040-Zero SCK/Pin 2** 
* **MAX7219 CS (Chip Select)** → **RP2040-Zero Pin 1** (on J2 header)
* **MAX7219 VCC** → **RP2040-Zero 5V** 
* **MAX7219 GND** → **RP2040-Zero GND**

I.E 

```
from machine import Pin
cs=Pin(1)
sck=Pin(2)
mosi=Pin(3)
```

**Important Notes:**
* Ensure your **MAX7219 modules are powered via 5V**, not 3.3V, for optimal brightness.
* **Double-check that you're connecting to the correct ESP32-S3-BOX headers (J2 and J3)** as indicated. These are the general-purpose headers on the back of the device, not the internal display connection.

---

## Software Setup

### MicroPython Firmware

Ensure your ESP32-S3-BOX Lite has MicroPython firmware installed. If you're encountering issues, a fresh firmware flash is often a good first step. You can use Thonny IDE's "Install MicroPython" feature or `esptool.py`.

### Project Structure

Create the following files on your ESP32-S3-BOX Lite:
