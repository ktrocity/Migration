import gpiozero
import time
import threading

# Initialize LEDs
led1 = gpiozero.PWMLED(14)
led2 = gpiozero.PWMLED(15)
led3_pin1 = gpiozero.PWMLED(21)  # First pin for CompositeLED
led3_pin2 = gpiozero.PWMLED(24)  # Second pin for CompositeLED
led4 = gpiozero.PWMLED(16)
led5 = gpiozero.PWMLED(7)

# Create a custom Composite LED to handle GPIO 21 and 24
class CompositeLED:
    def __init__(self, *leds):
        self.leds = leds

    def on(self):
        for led in self.leds:
            led.on()

    def off(self):
        for led in self.leds:
            led.off()

    def set_value(self, value):
        for led in self.leds:
            led.value = value

# Initialize Composite LED for GPIO 21 and 24
led3_composite = CompositeLED(led3_pin1, led3_pin2)

def fade_led(led, start_delay):
    # Wait for the specified start delay
    time.sleep(start_delay)

    while True:
        # Gradually increase brightness
        for brightness in range(101):
            led.set_value(brightness / 100)
            time.sleep(0.03)  # 3-second fade-in

        time.sleep(2)

        # Gradually decrease brightness
        for brightness in range(100, -1, -1):
            led.set_value(brightness / 100)
            time.sleep(0.03)  # 3-second fade-out

        time.sleep(8)

try:
    # Start the fading functions for all LEDs with appropriate delays
    threading.Thread(target=fade_led, args=(led1, 0), daemon=True).start()
    threading.Thread(target=fade_led, args=(led2, 2), daemon=True).start()
    threading.Thread(target=fade_led, args=(led3_composite, 4), daemon=True).start()  # Use Composite LED for GPIO 21 and 24
    threading.Thread(target=fade_led, args=(led4, 6), daemon=True).start()
    threading.Thread(target=fade_led, args=(led5, 8), daemon=True).start()

    # Keep the main thread alive
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    # Turn off all LEDs on keyboard interrupt
    led1.off()
    led2.off()
    led3_composite.off()
    led4.off()
    led5.off()
    print("Cleanup done. Exiting...")
