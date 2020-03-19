import random

d = {}
def checkUser(user):
	if user in d.keys():
		return 0 
	else:
		return 1 
def gennums(n):
	s = ""
	for i in range(n):
		s = s + str(random.randrange(0,9))
	return s 
def genchars(n):
	s = ""
	for i in range(n):
		s = s + chr(random.randrange(ord("a"),ord("z")))
	return s 
def genpwd(user):
	if checkUser(user) == 0:
		print("user already exists")
	else:
		password = gennums(4)+genchars(4)+gennums(4)+genchars(4)
		d[user] = password
		print(password)
genpwd("khan")
genpwd("john")
genpwd("jane")
genpwd("hari")
genpwd("john")
genpwd("harry")