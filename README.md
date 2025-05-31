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

**Connect the MAX7219 modules (chained together) to your ESP32-S3-BOX Lite as follows:**

| MAX7219 Pin      | RP2040-Zero Connection        |
| :--------------- | :---------------------------- |
| **DIN (Data In)** | **MOSI/Pin 3** |
| **CLK (Clock)** | **SCK/Pin 2** |
| **CS (Chip Select)** | **Pin 1** (on J2 header)        |
| **VCC** | **5V** |
| **GND** | **GND** |

I.E 

```
from machine import Pin
cs=Pin(1)
sck=Pin(2)
mosi=Pin(3)
```

**Important Notes:**
* Best to ensure your **MAX7219 modules are powered via 5V**, not 3.3V, for optimal brightness.

---

## Software Setup

### MicroPython Firmware

Ensure your ESP32-S3-BOX Lite has MicroPython firmware installed. If you're encountering issues, a fresh firmware flash is often a good first step. You can use Thonny IDE's "Install MicroPython" feature or `esptool.py`.

### Basic Configuration

The main parameters you can adjust to customize the display's behavior are located at the top of your `main.py` file:
```python
NUM_MATRICES = 4        # Number of 8x8 matrices chained together
BRIGHTNESS = 1          # Display brightness (0-15, 0 is off, 15 is brightest)
SCROLL_DELAY_MS = 80    # Scroll speed in milliseconds (smaller value = faster scroll)
```

## Customization Ideas

Here are some ideas to expand the functionality of your scrolling display:

- **Add different scroll directions**: Implement left-to-right, up-down, or diagonal scrolling.
- **Implement fade effects**: Make text appear and disappear gradually.
- **Create multiple animation modes**: Switch between different scrolling and display patterns.
- **Add sensor input for interactive displays**: For example, display different messages based on temperature, light, or button presses.
- **Include time/date display functionality**: Turn your scrolling display into a compact clock.

## Credits

- **3D Model**: The enclosure design is from [Thingiverse Thing #3154164](https://www.thingiverse.com/thing:3154164) by 'Andrewkuk'.
- **MAX7219 MicroPython library contributors** for [the display driver](https://github.com/mcauser/micropython-max7219).
- **Health messaging content** for acid reflux awareness, based on Dr. Jonathan Aviv's Acid Watcher Diet.

## License

This project is open source. Please credit original sources and this repository when sharing or modifying.
