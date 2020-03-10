#!/usr/bin/python3
import time, sys, json, sys, urllib.request
import pyautogui

# get version number
try: __version__ = open("version.txt", "r").read().rstrip()
except: print("Warning: unable to get local version info (no version file found)")

def error(ErrorMessage):
	print("\nError: " + ErrorMessage)
	raise SystemExit

def StoSMH(seconds):
	m, s = divmod(int(seconds), 60)
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

def main():
	UserArgs = sys.argv[1:]
	if "-v" in UserArgs or "-V" in UserArgs:
		print("version: " + str(__version__))
		exit()

	# checking for new versions
	try:
		response = urllib.request.urlopen("https://raw.githubusercontent.com/Dan-Vizor/cup/master/version.txt")
	except:
		print("Warning: unable to get remote version info (check internet connection)")
	lines = response.readlines()
	RemoteVersion = lines[0].decode("utf-8").rstrip()

	if RemoteVersion != __version__:
		print("Warning: Version {} is avalable, you are currently running version {}.\nPlease consider upgrading.".format(RemoteVersion, __version__))

	# OS detection
	OS = sys.platform
	OS = OS.lower()
	print("Running in {} mode".format(OS))
	if OS == "darwin": error("Every day we stray further from God.") # ugh Apple

	SETTINGS = ReadJSON("settings.json")

	# getting LoopCount value from user
	if UserArgs != []:
		try:
			LoopCount = int(UserArgs[0])
		except:
			error("invalid input")

		if LoopCount <= 0:
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
		print("ETA: {}".format(StoSMH((SETTINGS["interval"] + SETTINGS["buffer-time"]) * LoopCount)))

	# startup countdown
	i = SETTINGS["countdown-value"]
	if OS == "windows": print("starting in {}".format(i))
	while i > -1:
		if OS == "linux":
			print(" "*100, end="\r")
			print("starting in {}s".format(StoSMH(i)), end="\r")
		time.sleep(1)
		i -= 1
	if OS == "linux": print("\n")

	# printing "cup"
	i = 1
	StartTime = time.time()
	while True:
		try:
			if SETTINGS["do-backspace"]: pyautogui.press('backspace', presses = len(SETTINGS["print-text"]))
			pyautogui.write(SETTINGS["print-text"])
			pyautogui.press('enter')

		except: error("exiting due to pyautogui failsafe")

		# Linux user feedback
		if OS == "linux":
			if not INF:
				PrintProgressBar(i, LoopCount, prefix = "Progress:", length = 50)
				time.sleep(SETTINGS["interval"] + SETTINGS["buffer-time"])
			else:
				for WaitCounter in range(SETTINGS["interval"] + SETTINGS["buffer-time"]):
					timer = StoSMH(round((time.time() - StartTime), 2))
					print(" "*100, end = "\r")
					print("  {} cup(s)  {}".format(i, timer), end = "\r")
					time.sleep(1)

		if not INF:
			if i >= LoopCount: break

		# Windows user feedback
		if OS == "windows":
			print(i)
			time.sleep(SETTINGS["interval"] + SETTINGS["buffer-time"])
		i += 1

try:
	main()
except KeyboardInterrupt:
	print("\n program terminated by keyboard interrupt")
