from database import db

cursor = db.cursor()

sql = "INSERT INTO user (name, phone, email) values (%s, %s, %s)"
data = [
    ("Johansen Sagala", 62881388377456, "johansensagala.2001@gmail.com"),
    ("Jonatan Situmorang", 6281234567890, "jonatan@gmail.com"),
    ("Irpan Buri Siburian", 6281357903726, "irpan@gmail.com")
]

cursor.executemany(sql, data)

db.commit()

cursor.close()
db.close()