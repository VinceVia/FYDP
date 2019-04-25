import dao
import settings

class ResultByIDDao:
	def get_test_number():
		database = dao.Database('fydp')
		database.execute("SELECT id FROM result_by_id ORDER BY ID DESC LIMIT 1")
		return [item[0] for item in database.fetchall()]

	def get_test_passed(test_number):
		database = dao.Database('fydp')
		database.execute("SELECT test_passed FROM result_by_id WHERE id=(?)", (test_number,))
		return [item[0] for item in database.fetchall()]

	def get_test_status(test_number):
		database = dao.Database('fydp')
		database.execute("SELECT test_status FROM result_by_id WHERE id=(?)", (test_number,))
		return [item[0] for item in database.fetchall()]

	def get_failure_mode(test_number):
		database = dao.Database('fydp')
		database.execute("SELECT failure_mode FROM result_by_id WHERE id=(?)", (test_number,))
		return [item[0] for item in database.fetchall()]

	def set_test_status():
		database = dao.Database('fydp')
		database.execute("SELECT test_status FROM result_by_id WHERE id=(?)", (settings.test_number,))
		return [item[0] for item in database.fetchall()]

	def get_table():
		database = dao.Database('fydp')
		database.execute("SELECT * FROM result_by_id")
		return database.fetchall()

	def get_sensor_id(test_number):
		database = dao.Database('fydp')
		database.execute("SELECT sensor_id FROM result_by_id WHERE id=(?)", (test_number,))
		return [item[0] for item in database.fetchall()]

	def setSensorID(sensorID):
		database = dao.Database('fydp')
		database.execute("UPDATE result_by_id SET sensor_id=(?) WHERE id=(?)", (sensorID, settings.test_number,))
		database.commit()

	def setTestStatus(testStatus):
		database = dao.Database('fydp')
		database.execute("UPDATE result_by_id SET test_status=(?) WHERE id=(?)", (testStatus, settings.test_number,))
		database.commit()

	def setNewRow():
		database = dao.Database('fydp')
		database.execute("INSERT INTO result_by_id(id, sensor_id, test_status, failure_mode) VALUES (?, ? , ?, ?)", (settings.test_number + 1, None, 0, 0))
		database.commit()

	def clearDatabase():
		database = dao.Database('fydp')
		database.execute("DELETE FROM result_by_id")
		database.commit()
