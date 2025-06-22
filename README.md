# D-MACROPAD
Here's my Hackpad starter project for Hack Club's Highway to Undercity program! I made this to become more familiar with creating a Highway project and to gain more practice before I tackle a custom project.

The D-MACROPAD is a titled, customized macropad with an aesthetic design. With a row of four customizable buttons and the USB-C port hidden in the back, it was made to provide a smooth experience. (Scroll past pictures to see rest of description.)
![Screenshot 2025-06-22 040710](https://github.com/user-attachments/assets/dd3a8b95-d35b-4a16-a328-587ca53797ac)
![Screenshot 2025-06-22 033012](https://github.com/user-attachments/assets/e5b5c7bf-d3e1-4c58-ad8d-61d1eb1f3194)
![Screenshot 2025-06-22 040733](https://github.com/user-attachments/assets/a0f06b9e-7394-455b-a691-4c000407ee65)
Top plate in a different color for a more distinct image:
![Screenshot 2025-06-22 033105](https://github.com/user-attachments/assets/2fa3bb47-7b19-4fd5-8e92-cc600cf702f0)
![Screenshot 2025-06-22 033500](https://github.com/user-attachments/assets/be5e74e0-2d99-4d41-99fd-7ab77857f9e4)


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
- See pictures above for reference!

## Electronics/PCB
- Used KiCAD
- The four keys are in a straight row, the XIAO goes above it, and the LEDs sit on each side of the XIAO
![image](https://github.com/user-attachments/assets/136cd632-55a5-4650-80f0-c5f3a2c50105)
![image](https://github.com/user-attachments/assets/928a9f3f-cf9e-4b82-a828-172348de5d95)

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
