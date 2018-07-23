simple test script written in python for the raspberry pi

program fetches github repo, check is changes have been made and if so, compiles and uploads to an array of arduino boards connected

connected arduinos can be defined as a list of arguments (name port name port etc) through command line when initially running script, or in .txt passed as argument (see boards.txt as an example)


command line example:

python test2.py boards.txt blink_test

python test2.py mega ACM0 uno USB1 due ACM1 blink_test2
