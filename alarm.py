import time
import signal

signal.alarm(2)
time.sleep(2)
signal.alarm(8)
while True:
    time.sleep(1)
    print("等待始终")