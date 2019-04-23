import dao
import settings
import time

class DetailedResultsDao:
	def get_velocities(test_number):
		database = dao.Database('fydp')
		num = settings.test_number
		database.execute("SELECT velocity FROM detailed_results WHERE test_id=(?)", (test_number,))
		return [item[0] for item in database.fetchall()]

	def get_times(test_number):
		database = dao.Database('fydp')
		database.execute("SELECT time FROM detailed_results WHERE test_id=(?)", (test_number,))
		return [item[0] for item in database.fetchall()]

	def get_overheat(test_number):
		database = dao.Database('fydp')
		database.execute("SELECT overheat FROM detailed_results WHERE test_id=(?)", (test_number,))
		return [item[0] for item in database.fetchall()]

	def get_pressure_by_test_section(test_number, test_section):
		database = dao.Database('fydp')
		database.execute("SELECT pressure FROM detailed_results WHERE test_id=(?) AND test_section=(?)", (test_number, test_section,))
		return [item[0] for item in database.fetchall()]

	def get_times_activated(test_number):
		database = dao.Database('fydp')
		database.execute("SELECT time FROM detailed_results WHERE test_id=(?) AND pressure=(?)", (test_number, 1,))
		return [item[0] for item in database.fetchall()]

	def get_times_overheated(test_number):
		database = dao.Database('fydp')
		database.execute("SELECT time FROM detailed_results WHERE test_id=(?) AND overheat=(?)", (test_number, 1,))
		return [item[0] for item in database.fetchall()]

	def get_first_id_by_test_id(test_number):
		database = dao.Database('fydp')
		database.execute("SELECT id FROM detailed_results WHERE test_id=(?) AND time=(?)", (test_number, 0,))
		return [item[0] for item in database.fetchall()]

	def get_first_id_by_test_section(test_number, test_section):
		database = dao.Database('fydp')
		database.execute("SELECT id FROM detailed_results WHERE test_id=(?) AND test_section=(?) LIMIT 1", (test_number, test_section,))
		return [item[0] for item in database.fetchall()]

	def get_test_section_by_id(detailed_id):
		database = dao.Database('fydp')
		database.execute("SELECT test_section FROM detailed_results WHERE id=(?)", (detailed_id,))
		return [item[0] for item in database.fetchall()]

	def get_time_by_id(detailed_id):
		database = dao.Database('fydp')
		database.execute("SELECT time FROM detailed_results WHERE id=(?)", (detailed_id,))
		return [item[0] for item in database.fetchall()]

	def get_velocity_by_id(detailed_id):
		database = dao.Database('fydp')
		database.execute("SELECT velocity FROM detailed_results WHERE id=(?)", (detailed_id,))
		return [item[0] for item in database.fetchall()]

	def get_table():
		database = dao.Database('fydp')
		database.execute("SELECT * FROM detailed_results")
		return database.fetchall()

	def setNewRow(velocity, time, timestamp, sensor_id, pressure, test_section, overheat):
		database = dao.Database('fydp')
		database.execute("INSERT INTO detailed_results(id, test_id, velocity, time, timestamp, sensor_id, pressure, test_section, overheat) VALUES (? , ? , ?, ?, ?, ?, ?, ?, ?)", (None, settings.test_number, velocity, time, timestamp, sensor_id, pressure, test_section, overheat))
		database.commit()
