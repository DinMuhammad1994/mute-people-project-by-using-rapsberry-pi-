#! /usr/bin/env python

# Simple string program. Writes and updates strings.
# Demo program for the I2C 16x2 Display from Ryanteck.uk
# Created by Matthew Timmons-Brown for The Raspberry Pi Guy YouTube channel

# Import necessary libraries for communication and display use
import drivers
import os
from time import sleep
import time
import sys
# Import the ADS1x15 module.
import Adafruit_ADS1x15


# Create an ADS1115 ADC (16-bit) instance.
adc = Adafruit_ADS1x15.ADS1115()

# Choose a gain of 1 for reading voltages from 0 to 4.09V.
# Or pick a different gain to change the range of voltages that are read:
#  - 2/3 = +/-6.144V
#  -   1 = +/-4.096V
#  -   2 = +/-2.048V
#  -   4 = +/-1.024V
#  -   8 = +/-0.512V
#  -  16 = +/-0.256V
# See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.
GAIN = 1
# Load the driver and set it to "display"
# If you use something from the driver library use the "display." prefix first
display = drivers.Lcd()


print('Reading ADS1x15 values, press Ctrl-C to quit...')
# Print nice channel column headers.
#print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*range(4)))
#print('-' * 37)


# Main body of code
try:
    while True:
        values = [0]*4
        for i in range(4):
            values[i] = adc.read_adc(i, gain=GAIN)
        # Remember that your sentences can only be 16 characters long!
        #print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*values))
        print("values[0]", values[0]) 
        print("values[1]", values[1])
        print("values[2]", values[2])
        print("values[3]", values[3]) 
        # Pause for half a second.
        time.sleep(0.5)
        if (values[0] > 31000):
            print("Message 1")
            display.lcd_display_string("Message 1", 1)  # Write line of text to first line of display
            display.lcd_display_string("Hello! How are you.", 2)  # Write line of text to second line of display
            sleep(3) 
            os.system('omxplayer -o local Hellohowareyou.ogg')
            print ("hello how are you ")
            sleep(3)                                           # Give time for the message to be read
            display.lcd_clear()                                # Clear the display of any data
        elif (values[0] > 40000):
            print("Message 2")
            display.lcd_display_string("Message 2", 1)  # Write line of text to first line of display
            display.lcd_display_string("I am good.", 2)  # Write line of text to second line of display
            sleep(3)                                           # Give time for the message to be read
            os.system('omxplayer -o local Good.ogg')
            print ("i am good")
            time.sleep(3)
            display.lcd_clear()
        else:
            print("value 0 is ok")

        if (values[1] > 31000):    
            print("Message 3")
            display.lcd_display_string("Message 3", 1)  # Write line of text to first line of display
            display.lcd_display_string("I am hungry now.", 2)  # Write line of text to second line of display
            sleep(3)                                           # Give time for the message to be read
            os.system('omxplayer -o local iamhungrynow.ogg')
            print ("i am hungry now")
            time.sleep(3)
            display.lcd_clear()
        elif (values[1] > 40000):
            print("Message 4")
            display.lcd_display_string("Message 4", 1)  # Write line of text to first line of display
            display.lcd_display_string("i want go to", 2)  # Write line of text to second line of display
            display.lcd_display_string("washroom", 3)  # Write line of text to second line of display
            sleep(3)                                           # Give time for the message to be read
            os.system('omxplayer -o local wanttogowashroom.ogg')
            print ("i want to go washroom")
            time.sleep(3)
            display.lcd_clear()
        else :
            print ("value 1 is ok ")



        if (values[2] > 61000):    
            print("Message 5")
            display.lcd_display_string("Message 5", 1)  # Write line of text to first line of display
            display.lcd_display_string("please switch on", 2)  # Write line of text to second line of display
            display.lcd_display_string("the light", 3)  # Write line of text to second line of display
            sleep(2)                                           # Give time for the message to be read
            os.system('omxplayer -o local plzswitchonlight.ogg')
            print ("plz switch on light")
            time.sleep(5)

            display.lcd_clear()
        elif (values[2] > 40000):
            print("Message 6")
            display.lcd_display_string("Message 6", 1)  # Write line of text to first line of display
            display.lcd_display_string("please switch on ", 2)  # Write line of text to second line of display
            display.lcd_display_string("the fan", 3)  # Write line of text to second line of display
            sleep(3)                                           # Give time for the message to be read
            os.system('omxplayer -o local Plzswitchonfan.ogg')
            print ("Plz switch on fan")
            time.sleep(3)
            display.lcd_clear()
        else :
            print ("value 2 is ok ")



        if (values[3] > 61000):    
            print("Message 7")
            display.lcd_display_string("Message 7", 1)  # Write line of text to first line of display
            display.lcd_display_string("i am thirsty.", 2)  # Write line of text to second line of display
            sleep(2)                                           # Give time for the message to be read
            os.system('omxplayer -o local iamthirsty.ogg')
            print ("i am thirsty")
            time.sleep(3)
            display.lcd_clear()
        elif (values[3] > 40000):
            print("Message 8")
            display.lcd_clear()
            display.lcd_display_string("Message 8", 1)  # Write line of text to first line of display
            display.lcd_display_string("i need a doctor.", 2)  # Write line of text to second line of display
            sleep(3)                                           # Give time for the message to be read
            os.system('omxplayer -o local ineeddoctor.ogg')
            print ("i need doctor")
            time.sleep(3)
            display.lcd_clear()
        else :
            print ("value 3 is ok ")


        
        
except KeyboardInterrupt:
    # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
    display.lcd_clear()







