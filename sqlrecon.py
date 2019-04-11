import mysql.connector, sys, getopt
from mysql.connector import errorcode

# we will grab the database IP from the commandline.  
db_ip = str(sys.argv[1])

config = {
	'user': 'dbuser',
	'password': 'Goldilocks!23',
	'host': db_ip,
	'database': 'cords',
	'raise_on_warnings': True,
}


try:
	cnx = mysql.connector.connect(**config)
	cursor = cnx.cursor()

	query = ("show tables where Tables_in_cords like 'c%'")
	
	cursor.execute(query)
	
	for table in cursor:
		print("Table - {}".format(table))
	
	print("==================================")
	
	query = ("select * from customers")
	
	cursor.execute(query)
	
	for customer in cursor:
		print("Customers data: {}".format(customer))
	
except mysql.connector.Error as err:
	if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("Something is wrong with your user name or password")
	elif err.errno == errorcode.ER_BAD_DB_ERROR:
		print("Database does not exist")
	else:
		print(err)
else:
	cursor.close()
	cnx.close()
