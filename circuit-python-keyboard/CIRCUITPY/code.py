#
# SPDX-FileCopyrightText: 2021 Jeff Epler for Adafruit Industries
# SPDX-License-Identifier: MIT
#
import microcontroller
import digitalio
import adafruit_matrixkeypad

from time import sleep

import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode  import Keycode

kbd = Keyboard(usb_hid.devices)

# Use the same wiring as in the guide with the following setup lines:
cols = [digitalio.DigitalInOut(x) for x in (
              microcontroller.pin.GPIO1
            , microcontroller.pin.GPIO2
            , microcontroller.pin.GPIO4
            , microcontroller.pin.GPIO3
             )]

rows = [digitalio.DigitalInOut(x) for x in (
              microcontroller.pin.GPIO0
            , microcontroller.pin.GPIO7
            , microcontroller.pin.GPIO6
            , microcontroller.pin.GPIO29
            , microcontroller.pin.GPIO28
            , microcontroller.pin.GPIO27
            )]

keys = (
  (  Keycode.PAUSE          , Keycode.HOME                 , Keycode.END             , Keycode.SCROLL_LOCK ),

  (  Keycode.KEYPAD_NUMLOCK , Keycode.KEYPAD_FORWARD_SLASH , Keycode.KEYPAD_ASTERISK , Keycode.KEYPAD_MINUS ),
  (  Keycode.KEYPAD_SEVEN   , Keycode.KEYPAD_EIGHT         , Keycode.KEYPAD_NINE     , 0 ),
  (  Keycode.KEYPAD_FOUR    , Keycode.KEYPAD_FIVE          , Keycode.KEYPAD_SIX      , Keycode.KEYPAD_PLUS ),
  (  Keycode.KEYPAD_ONE     , Keycode.KEYPAD_TWO           , Keycode.KEYPAD_THREE    , 0 ),
  (  Keycode.KEYPAD_ZERO    , 0                            , Keycode.KEYPAD_PERIOD   , Keycode.KEYPAD_ENTER ))

keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)
oldKeys = ()

while True:

    newKeys = keypad.pressed_keys
    if newKeys:
        print("Pressed: ", newKeys)

    for oldKey in oldKeys:
        if not oldKey in newKeys:
            kbd.release(oldKey)

    for newKey in newKeys:
        if not newKey in oldKeys:
            kbd.press(newKey)

    oldKeys = newKeys
