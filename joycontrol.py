#!/usr/bin/env python3
#gamepad wireless controller interface by Robin Newman July 2017
#converts controller inputs to OSC messages
#which can be output to Sonic Pi 3, running on the local computer, or on an external machine
#rtested with gamepad "afterglow" wireless controller, dongle in Pi usb socket
#needs sudo apt-get install joystick after sudo apt-get update
#also needs sudo pip3 install python-osc
#Version 2. Modified to ensure clean exit on Ubuntu



#Modified by Carlos Santin for Trust Predator USB gamepad (8 buttons, 1 axis)
#Changes:
#--Removed support for non available buttons and axis
#--Added support for configuring port

import subprocess,pygame,sys
from signal import pause
from pythonosc import osc_message_builder
from pythonosc import udp_client
import argparse
from time import sleep

pygame.display.init()
pygame.joystick.init()
clock=pygame.time.Clock()
gamepad = pygame.joystick.Joystick(0)

gamepad.init()

def control(spip,spport):
 gate=0.1
 sender=udp_client.SimpleUDPClient(spip,spport) #sender set up for specified IP

 while True:
    try:
        print("gamepad.py: Python gamepad-> OSC interface")
        print ("Specify external Sonic Pi with  ./gamepad.py --sp [SP3 IP ADDRESS] on command line")
        print("For local Sonic Pi 3 just use ./gamepad.py")
        print ("Ctrl-C to exit")

        pygame.event.pump()
        lud=gamepad.get_axis(1)
        llr=gamepad.get_axis(0)
        #rud=gamepad.get_axis(3)
        #rlr=gamepad.get_axis(2)

##        #if abs(rud) > gate:
##            sender.send_message('/rud',-rud)
        if abs(lud) > gate:
            sender.send_message('/lud',-lud)
##        if abs(rlr) > gate:
##            sender.send_message('/rlr',rlr)
        if abs(llr) > gate:
            sender.send_message('/llr',llr)


        b0=gamepad.get_button(0)
        if b0>0:
            sender.send_message('/b0',b0)
        b1=gamepad.get_button(1)
        if b1>0:
            sender.send_message('/b1',b1)
        b2=gamepad.get_button(2)
        if b2>0:
            sender.send_message('/b2',b2)
        b3=gamepad.get_button(3)
        if b3>0:
            sender.send_message('/b3',b3)
        b4=gamepad.get_button(4)
        if b4>0:
            sender.send_message('/b4',b4)
        b5=gamepad.get_button(5)
        if b5>0:
            sender.send_message('/b5',b5)
        b6=gamepad.get_button(6)
        if b6>0:
            sender.send_message('/b6',b6)
        b7=gamepad.get_button(7)
        if b7>0:
            sender.send_message('/b7',b7)
##        b8=gamepad.get_button(8)
##        if b8>0:
##            sender.send_message('/b8',b8)
##        b9=gamepad.get_button(9)
##        if b9>0:
##            sender.send_message('/b9',b9)
##        b10=gamepad.get_button(10)
##        if b10>0:
##            sender.send_message('/b10',b10)
##        b11=gamepad.get_button(11)
##        if b11>0:
##            sender.send_message('/b11',b11)
##        b12=gamepad.get_button(12)
##        if b12>0:
##            sender.send_message('/b12',b12)

##        hat=gamepad.get_hat(0)
##        if hat[0]!=0 and hat[1]!=0:
##            sender.send_message('/hat',hat)

        clock.tick(5)
        subprocess.call("clear")
    except KeyboardInterrupt:
        print("\nExiting")
        sys.exit()

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    #This arg gets the server IP address to use. 127.0.0.1 or
    #The local IP address of the Pi, required when using external Sonic Pi
    parser.add_argument("--spip",
    default="127.0.0.1", help="The ip on the OSC Server")
    parser.add_argument("--spport",
    default=4559, help="The port of the OSC Server")
    args = parser.parse_args()
    spip=args.spip
    spport=args.spport
    print("Sonic Pi on ip",spip, "and port", spport)
    sleep(2)
    control(spip,spport)
