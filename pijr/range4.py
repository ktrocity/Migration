import time
import board
import adafruit_dotstar as dotstar

# Number of LEDs in the strip
NUM_LEDS = 90

# Define the colors (RGB format)
COLOR0 = (0, 0, 0)
COLOR1 = (139, 103, 126)
COLOR2 = (208, 141, 100)
COLOR3 = (224, 127, 53)
COLOR4 = (148, 86, 121)
COLOR5 = (158, 150, 140)
COLOR6 = (208, 141, 22)
COLOR7 = (134, 129, 90)
COLOR8 = (216, 123, 129)
COLOR9 = (177, 86, 21)

# Initialize the DotStar strip
leds = dotstar.DotStar(board.SCK, board.MOSI, NUM_LEDS, brightness=0.5)

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
    fade_led(58, COLOR3, .7)
    fade_led(5, COLOR1, .7)
    fade_led(69, COLOR9, .7)
    fade_led(51, COLOR8, .7)
    off_led(62, .7)
    off_led(57, .7)
    off_led(8, .7)
    off_led(49, .7)
    time.sleep(0)
    fade_led(12, COLOR8, .7)
    fade_led(45, COLOR3, .7)
    fade_led(77, COLOR2, .7)
    fade_led(43, COLOR4, .7)
    off_led(75, .7)
    off_led(42, .7)
    off_led(19, .7)
    off_led(40, .7)
    time.sleep(0)
    fade_led(21, COLOR4, .7)
    fade_led(38, COLOR6, .7)
    fade_led(85, COLOR3, .7)
    fade_led(33, COLOR1, .7)
    off_led(23, .7)
    off_led(35, .7)
    off_led(86, .7)
    off_led(32, .7)
    time.sleep(0)

    fade_led(2, COLOR7, .7)
    fade_led(55, COLOR8, .7)
    fade_led(70, COLOR4, .7)
    fade_led(11, COLOR5, .7)
    off_led(58, .7)
    off_led(5, .7)
    off_led(69, .7)
    off_led(51, .7)
    time.sleep(0)
    fade_led(48, COLOR9, .7)
    fade_led(74, COLOR2, .7)
    fade_led(44, COLOR5, .7)
    fade_led(18, COLOR1, .7)
    off_led(12, .7)
    off_led(45, .7)
    off_led(77, .7)
    off_led(43, .7)
    time.sleep(0)
    fade_led(41, COLOR7, .7)
    fade_led(22, COLOR5, .7)
    fade_led(37, COLOR4, .7)
    fade_led(87, COLOR2, .7)
    off_led(21, .7)
    off_led(38, .7)
    off_led(85, .7)
    off_led(33, .7)
    time.sleep(0)

    fade_led(62, COLOR3, .7)
    fade_led(57, COLOR8, .7)
    fade_led(8, COLOR2, .7)
    fade_led(49, COLOR9, .7)
    off_led(2, .7)
    off_led(55, .7)
    off_led(70, .7)
    off_led(11, .7)
    time.sleep(0)
    fade_led(75, COLOR5, .7)
    fade_led(42, COLOR2, .7)
    fade_led(19, COLOR6, .7)
    fade_led(40, COLOR4, .7)
    off_led(48, .7)
    off_led(74, .7)
    off_led(44, .7)
    off_led(18, .7)
    time.sleep(0)
    fade_led(23, COLOR9, .7)
    fade_led(35, COLOR4, .7)
    fade_led(86, COLOR1, .7)
    fade_led(32, COLOR3, .7)
    off_led(41, .7)
    off_led(22, .7)
    off_led(37, .7)
    off_led(87, .7)
    time.sleep(0)
