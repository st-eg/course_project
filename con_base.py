import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user = 'root',
    passwd = 'papa_dojo'
)

cursor = db.cursor()
cursor.execute('')