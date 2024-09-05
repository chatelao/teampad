# teampad

The repository for a little "Wormier k21" upgrade with a XIAO-RP2040

## Running "CircuitPython" firmware

The "CircuitPython" is easier to modify as it is 100% transparent in the "CIRCUITPY" mass storage drive.

1. Press "BOOT" & "RESET" (or unplug/plug USB cable).
2. Got to "circuit-python-keyboard" subdirectory.
3. Copy the "adafruit-circuitpython-seeeduino_xiao_rp2040-de_DE-9.1.3.uf2" file to the "**RPI-RP2**" mass storage.
4. Copy all files from "circuit-python-keyboard/CIRCUITPY" subdirectory to the mass storage.
5. Open the "code.py" file and modify whatever you need to change.
6. (Optional) Install the "Mu" editor for the terminal console debugging

More details here: https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython

## Running "QMK-Vial" firmware

The "QMK-Vial" is much easier to configure over https://vial.rocks.

1. Press "BOOT" & "RESET" (or unplug/plug USB cable).
2. Got to "circuit-python-keyboard" subdirectory to the "**RPI-RP2**" mass storage.
3. Install "chatelao_teampad_rp2040xiao_default.uf2"
