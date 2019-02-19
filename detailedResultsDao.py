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

	def get_table():
		database = dao.Database('fydp')
		database.execute("SELECT * FROM detailed_results")
		return database.fetchall()
