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

def notifyLinux(head, body):
    command = "notify-send '{}' '{}'".format(head, body)
    subprocess.call(command, shell=True)

def notifyWin32(head, body):
    raise NotImplementedError("Operating system not supported")

if __name__ == '__main__':
    platformCall = {
        "linux": notifyLinux,
        "linux2": notifyLinux,
        "win32": notifyWin32,
        "darwin": notifyOSX
    }

    print "PID = {}".format(os.getpid())
    while 1:
        platformCall[sys.platform](sys.argv[1], sys.argv[2])
        time.sleep(float(sys.argv[3]))
