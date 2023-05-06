
import ssd1306
import scd4x
from ws2812 import WS2812
import time
import utime
from machine import Pin, SoftI2C

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)

i2c = SoftI2C(scl=Pin(7), sda=Pin(6), freq=100000)

led = WS2812(12,1)

# setup the I2C communication
display = ssd1306.SSD1306_I2C(128, 64, i2c)

scd4x = scd4x.SCD4X(i2c)
scd4x.start_periodic_measurement()

while True:
    
    display.fill(0)
    
    co2_ppm = 0 if scd4x.co2 is None else scd4x.co2
    temp_deg = 0 if scd4x.temperature is None else scd4x.temperature
    humidity_percent = 0 if scd4x.relative_humidity is None else scd4x.relative_humidity
    
    display.text('CO2:'+str(co2_ppm), 0, 0)
    display.text('Temperature:'+str(temp_deg), 0, 16)
    display.text('Humidity:'+str(humidity_percent)+'%', 0, 32)
    display.show()
    
    if (int(co2_ppm) < 1000):
        led.pixels_fill(GREEN)
    elif (int(co2_ppm) < 1500):
        led.pixels_fill(YELLOW)
    else:
        led.pixels_fill(RED)
        
    led.pixels_show()
    time.sleep(1)