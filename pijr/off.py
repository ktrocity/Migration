import time
import board
import adafruit_dotstar as dotstar

# Define the number of LEDs
num_pixels = 90

# Create a DotStar instance
dots = dotstar.DotStar(board.SCK, board.MOSI, num_pixels, brightness=0.5)

# Turn off all LEDs initially
dots.fill((0, 0, 0))

