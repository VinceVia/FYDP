import time
import resultByIDDao
import settings

def fakeMotorRoutine(StartPage):
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

