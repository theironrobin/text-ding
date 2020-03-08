#!/usr/bin/python3
import gi
import dbus
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GLib
import os
from pathlib import Path

sound_path = Path("/usr/share/sounds/gnome/default/alerts/")
led_path = Path("/sys/devices/platform/leds/leds/pinephone:green:user/brightness")
my_sound = sound_path/"bark.ogg"
bark = "cvlc --play-and-exit " + str(my_sound)
led_on =  "echo '1' | sudo tee  " + str(led_path) + " > /dev/null"
led_off =  "echo '0' | sudo tee  " + str(led_path) + " > /dev/null"
ignore_read = False

def text_ding(account, sender, message, conversation, flags):
    os.system(led_on)
    #os.system(bark)
    #os.system(bark)

def delay_led_off(account, sender, x, y):
    global ignore_read
    ignore_read = True

def read_it(gtkconv):
    global ignore_read
    if (ignore_read == False):
        os.system(led_off)
    ignore_read = False

dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
bus = dbus.SessionBus()

bus.add_signal_receiver(text_ding,
                        dbus_interface="im.pidgin.purple.PurpleInterface",
                        signal_name="ReceivedImMsg")

bus.add_signal_receiver(delay_led_off,
                        dbus_interface="im.pidgin.purple.PurpleInterface",
                        signal_name="LurchStatusIm")

bus.add_signal_receiver(read_it,
                        dbus_interface="im.pidgin.purple.PurpleInterface",
                        signal_name="ConversationDisplayed")                        

GLib.MainLoop().run()
