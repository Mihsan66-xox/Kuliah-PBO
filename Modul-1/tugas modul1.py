class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def hitung_luas(self):
        return self.panjang * self.lebar

    def hitung_keliling(self):
        return 2 * (self.panjang + self.lebar)

# Contoh penggunaan

    # Input dari pengguna
    panjang = float(input("Masukkan panjang persegi panjang: "))
    lebar = float(input("Masukkan lebar persegi panjang: "))

    # Membuat objek persegi panjang
    persegi_panjang = PersegiPanjang(panjang, lebar)
    print()

    # Menghitung dan menampilkan hasil
    print(f"Luas persegi panjang: {persegi_panjang.hitung_luas()}")
    print(f"Keliling persegi panjang: {persegi_panjang.hitung_keliling()}")
