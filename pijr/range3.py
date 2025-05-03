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
COLOR4 = (177, 86, 121)
COLOR5 = (224, 171, 95)
COLOR6 = (208, 141, 22)
COLOR7 = (255, 200, 130)
COLOR8 = (124, 103, 131)
COLOR9 = (177, 86, 21)

# Initialize the DotStar strip
leds = dotstar.DotStar(board.SCK, board.MOSI, NUM_LEDS, brightness=0.75)

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
    fade_led(58, COLOR5, .71)
    fade_led(5, COLOR1, .71)
    fade_led(64, COLOR9, .71)
    off_led(48, .5)
    off_led(45, .5)
    off_led(17, .5)
    time.sleep(0)
    fade_led(53, COLOR8, .71)
    fade_led(70, COLOR3, .71)
    fade_led(50, COLOR2, .71)
    off_led(79, .5)
    off_led(41, .5)
    off_led(22, .5)
    time.sleep(0)
    fade_led(48, COLOR4, .71)
    fade_led(15, COLOR6, .71)
    fade_led(44, COLOR3, .71)
    off_led(24, .5)
    off_led(86, .5)
    off_led(34, .5)
    time.sleep(0)
    fade_led(20, COLOR7, .71)
    fade_led(83, COLOR8, .71)
    fade_led(37, COLOR4, .71)
    #start of off sequence
    off_led(58, .5)
    off_led(5, .5)
    off_led(64, .5)
    time.sleep(0)
    fade_led(33, COLOR9, .71)
    fade_led(87, COLOR2, .71)
    fade_led(31, COLOR5, .71)
    off_led(53, .5)
    off_led(70, .5)
    off_led(50, .5)
    time.sleep(0)

    fade_led(3, COLOR7, .71)
    fade_led(57, COLOR5, .71)
    fade_led(65, COLOR4, .71)
    off_led(48, .5)
    off_led(15, .5)
    off_led(44, .5)
    time.sleep(0)
    fade_led(69, COLOR3, .71)
    fade_led(52, COLOR8, .71)
    fade_led(72, COLOR2, .71)
    off_led(20, .5)
    off_led(83, .5)
    off_led(37, .5)
    time.sleep(0)
    fade_led(46, COLOR5, .71)
    fade_led(16, COLOR2, .71)
    fade_led(42, COLOR6, .71)
    off_led(33, .5)
    off_led(87, .5)
    off_led(31, .5)
    time.sleep(0)
    fade_led(81, COLOR9, .71)
    fade_led(39, COLOR4, .71)
    fade_led(23, COLOR1, .71)
    off_led(3, .5)
    off_led(57, .5)
    off_led(65, .5)
    time.sleep(0)
    fade_led(35, COLOR3, .71)
    fade_led(88, COLOR1, .71)
    fade_led(32, COLOR5, .71)
    off_led(69, .5)
    off_led(52, .5)
    off_led(72, .5)
    time.sleep(0)

    fade_led(4, COLOR3, .71)
    fade_led(56, COLOR6, .71)
    fade_led(67, COLOR2, .71)
    off_led(46, .5)
    off_led(16, .5)
    off_led(42, .5)
    time.sleep(0)
    fade_led(54, COLOR5, .71)
    fade_led(64, COLOR8, .71)
    fade_led(12, COLOR1, .71)
    off_led(81, .5)
    off_led(39, .5)
    off_led(23, .5)
    time.sleep(0)
    fade_led(48, COLOR2, .71)
    fade_led(45, COLOR7, .71)
    fade_led(17, COLOR3, .71)
    off_led(35, .5)
    off_led(88, .5)
    off_led(32, .5)
    time.sleep(0)
    fade_led(79, COLOR4, .71)
    fade_led(41, COLOR8, .71)
    fade_led(22, COLOR6, .71)
    off_led(4, .5)
    off_led(56, .5)
    off_led(67, .5)
    time.sleep(0)
    fade_led(24, COLOR1, .71)
    fade_led(86, COLOR2, .71)
    fade_led(34, COLOR5, .71)
    off_led(54, .5)
    off_led(64, .5)
    off_led(12, .5)
    time.sleep(0)
