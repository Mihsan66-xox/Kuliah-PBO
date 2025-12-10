class Siswa:
    def __init__(self, nama, nilai):
        self.nama = nama
        # Saat kita menulis 'self.nilai = nilai' di sini,
        # ini OTOMATIS memanggil method 'setter' di bawah.
        self.nilai = nilai 

    # 1. GETTER (menggunakan @property)
    @property
    def nilai(self):
        print("(Memanggil getter @property)")
        return self.__nilai

    # 2. SETTER (menggunakan @<nama_getter>.setter)
    @nilai.setter
    def nilai(self, nilai_baru):
        print(f"(Memanggil setter @nilai.setter dengan nilai {nilai_baru})")
        
        # Logika validasi ('satpam') tetap di sini
        if 0 <= nilai_baru <= 100:
            self.__nilai = nilai_baru
            print("-> Nilai berhasil diupdate.")
        else:
            print(f"-> Gagal! Nilai {nilai_baru} tidak valid.")

# --- Mari kita coba cara baru ---
susi = Siswa("Susi", 80)
# Output:
# (Memanggil setter @nilai.setter dengan nilai 80)
# -> Nilai berhasil diupdate.

print("-" * 20)

# A. Mengubah nilai (terlihat seperti atribut, tapi memanggil SETTER)
susi.nilai = 101 # Ini memanggil 'def nilai(self, 101)'
# Output:
# (Memanggil setter @nilai.setter dengan nilai 101)
# -> Gagal! Nilai 101 tidak valid.

print("-" * 20)

susi.nilai = 90  # Ini memanggil 'def nilai(self, 90)'
# Output:
# (Memanggil setter @nilai.setter dengan nilai 90)
# -> Nilai berhasil diupdate.

print("-" * 20)

# B. Membaca nilai (terlihat seperti atribut, tapi memanggil GETTER)
print(f"Nilai Susi sekarang: {susi.nilai}")
# Output:
# (Memanggil getter @property)
# Nilai Susi sekarang: 90