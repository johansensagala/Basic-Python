import locale
from datetime import date

locale.setlocale(locale.LC_ALL, 'id_ID.utf8')

print("Hari kejadian beberapa peristiwa penting\n")
kemerdekaan_indonesia = date(1945, 8, 17)
tsunami_aceh = date(2004, 12, 26)
konferensi_meja_bundar = date(1949, 8, 23)
revolusi_prancis = date(1789, 7, 14)
tembok_berlin_runtuh = date(1989, 11, 9)

print("Kemerdekaan Indonesia : " + kemerdekaan_indonesia.strftime("%A"))
print("Tsunami Aceh : " + tsunami_aceh.strftime("%A"))
print("Konferensi Meja Bundar : " + konferensi_meja_bundar.strftime("%A"))
print("Revolusi Prancis : " + revolusi_prancis.strftime("%A"))
print("Runtuhnya Tembok Berlin : " + tembok_berlin_runtuh.strftime("%A"))
print("\n")

print("Masukkan tanggal untuk diketahui harinya \n")
tanggal = int(input("Masukkan tanggal: "))
bulan = int(input("Masukkan bulan: "))
tahun = int(input("Masukkan tahun: "))
hari = date(tahun, bulan, tanggal).strftime("%A")

print("Tanggal " + str(tanggal) + " - " + str(bulan) + " - " + str(tahun) + " jatuh pada hari " + hari)