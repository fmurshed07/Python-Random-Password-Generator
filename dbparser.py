from configparser import ConfigParser 
def getcreds(file="config.ini",section="mysql"):
	db = {}

	parser = ConfigParser()
	parser.read(file)

	if parser.has_section(section):
		items = parser.items(section)
		# print(items)
		for i in items:
			db[i[0]] = i[1]
	return db
print(getcreds())