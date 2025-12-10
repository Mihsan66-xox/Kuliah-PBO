class RekeningBank:
    def __init__(self, nama, saldo):
        self.nama = nama
        self.__saldo = saldo 
    def tarik(self, jumlah):
        if jumlah > self.__saldo:
            print("Saldo tidak cukup!")
        else:
            self.__saldo -= jumlah
            print(f"Berhasil tarik Rp{jumlah}. Sisa saldo: Rp{self.__saldo}")


akun = RekeningBank("budi", 1000000)
akun.lihat_saldo()       # ✅ bisa
akun.setor(50000)        # ✅ bisa
akun.tarik(30000)        # ✅ bisa

# Percobaan akses langsung ke saldo
try:
    print(akun.__saldo)  # ❌ tidak boleh diakses
except AttributeError:
    print("ERROR (ANDA TIDAK BERHAK MENGAKSES SALDO INI)")

