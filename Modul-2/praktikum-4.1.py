class Siswa:
    def __init__(self, nama, nilai):
        self.nama = nama
        self.__nilai = 0  
        self.set_nilai(nilai) 

    # GETTER: Hanya untuk 'membaca'
    def get_nilai(self):
        print(f"(Akses getter untuk {self.nama})")
        return self.__nilai

    # SETTER: 'Satpam' untuk 'menulis'
    def set_nilai(self, nilai_baru):
        print(f"(Akses setter untuk {self.nama} dengan nilai {nilai_baru})")
        if 0 <= nilai_baru <= 100:
            self.__nilai = nilai_baru
            print("-> Nilai berhasil diupdate.")
        else:
            print(f"-> Gagal! Nilai {nilai_baru} tidak valid. Harus antara 0-100.")


budi = Siswa("Budi", 70) 

budi.set_nilai(95)

budi.set_nilai(105)


print(f"Nilai Budi sekarang: {budi.get_nilai()}")