import time
velocity = 0

def getVelocity():
	global velocity
	if(velocity == None):
		velocity=0
	return velocity

def setAccelerationAndTargetSpeed(acceleration, targetSpeed):
	global velocity
	print("Setting Acceleration to: " + str(acceleration) + " and Target Speed to: " + str(targetSpeed))
	velocity = getVelocity()
	currentTime = time.time()
	while(velocity < targetSpeed):
		if(time.time() - currentTime > 0.1):
			velocity += (acceleration/10)
			currentTime = time.time()
			print("Velocity: " + str(velocity))

def setDeccelerationAndTargetSpeed(acceleration, targetSpeed):
	global velocity
	print("Setting Acceleration to: " + str(acceleration) + " and Target Speed to: " + str(targetSpeed))
	velocity = getVelocity()
	currentTime = time.time()
	velocity = getVelocity()
	print(velocity)
	print(targetSpeed)
	while(velocity > targetSpeed):
		if(time.time() - currentTime > 0.1):
			velocity += (acceleration/10)
			currentTime = time.time()
			print("Velocity: " + str(velocity))

	#TODO