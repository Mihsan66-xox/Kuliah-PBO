class Hero:
    # Private class variable
    __jumlah = 0

    def __init__(self, nama, health, attPower, armor):
        # Private instance variables
        self.__name = nama
        self.__healthStandar = health
        self.__attPowerStandar = attPower
        self.__armorStandar = armor
        self.__level = 1
        self.__exp = 0
        # Atribut dinamis berdasarkan level
        self.__healthMax = self.__healthStandar * self.__level
        self.__attPower = self.__attPowerStandar * self.__level
        self.__armor = self.__armorStandar * self.__level
        self.__health = self.__healthMax
        # Tambah jumlah Hero setiap kali objek dibuat
        Hero.__jumlah += 1
    @property
    def info(self):
        return f"{self.__name} level {self.__level}:\n" \
               f"\thealth = {self.__health}/{self.__healthMax}\n" \
               f"\tattack = {self.__attPower}\n" \
               f"\tarmor = {self.__armor}" 
    @property
    def gainEXP(self):
        # Getter hanya untuk mengaktifkan setter
        pass

    @gainEXP.setter
    def gainEXP(self, addEXP):
        self.__exp += addEXP
        print(f"{self.__name} mendapatkan {addEXP} EXP.")

        # Cek apakah naik level
        while self.__exp >= 100:
            self.__exp -= 100
            self.__level += 1
            print(f"{self.__name} level up! Sekarang level {self.__level}")

            # Update atribut dinamis sesuai level baru
            self.__healthMax = self.__healthStandar * self.__level
            self.__attPower = self.__attPowerStandar * self.__level
            self.__armor = self.__armorStandar * self.__level

    # ------------------------------
    # Method Attack
    # ------------------------------
    def attack(self, musuh):
        print(f"{self.__name} menyerang {musuh.__name}")
        # Hero menyerang → mendapat EXP
        self.gainEXP = 50

    # ------------------------------
    # Static method (opsional) untuk melihat jumlah hero
    # ------------------------------
    @staticmethod
    def jumlahHero():
        return Hero.__jumlah

hero1 = Hero("Layla", 100, 20, 5)
hero2 = Hero("Tigreal", 200, 10, 10)

print(hero1.info)
print(hero2.info)

# Hero menyerang
hero1.attack(hero2)
hero1.attack(hero2)  # Setelah 2 serangan akan naik level

print(hero1.info)
print(f"Total hero: {Hero.jumlahHero()}")
