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

index = int(input("User yang ingin diedit: "))

if index < 1 or index > number_of_rows:
    print("Index tidak ada")

else:
    print("Nama: ", data_nama[index-1][0], "\n")

    while True:

        ubah_nama = input("Ubah nama? (y/n)\n")
        if ubah_nama == "y":
            nama_baru = input("Masukkan nama baru: ")

            sql_nama = "UPDATE user SET name = %s WHERE name = %s"
            cursor.execute(sql_nama, (nama_baru, data_nama[index-1][0]))

            db.commit()

            print("Nama: ", nama_baru, "\n")
            break

        elif ubah_nama == "n":

            print("Nama: ", data_nama[index-1][0], "\n")
            break

        else:

            print("Masukkan hanya 'y' atau 'n'\n")

    print("Telepon: ", data_phone[index-1][0], "\n")        
    
    while True:

        ubah_phone = input("Ubah nomor telepon? (y/n)\n")
        if ubah_phone == "y":
            phone_baru = input("Masukkan nomor telepon baru: ")

            sql_phone = "UPDATE user SET phone = %s WHERE phone = %s"
            cursor.execute(sql_phone, (phone_baru, data_phone[index-1][0]))

            db.commit()

            print("Telepon: ", phone_baru, "\n")
            break

        elif ubah_phone == "n":

            print("Telepon: ", data_phone[index-1][0], "\n")
            break

        else:

            print("Masukkan hanya 'y' atau 'n'\n")

    print("E-mail: ", data_email[index-1][0], "\n")

    while True:

        ubah_email = input("Ubah email? (y/n)\n")
        if ubah_email == "y":
            email_baru = input("Masukkan email baru: ")

            sql_email = "UPDATE user SET email = %s WHERE email = %s"
            cursor.execute(sql_email, (email_baru, data_email[index-1][0]))

            db.commit()

            print("E-mail: ", email_baru, "\n")
            break

        elif ubah_email == "n":

            print("E-mail: ", data_email[index-1][0], "\n")
            break

        else:

            print("Masukkan hanya 'y' atau 'n'\n")

cursor.close()
db.close()