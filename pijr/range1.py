import time
import board
import adafruit_dotstar as dotstar

# Number of LEDs in the strip
NUM_LEDS = 90


# Define the colors (RGB format)
COLOR0 = (0, 0, 0)
COLOR1 = (255, 200, 80)
COLOR2 = (255, 200, 105)
COLOR3 = (255, 200, 130)
COLOR4 = (255, 200, 155)
COLOR5 = (255, 200, 205)

# Initialize the DotStar strip
leds = dotstar.DotStar(board.SCK, board.MOSI, NUM_LEDS, brightness=.7)

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
    fade_led(5, COLOR1, 1)
    off_led(48, 1)
    time.sleep(0)
    fade_led(70, COLOR3, 1)
    off_led(81, 1)
    time.sleep(0)
    fade_led(20, COLOR4, 1)
    off_led(33, 1)
    time.sleep(0)
    fade_led(83, COLOR1, 1)
    off_led(5, 1)
    time.sleep(0)
    fade_led(31, COLOR2, 1)
    off_led(70, 1)
    time.sleep(0)

    fade_led(57, COLOR5, 1)
    off_led(20, 1)
    time.sleep(0)
    fade_led(69, COLOR3, 1)
    off_led(83, 1)
    time.sleep(0)
    fade_led(16, COLOR2, 1)
    off_led(31, 1)
    time.sleep(0)
    fade_led(39, COLOR4,1)
    off_led(57, 1)
    time.sleep(0)
    fade_led(87, COLOR1, 1)
    off_led(69, 1)
    time.sleep(0)

    fade_led(3, COLOR3, 1)
    off_led(16, 1)
    time.sleep(0)
    fade_led(66, COLOR5, 1)
    off_led(39, 1)
    time.sleep(0)
    fade_led(48, COLOR2, 1)
    off_led(87, 1)
    time.sleep(0)
    fade_led(81, COLOR4, 1)
    off_led(3, 1)
    time.sleep(0)
    fade_led(33, COLOR1, 1)
    off_led(66, 1)
    time.sleep(0)
