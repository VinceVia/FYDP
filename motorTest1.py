import time
import resultByIDDao
import settings
import motorFunctions

motorFunctions.connectVFD()

#TODO: may need to change decelerationTime settings to accelerationTime
print("Starting Test 1: Run-In, Operating Temperature, and Vibration")
print("Test 1 - Clockwise direction")
motorFunctions.setAccelerationTime(90) #9s
motorFunctions.setSpeed(900) #900rpm target speed
motorFunctions.startMotorForward()
time.sleep(9) #accelerate for 9s
time.sleep(20) #maintain speed for 10min TODO: change value to 600, add sensors
motorFunctions.setDecelerationTime(360) #36s
motorFunctions.stopMotor() #TODO: check if this uses the right deceleration rate, change to startMotorForwards() with target speed 0 if not
time.sleep(36) #decelerate for 36s 
print("Test 1 - Anticlockwise direction")
#motorFunctions.setAccelerationTime(900) #9s acceleration time - should be already set from before
motorFunctions.startMotorReverse()
time.sleep(9) #accelerate for 9s
time.sleep(20) #maintain speed for 10min TODO: change to 600, add sensors
motorFunctions.stopMotor() #TODO: check if this uses the right deceleration rate, change to startMotorBackwards() with target speed 0 if not
time.sleep(36) #decelerate for 36s 
print("Test 1 finished")
