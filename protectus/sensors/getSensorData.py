import time
# Import the ADS1x15 module.
import Adafruit_ADS1x15

# Create an ADS1115 ADC (16-bit) instance.
adc = Adafruit_ADS1x15.ADS1115(address=0x49)
adc2 = Adafruit_ADS1x15.ADS1115(address=0x48)

class getSensorData(object):

    def __init__(self,val):
        self.val = 0
        print('sensor data readings init')

# Choose a gain of 1 for reading voltages from 0 to 4.09V.
# Or pick a different gain to change the range of voltages that are read:
#  - 2/3 = +/-6.144V
#  -   1 = +/-4.096V
#  -   2 = +/-2.048V
#  -   4 = +/-1.024V
#  -   8 = +/-0.512V
#  -  16 = +/-0.256V
# See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.

    #the following function get as input the gain value with wich the sensor data will be amplified, and the rate of trasmission
    #of the data.
    def read_gas_sensor_one(self, gain, dataRate):
        value = adc2.read_adc(0,gain=gain) / 10000
        print('gas measurement on sensor one: ' + str(value))
        #allert trigger
        if value > 0.5:
            print ('alert gas sensor one')
        return value

    def read_gas_sensor_two(self, gain, dataRate):
        value = adc2.read_adc(1, gain=gain) * 3.7 / 10000
        print('gas measurement on sensor two: ' + str(value))
        # allert trigger
        if value > 0.6:
            print('alert gas sensor two')

    def read_motion_sensor_one(self, gain, dataRate):
        value = adc2.read_adc(2, gain=gain)
        print('motion measurement on sensor one: ' + str(value))
        # allert trigger
        if value == 0:
            print ("motion detected on sensor one")


    def read_motion_sensor_two(self, gain, dataRate):
        value = adc2.read_adc(3, gain=gain)
        print('motion measurement on sensor two: ' + str(value))
        # allert trigger
        if value == 0:
            print ("motion detected on sensor two")

    def read_microphone_sensor_one(self, gain, dataRate):
        value = adc.read_adc(0, gain=gain)
        print('sound measurement on sensor one: ' + str(value))

    def read_microphone_sensor_two(self, gain, dataRate):
        value = adc.read_adc(1, gain=gain)
        print('sound measurement on sensor two: ' + str(value))

    def read_sensor_bell(self, gain, dataRate):
        value = adc.read_adc(2, gain=gain)
        print('extra measurement on sensor one: ' + str(value))
        # allert trigger
        if value < 500:
            print("someone is at the door")

    def read_sensor_8(self, gain, dataRate):
        value = adc.read_adc(3, gain=gain)
        print('extra measurement on sensor two: ' + str(value))



