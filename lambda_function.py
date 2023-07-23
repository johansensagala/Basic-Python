# Definisikan fungsi lambda untuk menghitung luas segitiga
luas_segitiga = lambda alas, tinggi: 0.5 * alas * tinggi

# Input nilai alas dan tinggi segitiga
alas = float(input("Masukkan panjang alas segitiga: "))
tinggi = float(input("Masukkan tinggi segitiga: "))

# Hitung luas segitiga menggunakan fungsi lambda
luas = luas_segitiga(alas, tinggi)

# Cetak hasil perhitungan
print("Luas segitiga dengan alas", alas, "dan tinggi", tinggi, "adalah", luas)