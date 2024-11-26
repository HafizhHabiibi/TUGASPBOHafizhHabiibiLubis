from tabulate import tabulate

produk = []  #Produk

class Produk:
    id_counter = 1

    def __init__(self, nama="", jenis=""):
        self._kode = f"{jenis[:3].upper()}{Produk.id_counter:04d}"
        self.nama = nama
        self.jenis = jenis
        Produk.id_counter += 1

    def tampil_produk(self):
        return [self._kode, self.nama, self.jenis]  

class Snack(Produk):
    def __init__(self, nama="", harga=""):
        super().__init__(nama, jenis="snack")
        self.harga = harga
        produk.append(self)  

    def tambah(self):
        nama_produk = input("Masukkan nama produk snack yang ingin ditambahkan: ")
        harga = input("Masukkan harga produk snack yang ingin ditambahkan: ")
        new_produk = Snack(nama=nama_produk, harga=harga)
        produk.append(new_produk)  
        print(f"Produk Snack berhasil ditambahkan dengan kode: {new_produk._kode}")

    def tampil_produk(self):
        return super().tampil_produk() + [self.harga]  

class Makanan(Produk):
    def __init__(self, nama="", harga=""):
        super().__init__(nama, jenis="Makanan")
        self.harga = harga
        produk.append(self)  

    def tambah(self):
        nama_produk = input("Masukkan nama produk makanan yang ingin ditambahkan: ")
        harga = input("Masukkan harga produk makanan yang ingin ditambahkan: ")
        new_produk = Makanan(nama=nama_produk, harga=harga)
        produk.append(new_produk)  
        print(f"Produk Makanan berhasil ditambahkan dengan kode: {new_produk._kode}")

    def tampil_produk(self):
        return super().tampil_produk() + [self.harga]  

class Minuman(Produk):
    def __init__(self, nama="", harga=""):
        super().__init__(nama, jenis="Minuman")
        self.harga = harga
        produk.append(self)  

    def tambah(self):
        nama_produk = input("Masukkan nama produk minuman yang ingin ditambahkan: ")
        harga = input("Masukkan harga produk minuman yang ingin ditambahkan: ")
        new_produk = Minuman(nama=nama_produk, harga=harga)
        produk.append(new_produk)  
        print(f"Produk Minuman berhasil ditambahkan dengan kode: {new_produk._kode}")

    def tampil_produk(self):
        return super().tampil_produk() + [self.harga]  

# Isi Default
snack1 = Snack(nama="Keripik", harga="5000")
snack2 = Snack(nama="Kacang", harga="4000")
makanan1 = Makanan(nama="Nasi Goreng", harga="15000")
makanan2 = Makanan(nama="Ayam Penyet", harga="20000")
minuman1 = Minuman(nama="Teh Botol", harga="3000")
minuman2 = Minuman(nama="Air Mineral", harga="2000")

def lihat_produk():
    header = ["KODE", "NAMA", "JENIS", "HARGA"]  
    table = [p.tampil_produk() for p in produk]  
    print(tabulate(table, headers=header, tablefmt="grid"))  


def main():
    while True:
        try:
            print("="*20 + "HAPIS MART" + "="*20)
            print("1. Lihat Produk")
            print("2. Tambah Produk")
            print("3. Lihat Pegawai")
            print("4. Lihat Struk")
            print("5. Keluar")

            pilih = int(input("Masukan menu yang ingin dipilih : "))

            if pilih == 1:
                lihat_produk()
            if pilih == 2:
                print("1. Tambah Snack")
                print("2. Tambah Makan")
                print("3. Tambah Minuman")

                tambah = int(input("Pilih produk yang ingin ditambahkan"))

                if tambah == 1:
                    Snack().tambah()
                elif tambah == 2:
                    Makanan().tambah()
                elif tambah == 3:
                    Minuman().tambah()

        except ValueError:
            print("INPUTAN SALAH SILAHKAN MASUKAN INPUT YANG BENAR!")

class Transaksi:
    def __init__(self, no_transaksi, detail_transaksi ):
        self.no_transaksi = no_transaksi
        self.detail_transaksi = detail_transaksi

class Pegawai:
    def __init__(self, nik, nama_pegawai, alamat):
        self._nik = nik
        self.nama = nama_pegawai
        self.alamat = alamat

class Struk:
    def __init__(self, no_transaksi, nama_pegawai,nama_produk, jumlah_produk, total_harga):
        self.no_transaksi = no_transaksi
        self.nama_pegawai = nama_pegawai
        self.nama_produk = nama_produk
        self.jumlah_produk = jumlah_produk
        self.total_harga = total_harga

if __name__ == "__main__":
    main()


