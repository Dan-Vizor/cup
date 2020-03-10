# cup.py
cup.py is a keyboard emulation tool for Linux (as well as limated functionality on Windows) primarily designed for use on the cup Discord server.

## Dependencies 
- python-3.x
- pyautogui

## Usage
to run:
- enter `./cup.py` on Linux or dubble click the file on Windows.
- Select the target text box.
- Wait for the timer to count down.
- Profit!

By default cup.py will run until either the program is stopped manually (CURL + C) or the pyautogui failsafe is activated (by moving the mouse to any corner of the primary display)

### settings.json guide
The settings file has five options and there function are as follows:
- `countdown-value`  This is how long the startup timer will run for. (int)
- `buffer-time`  This is how long the program will wait between prints (on top of `interval`) to help reduse errors. (int)
- `interval`  This is how long the program will wait between prints and should be the same as Discord slowmode. (int)
- `do-backspace`  When on cup.py will remove any previous prints in the target text box to prevent "cupcup". (boolean)
- `print-text`  This is what gets printed. (string)

### Alternate running modes
Currently there is only one alternate running mode which will print a predefined number of prints before exiting. This can be activated by adding a number as a command line argument e.g. `./cup.py 3` will print three times before exiting. (This mode is only avalible on Linux.)

## Disclaimers
- This software is in beta so expect bugs and please report any you find to me.
- Due to it's nature as a input emulation tool cup.py may have unexpected results. (e.g. sending random "cup" messages to people on Discord.)
