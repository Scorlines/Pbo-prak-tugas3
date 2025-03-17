#Muhammad Fadhel
#123140106
#prak pbo 3 (3)

class BankAccount:
    exchange_rates = {
        ("USD", "EUR"): 0.91,
        ("EUR", "USD"): 1.1,
        ("USD", "IDR"): 15500,
        ("IDR", "USD"): 1 / 15500,
        ("EUR", "IDR"): 17000,
        ("IDR", "EUR"): 1 / 17000,
    }

    def __init__(self, pemilik_akun, saldo, mata_uang):
        self.pemilik_akun = pemilik_akun
        self.saldo = saldo
        self.mata_uang = mata_uang

    def __sub__(self, jumlah):
        if self.saldo >= jumlah:
            self.saldo -= jumlah
        else:
            print("Insufficient balance for withdrawal!")
            print(f"{self.pemilik_akun}'s Account: Balance remains at {self.mata_uang}{self.saldo}")

    def tambahkan_bunga(self):
        tingkat_bunga = 0.02 if self.saldo > 5000 else 0.01
        self.saldo += self.saldo * tingkat_bunga
        print(f"Applying interest... New Balance = ${self.saldo:.0f}")

    def konversi_ke_usd(self):
        if self.mata_uang == "USD":
            return self.saldo
        kurs = self.exchange_rates.get((self.mata_uang, "USD"), 1)
        return self.saldo * kurs


if __name__ == "__main__":
    akun_john = BankAccount("John", 5000, "USD")
    print(f"{akun_john.pemilik_akun}'s Account: Initial Balance = ${akun_john.saldo}")
    akun_john.tambahkan_bunga()
    print()

    akun_emily = BankAccount("Emily", 1000, "EUR")
    print(f"{akun_emily.pemilik_akun}'s Account: Initial Balance = €{akun_emily.saldo}")

    saldo_terkonversi = akun_emily.konversi_ke_usd()
    print(f"Converted to USD: ${saldo_terkonversi:.0f}")

    akun_emily - 1200
