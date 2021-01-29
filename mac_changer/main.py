import subprocess

subprocess.call('ifconfig wlan0 down', shell=True)
subprocess.call('ifconfig wlan0 hw ether 11:32:23:79:39:54', shell=True)
subprocess.call('ifconfig wlan0 up', shell=True)
