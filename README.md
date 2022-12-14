# PicoPong
Pong-typ game using a Raspberry Pi Pico and a SSD1306 OLED Screen

![IMG_6264](https://user-images.githubusercontent.com/11849451/181356213-cd1c9c82-63ec-49a1-8e19-0651a4f1ef39.jpeg)


## Overview
This is a 2-player Pong-type game forRaspberry Pi Pico, using an I2C OLED Screen for output and two Potentiometers as controllers.

It helps you learn the basics on how to output graphics and text to an OLED as well as how to control the Raspberry Pi Pico using the DAC (Digital to Analog Converter) as well as digital input through a push button.

Everything is easy to wire up on a bread board, and it can be powered using 2 AA batteries.

## Hardware Components
Everything I used, except for the OLED Screen, I took from my "Freenova Super Starter Kit with Pico", but they are all readily available to buy.

1x Raspberry Pi Pico  
1x Push button  
1x 128x64 I2C SSD1306 OLED Screen  
1x 10k Resistor  
2x 10K Potentiometer  
Jumper Cables  

### Optional Components
1x Bread Board  
1x AA Battery Holder  

For sound:  
1x Active Buzzer  
1x NPN Transistor (S8050 or similar)
1x 1k Resistor

## How to wire everything up.

### SSD1306 OLED Screen

GND -> GND  
VOC -> 3V3  
SCL -> Pin 1  
SDA -> Pin 0  

### Potentiometer Player 1 (Left Player)

VCC (Pin 1) -> 3V3  
Output (Pin 2) -> Pin 27  
GND (Pin3) -> GND  

### Potentiometer Player 2 (Right Player)

VCC (Pin 1) -> 3V3  
Output (Pin 2) -> Pin 26  
GND (Pin3) -> GND  

### Push Button

Pin 1 -> 3V3  
Pin 2 -> Pin 22 + GND via 10k Resistor (pull down)   

### Battery
Plus -> Vbus  
Minus -> GND  

### Buzzer
Plus -> Vbus  
Minus -  Collector of S8050  

S8050 Base -> Pin 15 via 1k Resistor  
S8080 Emitter -> GND  

## Software Requirements
You need the micropython-ssd1306 OLED driver in order to run the code.

You can install it through Thonny (Tools / Manage Packages...)


