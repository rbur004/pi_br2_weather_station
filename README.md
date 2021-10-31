# pi_br2_weather_station

## Intro

I have an old Lacrosse WS7000 weather station, where over time, each component has ceased to function.  I also have an old Raspberry Pi 2B Rev 2, so a weather station in the making.

Looking at the internal workings of the components
* The anemometer just has a magnet, and a reed switch that activates every turn.
* The wind vane looks to be a 360 degree 50K variable resister, though it's not in good condition
* The rain gauge is another magnet and reed switch, with a tipping bucket. The reed is either on or off (unlike the other WS-2300 rain gauge I have, where the reed is on momentarily, as the tipping bucket passes the mid point)
* The barometer sensor has failed, but the temperature and humidity sensors still work, but are 433MHz wireless. I will use a BMP180.

## Requirements
```
pip3 install RPi.bme280
pip install rpi.gpio
```
