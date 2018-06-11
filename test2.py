import os
import subprocess
import time
import sys


def get_arch(loc):

	try:
		parameters_from_file
		
	except:	#get from command line
		device = sys.argv[2*loc-1]
	else:	#get from file
		line = file.readline(loc)
		device,port = line.split("\t")
		
	print("Device found :" + device)
	if device == "mega" or device == "Mega" or device == "MEGA":
		arch = " --board arduino:avr:mega:cpu=atmega2560"
	elif device == "uno" or device == "Uno" or device == "UNO":
		arch = " --board arduino:avr:uno"
	elif device == "due" or device == "Due" or device == "DUE":
		arch = " --board arduino:sam:due"
	else:
		arch = ""
	return arch	

def get_port(loc):
	
	try:
		parameters_from_file
	except:
		port = " --port /dev/tty" + sys.argv[2*loc]
	else:
		line = file.readline(loc)
		device,port = line.split("\t")
		
	print("port found :" + port)
	return port

	
def get_mode():
	try:
		parameters_from_file
	except:
		try:
			verify
		
		except NameError:
			modeString = " --upload"
		else:
			modeString = " --verify"
	else:
		modeString = ""
		
	return modeString

def compile_code():

	mode = get_mode()
	
	try:
		parameters_from_file
	except: #num of board arguments in command line
		num_boards = range(1,len(sys.argv)/2+1)
	else: #num lines in file
		num_boards = sum(1 for line in open(config_file)
	
	for x in num_boards:
		
		arch = get_arch(x)
		port = get_port(x)
					
		print('~/Downloads/arduino-1.8.5/arduino' + mode + arch + port + ' ~/Desktop/rasp_pi_auto_download_test/blink_test/blink_test.ino')
		#os.system('~/Downloads/arduino-1.8.5/arduino' + mode + arch + port + ' ~/Desktop/rasp_pi_auto_download_test/blink_test/blink_test.ino')
	return


#______________________
#PROGRAM
#______________________

# will upload if not defined
verify = True
config_file = "boards.txt"
file_exists = os.path.isfile(config_file)
print("file exists : " fiel_exists)

if sys.argv[2] == "boards.txt" and file_exists
	parameters_from_file = True
	file = open(config_file, "r")


# initial pull and upload
#os.system('git pull')
compile_code()
'''
while(1):
	os.system('git fetch')
	git_diff_output = subprocess.check_output(['git', 'diff', 'origin'])
	
	if git_diff_output != "":
		print("\n NEW GIT PUSH DETECTED \n ")
		os.system('git pull')
		
		compile_code()

	time.sleep(5)

'''
