import os
import subprocess
import time
import sys


def compile_code():

	try:
		verify
	
	except NameError:
		modeString = " --upload"
	else:
		modeString = " --verify"

	for x in range(1,len(sys.argv)/2+1):
	
		port = " --port /dev/tty" + sys.argv[2*x]
		device = sys.argv[2*x-1]
		
		if device == "mega" or device == "Mega" or device == "MEGA":
			arch = " --board arduino:avr:mega:cpu=atmega2560"
		elif device == "uno" or device == "Uno" or device == "UNO":
			arch = " --board arduino:avr:uno"
		elif device == "due" or device == "Due" or device == "DUE":
			arch = " --board arduino:sam:due"
		else:
			arch = ""
		
		os.system('~/Downloads/arduino-1.8.5/arduino' + modeString + arch + port + ' ~/Desktop/rasp_pi_auto_download_test/blink_test/blink_test.ino')
	return


#______________________
#PROGRAM
#______________________

# will upload if not defined
verify = True


# initial pull and upload
os.system('git pull')
compile_code()

while(1):
	os.system('git fetch')
	git_diff_output = subprocess.check_output(['git', 'diff', 'origin'])
	
	if git_diff_output != "":
		print("\n NEW GIT PUSH DETECTED \n ")
		os.system('git pull')
		
		compile_code()

	time.sleep(5)


