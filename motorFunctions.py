import time
import resultByIDDao
import detailedResultsDao
import settings
import serial
import minimalmodbus
from RPi import GPIO
from time import sleep
import math

B = 17
A = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(B, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(A, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

counter = 0
clkLastState = GPIO.input(B)
dtLastState = GPIO.input(A)

#instr = minimalmodbus.Instrument('/dev/ttyUSB0', 1)
#instr.debug = True
#instr.serial.parity = serial.PARITY_EVEN

velocity = 0
basetime = time.time()

# def getVelocity():
# 	global velocity
# 	if(velocity == None):
# 		velocity=0
# 	return velocity

def connectVFD():
    try:
        instr = minimalmodbus.Instrument('/dev/ttyUSB0',1)
        instr.debug = True #TODO:comment this out after testing is done
        instr.serial.parity = serial.PARITY_EVEN
    except IOError:
        print("Failed to connect to VFD")

def calculateSpeed(numOfPulses, sampleTime):
    N=1000
    w = (2*numOfPulses*math.pi)/(N*sampleTime)
    RPM = w*9.55
    print(RPM)

def getVelocity(numOfPulses, sampleTime):
	try:
		start = time.time()
		while counter<50000:
			clkState = GPIO.input(B)
			dtState = GPIO.input(A)
			if(clkState != clkLastState or dtState != dtLastState):
				counter += 1
				clkLastState = clkState
				dtLastState = dtState
			timeElapsed=(time.time() - start)
			pulses=(counter/5)
			calculateSpeed(pulses, timeElapsed)
	finally:
		GPIO.cleanup()

def getPressure():
	return(0)

def getOverHeat():
	return(0)

def writeRow(velocity, basetime, testSection):
	elapsedTime = time.time() - basetime
	pressure = getPressure()
	overheat = getOverHeat()
	testNumber = resultByIDDao.ResultByIDDao.get_test_number()[0]
	sensorID = resultByIDDao.ResultByIDDao.get_sensor_id(testNumber)[0]
	detailedResultsDao.DetailedResultsDao.setNewRow(velocity, elapsedTime, time.time(), sensorID, pressure, testSection, overheat)

def setSpeed(targetSpeed): #VFD register S01
	#velocity = int(targetSpeed*(20000/60))
    frequency = 0.056891*targetSpeed - 6.385283 #from experiment, see graph Motor_RPM_vs_VFD_Frequency_trend.ods
    try:
        instr.write_register(1793, frequency, functioncode=6)
    except IOError:
        print("Failed to set frequency S01")

def startMotorForward(): #VFD register S06
    try:
        instr.write_register(1798, 1, functioncode=6)
    except IOError:
        print("Failed to set motor forward S06")

def startMotorReverse(): #VFD register S06
    try:
        instr.write_register(1798, 2, functioncode=6)
    except IOError:
        print("Failed to set motor reverse S06")

def stopMotor(): #VFD register S06
    try:
        instr.write_register(1798, 0, functioncode=6)
    except IOError:
        print("Failed to stop motor S06")

def setAccelerationTime(accelerationTime): #VFD register S08
        try:
            instr.write_register(1800, accelerationTime, functioncode=6)
        except IOError:
            print("Failed to set acceleration time S08")

def setDecelerationTime(decelerationTime): #VFD register S09
    try: 
        instr.write_register(1801, decelerationTime, functioncode=6)
    except IOError:
        print("Failed to set deceleration time S09")


#def setAccelerationAndTargetSpeed(acceleration, targetSpeed, testSection, basetime):
#	global velocity
#	print("Setting Acceleration to: " + str(acceleration) + " and Target Speed to: " + str(targetSpeed))
#	velocity = getVelocity()
#	timeSinceLastRow = time.time()
#
#	#THIS CAN BE CLEANED UP ONCE REAL SPEED IS BEING READ
#	if(acceleration > 0):
#		while(velocity < targetSpeed):
#			if(time.time() - timeSinceLastRow > 0.2):
#				velocity += (acceleration/10)
#				timeSinceLastRow = time.time()
#				writeRow(velocity, basetime, testSection)
#	else:
#		while(velocity > targetSpeed):
#			if(time.time() - timeSinceLastRow > 0.2):
#				velocity += (acceleration/10)
#				timeSinceLastRow = time.time()
#				writeRow(velocity, basetime, testSection)
#
#
#def holdVelocityForTime(holdTime, testSection, basetime):
#	global velocity
#	print("Holding for: " + str(holdTime) + " s")
#	velocity = getVelocity()
#	timeSinceLastRow = time.time()
#	baseTimeOfHold = time.time()
#	while(time.time() - baseTimeOfHold < holdTime):
#		if(time.time() - timeSinceLastRow > 0.2):
#			timeSinceLastRow = time.time()
#			writeRow(velocity, basetime, testSection)

	#TODO
