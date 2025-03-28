import gpiozero
import time
import threading

# Initialize LEDs
led1 = gpiozero.PWMLED(14)
led2 = gpiozero.PWMLED(15)
led3 = gpiozero.PWMLED(16)
led4 = gpiozero.PWMLED(24)
led5 = gpiozero.PWMLED(21)
led6 = gpiozero.PWMLED(18)
led7 = gpiozero.PWMLED(12)
led8 = gpiozero.PWMLED(7)


def fade_led(led, start_delay):
    # Wait for the specified start delay
    time.sleep(start_delay)

    while True:
        # Gradually increase brightness
        for brightness in range(101):
            led.value = brightness / 100
            time.sleep(0.1)  # 3-second fade-in

        time.sleep(2)

        # Gradually decrease brightness
        for brightness in range(100, -1, -1):
            led.value = brightness / 100
            time.sleep(0.1)  # 3-second fade-out

        time.sleep(10)

try:
    threading.Thread(target=fade_led, args=(led1, 0)).start()
    threading.Thread(target=fade_led, args=(led2, 2)).start()
    threading.Thread(target=fade_led, args=(led3, 4)).start()
    threading.Thread(target=fade_led, args=(led4, 6)).start()
    threading.Thread(target=fade_led, args=(led5, 8)).start()
    threading.Thread(target=fade_led, args=(led6, 10)).start()
    threading.Thread(target=fade_led, args=(led7, 12)).start()
    threading.Thread(target=fade_led, args=(led8, 14)).start()
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    led1.off()
    led2.off()
    led3.off()
    led4.off()
    led5.off()
    led6.off()
    led7.off()
    led8.off()
    print("Cleanup done. Exiting...")
