# Pico W Hardware Reset with Transistor
How to trigger a hardware level reset of a Raspberry Pico W from within software with the help of a transistor.

**hw_transistor_reset.py** in this repo shows you how you can trigger a hardware level reset from witin software by using a transistor that has its three pins (known as Emitter, Base and Collector) connected as follows:

1. Emitter to GND
2. Base to GP20 (or a different GPIO pin if you prefer)
3. Collector to RUN

![Transistor](https://github.com/ashleycawley/Pico_W_Hardware_Reset_with_Transistor/blob/main/transistor.png?raw=true)

The code to then reset could at its simplest form be reduced to just three lines:

```
from machine import Pin
pin_reset = Pin(20, mode=Pin.OUT)
pin_reset.value(1)
```
But the MicroPython script in this repo gives a better example of how it might be implemented within a script, it has an example workload; blinking the onboard LED, some sleeps and explinations along the way.

I hope you find this useful, feel free to get in touch to say hi [@ashleycawley](https://twitter.com/ashleycawley)
