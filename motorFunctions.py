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

clkLastState = GPIO.input(B)
dtLastState = GPIO.input(A)

instr = minimalmodbus.Instrument('/dev/ttyUSB0', 1)
instr.debug = True
instr.serial.parity = serial.PARITY_EVEN

velocity = 0
#basetime = time.time()

# def getVelocity():
# 	global velocity
# 	if(velocity == None):
# 		velocity=0
# 	return velocity

def calculateSpeed(numOfPulses, sampleTime): #encoder measurement - part 2
	N=1000
	w = (2*numOfPulses*math.pi)/(N*sampleTime)
	RPM = w*9.55
	print(RPM)

def getVelocity(numOfPulses, sampleTime): #encoder measurement - part 1
#TODO: might need to adjust - inconsistent
	counter = 0

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
			pulses=(counter/5) #5 pulses per rotation, NOT 4
		calculateSpeed(pulses, timeElapsed)
	finally:
		GPIO.cleanup()

def getPressure(): #TODO: write this for airflow sensor
	return(0)

def getOverHeat(): #TODO: write this for temperature sensor
	return(0)

def writeRow(velocity, basetime, testSection):
	elapsedTime = time.time() - basetime
	pressure = getPressure()
	overheat = getOverHeat()
	testNumber = resultByIDDao.ResultByIDDao.get_test_number()[0]
	sensorID = resultByIDDao.ResultByIDDao.get_sensor_id(testNumber)[0]
	detailedResultsDao.DetailedResultsDao.setNewRow(velocity, elapsedTime, time.time(), sensorID, pressure, testSection, overheat)

def setVelocity(targetSpeed):
	velocity = int(targetSpeed*(20000/60))
	#TODO: convert target velocity to a frequency using chart, this is "velocity" var below
	try:
		instr.write_register(1793, velocity, numberOfDecimals=0, functioncode=6, signed=False)
	except IOError:
		print("Failed to set frequency")

def startMotorForward():
	try:
		instr.write_register(1798, 1, numberOfDecimals=0, functioncode=6, signed=False)
	except IOError:
		print("Failed to set motor forward")

def startMotorReverse():
	try:
		instr.write_register(1798, 2, numberOfDecimals=0, functioncode=6, signed=False)
	except IOError:
		print("Failed to set motor reverse")

def stopMotor():
	try:
		instr.write_register(1798, 0, numberOfDecimals=0, functioncode=6, signed=False)
	except IOError:
		print("Failed to set motor forward")

def setAccelerationAndTargetSpeed(acceleration, targetSpeed, testSection, basetime):
	global velocity
	print("Setting Acceleration to: " + str(acceleration) + " and Target Speed to: " + str(targetSpeed))
	velocity = getVelocity()
	timeSinceLastRow = time.time()

	#THIS CAN BE CLEANED UP ONCE REAL SPEED IS BEING READ
	#TODO: replace or remove this, as we will be reading velocity from the encoder
	if(acceleration > 0):
		while(velocity < targetSpeed):
			if(time.time() - timeSinceLastRow > 0.2):
				velocity += (acceleration/10)
				timeSinceLastRow = time.time()
				writeRow(velocity, basetime, testSection) #When you call this, you want to use getVelocity(), basetime from start and current 
	else:
		while(velocity > targetSpeed):
			if(time.time() - timeSinceLastRow > 0.2):
				velocity += (acceleration/10)
				timeSinceLastRow = time.time()
				writeRow(velocity, basetime, testSection)
