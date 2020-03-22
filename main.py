#!/usr/bin/python3
import gi
import dbus
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GLib
import os
from pathlib import Path

sound_path = Path("/usr/share/sounds/gnome/default/alerts/")
green_led_path = Path("/sys/devices/platform/leds/leds/pinephone:green:user/brightness")
blue_led_path = Path("/sys/devices/platform/leds/leds/pinephone:blue:user/brightness")
my_sound = sound_path/"bark.ogg"
bark = "cvlc --play-and-exit " + str(my_sound)
green_led_on =  "echo '1' | sudo tee  " + str(green_led_path) + " > /dev/null"
green_led_off =  "echo '0' | sudo tee  " + str(green_led_path) + " > /dev/null"
blue_led_on = "echo '1' | sudo tee  " + str(blue_led_path) + " > /dev/null"
blue_led_off = "echo '0' | sudo tee  " + str(blue_led_path) + " > /dev/null"
ignore_read = False

def text_ding(account, sender, message, conversation, flags):
    os.system(green_led_on)
    os.system(bark)

def delay_led_off(account, sender, x, y):
    global ignore_read
    ignore_read = True

def read_it(gtkconv):
    global ignore_read
    if (ignore_read == False):
        os.system(green_led_off)
    ignore_read = False

def called(x, y, z):
    if (x=="org.gnome.Mutter.DisplayConfig" and int(y[dbus.String("PowerSaveMode")])==0):
        #os.system(blue_led_on)

def launched(a, b, c, d, e):
    encoding = 'utf-8'
    launchedapp = str(bytes(a), encoding).split("/")[-1][0:-1]
    if (launchedapp == "sm.puri.Calls.desktop"):
        #os.system(blue_led_off)


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

bus.add_signal_receiver(called,
                        dbus_interface="org.freedesktop.DBus.Properties",
                        signal_name="PropertiesChanged")

bus.add_signal_receiver(launched,
                        dbus_interface="org.gtk.gio.DesktopAppInfo",
                        signal_name="Launched")

GLib.MainLoop().run()
