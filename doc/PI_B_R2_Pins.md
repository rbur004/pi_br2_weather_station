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
