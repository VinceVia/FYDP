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

instr = minimalmodbus.Instrument('/dev/ttyUSB0', 1)
instr.debug = True
instr.serial.parity = serial.PARITY_EVEN

velocity = 0
basetime = time.time()

# def getVelocity():
# 	global velocity
# 	if(velocity == None):
# 		velocity=0
# 	return velocity

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

def setSpeed(targetSpeed):

	try:
		instr.write_register(1793, velocity, numberOfDecimals=0, functioncode=6, signed=False)
	except IOError:
		print("Failed to set motor forward")

def startMotorForward():
	try:
		instr.write_register(1798, 1, numberOfDecimals=1, functioncode=6, signed=False)
	except IOError:
		print("Failed to set motor forward")

def startMotorReverse():
	try:
		instr.write_register(1798, 1, numberOfDecimals=2, functioncode=6, signed=False)
	except IOError:
		print("Failed to set motor reverse")

def stopMotor():
	try:
		instr.write_register(1798, 1, numberOfDecimals=0, functioncode=6, signed=False)
	except IOError:
		print("Failed to set motor forward")

def setAccelerationAndTargetSpeed(acceleration, targetSpeed, testSection, basetime):
	global velocity
	print("Setting Acceleration to: " + str(acceleration) + " and Target Speed to: " + str(targetSpeed))
	velocity = getVelocity()
	timeSinceLastRow = time.time()

	#THIS CAN BE CLEANED UP ONCE REAL SPEED IS BEING READ
	if(acceleration > 0):
		while(velocity < targetSpeed):
			if(time.time() - timeSinceLastRow > 0.2):
				velocity += (acceleration/10)
				timeSinceLastRow = time.time()
				writeRow(velocity, basetime, testSection)
	else:
		while(velocity > targetSpeed):
			if(time.time() - timeSinceLastRow > 0.2):
				velocity += (acceleration/10)
				timeSinceLastRow = time.time()
				writeRow(velocity, basetime, testSection)


def holdVelocityForTime(holdTime, testSection, basetime):
	global velocity
	print("Holding for: " + str(holdTime) + " s")
	velocity = getVelocity()
	timeSinceLastRow = time.time()
	baseTimeOfHold = time.time()
	while(time.time() - baseTimeOfHold < holdTime):
		if(time.time() - timeSinceLastRow > 0.2):
			timeSinceLastRow = time.time()
			writeRow(velocity, basetime, testSection)

	#TODO