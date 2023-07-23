def hitung_luas_persegi_panjang(panjang: float, lebar: float) -> float:
    """
    Fungsi untuk menghitung luas persegi panjang.

    Args:
        panjang (float): Panjang persegi panjang.
        lebar (float): Lebar persegi panjang.

    Returns:
        float: Luas persegi panjang.
    """
    luas = panjang * lebar
    return luas

# contoh pemanggilan fungsi
print(hitung_luas_persegi_panjang(5, 6.5))