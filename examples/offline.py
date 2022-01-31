from machine import Pin, I2C, ADC
from time import sleep
from tcs34725 import TCS34725
from ssd1306 import SSD1306_I2C

# using default address 0x3C
i2c_bus = I2C(sda=Pin(4), scl=Pin(5))
display = SSD1306_I2C(128, 32, i2c_bus)
tcs = TCS34725(i2c_bus)

def flash_screen():
    display = SSD1306_I2C(128, 32, i2c_bus)
    for i in range(0,5):
        display.fill(1)
        display.show()
        display.fill(0)
        display.show()

while True:
  x = tcs.read('lux')[0] 
  sleep(.01)
  if tcs.read('lux')[0]  > x:
    flash_screen()
