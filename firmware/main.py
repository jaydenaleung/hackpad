import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

PINS = [board.D7, board.D8, board.D9, board.D10] # These are my defined pins

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

keyboard.keymap = [
    [KC.MACRO(Press(KC.LCTRL),Tap(KC.Z),Release(KC.LCTRL)), KC.MACRO(Press(KC.LCTRL),Tap(KC.Y),Release(KC.LCTRL)), KC.F11, KC.MACRO(Press(KC.LWIN),Press(KC.LSHIFT),Tap(KC.S),Release(KC.LWIN),Release(KC.LSHIFT))] # CTRL+Z, CTRL+Y, F11, Windows Screenshot
]

if __name__ == '__main__':
    keyboard.go()