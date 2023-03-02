#!/usr/bin/env python3
from sensor import IRSeeker360

from ev3dev2.sensor import INPUT_1

# Change '1' to whatever port you are using

sensor = IRSeeker360(1)
# or you can do this
sensor = IRSeeker360(INPUT_1)

while True:
    # This will return a ball angle (0 to 12) and strength
    angle, strength = sensor.read()
  
    print("Angle:", angle)
    print("Strength:", strength) # The higher the value, the closer it is
  
# You should practice closing the sensor after use
sensor.close()
