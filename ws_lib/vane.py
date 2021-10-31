# Wind Vane
from gpiozero import MCP3008

pot = MCP3008(channel=0)

class Vane:
  '''
    Weather Vane direction, over time
  '''
  SPI_PORT = 0            # Just the one SPI port on a Pi 1B Rev 2
  SPI_DEVICE_ADDRESS = 0  # (Pin 24. Pi can select 2 SPI slaves, using GPIO 7 and 8
  ANALOGUE_PORT = 0       # MCP3008 has 8 analogue ports we could sample from

  def __init__(self, port=SPI_PORT, address=SPI_DEVICE_ADDRESS, channel=ANALOGUE_PORT):
    '''
      Set up MCP3008 Connection

      port:     SPI port on the PI
      address:  SPI device address
      channel:  MCP3008 Analogue port (0-7)
    '''
    self.direction = 0  # North
    self.adc = MCP3008(channel=channel, port=port, device=address)

  def sample():
    '''
      fetch the current reading from the sensor
    '''
    voltage = self.adc.value
    # self.direction = some function of voltage
