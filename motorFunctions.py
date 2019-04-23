import time
import resultByIDDao
import detailedResultsDao
import settings

velocity = 0
basetime = time.time()

def getVelocity():
	global velocity
	if(velocity == None):
		velocity=0
	return velocity

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