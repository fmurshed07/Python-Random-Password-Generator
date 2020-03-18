# connpy.py

import pymysql
import dbparser

creds = dbparser.getcreds()
conn = pymysql.connect(*creds)
cur = conn.cursor()
createTable = '''create table if not exists students(
	rno int(32) ,
	name varchar(64) ,
	standard varchar(16) ,
	fee_status tinyint ,
	email varchar(32)
	);'''
cur.execute(createTable)
insertquery = '''insert into students(name,email) 
				values ("khan","khan@g.com");'''
cur.execute(insertquery)
conn.commit()
conn.close()