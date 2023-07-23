def member(*args):
    if len(args) > 5:
        print("Jumlah member maksimum 5")
        return None
    elif len(args) < 2:
        print("Jumlah member minimum 2")
        return None
    else:
        daftar_member = list(args)
        return daftar_member

geng = member("Ani", "Budi", "Coki", "Dodi", "Eka", "Fajar")

print(geng)