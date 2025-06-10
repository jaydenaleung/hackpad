# D-MACROPAD
Here's my Hackpad starter project for Hack Club's Highway to Undercity program! I made this to become more familiar with creating a Highway project and to gain more practice before I tackle a custom project.

The D-MACROPAD is a titled, customized macropad with an aesthetic design. With a row of four customizable buttons and the USB-C port hidden in the back, it was made to provide a smooth experience. (Scroll past pictures to see rest of description.)
![Macropad (Highway)](https://github.com/user-attachments/assets/ccea52ff-b33b-4de5-be28-8604668b59ff)
![Macropad (Highway) (1)](https://github.com/user-attachments/assets/473e6de3-8792-462a-80ba-a0d12bef1485)

## Features
- A row of four programmable/customizable buttons
- Tilted stand for easier reach
- USB-C connectivity, hidden at the back to preserve aesthetic detail
- Seeed XIAO RP2040 Microcontroller
- White keycaps (not shown in picture)
- Yellow-black bumblebee color theme (cause it looks cool)

## Possible Additional Features
- Some kind of screen on each of the keys OR OLED screen above the keys that displays the album of the song playing right now, etc. - because nothing's above the keys right now
- Functionality for the connected LEDs
- A more interesting case design
- Software or easier way to reprogram the keys
- RGB lights on case
- Etc.

## CAD Modeling
- Designed with Onshape
- Top plate, black
- Bottom case, titled, yellow
- 3.4mm holes for 3mm bolts and heatset inserts (inserts go on the bottom)
- See picture for reference!

## Electronics/PCB
- Used KiCAD
- The four keys are in a straight row, the XIAO goes above it, and the LEDs sit on each side of the XIAO
![image](https://github.com/user-attachments/assets/be93e4ac-1608-48eb-9ad4-99f8627aa8cd)
![image](https://github.com/user-attachments/assets/9a32654c-b0a9-4a2e-82cd-c9aafc2638b5)
![image](https://github.com/user-attachments/assets/eb9a2bce-a05f-47d9-b114-5ed3042904d2) (I layered all the gerber files and drill maps on top of each other.)

## Firmware - KMK
- Used KMK
- Key legend: 1st key = open "Sultans of Swing" in Spotify (a.k.a. my favorite song), 2nd key = press "A", 3rd key = display some text only when held down, 4th key = press "B"
- Keys were pretty random as firmware can be buggy and I wanted to test some simpler keys (i.e. 2nd key, 4th) as well as more complex commands
- Opened Spotify songs by using the method .SYSTEM_EXEC(command), with the command being "start spotify:track:TRACKID"

## BOM
- 1 3D printed case (2 parts in total, top and bottom)
- 1 USB-C cable
- 1 Seeed XIAO RP2040 Microcontroller
- 1 Custom PCB found in 'pcb' folder in this repo
- 4 MX-Style switches
- 4 DSA white keycaps
- 2 SK6812 MINI-E LEDs
- 4 M3x16mm screws
- 4 M3x5mx4mm heatset inserts
