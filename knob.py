import time
from machine import Pin

class Knob:
    def __init__(self, button_pin, a_pin, b_pin, min=0, max=9999):
        self.button = Pin(button_pin, Pin.IN, Pin.PULL_DOWN)
        self.a = Pin(a_pin, Pin.IN, Pin.PULL_DOWN)
        self.b = Pin(b_pin, Pin.IN, Pin.PULL_DOWN)

        self.count = 0
        self.last_change = None

        self.a_val = self.a.value()
        self.b_val = self.b.value()

        self.min = min
        self.max = max

        self.button_state = self.button.value()

    def get(self): return self.count, self.button_state
    
    def poll(self):
            new_a = self.a.value()
            new_b = self.b.value()
            if self.a_val != new_a:
                self.a_val = new_a
                #print("A:", a_val)
                if self.a_val == 0:
                    self.process_change("a")
                else:
                    self.process_change(None)
            if self.b_val != new_b:
                self.b_val = new_b
                #print("B:", b_val)
                if self.b_val == 0:
                    self.process_change("b")
            
            self.button_state = self.button.value()
            

    
    def process_change(self, letter):
        if letter == None:
            self.last_change = None
            return
        if letter == self.last_change:
            self.last_change = None
            return
        
        if not self.last_change:
            self.last_change = letter
        elif self.last_change == "a":
            self.count += 1
            self.last_change = None
        else:
            self.count -= 1
            self.last_change = None
        
        if self.count < self.min:
            self.count = self.min

        if self.count > self.max:
            self.count = self.max