class Pegawai:
    def __init__(self, nama, nip, gaji_pokok):
        self.nama = nama
        self.nip = nip
        self.__gaji_pokok = gaji_pokok   # PRIVATE

    # Getter gaji pokok (TIDAK ADA setter)
    def get_gaji_pokok(self):
        return self.__gaji_pokok

    # Method hitung bonus (akan dioverride di subclass)
    def hitung_bonus(self):
        return 0

    # Getter gaji total
    def get_gaji_total(self):
        return self.__gaji_pokok + self.hitung_bonus()

    # Tampilkan info dasar pegawai
    def tampilkan_info(self):
        print(f"Nama: {self.nama}, NIP: {self.nip}")
        print(f"Gaji Pokok: Rp {self.get_gaji_pokok():,}".replace(",", "."))


# ===================== CHILD CLASS: MANAGER =====================

class Manager(Pegawai):
    def __init__(self, nama, nip, gaji_pokok, tunjangan_jabatan):
        super().__init__(nama, nip, gaji_pokok)
        self.tunjangan_jabatan = tunjangan_jabatan

    # Override bonus: 15%
    def hitung_bonus(self):
        return int(self.get_gaji_pokok() * 0.15)

    # Override info
    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Tunjangan: Rp {self.tunjangan_jabatan:,}".replace(",", "."))
        print(f"Gaji Total Manager: Rp {self.get_gaji_total():,}".replace(",", "."))


# ===================== CHILD CLASS: STAFF TEKNIS =====================

class StaffTeknis(Pegawai):
    def __init__(self, nama, nip, gaji_pokok, jumlah_proyek):
        super().__init__(nama, nip, gaji_pokok)
        self.jumlah_proyek = jumlah_proyek

    # Override bonus: 500.000 x jumlah proyek
    def hitung_bonus(self):
        return 500_000 * self.jumlah_proyek

    # Override info
    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Jumlah Proyek: {self.jumlah_proyek}")
        print(f"Gaji Total Staff: Rp {self.get_gaji_total():,}".replace(",", "."))


# ========================== DEMO OUTPUT ==========================

# Manager
print("\n--- Info Manager ---")
manager = Manager("Budi Hartono", "M-001", 10_000_000, 5_000_000)
manager.tampilkan_info()

print("\n==============================\n")

# Staff Teknis
print("--- Info Staff Teknis ---")
staff = StaffTeknis("Susi Susanti", "S-001", 6_000_000, 3)
staff.tampilkan_info()

print("\n==============================\n")

# Test keamanan enkapsulasi
print("--- Tes Keamanan (Encapsulasi) ---")
try:
    print(staff.__gaji_pokok)  # AKAN ERROR
except Exception as e:
    print(f"ERROR: {e}")
    print("-> TIDAK BISA diakses langsung dari luar!")

print(f"Gaji Total Susi (tetap): Rp {staff.get_gaji_total():,}".replace(",", "."))
