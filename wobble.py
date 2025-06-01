import time

# --- Pin Definitions ---
# Adjust these pins if your wiring is different
from max_7219_config import display, DISPLAY_WIDTH

# --- Display Configuration ---
BRIGHTNESS = 1      # Brightness level (0-15)
SCROLL_DELAY_MS = 80 # Delay between each scroll step in milliseconds (adjust for speed)

MSG= ["Heal Acid Damage",
    "pH over 5",
    "28-Day Healing Phase",
    "Food as Medicine",
    "Neutralize Acid",
    "Reduce Inflammation",
    "Avoid Dirty Dozen",
    "Low-Acid Living",
    "Reflux Gourmet",  
    "Go Beyond Heartburn",
    "Whole Body Healing",
    "Balanced Macronutrients",
    "Fiber Is Key",
    "No More Processed",
    "Mindful Eating",
    "pH Values Matter",
    "Identify Triggers",
    "acidwatcher.com",
    "Prevent Esophageal Cancer",
    "Restore Cellular Integrity",
    "Sleep Position Matters",
    "Chew Your Food Well",
    "Post-Meal Walk",
    "Small Frequent Meals",
    "Eliminate Nighttime Snacking",
    "Stress Reduction for Digestion",
    "Avoid Carbonation",
    "No Coffee or Alcohol",
    "Mind Your Tomatoes",
    "Vinegar-Free Dressing",
    "Stay Hydrated, Stay Healthy",
    "Long-Term Wellness",   
]    
    
# Set initial display properties
display.brightness(BRIGHTNESS)
display.fill(0) # Clear the entire display buffer (all pixels off)
display.show() # Update the physical display with the empty buffer

# --- Vertical Wobble Configuration ---
# These define how far up/down the text can shift and how fast it moves vertically
MAX_Y_OFFSET = 2  # Max pixels down from the top (positive value shifts text down, causing bottom clip)
MIN_Y_OFFSET = -2 # Max pixels up from the top (negative value shifts text up, causing top clip)
Y_STEP = 1        # Pixels to move vertically per horizontal step

# Calculate the total display width and height
DISPLAY_HEIGHT = 8               # Standard height for 8x8 matrices
current_y_offset = 0 # Starting vertical offset (0 means top-aligned)
y_direction = Y_STEP # Initial vertical movement direction (start moving down)

# --- Main Scrolling Loop ---
while True:
    for TEXT_TO_SCROLL in MSG:
        # Outer loop for continuous scrolling
        # Calculate the width of the text in pixels
        text_pixel_width = len(TEXT_TO_SCROLL) * 8
        
        # Horizontal scroll loop (right-to-left)
        for x_position in range(DISPLAY_WIDTH, -text_pixel_width, -1):
            display.fill(0) # Clear the entire display buffer for the new frame
            
            # Draw the text at the current horizontal (x_position) and vertical (current_y_offset) coordinates.
            # Changing current_y_offset will make the text appear to wobble or bounce vertically.
            display.text(TEXT_TO_SCROLL, x_position, current_y_offset) 
            
            display.show() # Send the buffer content to the physical LED matrices
            time.sleep_ms(SCROLL_DELAY_MS)

            # Update vertical offset for the next horizontal step
            current_y_offset += y_direction

            # Check and reverse vertical direction if bounds are hit
            if current_y_offset >= MAX_Y_OFFSET:
                y_direction = -Y_STEP # Change direction to move up
            elif current_y_offset <= MIN_Y_OFFSET:
                y_direction = Y_STEP  # Change direction to move down
            
    # Optional: Add a short delay or fill(0) before the next full scroll cycle starts
    # to give a visual break, though the loop itself is continuous.