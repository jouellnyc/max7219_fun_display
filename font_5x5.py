import time
from max_7219_config import display, DISPLAY_WIDTH

# 5-Pixel Font Renderer for MAX7219
# Complete alphabet A-Z and digits 0-9
# Requires: from max_7219_config import display, DISPLAY_WIDTH

import time
from max_7219_config import display, DISPLAY_WIDTH

# Complete 5x5 Font definitions (A-Z, 0-9, space)
FONT_5x5 = {
    'a': [
        [0, 1, 1, 1, 0],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1]
    ],
    'b': [
        [1, 1, 1, 1, 0],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 0],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 0]
    ],
    'c': [
        [0, 1, 1, 1, 0],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0],
        [1, 0, 0, 0, 1],
        [0, 1, 1, 1, 0]
    ],
    'd': [
        [1, 1, 1, 1, 0],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 0]
    ],
    'e': [
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1]
    ],
    'f': [
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0],
        [1, 0, 0, 0, 0]
    ],
    'g': [
        [0, 1, 1, 1, 0],
        [1, 0, 0, 0, 0],
        [1, 0, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [0, 1, 1, 1, 0]
    ],
    'h': [
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1]
    ],
    'i': [
        [0, 1, 1, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 1, 1, 0]
    ],
    'j': [
        [0, 0, 1, 1, 1],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 0, 0, 1, 0],
        [0, 1, 1, 0, 0]
    ],
    'k': [
        [1, 0, 0, 1, 0],
        [1, 0, 1, 0, 0],
        [1, 1, 0, 0, 0],
        [1, 0, 1, 0, 0],
        [1, 0, 0, 1, 0]
    ],
    'l': [
        [1, 0, 0, 0, 0],
        [1, 0, 0, 0, 0],
        [1, 0, 0, 0, 0],
        [1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1]
    ],
    'm': [
        [1, 0, 0, 0, 1],
        [1, 1, 0, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1]
    ],
    'n': [
        [1, 0, 0, 0, 1],
        [1, 1, 0, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 0, 1, 1],
        [1, 0, 0, 0, 1]
    ],
    'o': [
        [0, 1, 1, 1, 0],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [0, 1, 1, 1, 0]
    ],
    'p': [
        [1, 1, 1, 1, 0],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0],
        [1, 0, 0, 0, 0]
    ],
    'q': [
        [0, 1, 1, 1, 0],
        [1, 0, 0, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 0, 1, 0],
        [0, 1, 1, 0, 1]
    ],
    'r': [
        [1, 1, 1, 1, 0],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 0],
        [1, 0, 1, 0, 0],
        [1, 0, 0, 1, 1]
    ],
    's': [
        [0, 1, 1, 1, 1],
        [1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1],
        [1, 1, 1, 1, 0]
    ],
    't': [
        [1, 1, 1, 1, 1],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0]
    ],
    'u': [
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [0, 1, 1, 1, 0]
    ],
    'v': [
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [0, 1, 0, 1, 0],
        [0, 0, 1, 0, 0]
    ],
    'w': [
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 1, 0, 1, 1],
        [1, 0, 0, 0, 1]
    ],
    'x': [
        [1, 0, 0, 0, 1],
        [0, 1, 0, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 0, 1, 0],
        [1, 0, 0, 0, 1]
    ],
    'y': [
        [1, 0, 0, 0, 1],
        [0, 1, 0, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0]
    ],
    'z': [
        [1, 1, 1, 1, 1],
        [0, 0, 0, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 0, 0, 0],
        [1, 1, 1, 1, 1]
    ],
    '0': [
        [0, 1, 1, 1, 0],
        [1, 0, 0, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 1, 0, 0, 1],
        [0, 1, 1, 1, 0]
    ],
    '1': [
        [0, 0, 1, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 1, 1, 0]
    ],
    '2': [
        [0, 1, 1, 1, 0],
        [1, 0, 0, 0, 1],
        [0, 0, 1, 1, 0],
        [0, 1, 0, 0, 0],
        [1, 1, 1, 1, 1]
    ],
    '3': [
        [1, 1, 1, 1, 0],
        [0, 0, 0, 0, 1],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1],
        [1, 1, 1, 1, 0]
    ],
    '4': [
        [1, 0, 0, 1, 0],
        [1, 0, 0, 1, 0],
        [1, 1, 1, 1, 1],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0]
    ],
    '5': [
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0],
        [0, 0, 0, 0, 1],
        [1, 1, 1, 1, 0]
    ],
    '6': [
        [0, 1, 1, 1, 0],
        [1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0],
        [1, 0, 0, 0, 1],
        [0, 1, 1, 1, 0]
    ],
    '7': [
        [1, 1, 1, 1, 1],
        [0, 0, 0, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 0, 0, 0],
        [1, 0, 0, 0, 0]
    ],
    '8': [
        [0, 1, 1, 1, 0],
        [1, 0, 0, 0, 1],
        [0, 1, 1, 1, 0],
        [1, 0, 0, 0, 1],
        [0, 1, 1, 1, 0]
    ],
    '9': [
        [0, 1, 1, 1, 0],
        [1, 0, 0, 0, 1],
        [0, 1, 1, 1, 1],
        [0, 0, 0, 0, 1],
        [0, 1, 1, 1, 0]
    ],
    ' ': [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
}

def add_char(char, pattern):
    """Add a new character to the font dictionary"""
    FONT_5x5[char.lower()] = pattern

def get_char_pattern(char):
    """Get the 5x5 pattern for a character"""
    return FONT_5x5.get(char.lower(), FONT_5x5[' '])

def render_char(char, x_offset=0, y_offset=1):
    """
    Render a single character on the display
    Returns the character width for positioning next character
    """
    if char.lower() not in FONT_5x5:
        return 5  # Return width even if char not found
    
    pattern = FONT_5x5[char.lower()]
    
    for row in range(5):
        for col in range(5):
            if pattern[row][col] and (x_offset + col) < DISPLAY_WIDTH:
                display.pixel(x_offset + col, y_offset + row, 1)
    
    return 5  # Character width

def render_text(text, x_offset=1, y_offset=1, char_spacing=1, clear_first=True):
    """
    Render text on the display
    Args:
        text: String to display
        x_offset: Starting X position
        y_offset: Starting Y position  
        char_spacing: Pixels between characters
        clear_first: Whether to clear display before rendering
    """
    if clear_first:
        display.fill(0)
    
    current_x = x_offset
    
    for char in text:
        if current_x >= DISPLAY_WIDTH:
            break  # Text extends beyond display
        
        char_width = render_char(char, current_x, y_offset)
        current_x += char_width + char_spacing
    
    display.show()

def scroll_text(text, delay=0.2, loops=1, y_offset=1):
    """
    Scroll text across the display from right to left
    Args:
        text: String to scroll
        delay: Time between scroll steps
        loops: Number of times to repeat scroll
        y_offset: Vertical position of text
    """
    if not text:
        return
    
    # Calculate total text width
    text_width = len(text) * 6 - 1  # 5 pixels per char + 1 space between
    
    for loop in range(loops):
        # Scroll from right to left
        for x in range(DISPLAY_WIDTH, -text_width, -1):
            display.fill(0)
            
            current_x = x
            for char in text:
                if current_x >= -5 and current_x < DISPLAY_WIDTH:  # Only render visible chars
                    render_char(char, current_x, y_offset)
                current_x += 6
            
            display.show()
            time.sleep(delay)

def center_text(text, y_offset=1):
    """
    Center text horizontally on the display
    """
    text_width = len(text) * 6 - 1  # Calculate text width
    x_offset = max(0, (DISPLAY_WIDTH - text_width) // 2)
    render_text(text, x_offset, y_offset)

def render_text_buffer(text, x_offset=0, y_offset=1, char_spacing=1):
    """
    Render text to a buffer without displaying
    Returns 2D list representing the pixels
    Useful for animations or custom effects
    """
    # Create buffer
    buffer = [[0 for _ in range(DISPLAY_WIDTH)] for _ in range(8)]
    
    current_x = x_offset
    
    for char in text:
        if current_x >= DISPLAY_WIDTH:
            break
        
        pattern = get_char_pattern(char)
        
        for row in range(5):
            for col in range(5):
                if pattern[row][col] and (current_x + col) < DISPLAY_WIDTH:
                    if (y_offset + row) < 8:  # Make sure we don't exceed display height
                        buffer[y_offset + row][current_x + col] = 1
        
        current_x += 5 + char_spacing
    
    return buffer

def display_buffer(buffer):
    """Display a buffer on the LED matrix"""
    display.fill(0)
    for row in range(min(8, len(buffer))):
        for col in range(min(DISPLAY_WIDTH, len(buffer[0]))):
            if buffer[row][col]:
                display.pixel(col, row, 1)
    display.show()

def blink_text(text, blink_count=3, on_time=0.5, off_time=0.3, x_offset=0, y_offset=1):
    """Make text blink on the display"""
    for _ in range(blink_count):
        render_text(text, x_offset, y_offset)
        time.sleep(on_time)
        display.fill(0)
        display.show()
        time.sleep(off_time)

def typewriter_effect(text, char_delay=0.3, x_offset=0, y_offset=1):
    """Display text with typewriter effect"""
    display.fill(0)
    current_text = ""
    
    for char in text:
        current_text += char
        render_text(current_text, x_offset, y_offset)
        time.sleep(char_delay)

# Example usage functions
def demo_alphabet():
    """Demo displaying the alphabet"""
    print("Displaying alphabet...")
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    scroll_text(alphabet, delay=0.1, loops=1)

def demo_numbers():
    """Demo displaying numbers"""
    print("Displaying numbers 0-9...")
    for i in range(10):
        render_text(str(i), x_offset=2, y_offset=1)
        time.sleep(0.8)

def demo_static():
    """Demo static text display"""
    print("Displaying 'hello'...")
    render_text('hello')
    time.sleep(2)
    
    print("Centering 'world'...")
    center_text('world')
    time.sleep(2)

def demo_scroll():
    """Demo scrolling text"""
    print("Scrolling 'hello world'...")
    scroll_text('hello world', delay=0.15, loops=2)

def demo_effects():
    """Demo text effects"""
    print("Blinking 'blink'...")
    blink_text('blink', blink_count=3)
    
    time.sleep(1)
    
    print("Typewriter effect...")
    typewriter_effect('hello', char_delay=0.5)
    time.sleep(2)

def demo_mixed():
    """Demo mixed text and numbers"""
    print("Displaying mixed content...")
    render_text('abc123')
    time.sleep(2)
    scroll_text('the quick brown fox jumps over lazy dog 0123456789', delay=0.1)

# Main demo function
def demo_all():
    """Run all demonstrations"""
    try:
        # Import the display configuration
        from max_7219_config import display, DISPLAY_WIDTH
        globals()['display'] = display
        globals()['DISPLAY_WIDTH'] = DISPLAY_WIDTH
        
        print("Running complete font renderer demos...")
        print(f"Font contains {len(FONT_5x5)} characters: A-Z, 0-9, and space")
        
        demo_alphabet()
        demo_numbers()
        demo_static()
        demo_scroll()
        demo_effects()
        demo_mixed()
        
        # Clear display
        display.fill(0)
        display.show()
        print("Demo complete!")
        
    except ImportError:
        print("Error: Could not import from max_7219_config")
        print("Make sure max_7219_config.py exists with 'display' and 'DISPLAY_WIDTH' defined")
    except Exception as e:
        print(f"Error during demo: {e}")

def list_available_chars():
    """List all available characters in the font"""
    chars = sorted(FONT_5x5.keys())
    print(f"Available characters ({len(chars)}): {', '.join(chars)}")
    return chars

if __name__ == "font_5x5":
    list_available_chars()
    demo_all()