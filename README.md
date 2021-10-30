# pi_br2_weather_station

## Intro

I have an old Lacrosse WS7000 weather station, where over time, each component has ceased to function.  I also have an old Raspberry Pi 2B Rev 2, so a weather station in the making.

Looking at the internal workings of the components
* The anemometer just has a magnet, and a reed switch that activates every turn.
* The wind vane looks to be a 360 degree 50K variable resister, though it's not in good condition
* The rain gauge is another magnet and reed switch, with a tipping bucket. The reed is either on or off (unlike the other WS-2300 rain gauge I have, where the reed is on momentarily, as the tipping bucket passes the mid point)
* The barometer sensor has failed, but the temperature and humidity sensors still work. I will use a BMP180 pressure and temperature sensor

The Pi B Rev 2 has pinout (output from the pinout command line tool)
```
+------------------| |--| |------+
| ooooooooooooo P1 |C|  |A|      |
| 1oooooooooooo    +-+  +-+      |
|    1ooo                        |
| P5 oooo        +---+          +====
|                |SoC|          | USB
|   |D| Pi Model +---+          +====
|   |S| B  V2.0                  |
|   |I|                  |C|+======
|                        |S||   Net
|                        |I|+======
=pwr             |HDMI|          |
+----------------|    |----------+

P1:
             3V3  (1) (2)  5V    
 GPIO2 (SDA0 I2C) (3) (4)  5V    
 GPIO3 (SCL0 I2C) (5) (6)  GND   
           GPIO4  (7) (8)  GPIO14 (TX UART)
             GND  (9) (10) GPIO15 (RX UART)
          GPIO17 (11) (12) GPIO18
          GPIO27 (13) (14) GND   
          GPIO22 (15) (16) GPIO23
             3V3 (17) (18) GPIO24
          GPIO10 (19) (20) GND   
           GPIO9 (21) (22) GPIO25
          GPIO11 (23) (24) GPIO8
             GND (25) (26) GPIO7

P5:
               5V (1) (2) 3V3   
           GPIO28 (3) (4) GPIO29
           GPIO30 (5) (6) GPIO31
              GND (7) (8) GND   

```
