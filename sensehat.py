import sys
import time
import random
import datetime
import telepot
from sense_hat import SenseHat
from time import sleep

sense= SenseHat()
sense.clear()

temp = sense.get_temperature()
hum = sense.get_humidity()
press = sense.get_pressure()

def handle(msg):
	chat_id = msg['chat']['id']
	command = msg['text']
#print 'Got command: %s ' % command
	if command == 'blah':
		bot.sendMessage(chat_id="515182637", text=(temp))

bot = telepot.Bot("5695185577:AAHXQyWyDCZOsEa32ZKkLInArFSjhx65LaM")
bot.message_loop(handle)

while 1:
	time.sleep(10)

