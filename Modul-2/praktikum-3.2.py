class Kalkulator:

    def __init__(self, nilai_awal):
        self.nilai = nilai_awal
    
    def tambah(self, angka):
        self.nilai += angka
        return self.nilai

    @staticmethod
    def kali(a, b):
        return a * b

calc = Kalkulator(10)
print(f"Hasil tambah: {calc.tambah(5)}")

print(f"Hasil kali: {Kalkulator.kali(5, 3)}")