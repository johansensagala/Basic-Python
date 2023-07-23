from datetime import date

identitas = ["Johansen Sagala", "Teknik Informatika", date(2001, 6, 5), +6281388377456, 3.83]

biodata = {
    "Nama": identitas[0],
    "Jurusan": identitas[1],
    "Tanggal Lahir": identitas[2],
    "Umur": int((date.today() - identitas[2]).days/365),
    "Nomor Telepon": identitas[3],
    "IPK": identitas[4]
}

# mendapatkan masing masing keys dan value
print("Attribute dalam dictionary: ")
keys = biodata.keys()
print(keys)
print("Nilai dalam dictionary: ")
values = biodata.values()
print(values)
print("\n")

# membuat ulang biodata berdasarkan pecahan keys dan value
biodata_baru = dict(zip(keys, values))

# memperbaiki format tanggal lahir
biodata_baru["Tanggal Lahir"] = identitas[2].strftime("%A, %d %B %Y")

print(biodata_baru)