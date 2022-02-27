import esp
import gc
import machine
from machine import Pin, I2C, ADC
from tcs34725 import TCS34725
from ssd1306 import SSD1306_I2C
machine.freq(160000000)
i2c_bus = I2C(sda=Pin(4), scl=Pin(5))
display = SSD1306_I2C(128, 16, i2c_bus)
tcs = TCS34725(i2c_bus)

def flash_screen(winner):
    i2c_bus = I2C(sda=Pin(4), scl=Pin(5))
    display = SSD1306_I2C(128, 16, i2c_bus)
    for i in range(0,5):
        display.fill(1)
        display.text(winner,64,0,0)
        display.show()
        display.fill(0)
        display.text(winner,64,0,1)
        display.show()

def avg_round(numbs):
  return round(sum(numbs)/len(numbs))

while True:
  red0 = tcs.read('lux')[0] 
  grn0 = tcs.read('lux')[1] 
  red1 = tcs.read('lux')[0]
  grn1 = tcs.read('lux')[1] 
  red2 = tcs.read('lux')[0]
  grn2 = tcs.read('lux')[1] 
  red3 = tcs.read('lux')[0]
  grn3 = tcs.read('lux')[1] 
  ts = time.time_ns()
  grn_avg = avg_round([grn0,grn1,grn2,grn3])
  red_avg = avg_round([red0,red1,red2,red3])
  str_grn_avg = avg_round([grn0,grn1])
  end_grn_avg = avg_round([grn2,grn3])
  str_red_avg = avg_round([red0,red1])
  end_red_avg = avg_round([red2,red3])
  red_total = sum([red0,red1,red2,red3])
  grn_total =  sum([grn0,grn1,grn2,grn3])
  shot_data ={
    "ts":ts,
    "red_total":red_total,
    "grn_total":grn_total,
    "grn_avg":grn_avg,
    "red_avg":red_avg,
    "str_grn_avg":str_grn_avg,
    "end_grn_avg":end_grn_avg,
    "str_red_avg":str_red_avg,
    "end_red_avg":end_red_avg,
    "grn":[grn0,grn1,grn2,grn3],
    "red":[red0,red1,red2,red3],
    "red_sub_grn_avg":red_avg-grn_avg  
  }
  if end_red_avg > str_red_avg or end_grn_avg > str_grn_avg:
    if (red_avg - grn_avg)>1:
      print("WIN RED ",shot_data)
      flash_screen("RED")
    elif (grn_avg - red_avg)>1:
      print("WIN GREEN ",shot_data)
      flash_screen("GREEN")
  gc.collect()
    
