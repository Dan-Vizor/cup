# cup.py
cup is a keyboard emulation tool for Linux (as well as limated functionalaty on Windows) primarily designed to work on the cup Discord server.

##Dependencies 
- pyautogui

##Usage
to run:
- enter `./cup.py` on Linux or dobble click the file on Windows.
- Select the target text box.
- Wait for the timer to count down.
- Profit!

By default cup.py will run until either the program is stopped (CURL + C) or the pyautogui failsafe is activated (by moving the mouse to any corner of the primary display)

###settings.json guide
The settings file has four options and there function is as follows:
- `countdown-value`  This is how long the startup timer will run for.
- `buffer-time`  This is how long the program will wait between prints (on top of `interval`) to help reduse errors.
- `interval`  This is how long the program will wait between prints and should be the same as Discord slowmode.
- `print-text`  This is what gets printed.

###Alternate running modes
Currently there is only one alternate running mode which will print a predefined number of prints before exiting. This can be activated by adding a number as a command line argument e.g. `./cup.py 3` will print three times before exiting. (This mode is only avalible on Linux.)

##disclaimers
- This software is in beta so expect bugs and please report them to me.
- Due to it's nature as a input emulation tool may have unexpected results (e.g. sending random "cup" messages to people on Discord.)
