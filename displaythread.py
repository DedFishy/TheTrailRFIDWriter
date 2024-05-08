from machine import Pin, I2C
from hybotics_ht16k33.segments import Seg7x4
from time import sleep
import _thread

SDA_PIN = Pin(26)
SCL_PIN = Pin(27)

i2c = I2C(id=1, scl=SCL_PIN, sda=SDA_PIN, freq=400000)

print("Waiting for I2C initialization...")
sleep(1)
display = Seg7x4(i2c, 0x70, True)

display_value = 0

load_anim_i = 0
load_anim_dir = 1
is_loading = True

is_running = True

def update_display():
    global load_anim_i, load_anim_dir
    while is_running:
        if not is_loading:
            print("Writing: " + str(display_value))
            display.print(display_value)
            sleep(0.1)
            display.fill(0)
        else:
            load_anim_i += load_anim_dir
            if load_anim_i == 3:
                load_anim_dir = -1
            elif load_anim_i == 0:
                load_anim_dir = 1
            for i in range(0, 4):
                if i == load_anim_i:
                    display[i] = "-"
                else:
                    display[i] = " "
            sleep(0.2)

def create_display_thread(): return _thread.start_new_thread(update_display, ())
