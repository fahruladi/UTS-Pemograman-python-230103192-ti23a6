def hitung_ongkir(berat_kg, kota, asuransi=False):
    """Menghitung ongkir berdasarkan kota, berat, dan opsi asuransi."""
    tarif_dasar = {
        "Jakarta": 10000,
        "Bandung": 12000,
        "Surabaya": 15000
    }
    ongkir = tarif_dasar.get(kota, 0) + 2000 * berat_kg
    if asuransi:
        ongkir += 3000
    return ongkir

print(hitung_ongkir(2, "Jakarta"))
print(hitung_ongkir(3, "Bandung", asuransi=True))
