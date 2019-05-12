import sys
import time
import multiprocessing

def processTest():
#    name = multiprocessing.current_process().name
    print("Hi")
    sys.stdout.flush()
#    print("Name is: " + motorProcessTest.name + ", PID is: " + motorProcessTest.pid)
#    sys.stdout.flush()
    time.sleep(5) #wait 10s
    print("Waiting...")
    sys.stdout.flush()
    time.sleep(5) #wait 10s
    print("Waiting...")
    sys.stdout.flush()
    time.sleep(5) #wait 10s
    print("Waiting...")
    sys.stdout.flush()
    time.sleep(5) #wait 10s
    print("Waiting...")
    sys.stdout.flush()
    time.sleep(5) #wait 10s
    print("Waiting...")
    sys.stdout.flush()
    print("Bye")
    sys.stdout.flush()
