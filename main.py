import eel
import pyowm
import time
import os


eel.init('web')

eel.start('main.html', size=(400, 400))



nowisday = time.strftime("%B", time.localtime())