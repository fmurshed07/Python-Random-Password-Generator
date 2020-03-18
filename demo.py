# print(ord("a"))
# nums = [1,7,8,53,1,232,43,5,46,3,2,1,3]
# # nums.sort()
# # nums.reverse()
# nums.sort(reverse = True)
# print(nums)

# chars = ["p","y","t","h","o","n"]
# chars.sort()
# print(chars)

# mixed = [53,1,232,"t","h","o","n",43,5,46,3,2]
# mixed.sort()
# print(mixed)

# chars = ["p","y","t","h","o","n"]
# nums = [1,7,8,53,1,232]
# chars.extend(nums)
# print(chars)
# print(nums)

# nums = (1,7,8,53,1,232)
# print(nums[2:4])

# a,b = 10,20,30
# print(a)

# nums = (1,7,8,53,1,232)
# for i in nums:
# 	print(i, end="")

# chars = ["p","y","t","h","o","n"]
# nums = (1,7,8,53,1,232)

# fees = (10,30,25,40,50)
# fees = list(fees)
# print(type(fees))
# fees[2] = 200
# fees = tuple(fees)
# print(type(fees))
# print(fees)

# t1 = (4,6,"python",3,"php",)
# nums = [i for i in range(1,11)]
# print(nums)

# def avgnums(a,b,*args): # variable length parameters
# 	res = (a+b+sum(args)) // (2+len(args))
# 	print(res)
# avgnums(10,30,40,50)
# avgnums(10,20)
# avgnums()
# avgnums(10)

# def login(user,pwd,**kwargs):
# 	print("user name is "+ user )
# 	print("password name is "+ pwd )
# 	print(kwargs)

# login("khan","32153")
# login(pwd = "3984723",user = "john")
# login("jane","3784578",role="ceo")

# def hello():
# 	print("hi")
# 	# return 100

# def bye():
# 	print("bye")
# 	return hello()
# print(bye())
# print(type(bye()))


# class company:
# 	cname = "digitallync"
# 	caddress = "hyd"
# 	count = 10 

# 	def __init__(self,emp_name,emp_sal,emp_role):
# 		print("employee name is "+ emp_name)
# 		print("employee role is "+ emp_role)
# 		print("employee salary is "+ emp_sal)
# 		company.count += 1

# 	# def printer(self):
# 	# 	print("employee name is "+ self.emp_name)
# 	# 	print("employee role is "+ self.emp_role)
# 	# 	print("employee salary is "+ self.emp_sal)

# emp1 = company("khan","1","pd") # 1 __init__
# emp2 = company("john","3","d") # 2 __init__
# emp3 = company("jane","4","p") # 3 __init__
# # emp4 = company() # 4 __init__ --> 3 parameters
# emp4 = company("harry","1","c") # 4 __init__ --> 3 parameters

# print(company.count)
# # # emp2.printer()


# class company:
# 	# class variables
# 	cname = "digitallync"
# 	caddress = "hyd"
# 	count = 10 

# 	def __init__(self,emp_name,emp_sal,emp_role):
# 		self.emp_name = emp_name
# 		self.emp_role = emp_role
# 		self.emp_sal = emp_sal
# 		company.count += 1

# 	def printer(self):
# 		print("employee name is "+ self.emp_name)
# 		print("employee role is "+ self.emp_role)
# 		print("employee salary is "+ self.emp_sal)

# 	@classmethod
# 	def changeCname(cls,newname):
# 		company.cname = newname
# 		print("company name changed")

# 	@staticmethod
# 	def calc(num,perc):
# 		res = num + (num*perc)
# 		print(res)

# emp1 = company("khan","1","pd") 
# emp2 = company("john","3","d") 
# emp3 = company("jane","4","p")
# emp4 = company("jane","4","p")

# print(company.count)
# emp2.printer()

# print(company.cname)
# company.changeCname("DL")
# print(company.cname)
# print(emp1.cname)

# emp1.calc(100,0.2)

# class company:
# 	cname = "digitallync"
# 	caddress = "hyd"
# 	count = 10 

# 	def __init__(self,emp_name,emp_sal,emp_role):
# 		self.emp_name = emp_name
# 		self.emp_role = emp_role
# 		self.emp_sal = emp_sal
# 		company.count += 1

# class organization(company):
# 	org_name = "DL"
# 	ord_loc = "Mumbai"
# 	org_count = 30
# 	super() .__init__
# # c1 = company()
# o1 = organization("khan","1","pd")

# import time
# import threading
# a = [3,4,5,6]

# def square(a):
# 	for i in a:
# 		time.sleep(0.2)
# 		print(i**2)

# def cube(a):
# 	for i in a:
# 		time.sleep(0.5)
# 		print(i**3)

# t = time.time()
# # print(t)
# square(a)
# cube(a)
# print("Time taken to execute: ", time.time() - t)

# import PyMySQL
# conn = PyMySQL.connect()


# for i in range(10):
# 	print(i)

# l1 = [10,20,30,40]
# i = iter(l1)
# print(i)
# print(i.__next__())
# print(i.__next__())
# print(i.__next__())
# print(i.__next__())
# print(i.__next__())

# class sqrange:
# 	def __init__(self,n):
# 		self.n = n
# 	def __iter__(self):
# 		self.i = 0
# 		return self
# 	def __next__(self):
# 		if self.i <= self.n:
# 			res = self.i ** 2
# 			self.i += 1
# 			return res
# 		else:
# 			raise StopIteration

# for i in sqrange(5):
# 	print(i)

# fo = open("demo.txt","a")
# fo.write("python\n")
# fo.write("java\n")
# fo.write("digitallync\n")

# l1 = ["10","20","30"]
# fo.writelines(l1)

# fo.close()

# fo = open("demo.txt","r") # cp = 0 
# print(fo.readlines(20))
# print(fo.readline())
# print(fo.readline())

# fo.close()

# class company:
# 	# class variables
# 	cname = "digitallync"
# 	caddress = "hyd"
# 	count = 10 
# emp1 = company()
# emp2 = company()

# print(company.cname)
# print(emp1.cname)
# print(emp2.cname)
# emp1.cname = "Digital"
# emp2.cname = "DL"
# print(company.cname)
# print(emp1.cname)
# print(emp2.cname)
# company.cname = "DLync"
# print(company.cname)
# print(emp1.cname)
# print(emp2.cname)

nums = {1:20,3:23,"python":2.7,"city":"hyd"}

# for i in nums.keys():
# 	print (i)

# for i in nums.values():
# 	print (i)

# for i in nums.items():
# 	print (i)

# print(nums.keys())
# print(nums.values())
# print(nums.items())

# enter a number 
# 10
# {1:1 ,2:4 ,3:9 . .. 10:100}

# n = 10
# d = {}
# for i in range(1,n+1):
# 	d[i] = i**2
# print(d)

# enter a statement
# "python is easy"
# {python:6,is:2,easy:4}

# stmt = "python is easy"
# d = {}
# for i in stmt.split():
# 	d[i] = len(i)
# print(d)

# nums = {1:20,3:23,"python":2.7,"city":"hyd"}
# print(nums)

# nums.pop(1)
# print(nums)

# import random
# for i in range(500):
# 	r = random.randrange(255)
# 	it = r%10
# 	print(r,' ',it)

import numpy as np
np.random.seed(100)
x = np.random.randint(10,100,8)
print(x)