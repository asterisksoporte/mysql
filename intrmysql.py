#Server Connection to MySQL:

import csv
import MySQLdb
conn = MySQLdb.connect(host= "localhost",
                  user="root",
                  passwd="neosistec",
                  db="astercdr")
x = conn.cursor()

csv_data = csv.reader(file('salida.csv'))


for row in csv_data:
	x.execute('INSERT INTO cdr(uuid,amaflags,accountcode,src,lastapp,lastdata,userfield,calldate,duration) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)', row)
	conn.commit()



