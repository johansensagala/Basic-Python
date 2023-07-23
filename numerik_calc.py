def konversi_desimal_ke_biner(desimal):
    return bin(desimal)

def konversi_desimal_ke_oktal(desimal):
    return oct(desimal)

def konversi_desimal_ke_heksa(desimal):
    return hex(desimal)

def konversi_biner_ke_desimal(biner):
    return int(biner, 2)

def konversi_oktal_ke_desimal(oktal):
    return int(oktal, 8)

def konversi_heksa_ke_desimal(heksa):
    return int(heksa, 16)

# Contoh penggunaan kalkulator konversi
desimal = 255
biner = konversi_desimal_ke_biner(desimal)
oktal = konversi_desimal_ke_oktal(desimal)
heksa = konversi_desimal_ke_heksa(desimal)

print(f"Desimal: {desimal}")
print(f"Biner: {biner}")
print(f"Oktal: {oktal}")
print(f"Heksadesimal: {heksa}")

# Contoh penggunaan kalkulator konversi dari biner ke desimal
bilangan_biner = "110101"
desimal_dari_biner = konversi_biner_ke_desimal(bilangan_biner)
print(f"Biner {bilangan_biner} dalam desimal: {desimal_dari_biner}")
