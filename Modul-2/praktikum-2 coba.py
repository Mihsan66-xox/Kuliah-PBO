class Rekening:
    def __init__(self, nama, saldo_awal):
        self.nama = nama
        self.__saldo = saldo_awal  # atribut privat

    def lihat_saldo(self):
        # method resmi untuk melihat saldo
        print(f"Saldo anda saat ini adalah Rp{self.__saldo}")

    def setor(self, jumlah):
        self.__saldo += jumlah
        print(f"Berhasil setor Rp{jumlah}. Saldo sekarang: Rp{self.__saldo}")

    def tarik(self, jumlah):
        if jumlah > self.__saldo:
            print("Saldo tidak cukup!")
        else:
            self.__saldo -= jumlah
            print(f"Berhasil tarik Rp{jumlah}. Sisa saldo: Rp{self.__saldo}")


# Contoh penggunaan
akun = Rekening("Isan", 100000)
akun.lihat_saldo()       # ✅ bisa
akun.setor(50000)        # ✅ bisa
akun.tarik(30000)        # ✅ bisa  

# Percobaan akses langsung ke saldo
try:
    print(akun.__saldo)  # ❌ tidak boleh diakses
except AttributeError:
    print("ERROR (ANDA TIDAK BERHAK MENGAKSES SALDO INI)")
