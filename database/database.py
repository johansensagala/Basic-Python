import mysql.connector as mysql
from mysql.connector import Error

# Cek koneksi

try:
    db = mysql.connect(
        host="localhost",
        user="root",
        password="",
        database="pydata"
    )

    is_connected = db.is_connected()

    if is_connected == True:
        print("Koneksi Berhasil")

except Error as e:
    print(f"Koneksi gagal {e}")