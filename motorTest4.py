import time
import resultByIDDao
import settings
import motorFunctions

basetime = time.time()
motorFunctions.connectVFD()

print("Starting Test 4: Insensitivity Test")
print("Test 4 - Clockwise direction")
motorFunctions.setAccelerationTime(90) #9s
motorFunctions.setSpeed(900) #900rpm
motorFunctions.startMotorForward()
time.sleep(9) #accelerate for 9s
time.sleep(30) #maintain speed for 30s TODO: add sensors
motorFunctions.setDecelerationTime(125) #12.5s
motorFunctions.stopMotor()
time.sleep(12.5) #decelerate for 12.5s
print("Test 4 - Anticlockwise direction")
motorFunctions.setAccelerationTime(90) #9s
motorFunctions.setSpeed(900) #900rpm
motorFunctions.startMotorReverse()
time.sleep(9) #accelerate for 9s
time.sleep(30) #maintain speed for 30s TODO: add sensors
motorFunctions.setDecelerationTime(125) #12.5s
motorFunctions.stopMotor()
time.sleep(12.5) #decelerate for 12.5s
print("Test 4 finished")

