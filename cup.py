#!/usr/bin/python3
__version__ = 0.9

import time, sys, json
import pyautogui

def error(ErrorMessage):
	print("\nError: " + ErrorMessage)
	raise SystemExit

def StoSMH(seconds):
	m, s = divmod(LoopCount * seconds, 60)
	h, m = divmod(m, 60)
	if s < 10: s = "0" + str(s)
	if m < 10: m = "0" + str(m)
	if h < 10: h = "0" + str(h)

	return "{}:{}:{}".format(h, m, s)

# from https://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console
def PrintProgressBar(iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
	"""
	Call in a loop to create terminal progress bar
	params:
		iteration   - Required  : current iteration (Int)
		total	    - Required  : total iterations (Int)
		prefix	    - Optional  : prefix string (Str)
		suffix	    - Optional  : suffix string (Str)
		decimals	- Optional  : positive number of decimals in percent complete (Int)
		length	    - Optional  : character length of bar (Int)
		fill		- Optional  : bar fill character (Str)
		printEnd	- Optional  : end character (e.g. "\r", "\r\n") (Str)
	"""
	percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
	filledLength = int(length * iteration // total)
	bar = fill * filledLength + '-' * (length - filledLength)
	print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = printEnd)
	if iteration == total: # Print New Line on Complete
		print("\nDone")

def ReadJSON(File):
	try:
		# from https://stackoverflow.com/questions/20199126/reading-json-from-a-file
		with open(File) as f:
			return json.load(f)
	except IOError:
		error("unable to locate file ({})".format(File))

# main program start
SETTINGS = ReadJSON("settings.json")

# getting LoopCount value from user
UserArgs = sys.argv[1:]
if UserArgs != []:
	try:
		LoopCount = int(UserArgs[0])
	except:
		error("invalid value")

else:
	LoopCount = 0

#setting INF mode
INF = False
if LoopCount <= 0:
	INF = True
	LoopCount = 2

# working out how long it will take to do
if not INF:
	print("ETA: {}".format(StoSMH(round(SETTINGS["interval"] + SETTINGS["buffer-time"]))))

# startup countdown
i = SETTINGS["countdown-value"]
while i > -1:
	print(" "*100, end="\r")
	print("starting in {}s".format(i), end="\r")
	time.sleep(1)
	i -= 1
print("\n")

# printing "cup"
i = 1
while True:
	print(" "*100, end="\r")
	if not INF:
		PrintProgressBar(i, LoopCount, prefix = "Progress:", length = 50)
	else:
		print(" {} cups".format(i), end="\r")

	try:
		pyautogui.press('backspace', presses = len(SETTINGS["print-text"]))
		pyautogui.write(SETTINGS["print-text"])
		pyautogui.press('enter')
	except:
		error("exiting due to pyautogui failsafe")

	if not INF:
		if i >= LoopCount: break

	i += 1
	time.sleep(SETTINGS["interval"] + SETTINGS["buffer-time"])
