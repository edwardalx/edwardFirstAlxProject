import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost", 
    user = "root", 
    password="Edward@alx2025", 
    database = "edward_hostels")
mycursor = mydb.cursor()
#mycursor.execute("show databases")
#mycursor.execute("SELECT * FROM residents")
#mycursor.execute("DESC residents")
# mycursor.execute("UPDATE residents SET first_name = 'Kwaku-Bonsu' WHERE id = 4")
# mydb.commit()
sql = ("INSERT INTO residents(first_name, other_names,email,age) VALUES (%s, %s,%s,%s)")
val = [
    ('Robert', 'Wood', "robert@mail.com",21),
    ('Sydney', "Asante","sydney@mail.com",40 ),
    ('Ronney', "Rattan", "rooney@mail.com",18),
    ('Raja', "Malik", "raja@mail.com", 27)
    ]
mycursor.executemany(sql, val)
mydb.commit()
mycursor.execute("SELECT * FROM residents")
for i in mycursor:
    print(i)