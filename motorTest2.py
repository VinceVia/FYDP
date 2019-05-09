import time
import resultByIDDao
import settings
import motorFunctions

basetime = time.time()
motorFunctions.connectVFD()

print("Starting Test 2: Severe Skid Sensitivity Test")
print("Test 2 - Clockwise direction")
motorFunctions.setAccelerationTime(900) #9s
motorFunctions.setSpeed(900) #900rpm
motorFunctions.startMotorForward()
time.sleep(9) #accelerate for 9s
time.sleep(30) #maintain speed for 30s TODO: add sensors
motorFunctions.setDecelerationTime(900) #9s
motorFunctions.setSpeed(0) #0rpm target sped
motorFunctions.stopMotor() #TODO: check if this uses the right deceleration rate, change to startMotorForwards() with target speed 0 if not
print("Test 2 - Anticlockwise direction")
#motorFunctions.setAccelerationTime(900) #9s
motorFunctions.setSpeed(900) #900rpm
motorFunctions.startMotorBackward()
time.sleep(9) #accelerate for 9s
time.sleep(30) #maintain speed for 30s TODO: add sensors
#motorFunctions.setDecelerationTime(90) #9s
motorFunctions.setSpeed(0) #0rpm target sped
motorFunctions.stopMotor() #TODO: check if this uses the right deceleration rate, change to startMotorForwards() with target speed 0 if not
print("Test 2 finished") 


