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
   GPIO2 (I2C1SDA0) (3) (4)  5V    
   GPIO3 (I2C1SCL0) (5) (6)  GND   
    GPIO4 (GP CLK0) (7) (8)  GPIO14 (UART0 TX)
               GND  (9) (10) GPIO15 (UART0 RX)
            GPIO17 (11) (12) GPIO18 (PWM0/Audio)
  GPIO27 (ARM TMS) (13) (14) GND   
            GPIO22 (15) (16) GPIO23
               3V3 (17) (18) GPIO24
 GPIO10 (SPI MOSI) (19) (20) GND   
  GPIO9 (SPI MISO) (21) (22) GPIO25
 GPIO11 (SPI SCLK) (23) (24) GPIO8 (SPI CS0)
               GND (25) (26) GPIO7 (SPI CS1)

P5: (beside P1, with no head pins)
              3V3  (2) (1) 5V   
 GPIO29 (I2C0 SCL) (4) (3) GPIO28 (I2C0 SDA)
            GPIO31 (6) (5) GPIO30
               GND (8) (7) GND   

```
