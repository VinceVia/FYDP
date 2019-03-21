import dao
import settings

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

	def get_first_id_by_test_id(test_number):
		database = dao.Database('fydp')
		database.execute("SELECT id FROM detailed_results WHERE test_id=(?) AND time=(?)", (test_number, 0,))
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
