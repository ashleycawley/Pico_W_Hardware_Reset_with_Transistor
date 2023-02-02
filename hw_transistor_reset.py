from machine import Pin
import time

# This is script shows you how you can trigger a hardware level reset from witin software
# by using a transistor that has its three pins (known as Emitter, Base and Collector)
# connected as follows: | Emitter-->GND | Base-->GP20 | Collector-->RUN |
# I hope you find this useful, feel free to get in touch @ashleycawley on Twitter <3

# Defining Pins
pin_reset = Pin(20, mode=Pin.OUT) # Defining GP20 (Physical Pin 26) as pin_reset to control Transistor
led_onboard = machine.Pin(25, machine.Pin.OUT) # Defining internal LED just for visuals to check everything is working

print('Starting Script - In five seconds I will start blinking my onboard LED...')
time.sleep(5)

print('Just blinking the onboard LED for a few seconds...')
i = 0
while i < 25:
    led_onboard.value(1)
    time.sleep(0.1)
    led_onboard.value(0)
    time.sleep(0.1)
    i += 1

print('Sleeping for a few seconds before reset')
time.sleep(2)

print('Resetting Pico by activating transistor pins...')
time.sleep(2) # If this wasn't here you wouldn't see the print on the line above because it resets too quick to process the output
pin_reset.value(1) # This sets GP20 high which activates the transistor, setting the RUN pin high and resetting the Pico
