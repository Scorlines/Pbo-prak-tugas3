from abc import ABC, abstractmethod

class Karyawan(ABC):
    def __init__(self, nama, peran, jam_kerja, tugas_selesai):
        self.nama = nama
        self.peran = peran
        self.jam_kerja = jam_kerja
        self.tugas_selesai = tugas_selesai

    @abstractmethod
    def bekerja(self):
        pass

    @abstractmethod
    def evaluasi_kinerja(self):
        pass

    def nilai_kinerja(self):
        skor = self.evaluasi_kinerja()
        if skor >= 8:
            return "High Performance"
        elif skor >= 5:
            return "Medium Performance"
        else:
            return "Low Performance"
        
class SoftwareEngineer(Karyawan):
    def __init__(self, nama, jam_kerja, tugas_selesai):
        super().__init__(nama, "Software Engineer", jam_kerja, tugas_selesai)

    def bekerja(self):
        print(f"{self.nama} ({self.peran}) is coding.")

    def evaluasi_kinerja(self):
        return (self.tugas_selesai / max(1, self.jam_kerja)) * 10
        
class DataScientist(Karyawan):
    def __init__(self, nama, jam_kerja, tugas_selesai):
        super().__init__(nama, "Data Scientist", jam_kerja, tugas_selesai)

    def bekerja(self):
        print(f"{self.nama} ({self.peran}) is analyzing data.")

    def evaluasi_kinerja(self):
        return (self.tugas_selesai / max(1, self.jam_kerja)) * 8
        
class ProductManager(Karyawan):
    def __init__(self, nama, jam_kerja, tugas_selesai):
        super().__init__(nama, "Product Manager", jam_kerja, tugas_selesai)

    def bekerja(self):
        print(f"{self.nama} ({self.peran}) is managing the product.")

    def evaluasi_kinerja(self):
        return (self.tugas_selesai / max(1, self.jam_kerja)) * 7

if __name__ == "__main__":
    karyawan = [
        SoftwareEngineer("Abdul", 40, 35),
        DataScientist("Budi", 45, 30),
        ProductManager("Cinta", 50, 28),
        SoftwareEngineer("Doni", 30, 10)
    ]
    
    for k in karyawan:
        k.bekerja()
        print(f"Performance Rating: {k.nilai_kinerja()}\n")
