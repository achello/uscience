from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.clear()

temp = sense.get_temperature()
hum = sense.get_humidity()
press = sense.get_pressure()

while True:
	sleep(3)
	print(temp)
	print(hum)
	print(press)
