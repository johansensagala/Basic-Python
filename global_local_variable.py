# variabel global
jumlah_pesanan = 0
total_harga = 0

def hitung_harga_produk(nama_produk, harga_produk, jumlah):
    # variabel local
    global jumlah_pesanan
    global total_harga

    jumlah_pesanan += jumlah
    total_harga += harga_produk * jumlah

    print("Anda memesan", jumlah, "buah", nama_produk)
    print("Total harga sekarang:", total_harga)

# contoh pemanggilan fungsi dan penggunaan variabel global
hitung_harga_produk("Apel", 5000, 2)
hitung_harga_produk("Jeruk", 7000, 1)

# contoh penggunaan variabel global setelah fungsi dipanggil
print("Total pesanan:", jumlah_pesanan)
print("Total harga:", total_harga)


# variabel global
jumlah_pesanan = 0
total_harga = 0

def hitung_harga_produk(nama_produk, harga_produk, jumlah):
    # variabel local
    jumlah_pesanan = 0
    total_harga = 0

    jumlah_pesanan += jumlah
    total_harga += harga_produk * jumlah

    print("Anda memesan", jumlah, "buah", nama_produk)
    print("Total harga sekarang:", total_harga)

# contoh pemanggilan fungsi dan penggunaan variabel global
hitung_harga_produk("Apel", 5000, 2)
hitung_harga_produk("Jeruk", 7000, 1)

# contoh penggunaan variabel global setelah fungsi dipanggil
print("Total pesanan:", jumlah_pesanan)
print("Total harga:", total_harga)