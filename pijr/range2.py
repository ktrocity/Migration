import time
import board
import adafruit_dotstar as dotstar

# Number of LEDs in the strip
NUM_LEDS = 90

# Define the colors (RGB format)
COLOR0 = (0, 0, 0)
COLOR1 = (208, 141,170)
COLOR2 = (208, 141, 100)
COLOR3 = (177, 86, 121)
COLOR4 = (124, 103, 131)
COLOR5 = (255, 200, 80)

# Initialize the DotStar strip
leds = dotstar.DotStar(board.SCK, board.MOSI, NUM_LEDS, brightness=0.4)

def all_off():
    """Turn off all LEDs."""
    leds.fill(COLOR0)
    leds.show()

def set_led(index, color):
    """Set a specific LED to a color."""
    if 0 <= index < NUM_LEDS:
        leds[index] = color
        leds.show()
    else:
        print(f"Index {index} is out of range. Please choose an index between 0 and {NUM_LEDS-1}.")

def interpolate_color(start_color, end_color, t):
    """Interpolate between two colors."""
    return tuple(int(start + (end - start) * t) for start, end in zip(start_color, end_color))

def fade_led(index, color, duration):
    """Fade LED to a specific color over a duration."""
    if 0 <= index < NUM_LEDS:
        start_color = leds[index]
        steps = int(duration * 100)  # Number of steps for the fade
        for step in range(steps):
            t = step / steps
            intermediate_color = interpolate_color(start_color, color, t)
            leds[index] = intermediate_color
            leds.show()
            time.sleep(duration / steps)
        # Ensure the final color is set
        leds[index] = color
        leds.show()
    else:
        print(f"Index {index} is out of range. Please choose an index between 0 and {NUM_LEDS-1}.")

def off_led(index, duration):
    """Fade LED off over a duration."""
    if 0 <= index < NUM_LEDS:
        start_color = leds[index]  # Start from the current color
        end_color = (0, 0, 0)  # Fade to black (off)
        steps = int(duration * 100)  # Number of steps for the fade
        for step in range(steps):
            t = step / steps
            intermediate_color = interpolate_color(start_color, end_color, t)
            leds[index] = intermediate_color
            leds.show()
            time.sleep(duration / steps)
        # Ensure the final color is black (off)
        leds[index] = end_color
        leds.show()


all_off()

while True:
    fade_led(58, COLOR1, 1)
    fade_led(8, COLOR5, 1)
    off_led(62, 1)
    off_led(52, 1)
    time.sleep(0)
    fade_led(70, COLOR4, 1)
    fade_led(45, COLOR1, 1)
    off_led(75, 1)
    off_led(42, 1)
    time.sleep(0)
    fade_led(23, COLOR2, 1)
    fade_led(85, COLOR5, 1)
    off_led(39, 1)
    off_led(88, 1)
    time.sleep(0)

    fade_led(3, COLOR3, 1)
    fade_led(53, COLOR4, 1)
    off_led(58, 1)
    off_led(8, 1)
    time.sleep(0)
    fade_led(11, COLOR5, 1)
    fade_led(73, COLOR1, 1)
    off_led(70, 1)
    off_led(45, 1)
    time.sleep(0)
    fade_led(19, COLOR5, 1)
    fade_led(24, COLOR3, 1)
    off_led(23, 1)
    off_led(85, 1)
    time.sleep(0)

    fade_led(62, COLOR4, 1)
    fade_led(52, COLOR3, 1)
    off_led(3, 1)
    off_led(53, 1)
    time.sleep(0)
    fade_led(75, COLOR5, 1)
    fade_led(42, COLOR1, 1)
    off_led(11, 1)
    off_led(73, 1)
    time.sleep(0)
    fade_led(39, COLOR3, 1)
    fade_led(88, COLOR4, 1)
    off_led(19, 1)
    off_led(24, 1)
    time.sleep(0)
