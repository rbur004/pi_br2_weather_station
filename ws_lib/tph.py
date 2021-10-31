# Temperature Pressure Humidity
import bme280  # For the sensor
import smbus2  # For the I2C bus, to communicate with the sensor


class BME280:
  '''
    Barometer, Temperature and Humidity Sensor calls
  '''
  I2C_PORT = 1
  I2C_DEVICE_ADDRESS = 0x77

  def __init__(self, port=I2C_PORT, address=I2C_DEVICE_ADDRESS):
    '''
      Set up BME280 Connection

      port:     I2C port on the PI (2 on the Pi B Rev 2, one on P1 and one on P5)
      address:  I2C device address
    '''
    self.address = address
    self.bus = smbus2.SMBus(port)
    bme280.load_calibration_params(bus, address)

  def sample():
    '''
      fetch the current reading from the sensor
    '''
    bme280_data = bme280.sample(self.bus, self.address)
    self.humidity = bme280_data.humidity
    self.pressure = bme280_data.pressure
    self.temperature = bme280_data.temperature
