from machine import Pin, SoftI2C

i2c = SoftI2C(scl=Pin(7), sda=Pin(6), freq=100000)
devices = i2c.scan()
for device in devices:  
    print("Decimal address: ",device," | Hexa address: ",hex(device))
