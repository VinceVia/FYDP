import time
import resultByIDDao
import settings

def fakeMotorRoutine(StartPage):
	print("SET TO SUCCESS")
	resultByIDDao.ResultByIDDao.setTestStatus(4) #SUCCESS
	StartPage.status = StartPage.getStatus()
	StartPage.progress_label.configure(text=settings.languageList[1][settings.language] + ' ' + StartPage.status)
