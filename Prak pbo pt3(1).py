from abc import ABC, abstractmethod

class Tanaman(ABC):
    def __init__(self, nama, kebutuhan_air, kebutuhan_pupuk):
        self.nama = nama
        self.kebutuhan_air = kebutuhan_air
        self.kebutuhan_pupuk = kebutuhan_pupuk
    
    @abstractmethod
    def tumbuh(self):
        pass

    def hitung_kebutuhan(self, curah_hujan, kelembapan_tanah):
        air_disesuaikan = max(0, self.kebutuhan_air - curah_hujan * 1.5)
        pupuk_disesuaikan = self.kebutuhan_pupuk

        if kelembapan_tanah > 70:
            air_disesuaikan *= 0.7

        return air_disesuaikan, pupuk_disesuaikan
    
    def tampilkan_kebutuhan(self, curah_hujan, kelembapan_tanah):
        air_disesuaikan, pupuk_disesuaikan = self.hitung_kebutuhan(curah_hujan, kelembapan_tanah)
        print(f"Weather Report: Rainfall = {curah_hujan} mm, Soil Moisture = {kelembapan_tanah}%")
        print(f"Adjusted Water Needs: {air_disesuaikan:.1f} liters")
        print(f"Adjusted Fertilizer Needs: {pupuk_disesuaikan:.1f} kg\n")

class TanamanPadi(Tanaman):
    def __init__(self):
        super().__init__("Rice", 20, 4)

    def tumbuh(self):
        print(f"{self.nama} is growing in the paddy field")

class TanamanJagung(Tanaman):
    def __init__(self):
        super().__init__("Corn", 18, 7)

    def tumbuh(self):
        print(f"{self.nama} is growing in the farm")

if __name__ == "__main__":
    curah_hujan_padi = 10
    kelembapan_tanah_padi = 75

    curah_hujan_jagung = 2
    kelembapan_tanah_jagung = 40

    padi = TanamanPadi()
    jagung = TanamanJagung()

    padi.tumbuh()
    padi.tampilkan_kebutuhan(curah_hujan_padi, kelembapan_tanah_padi)

    jagung.tumbuh()
    jagung.tampilkan_kebutuhan(curah_hujan_jagung, kelembapan_tanah_jagung)