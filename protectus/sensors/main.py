import time

# Import the ADS1x15 module.
import Adafruit_ADS1x15


# Create an ADS1115 ADC (16-bit) instance.
adc = Adafruit_ADS1x15.ADS1115(address=0x49)
adc2 = Adafruit_ADS1x15.ADS1115(address=0x48)


# Choose a gain of 1 for reading voltages from 0 to 4.09V.
# Or pick a different gain to change the range of voltages that are read:
#  - 2/3 = +/-6.144V
#  -   1 = +/-4.096V
#  -   2 = +/-2.048V
#  -   4 = +/-1.024V
#  -   8 = +/-0.512V
#  -  16 = +/-0.256V
# See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.
GAIN = 1

print('Reading ADS1x15 values, press Ctrl-C to quit...')
# Print nice channel column headers.
print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} | {4:>6} | {5:>6} | {6:>6} | {7:>6} |'.format(*range(8)))
print('-' * 37 * 2)
# Main loop.
while True:
    # Read all the ADC channel values in a list.
    values = [0]*8

    for i in range(8):
        # Read the specified ADC channel using the previously set gain value.
        if i < 4:
            values[i] = adc.read_adc(i, gain=GAIN)
        else:
            values[i] = adc2.read_adc(i-4, gain=GAIN)

    # TODO: divide each channel and print its name accordingly
    # TODO: place each channel in separate function
    # TODO: run mic input on speaker

        # Note you can also pass in an optional data_rate parameter that controls
        # the ADC conversion time (in samples/second). Each chip has a different
        # set of allowed data rate values, see datasheet Table 9 config register
        # DR bit values.
        #values[i] = adc.read_adc(i, gain=GAIN, data_rate=128)

    # Print the ADC values.
    print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} | {4:>6} | {5:>6} | {6:>6} | {7:>6} |'.format(*values))
    # print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*values2))



    # Pause for half a second.
    time.sleep(0.5)



