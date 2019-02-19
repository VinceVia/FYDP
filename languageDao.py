import dao
import settings

class LanguageDao:
	def get_strings():
		database = dao.Database('fydp')
		database.execute("SELECT * FROM language")
		settings.languageList = database.fetchall()
