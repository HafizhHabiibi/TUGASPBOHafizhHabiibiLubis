class DaftarMenu:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    def displayMakanan(self):
        print("="*5 + "Makanan" + "="*5)
        print(f"{self.nama} => {self.harga}")


    def displayMinuman(self):
        print("="*5 + "Makanan" + "="*5)
        print(f"{self.nama} => {self.harga}")

makanan = []
def tambahMakan():
    makan = str(input("Masukan Nama Makanan : "))
    harga = int(input("Masukan Harga Makanan : "))

    masuk = DaftarMenu(makan, harga)
    makanan.append(masuk)

minuman = []
def tambahMinuman():
    minum = str(input("Masukan Nama Minuman : "))
    harga = int(input("Masukan Harga Minuman : "))

    masuk = DaftarMenu(minum, harga)
    minuman.append(masuk)

def displayMakan():
    for i in makanan:
        i.displayMakanan()

def displayMinum():
    for i in minuman:
        i.displayMinuman()

udang = DaftarMenu("Udang", 5000)
roti = DaftarMenu("Roti", 2000)
telurAsin = DaftarMenu("Telur Asin", 2500)
esTeh = DaftarMenu("Es Teh", 3000)
airPutih = DaftarMenu("AirPutih", 2500)
kopi = DaftarMenu("Kopi", 5000)

makanan.append(udang)
makanan.append(roti)
makanan.append(telurAsin)
minuman.append(esTeh)
minuman.append(airPutih)
minuman.append(kopi)

def tambah():
    while True:
        try:
            print("="*5 + "Tambahkan" + "="*5)
            print("1. Makanan")
            print("2. Minuman")
            print("3. Keluar")

            pilih = int(input("Pilih Menu : "))

            if pilih == 1:
                tambahMakan()
            elif pilih == 2:
                tambahMinuman()
            elif pilih == 3:
                return
        except ValueError:
            print("Inputan Salah Silahkan Input Ulang")
            continue

def Menu():
    while True:
        try:

            print("="*5 + "Daftar Menu" + "="*5)
            print("1. Menu Makanan")
            print("2. Menu Minuman")
            print("3. Tambah Makanan Minuman")
            print("4. Keluar")

            pilih = int(input("Pilih Menu : "))

            if pilih == 1:
                displayMakan()
            elif pilih == 2:
                displayMinum()
            elif pilih == 3:
                tambah()
            elif pilih == 4:
                print("Terimakasih")
                return

        except ValueError:
            print("Inputan Salah Silahkan Input Ulang")
            continue

Menu()

