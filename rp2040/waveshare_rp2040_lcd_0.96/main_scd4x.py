#
# https://github.com/andypiper/mpy-rp2040-lcd
#
import LCD_0inch96
import time
import scd4x
from machine import Pin, SoftI2C

#color is BGR
RED = 0x00F8
GREEN = 0xE007
BLUE = 0x1F00
WHITE = 0xFFFF
BLACK = 0x0000

i2c = SoftI2C(scl=Pin(17), sda=Pin(16), freq=100000)

scd4x = scd4x.SCD4X(i2c)
scd4x.start_periodic_measurement()

lcd = LCD_0inch96.LCD_0inch96()   

while True:
    
    lcd.fill(BLACK) 
    
    co2_ppm = 0 if scd4x.co2 is None else scd4x.co2
    temp_deg = 0 if scd4x.temperature is None else scd4x.temperature
    humidity_percent = 0 if scd4x.relative_humidity is None else scd4x.relative_humidity
    
    lcd.hline(10,10,140,BLUE)
    lcd.hline(10,70,140,BLUE)
    lcd.vline(10,10,60,BLUE)
    lcd.vline(150,10,60,BLUE)

    lcd.hline(0,0,160,BLUE)
    lcd.hline(0,79,160,BLUE)
    lcd.vline(0,0,80,BLUE)
    lcd.vline(159,0,80,BLUE)
    
    lcd.text('CO2:'+str(co2_ppm),20,15,RED)
    lcd.text('Temperature:'+str(temp_deg),20,35,GREEN)    
    lcd.text('Humidity:'+str(humidity_percent)+'%',20,55,WHITE)
    
    lcd.display()

    time.sleep(1)