import mysql.connector
connection=mysql.connector.connect(host="localhost",database="demodb",user="root",password='cdac123')
qry="select * from laptop;"
cursor=connection.cursor()
cursor.execute(qry)
records=cursor.fetchall()
print("Total no. of records : ",cursor.rowcount)
for row in records:
    print(" ID : ",row[0])
    print(" Name : ",row[1])
    print(" Price : ",row[2])
    print(" Purchase Date : ",row[3])
    print()
    print("------------------------------------------")
    print()
cursor.close()
connection.close()
    
