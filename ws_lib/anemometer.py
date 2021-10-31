# Wind Speed
from gpiozero import Button

class WindSpeed:
  '''
  Process anemometer clicks (one per rotation)
  How do we deal with wind gusts?
  Locking?
  '''
  ANEMOMETER_BUTTON = 23 # GPIO number (physical pin 16)
  MPS = 0.0069638637154573755 # Convert RPM to m/s (Radius 66.5mm). Need to test


  def __init__(self, button=ANEMOMETER_BUTTON ):
    '''
    Set up interrupts to count rotations
    '''

    self.wind_speed_sensor = Button(button)
    self.wind_count = 0
    self.wind_speed_sensor.when_pressed = self.spin

  def spin():
    '''
    Button push interrupts call this counter
    Locking?
    '''
    global self.wind_count
    self.wind_count = self.wind_count + 1

  def read_and_reset():
    '''
    Return the wind_cound, and reset it 0
    Locking?
    '''
    wind_count = self.wind_count
    self.wind_count = 0
    return wind_count * MPS
