from sense_hat import SenseHat
import time
from time import asctime

sense = SenseHat()

while True:
 message ='lab4 exam'
 sense.show_message(message,scroll_speed=(0.08),text_colour=[200,240,200], back_colour =[0,0,0])
