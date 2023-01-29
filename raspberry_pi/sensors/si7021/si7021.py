import board
import adafruit_si7021
sensor = adafruit_si7021.SI7021(board.I2C())

print('Temperature: {} degrees C'.format(sensor.temperature))
print('Humidity: {}%'.format(sensor.relative_humidity))

