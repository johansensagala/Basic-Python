from database import db

cursor = db.cursor()

name = "SELECT name FROM user"
phone = "SELECT phone FROM user"
email = "SELECT email FROM user"

cursor.execute(name)
data_nama = cursor.fetchall()
cursor.execute(phone)
data_phone = cursor.fetchall()
cursor.execute(email)
data_email = cursor.fetchall()

cursor.execute("SELECT COUNT(id) FROM user")
number_of_rows = cursor.fetchone()[0]

for i in range(1, (number_of_rows + 1)):
    print("User ", i, ":")
    print("Nama: ", data_nama[i-1][0])
    print("Telepon: ", data_phone[i-1][0])
    print("E-mail: ", data_email[i-1][0])
    print("\n")

index = int(input("User yang ingin dihapus: "))

if index < 1 or index > number_of_rows:
    print("Index tidak ada")

else:

    sql = "DELETE FROM user WHERE name = %s"
    deleted_name = data_nama[index-1][0]

    cursor.execute(sql, (deleted_name, ))

    db.commit()

cursor.close()
db.close()