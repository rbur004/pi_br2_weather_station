# Wind Speed
from gpiozero import Button

class RainGauge:
  '''
  Process rain gauge clicks
  How do we deal with wind gusts?
  Locking?
  '''
  RAIN_GAUGE_BUTTON = 24 # GPIO number (Physical pin 18)
  RAIN_UNIT = 0.518     # mm per button going to/from on/off (need to test this value)

  def __init__(self, button=RAIN_GAUGE_BUTTON ):
    '''
    Set up interrupts to count edge changes of rain gauge
    Our gauge flips from on to off, ever 0.518mm of rain
    '''

    self.rain_gauge_sensor = Button(button)
    self.rain_gauge_count = 0
    self.rain_gauge_sensor.when_pressed = self.flop
    self.rain_gauge_sensor.when_released = self.flop

  def flop():
    '''
    Button push interrupts call this counter
    Locking?
    '''
    global self.wind_count
    self.rain_gauge_count = self.rain_gauge_count + 1

  def read_and_reset():
    '''
    Return the wind_cound, and reset it 0
    Locking?
    '''
    rain_gauge_count = self.wind_count
    self.rain_gauge_count = 0
    return rain_gauge_count * RAIN_UNITS
