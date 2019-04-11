import mysql.connector
from mysql.connector import errorcode

config = {
	'user': 'dbuser',
	'password': 'Goldilocks!23',
	'host': '10.0.10.211',
	'database': 'cords',
	'raise_on_warnings': True,
}


try:
	cnx = mysql.connector.connect(**config)
	cursor = cnx.cursor()

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

