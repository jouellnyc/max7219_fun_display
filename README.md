# MicroPython Scrolling Matrix Display 

This repository contains the MicroPython code and instructions to build a scrolling ('wobbling/jumping') LED matrix display unit (see the video).

It's designed to continuously display phrases -- in the case I chose to use text related to Dr. Aviv's Acid Watcher Diet -- providing a constant reminder of key principles. The physical unit can be built using 3D-printable parts for a neat, enclosed design.

![pic](https://github.com/user-attachments/assets/df123fb4-9a84-4340-b4f2-b671de95a387)

| Asset Type | Link |
|------------|------|
| **Video** | `https://github.com/jouellnyc/max7219_fun_display/blob/main/w.mp4` |

---
Note: the 5x5 font and all of the max 7219 code was written entirely by ClaudeAi

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
| **RP2040-Zero** | It works with the soldered pins  | [Waveshare RP2040-Zero Wiki](https://www.waveshare.com/wiki/RP2040-Zero)                                                                                                  |
| **OR a ESP32-S3-Zero Mini** | It works with the soldered pins | [ESP32-S3-Zero Mini](https://www.amazon.com/ESP32-C6-Development-ESP32-C6FH4-Processors-Bluetooth/dp/B0CZDW5F6Q)                                                                                                  |
| **4 x MAX7219 8x8 LED Matrix Modules** | Ensure these are chained together                                                                    | [Amazon - MAX7219 Modules](https://www.amazon.com/dp/B0BXDKHZL6?ref_=ppx_hzsearch_conn_dt_b_fed_asin_title_1&th=1)                                                         |
| **Jumper Wires** | Female-to-female                                                                       |                                                                                                                                                                       |
| **USB-C Cable** | For power and programming                                                                            |                                                          


### Wiring Diagram

**Connect the MAX7219 modules (chained together) to your zero  as follows:**


| MAX7219 Pin      | RP2040-Zero Connection        |
| :--------------- | :---------------------------- |
| **DIN (Data In)** | **MOSI/Pin 3** |
| **CLK (Clock)** | **SCK/Pin 2** |
| **CS (Chip Select)** | **Pin 1**       |
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

Ensure your device has MicroPython firmware installed. If you're encountering issues, a fresh firmware flash is often a good first step. You can use Thonny IDE's "Install MicroPython" feature or `esptool.py`.

### Basic Configuration

The main parameters you can adjust to customize the display's behavior are located at the top of your `wobble.py` file:
```python
NUM_MATRICES = 4        # Number of 8x8 matrices chained together
BRIGHTNESS = 1          # Display brightness (0-15, 0 is off, 15 is brightest)
SCROLL_DELAY_MS = 80    # Scroll speed in milliseconds (smaller value = faster scroll)
```

## Customization Ideas

Here are some ideas to expand the functionality of your scrolling display:

- Add different scroll directions: Implement left-to-right, up-down, or diagonal scrolling.
- Implement fade effects: Make text appear and disappear gradually.
- Create multiple animation modes: Switch between different scrolling and display patterns.
- Add sensor input for interactive displays: For example, display different messages based on temperature, light, or button presses.
- Use your own Fun/Inspirational/Educational Text: Turn your scrolling display into your own custom device. 

## Credits

- **3D Model**: The enclosure design is from [Thingiverse Thing #3154164](https://www.thingiverse.com/thing:3154164) by 'Andrewkuk'.
- **MAX7219 MicroPython library (mcauser)** for [the display driver](https://github.com/mcauser/micropython-max7219).
- **Health messaging content** for acid reflux awareness, based on Dr. Jonathan Aviv's Acid Watcher Diet.

## License

This project is open source. Please credit original sources and this repository when sharing or modifying.
