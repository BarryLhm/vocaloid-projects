#!/bin/python3

import os
import sys
import time
from pathlib import Path

action = sys.argv[1]
serial_file = sys.argv[2] if len(sys.argv) > 2 else Path(__file__).parent / "serial.txt"
bpm = sys.argv[3] if len(sys.argv) > 3 else 170

fd = open(serial_file)
serial=fd.read().split()
fd.close()

for i in range(len(serial)):
	os.system(action)
	time.sleep(int(serial[i]) * 60 / bpm)
