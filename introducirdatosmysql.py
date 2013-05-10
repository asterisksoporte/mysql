import csv
import MySQLdb

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='neosistec',
    db='astercdr')
cursor = mydb.cursor()

csv_data = csv.reader(file('salida.csv'))
for row in csv_data:

    cursor.execute('INSERT INTO cdr(uuid, \
	userfield, clid, src, calldate, duration)' \
        'VALUES("%s", "%s", "%s" , "%s" , "%s" , "%s" , "%s" , "%s" , "%s")', row)

#close the connection to the database.
mydb.commit()
cursor.close()
print "Done"
