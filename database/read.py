from database import db

cursor = db.cursor()

sql = "SELECT * FROM user"

cursor.execute(sql)

data = cursor.fetchall()

for row in data:
    print(row)

cursor.close()
db.close()