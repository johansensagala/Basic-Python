# Fungsi untuk menambahkan pengguna baru
def tambah_pengguna(nama, email, **kwargs):
    pengguna_baru = {
        "nama": nama,
        "email": email
    }

    for key, value in kwargs.items():
        pengguna_baru[key] = value
        
    return pengguna_baru

# Fungsi untuk mencari pengguna berdasarkan email
def cari_pengguna(email, daftar_pengguna):
    for pengguna in daftar_pengguna:
        if pengguna["email"] == email:
            return pengguna
    return None

# Daftar pengguna awal
daftar_pengguna = [
    {"nama": "johansen", "email": "johansen@example.com", "pekerjaan": "programmer"},
    {"nama": "irpan", "email": "irpan@example.com", "pekerjaan": "designer"}
]

# Menambahkan pengguna baru
pengguna_baru = tambah_pengguna(nama="jonatan", email="jonatan@example.com", pekerjaan="writer")
daftar_pengguna.append(pengguna_baru)

# Mencari pengguna berdasarkan email
pengguna_cari = cari_pengguna(email="johansen@example.com", daftar_pengguna=daftar_pengguna)

# Menampilkan informasi pengguna yang ditemukan
if pengguna_cari:
    print("Informasi pengguna:")
    for key, value in pengguna_cari.items():
        print(f"{key}: {value}")
else:
    print("Pengguna tidak ditemukan")
