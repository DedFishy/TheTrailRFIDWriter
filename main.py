import displaythread
from knob import Knob
import rfid
import byteutil

try:
    knob = Knob(14, 20, 21)

    displaythread.is_loading = True
    displaythread.create_display_thread()

    current_data = sum(rfid.read_raw())

    knob.count = current_data

    displaythread.is_loading = False

    while True:
        knob.poll()
        count, button = knob.get()

        displaythread.display_value = count

        if button:
            break
    
    displaythread.is_loading = True
    rfid.write_raw(byteutil.int_to_bytes(knob.count))
finally:
    displaythread.display_value = "----"
    displaythread.is_running = False



'''write_raw(byteutil.int_to_bytes(521))
    data = read_raw()
    print(sum(data))'''