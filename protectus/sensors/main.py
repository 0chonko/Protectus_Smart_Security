import time
import sys
sys.path.append(".")
from GetSensorData import getSensorData

GAIN = 1
dataRate = 250

sensorData = getSensorData(val = 0)

while True:

    # sensorData.read_gas_sensor_one(GAIN,dataRate)
    # time.sleep(0.05)

    # sensorData.read_gas_sensor_two(GAIN,dataRate)
    # time.sleep(0.05)
    #
    sensorData.read_motion_sensor_one(GAIN, dataRate)
    time.sleep(0.05)
    #
    # sensorData.read_motion_sensor_two(GAIN, dataRate)
    # time.sleep(0.05)
    #
    # sensorData.read_microphone_sensor_one(2/3, dataRate)
    # time.sleep(0.05)
    #
    # sensorData.read_microphone_sensor_two(GAIN, dataRate)
    # time.sleep(0.05)
    #
    # sensorData.read_sensor_bell(GAIN, dataRate)
    # time.sleep(0.05)
    #
    # sensorData.read_sensor_8(GAIN, dataRate)
    # time.sleep(0.05)


