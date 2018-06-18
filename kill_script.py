import os

os.system("pgrep -f main.py")
os.system("pkill -9 -f main.py")