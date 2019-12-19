# A tool that displays popup notifications periodically 
# The tool, after starting will print its PID.
# To stop execution kill the process with the given PID.
#   python notifier.py <message tittle> <message body> <period in seconds> &

import os
import subprocess
import sys
import time

def notifyOSX(head, body):
    command = "osascript -e 'display notification \"{}\" with title \"{}\"'".format(head, body)
    subprocess.call(command, shell=True)

def notify(head, body):
    if sys.platform == "linux" or sys.platform == "linux2":
        raise NotImplementedError("Operating system not supported")
    elif sys.platform == "darwin":
        notifyOSX(head, body)
    elif sys.platform == "win32":
        raise NotImplementedError("Operating system not supported")
    else:
        raise NotImplementedError("Operating system not supported")

if __name__ == '__main__':
    print "PID = {}".format(os.getpid())
    while 1:
        notify(sys.argv[1], sys.argv[2])
        time.sleep(float(sys.argv[3]))
