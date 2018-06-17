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
		line = lines[loc]
		device,port = line.split(" ")
		
	
	if device == "mega" or device == "Mega" or device == "MEGA":
		arch = " --board arduino:avr:mega:cpu=atmega2560"
	elif device == "uno" or device == "Uno" or device == "UNO":
		arch = " --board arduino:avr:uno"
	elif device == "due" or device == "Due" or device == "DUE":
		arch = " --board arduino:sam:due"
	else:
		arch = ""
		
	print("\n Architecture found :" + arch)
	return arch	

def get_port(loc):
	
	try:
		parameters_from_file
	except:
		port = " --port /dev/tty" + sys.argv[2*loc]
	else:
		line = lines[loc]
		device,port = line.split(" ")
		if len(port) <6:
            port = " --port /dev/tty" + port
                    
        else:
            port = " --port " + port
		
	print("\n Port found :" + port)
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
		num_boards = len(sys.argv)/2+1
	else: #num lines in file
		num_boards = sum(1 for line in open(config_file))
	
	print(num_boards)
	for x in range(1,num_boards):
		
		arch = get_arch(x)
		port = get_port(x)
					
		#os.system('~/Downloads/arduino-1.8.5/arduino' + mode + arch + port + ' ~/Desktop/rasp_pi_auto_download_test/'+ file +'/' + file + '.ino')
		print('~/Downloads/arduino-1.8.5/arduino' + mode + arch + port + ' ~/Desktop/rasp_pi_auto_download_test/'+ file +'/' + file + '.ino')

		return


#______________________
#PROGRAM
#______________________

# will upload if not defined
verify = True
config_file = "boards.txt"
file_exists = os.path.isfile(config_file)
print("file exists : " + str(file_exists))


if len(sys.argv) == 1:
    print("no input arguments, exiting script")
    exit()

elif sys.argv[1] == config_file and file_exists == True:
    parameters_from_file = True
    file = open(config_file, "r")
    lines = file.readlines()
elif sys.argv[1] == config_file and file_exists == False:
    print("file not found, exiting script")
    exit()
else:
    print("No file provided, assuming boards as command line arguments")
    
if parameters_from_file == False:
	file = sys.argv(len(sys.argv)-1)		#last element
else: 
	file = lines[1]							#first line of 

print(file)


	'''
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
'''

