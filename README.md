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

* **RP2040 - Zero** - (suggested for it's size) - https://www.waveshare.com/wiki/RP2040-Zero or similarly small microcontroller running micropython
* **4 x MAX7219 8x8 LED Matrix Modules** (often come chained together or with headers for chaining)
* **Jumper Wires** (male-to-female and male-to-male)
* **USB-C Cable** (for power and programming)

### Wiring Diagram

The ESP32-S3-BOX Lite has a limited number of "safe" and accessible GPIO pins for external SPI communication. Based on extensive testing, the following pinout for a **separate SPI bus (SPI2)** is recommended for the MAX7219 module, using safe and exposed GPIOs on the J2/J3 headers. The internal display (OLED) on your ESP32-S3-BOX uses `SPI(1)` internally.

**Connect the MAX7219 modules (chained together) to your ESP32-S3-BOX Lite as follows:**

* **MAX7219 DIN (Data In)** → **ESP32-S3-BOX GPIO39** (on J3 header)
* **MAX7219 CLK (Clock)** → **ESP32-S3-BOX GPIO40** (on J3 header)
* **MAX7219 CS (Chip Select)** → **ESP32-S3-BOX GPIO41** (on J2 header)
* **MAX7219 VCC** → **ESP32-S3-BOX 5V** (on J3 header for best brightness/stability)
* **MAX7219 GND** → **ESP32-S3-BOX GND** (on J3 header)

**Important Notes:**
* Ensure your **MAX7219 modules are powered via 5V**, not 3.3V, for optimal brightness.
* **Double-check that you're connecting to the correct ESP32-S3-BOX headers (J2 and J3)** as indicated. These are the general-purpose headers on the back of the device, not the internal display connection.

---

## Software Setup

### MicroPython Firmware

Ensure your ESP32-S3-BOX Lite has MicroPython firmware installed. If you're encountering issues, a fresh firmware flash is often a good first step. You can use Thonny IDE's "Install MicroPython" feature or `esptool.py`.

### Project Structure

Create the following files on your ESP32-S3-BOX Lite:
