import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

# Main instance
keyboard = KMKKeyboard()

# Add macro extension
macros = Macros()
keyboard.modules.append(macros)

# Define pins
PINS = [board.D3, board.D4, board.D2, board.D1]

# tell kmk not using key matrix
keyboard.matrix = KeysScanner(pins=PINS, value_when_pressed=False)

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
# KEYCODES: 1st key - 
# Play Sultans of Swing - KC.SYSTEM_EXEC('start spotify:track:6cr6UDpkjEaMQ80OjWqEBQ')

def show_afwa():
    return "afwa is a polar bear"

def hide_afwa():
    for i in range(20):
        Tap(KC.BSPACE)

keyboard.keymap = [
    [KC.SYSTEM_EXEC('start spotify:track:6cr6UDpkjEaMQ80OjWqEBQ'), KC.A, KC.Macro(on_press=show_afwa, on_release=hide_afwa), KC.D],
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()