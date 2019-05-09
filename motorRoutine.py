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
        motorFunctions.setAccelerationTime(900) #9s
        motorFunctions.setSpeed(900) #900rpm target speed
        motorFunctions.startMotorForward()
        time.sleep(9) #accelerate for 9s
        time.sleep(600) #maintain speed for 10min TODO: add sensors
        motorFunctions.setDecelerationTime(1060) #36s
        motorFunctions.setSpeed(0) #0rpm
        motorFunctions.stopMotor() #TODO: check if this uses the right deceleration rate, change to startMotorForwards() with target speed 0 if not
        time.sleep(36) #decelerate for 36s 
        print("Test 1 - Anticlockwise direction")
        #motorFunctions.setAccelerationTime(900) #9s acceleration time - should be already set from before
        motorFunctions.setSpeed(900) #900rpm target speed
        motorFunctions.startMotorBackward()
        time.sleep(9) #accelerate for 9s
        time.sleep(600) #maintain speed for 10min TODO: add sensors
        #motorFunctions.setDecelerationTime(1060) #36s deceleration time - already set
        motorFunctions.setSpeed(0) #0rpm
        motorFunctions.stopMotor() #TODO: check if this uses the right deceleration rate, change to startMotorBackwards() with target speed 0 if not
        time.sleep(36) #decelerate for 36s 
        print("Test 1 finished")

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
        
        print("Starting Test 3: Short Skid Tests")
        print("Test 3 - Clockwise direction")
        motorFunctions.setAccelerationTime(900) #9s
        motorFunctions.setSpeed(900) #900rpm
        motorFunctions.startMotorForward()
        time.sleep(9) #accelerate for 9s
        time.sleep(30) #maintain speed for 30s TODO: add sensors, may need
        motorFunctions.setDecelerationTime(40) #0.4s 
        motorFunctions.setSpeed(860) #860rpm
        time.sleep(0.4) #decelerate for 0.4s TODO: add sensors
        time.sleep(10) #maintain speed for 10s TODO: sensors
        motorFunctions.setDecelerationTime(900) #9s deceleration time
        motorFunctions.setSpeed(500) #500rpm
        time.sleep(9) #decelerate for 9s TODO: sensors
        time.sleep(30) #maintain speed for 10s
        motorFunctions.setDecelerationTime(40) #0.4s
        motorFunctions.setSpeed(460) #460rpm
        time.sleep(0.4) #decelerate for 0.4s TODO: sensors
        time.sleep(10) #maintain speed for 10s TODO: sensors
        motorFunctions.setDecelerationTime(900) #9s
        motorFunctions.setSpeed(100) #100rpm
        time.sleep(9) #decelerate for 9s
        time.sleep(30) #maintain speed for 30s TODO: sensors
        motorFunctions.setDecelerationTime(40) #0.4s
        motorFunctions.setSpeed(60) #60rpm
        time.sleep(0.4) #decelerate for 0.4s TODO: sensors
        time.sleep(10) #maintain speed for 10s
        motorFunctions.setDecelerationTime(150) #1.5s
        motorFunctions.setSpeed(0) #0rpm
        time.sleep(1.5) #decelerate for 1.5s
        motorFunctions.stopMotor()
        print("Test 3 - Anticlockwise direction")
        motorFunctions.setAccelerationTime(900) #9s
        motorFunctions.setSpeed(900) #900rpm
        motorFunctions.startMotorBackward()
        time.sleep(9) #accelerate for 9s
        time.sleep(30) #maintain speed for 30s TODO: add sensors, may need
        motorFunctions.setDecelerationTime(40) #0.4s 
        motorFunctions.setSpeed(860) #860rpm
        time.sleep(0.4) #decelerate for 0.4s TODO: add sensors
        time.sleep(10) #maintain speed for 10s TODO: sensors
        motorFunctions.setDecelerationTime(900) #9s deceleration time
        motorFunctions.setSpeed(500) #500rpm
        time.sleep(9) #decelerate for 9s TODO: sensors
        time.sleep(30) #maintain speed for 10s
        motorFunctions.setDecelerationTime(40) #0.4s
        motorFunctions.setSpeed(460) #460rpm
        time.sleep(0.4) #decelerate for 0.4s TODO: sensors
        time.sleep(10) #maintain speed for 10s TODO: sensors
        motorFunctions.setDecelerationTime(900) #9s
        motorFunctions.setSpeed(100) #100rpm
        time.sleep(9) #decelerate for 9s
        time.sleep(30) #maintain speed for 30s TODO: sensors
        motorFunctions.setDecelerationTime(40) #0.4s
        motorFunctions.setSpeed(60) #60rpm
        time.sleep(0.4) #decelerate for 0.4s TODO: sensors
        time.sleep(10) #maintain speed for 10s
        motorFunctions.setDecelerationTime(150) #1.5s
        motorFunctions.setSpeed(0) #0rpm
        time.sleep(1.5) #decelerate for 1.5s
        motorFunctions.stopMotor()
        print("Test 3 finished")

        print("Starting Test 4: Insensitivity Test")
        print("Test 4 - Clockwise direction")
        motorFunctions.setAccelerationTime(900) #9s
        motorFunctions.setSpeed(900) #900rpm
        motorFunctions.startMotorForward()
        time.sleep(9) #accelerate for 9s
        time.sleep(30) #maintain speed for 30s TODO: add sensors
        motorFunctions.setDecelerationTime(1149) #12.5s
        motorFunctions.setSpeed(0) 
        time.sleep(12.5) #decelerate for 12.5s
        motorFunctions.stopMotor()
        print("Test 4 - Anticlockwise direction")
        motorFunctions.setAccelerationTime(900) #9s
        motorFunctions.setSpeed(900) #900rpm
        motorFunctions.startMotorBackward()
        time.sleep(9) #accelerate for 9s
        time.sleep(30) #maintain speed for 30s TODO: add sensors
        motorFunctions.setDecelerationTime(1149) #12.5s
        motorFunctions.setSpeed(0) 
        time.sleep(12.5) #decelerate for 12.5s
        motorFunctions.stopMotor()

        #motorFunctions.setSpeed(900)
	#motorFunctions.startMotorForward()
	#startTime = time.time()
	#while(True):
	
	#	if((time.time() - startTime) > 10):
	#		break
	#motorFunctions.stopMotor() 
	#motorFunctions.holdVelocityForTime(30, "1A", basetime) #1 min but should be 10
	#motorFunctions.setAccelerationAndTargetSpeed(-25, 0, "1A", basetime)

	#motorFunctions.holdVelocityForTime(10, "1A", basetime)

	#motorFunctions.setAccelerationAndTargetSpeed(-100, -900, "1B", basetime)
	#motorFunctions.holdVelocityForTime(30, "1B", basetime)
	#motorFunctions.setAccelerationAndTargetSpeed(25, 0, "1B", basetime)
	#print("Test 1 Complete")
	
	#motorFunctions.holdVelocityForTime(10, "1B", basetime)

	# print("Starting Test 2")
	# motorFunctions.setAccelerationAndTargetSpeed(100, 900, "2A", basetime)
	# motorFunctions.holdVelocityForTime(30, "2A", basetime)
	# motorFunctions.setAccelerationAndTargetSpeed(-100, 0, "2A", basetime)

	# motorFunctions.holdVelocityForTime(30, "2A", basetime)

	# motorFunctions.setAccelerationAndTargetSpeed(-100, -900, "2B", basetime)
	# motorFunctions.holdVelocityForTime(30, "1A", basetime)
	# motorFunctions.setAccelerationAndTargetSpeed(100, 0, "2B", basetime)
	# print("Finished Test 2")

	# motorFunctions.holdVelocityForTime(30, "2B", basetime)

	# print("Starting Test 3")
	# motorFunctions.setAccelerationAndTargetSpeed(100, 900, "3A", basetime)
	# motorFunctions.holdVelocityForTime(30, "3A", basetime)
	# motorFunctions.setAccelerationAndTargetSpeed(-100, 860, "3A", basetime)
	# motorFunctions.holdVelocityForTime(10, "3A", basetime)
	# motorFunctions.setAccelerationAndTargetSpeed(-40, 500, "3A", basetime)
	# motorFunctions.holdVelocityForTime(30, "3A", basetime)
	# motorFunctions.setAccelerationAndTargetSpeed(-100, 460, "3A", basetime)
	# motorFunctions.holdVelocityForTime(10, "3A", basetime)
	# motorFunctions.setAcelerationAndTargetSpeed(-40, 100, "3A", basetime)
	# motorFunctions.holdVelocityForTime(30, "3A", basetime)
	# motorFunctions.setAccelerationAndTargetSpeed(-100, 60, "3A", basetime)
	# motorFunctions.holdVelocityForTime(10, "3A", basetime)
	# motorFunctions.setAccelerationAndTargetSpeed(-40, 0, "3A", basetime)
	
	# motorFunctions.holdVelocityForTime(10, "3A", basetime)

	# motorFunctions.setAccelerationAndTargetSpeed(-100, -900, "3B", basetime)
	# motorFunctions.holdVelocityForTime(30, "3B", basetime)
	# motorFunctions.setAccelerationAndTargetSpeed(100, -860, "3B", basetime)
	# motorFunctions.holdVelocityForTime(30, "3B", basetime)
	# motorFunctions.setAccelerationAndTargetSpeed(40, -500, "3B", basetime)
	# motorFunctions.holdVelocityForTime(30, "3B", basetime)
	# motorFunctions.setAccelerationAndTargetSpeed(100, -460)
	# motorFunctions.holdVelocityForTime(30, "3B", basetime)
	# motorFunctions.setAccelerationAndTargetSpeed(40, -100, "3B", basetime)
	# motorFunctions.holdVelocityForTime(30, "3B", basetime)
	# motorFunctions.setAccelerationAndTargetSpeed(100, -60)
	# motorFunctions.holdVelocityForTime(10, "3B", basetime)
	# motorFunctions.setAccelerationAndTargetSpeed(40, -0, "3B", basetime)
	# print("Finished Test 3")
	
	#motorFunctions.holdVelocityForTime(10, "3B", basetime)

	# print("Starting Test 4")
	# motorFunctions.setAccelerationAndTargetSpeed(100, 900, "4A", basetime)
	# motorFunctions.holdVelocityForTime(30, "4A", basetime)
	# motorFunctions.setAccelerationAndTargetSpeed(-72, 0, "4A", basetime)
	
	#motorFunctions.holdVelocityForTime(10, "4A", basetime)

	# motorFunctions.setAccelerationAndTargetSpeed(-100, -900, "4B", basetime)
	# motorFunctions.holdVelocityForTime(30, "4A", basetime)
	# motorFunctions.setAccelerationAndTargetSpeed(72, 0, "4B", basetime)
	# print("Finished Test 4")
	# #Some pause inbetween tests

	#motorFunctions.holdVelocityForTime(30, "1A", basetime)

	#SET FAILURE MODE WHEN IT OCCURS IN TEST AND BREAK
	#FOR NOW ALWAYS SUCCESS
	
        print("SET TO SUCCESS")
        resultByIDDao.ResultByIDDao.setTestStatus(4) #SUCCESS
        StartPage.status = StartPage.getStatus()
        StartPage.progress_label.configure(text=settings.languageList[1][settings.language] + ' ' + StartPage.status)

# 1. RUN-IN, OPERATING TEMPERATURE AND VIBRATION TEST
# 	a.	Accelerate to 900 RPM clockwise at a rate of 100 RPM/s
# 	b.	Maintain speed for 10 min. MUST NOT GET WARM, MUST NOT VIBRATE OR FLUCTUATE, NUST NOT ACTIVATE, LEAK AIR OR ACTIVATE.
# 	c.	Decelerate to 0 RPM at a rate of -25 RPM/s
# 	d.	Redo test in counter clockwise direction
# 2. SEVERE SKID SENSITIVITY TEST
# 	a.	Accelerate to 900 RPM clockwise at a rate of 100 RPM/s
# 	b.	Maintain speed for 30 seconds
# 	c.	Decelerate to 0 RPM at a rate of -100 RPM/s (tol: -0 +5). DEVICE MUST REACT AND EXAUST AIR CONSTANTLY THROUGHOUT THE DECELERATION INTERVAL BETWEEN 850 RPM AND 50 RPM
# 	d.	Redo test in counter clockwise direction
# 3. SHORT SKID TESTs
# 	a.	Accelerate to 900 RPM clockwise at a rate of 100 RPM/s
# 	b.	Maintain speed for 30 seconds
# 	c.	Decelerate to 860 RPM at a rate of -100 RPM/s (tol: -0 +5) (0,4s). DEVICE MUST EXHAUST BRIEFLY (LESS THAN 1 SEC.)
# 	d.	Maintain speed for 10 seconds
# 	e.	Decelerate to 500 RPM at a rate of -40 RPM/s.
# 	f.	Maintain speed for 30 seconds
# 	g.	Decelerate to 460 RPM at a rate of -100 RPM/s (tol: -0 +5) (0,4s). DEVICE MUST EXHAUST BRIEFLY (LESS THAN 1 SEC.)
# 	h.	Maintain speed for 10 seconds
# 	i.	Decelerate to 100 RPM at a rate of -40 RPM/s.
# 	j.	Maintain speed for 30 seconds
# 	k.	Decelerate to 60 RPM at a rate of -100 RPM/s (tol: -0 +5) (0,4s). DEVICE MUST EXAHUST BRIEFLY (LESS THAN 1 SEC.)
# 	l.	Maintain speed for 10 seconds
# 	m.	Decelerate to 0 RPM at a rate of -40 RPM/s.
# 	n.	Redo tests in counter clockwise direction
# 4. INSENSITIVITY TEST
# 	a.	Accelerate to 900 RPM clockwise at a rate of 100 RPM/s
# 	b.	Maintain speed for 30 seconds
# 	c.	Decelerate to 0 RPM at a rate of -72 RPM/s (tol: -5 +0). DEVICE MUST NOT EXAUST AIR THROUGHOUT THE DECELERATION INTERVAL BETWEEN 800 RPM AND 200 RPM
# 	d.	Redo test in counter clockwise direction

