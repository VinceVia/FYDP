import time
import resultByIDDao
import settings
import motorFunctions

def fakeMotorRoutine(StartPage):
	basetime = time.time()
	#TODO Create some kind of logging file

	print("Starting Test 1")
	motorFunctions.setAccelerationAndTargetSpeed(100, 900, "1A", basetime)
	motorFunctions.holdVelocityForTime(30, "1A", basetime) #1 min but should be 10
	motorFunctions.setAccelerationAndTargetSpeed(-25, 0, "1A", basetime)

	motorFunctions.holdVelocityForTime(10, "1A", basetime)

	motorFunctions.setAccelerationAndTargetSpeed(-100, -900, "1B", basetime)
	motorFunctions.holdVelocityForTime(30, "1B", basetime)
	motorFunctions.setAccelerationAndTargetSpeed(25, 0, "1B", basetime)
	print("Test 1 Complete")
	
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

