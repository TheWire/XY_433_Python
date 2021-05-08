from time import sleep
from gpiozero import OutputDevice
from threading import Thread

class XY_433_trans:

    PULSE =  0.00035


    def __init__(self, pin=2):
        self._pin = pin
        try:
            self.transPin = OutputDevice(self._pin)
        except GPIOZeroError:
            print("gpio zero error on setup")

    def XY_send(self, code, bits, repeat = 3):
        for r in range(0, repeat):
            mask = 0x1
            mask = mask << (bits - 1)
            for i in range(0, bits):
                if (code & mask) > 0:
                    try:
                        self.transPin.on()
                        sleep(self.PULSE * 3)
                        self.transPin.off()
                        sleep(self.PULSE * 1)
                    except GPIOZeroError:
                        print("gpio zero error on trans pin")
                else:
                    try:
                        self.transPin.on()
                        sleep(self.PULSE * 1)
                        self.transPin.off()
                        sleep(self.PULSE * 3)
                    except GPIOZeroError:
                        print("GPIO error on trans pin")
                mask = mask >> 1
            try:
                self.transPin.on()
                sleep(self.PULSE * 1)
                self.transPin.off()
                sleep(self.PULSE * 31)
            except GPIOZeroError:
                print("gpio zero error on trans pin")
    
    def close(self):
        self.transPin.close()

    @property    
    def pin(self):
        return self.pin
