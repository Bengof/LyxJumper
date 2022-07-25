# LyxJumper
A short python program to quickly jump from a Latex equation to its solution in an online solver.

## Prerequisites
1. Python 3+ with PATH environment variable set. 
2. Chrome Installed (Assuming location in `C:/Program Files (x86)/Google/Chrome/Application/chrome.exe`)
## Usage:
1. Copy the equation from the Latex document to the clipboard (Ctrl+C).
2. Use preassigned shortcut keys to jump to the solution.

## Installation:
1. Clone the Repository
2. Create a desktop shortcut to run the `lyx_jumper.py` script:
    - Right click on the desktop and  `New` -> `Shortcut`.
    - Specify the location of the CMD exe. This is usually in `C:\Windows\System32\cmd.exe`
    - Add to the target of the shortcut: `/k cd <PATH_TO_lyx_jumper.py> & python lyx_jumper.py & exit`   Where PATH_TO_lyx_jumper.py is the path to the `lyx_jumper.py` script.
    - Save the shortcut.
3. Assign a shortcut key to the shortcut you created.
