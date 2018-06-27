import os
import subprocess
import time
import sys


def get_arch(loc):

	if parameters_from_file == False:
		#get from command line
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
	
	if parameters_from_file == False:
            port = " --port /dev/tty" + sys.argv[2*loc]
	else:
            line = lines[loc]
            device,port = line.split(" ")
            if len(port) <6:
                port = " --port /dev/tty" + port
                
            else:
                port = " --port " + port
            
            if (len(lines)-1) != loc:
                port = port[:-1]
                    
	#print("\n Port found :" + port)
	return port

	
def get_mode():
	
        try:
                verify
        except NameError:
                modeString = " --upload"
        else:
                modeString = " --verify"
			
	return modeString

def compile_code():

	mode = get_mode()
	
	if parameters_from_file == False:
	 #num of board arguments in command line
            
		num_boards = len(sys.argv)/2
		
	else: #num lines in file
		num_boards = sum(1 for line in open(config_file))
	
	
	for x in range(1,num_boards):
		
		arch = get_arch(x)
		port = get_port(x)
					
		print(path_to_arduino + mode + arch + port + ' ' + path_to_this_dir + '/'+ file +'/' + file + '.ino')
                #os.system(path_to_arduino + mode + arch + port + ' ' + path_to_this_dir + '/'+ file +'/' + file + '.ino')

	return

def log_data(file):
    git_data = subprocess.check_output(['git', 'log', '-1', '--abbrev-commit'])
	
    with open(file, 'w', 0) as f:
        f.write(git_data);
	f.close();
    return


#______________________
#PROGRAM
#______________________

# will upload if not defined
verify = True
config_file = "boards.txt"
log_file = "git_data_log.txt"
path_to_arduino = "~/Downloads/arduino-1.8.5/arduino"
path_to_this_dir = os.path.dirname(os.path.abspath(__file__))

file_exists = os.path.isfile(config_file)
print("boards.txt exists : " + str(file_exists))



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
    parameters_from_file = False
    
if parameters_from_file == False:
	file = sys.argv[len(sys.argv)-1]		#last element
else: 
	file = lines[0]							#first line of 
        file = file[:-1]
target_exists = os.path.isfile(file + '/' + file +'.ino')


if target_exists == False:
    print('target file does not exist, exiting script')
    print('target file:' + file + '/' + file +'.ino')
    exit()
    




# initial pull and upload
os.system('git pull')
compile_code()
log_data(log_file);

while(1):
	os.system('git fetch')
	git_diff_output = subprocess.check_output(['git', 'diff', 'origin'])
	print (git_diff_output)
	if git_diff_output != "":
		print("\n NEW GIT PUSH DETECTED \n ")
		os.system('git pull')
		
		compile_code()
		log_data(log_file);

	time.sleep(5)


