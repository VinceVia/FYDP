import time
import resultByIDDao
import settings
import motorFunctions

def MotorRoutine(StartPage):
    basetime = time.time()
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
    
    
    print("Starting Test 2: Severe Skid Sensitivity Test")
    print("Test 2 - Clockwise direction")
    motorFunctions.setAccelerationTime(90) #9s
    motorFunctions.setSpeed(900) #900rpm
    motorFunctions.startMotorForward()
    time.sleep(9) #accelerate for 9s
    time.sleep(30) #maintain speed for 30s TODO: add sensors
    motorFunctions.setDecelerationTime(90) #9s
    motorFunctions.stopMotor() #TODO: check if this uses the right deceleration rate, change to startMotorForwards() with target speed 0 if not
    print("Test 2 - Anticlockwise direction")
    motorFunctions.startMotorReverse()
    time.sleep(9) #accelerate for 9s
    time.sleep(30) #maintain speed for 30s TODO: add sensors
    #motorFunctions.setDecelerationTime(90) #9s
    motorFunctions.stopMotor() #TODO: check if this uses the right deceleration rate, change to startMotorForwards() with target speed 0 if not
    print("Test 2 finished") 
    
    
    print("Starting Test 3: Short Skid Tests")
    print("Test 3 - Clockwise direction")
    motorFunctions.setAccelerationTime(90) #9s
    motorFunctions.setSpeed(900) #900rpm
    motorFunctions.startMotorForward()
    time.sleep(9) #accelerate for 9s
    time.sleep(30) #maintain speed for 30s TODO: add sensors, may need
    motorFunctions.setSmallDecelerationTime(0.4) #0.4s 
    motorFunctions.setSpeed(860) #860rpm
    time.sleep(0.4) #decelerate for 0.4s TODO: add sensors
    time.sleep(10) #maintain speed for 10s TODO: sensors
    motorFunctions.setDecelerationTime(90) #9s deceleration time
    motorFunctions.setSpeed(500) #500rpm
    time.sleep(9) #decelerate for 9s TODO: sensors
    time.sleep(30) #maintain speed for 10s
    motorFunctions.setSmallDecelerationTime(0.4) #0.4s
    motorFunctions.setSpeed(460) #460rpm
    time.sleep(0.4) #decelerate for 0.4s TODO: sensors
    time.sleep(10) #maintain speed for 10s TODO: sensors
    motorFunctions.setDecelerationTime(90) #9s
    motorFunctions.setSpeed100() #100rpm
    time.sleep(9) #decelerate for 9s
    time.sleep(30) #maintain speed for 30s TODO: sensors
    motorFunctions.setSmallDecelerationTime(0.4) #0.4s
    motorFunctions.setSpeed60() #60rpm
    time.sleep(0.4) #decelerate for 0.4s TODO: sensors
    time.sleep(10) #maintain speed for 10s
    motorFunctions.setDecelerationTime(15) #1.5s
    motorFunctions.stopMotor()
    time.sleep(1.5) #decelerate for 1.5s
    time.sleep(1) #rest for a second
    print("Test 3 - Anticlockwise direction")
    motorFunctions.setAccelerationTime(90) #9s
    motorFunctions.setSpeed(900) #900rpm
    motorFunctions.startMotorReverse()
    time.sleep(9) #accelerate for 9s
    time.sleep(30) #maintain speed for 30s TODO: add sensors, may need
    motorFunctions.setSmallDecelerationTime(0.4) #0.4s 
    motorFunctions.setSpeed(860) #860rpm
    time.sleep(0.4) #decelerate for 0.4s TODO: add sensors
    time.sleep(10) #maintain speed for 10s TODO: sensors
    motorFunctions.setDecelerationTime(90) #9s deceleration time
    motorFunctions.setSpeed(500) #500rpm
    time.sleep(9) #decelerate for 9s TODO: sensors
    time.sleep(30) #maintain speed for 10s
    motorFunctions.setSmallDecelerationTime(0.4) #0.4s
    motorFunctions.setSpeed(460) #460rpm
    time.sleep(0.4) #decelerate for 0.4s TODO: sensors
    time.sleep(10) #maintain speed for 10s TODO: sensors
    motorFunctions.setDecelerationTime(90) #9s
    motorFunctions.setSpeed100() #100rpm
    time.sleep(9) #decelerate for 9s
    time.sleep(30) #maintain speed for 30s TODO: sensors
    motorFunctions.setSmallDecelerationTime(0.4) #0.4s
    motorFunctions.setSpeed60() #60rpm
    time.sleep(0.4) #decelerate for 0.4s TODO: sensors
    time.sleep(10) #maintain speed for 10s
    motorFunctions.setDecelerationTime(15) #1.5s
    motorFunctions.stopMotor()
    time.sleep(1.5) #decelerate for 1.5s
    print("Test 3 finished")
    
    
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

    #SET FAILURE MODE WHEN IT OCCURS IN TEST AND BREAK
    #FOR NOW ALWAYS SUCCESS

    print("SET TO SUCCESS")
    resultByIDDao.ResultByIDDao.setTestStatus(4) #SUCCESS
    StartPage.status = StartPage.getStatus()
    StartPage.progress_label.configure(text=settings.languageList[1][settings.language] + ' ' + StartPage.status)



