import mysql.connector
import uuid
from tabulate import tabulate

conn = mysql.connector.connect(
    user = "root",
    host = "localhost",
    password = "",
    database = "penjualan"
)

cur = conn.cursor()

# # membuat database
# cur.execute("CREATE DATABASE penjualan")

# # membuat tabel pegawai
# cur.execute("""CREATE TABLE Pegawai (
#             NIK CHAR(5) NOT NULL PRIMARY KEY,
#             Nama_Pegawai VARCHAR(25),
#             Alamat_Pegawai VARCHAR(255))""")

# # membuat tabel produk
# cur.execute("""CREATE TABLE Produk (
#             Kode_Produk CHAR(5) NOT NULL PRIMARY KEY,
#             Nama_Produk VARCHAR(20),
#             Jenis_Produk VARCHAR(8),
#             Harga INT(10))""")

# # membuat tabel transaksi
# cur.execute("""CREATE TABLE Transaksi (
#             No_Transaksi CHAR(7) NOT NULL PRIMARY KEY,
#             NIK CHAR(5) NOT NULL,
#             Kode_Produk CHAR(5) NOT NULL,
#             FOREIGN KEY (NIK) REFERENCES pegawai(NIK),
#             FOREIGN KEY (Kode_Produk) REFERENCES produk(Kode_Produk))""")

# # membuat tabel struk membuat composite key 
# cur.execute("""CREATE TABLE Struk (
#             No_Struk CHAR(5) NOT NULL PRIMARY KEY,
#             No_Transaksi CHAR(7) NOT NULL,
#             Jumlah_Produk INT(2),
#             Total_Harga INT(10),
#             FOREIGN KEY (No_Transaksi) REFERENCES transaksi(No_Transaksi))""")

class Pegawai:
    def __init__(self, NIK, nama_pegawai, alamat_pegawai):
        self._NIK = NIK
        self.nama_pegawai = nama_pegawai
        self.alamat_pegawai = alamat_pegawai

    def tambah_pegawai(self):
        cur.execute("""INSERT INTO pegawai (NIK, Nama_Pegawai, Alamat_Pegawai) VALUES (%s, %s, %s)""", 
                    (self._NIK, self.nama_pegawai, self.alamat_pegawai))
        conn.commit()

    @staticmethod
    def lihat_pegawai():
        cur.execute("SELECT * FROM pegawai")
        list_pegawai = cur.fetchall()
        print(tabulate(list_pegawai, headers=["NIK", "Nama Pegawai", "Alamat Pegawai"], tablefmt="pretty"))

    @staticmethod
    def edit_pegawai(nama_baru, alamat_baru, NIK):
        cur.execute("""UPDATE pegawai SET Nama_Pegawai = %s, Alamat_Pegawai = %s WHERE NIK = %s""", (nama_baru, alamat_baru, NIK))
        conn.commit()

    @staticmethod
    def hapus_pegawai(NIK):
        cur.execute("DELETE FROM pegawai WHERE NIK = %s", (NIK,))
        conn.commit()

class Produk:
    def __init__(self, nama_produk, jenis_produk, harga):
        self._kode_produk = f"PR{str(uuid.uuid4().int)[:3]}"
        self.nama_produk = nama_produk
        self.jenis_produk = jenis_produk
        self.harga = harga

    def tambah_produk(self):
        cur.execute("""INSERT INTO produk (Kode_Produk, Nama_Produk, Jenis_Produk, Harga) 
                    VALUES (%s, %s, %s, %s)""", (self._kode_produk, self.nama_produk, self.jenis_produk, self.harga))
        
        conn.commit()

    @staticmethod
    def lihat_produk():
        cur.execute("SELECT * FROM produk")
        list_produk = cur.fetchall()
        print(tabulate(list_produk, headers=["Kode_Produk", "Nama_Produk", "Jenis_Produk", "Harga"], tablefmt="pretty"))

    @staticmethod
    def edit_produk(kode_produk, nama_baru, jenis_baru, harga_baru):
        cur.execute("UPDATE produk SET Nama_Produk = %s, Jenis_Produk = %s, Harga = %s WHERE Kode_Produk = %s", (nama_baru, jenis_baru, harga_baru, kode_produk))
        conn.commit()

    @staticmethod
    def hapus_produk(kode_produk):
        cur.execute("DELETE FROM produk WHERE Kode_Produk = %s", (kode_produk,))
        conn.commit()

    def get_kode_produk(self):
        return self._kode_produk

class Transaksi:
    def __init__(self, no_transaksi, produk, jumlah_produk):
        self.no_transaksi = no_transaksi
        self.produk = produk
        self.jumlah_produk = jumlah_produk
        self.total_harga = 0

    def pembelian(self):
        self.no_transaksi.no_transaksi = f"TR{str(uuid.uuid4()[:5])}"
        self.total_harga = self.harga * self.jumlah_produk
        return self.total_harga

class Struk:
    def __init__(self, no_struk, transaksi):
        self.no_struk = no_struk
        self.transaksi = transaksi

    def cetak_struk(self):
        self.no_struk = f"ST{str(uuid.uuid4()[:3])}"
        print("="*5 + "TOKO KUE BHARATA" + "="*5)
        print(F"No Struk        : {self.no_struk}")
        print(f"No Transaksi    : {self.transaksi.no_transaksi}")   
        print(f"Nama Produk     : {self.transaksi.produk.nama_produk}")   
        print(f"Jumlah Produk   : {self.transaksi.jumlah_produk}")   
        print(f"Total Harga     : Rp. {self.transaksi.total_harga}")   
        print(f"Nama Pegawai    : {self.nama_pegawai}")
        print("="*20)

def menu_produk():
    while True:
        try:
            print("="*10 + "MENU PRODUK" + "="*10)
            print("1. Tambah Produk")
            print("2. Lihat Produk")
            print("3. Hapus Produk")
            print("4. Ubah Informasi Produk")
            print("5. Keluar")

            pilih = int(input("Masukan Pilihan Menu : "))

            if pilih == 1:
                nama_produk = str(input("Masukan Nama Produk : "))
                jenis_produk = str(input("Masukan Jenis Produk : "))
                harga = int(input("Masukan Harga Produk : "))

                # objek produk
                produk = Produk(nama_produk, jenis_produk, harga)
                produk.tambah_produk()

            elif pilih == 2:
                Produk.lihat_produk()

            elif pilih == 3:
                kode_produk = str(input("Masukan Kode Produk Yang Akan Dihapus : "))
                Produk.hapus_produk(kode_produk)

            elif pilih == 4:
                kode_produk_ubah = str(input("Masukan Kode Produk Yang Akan Diubah : "))
                nama_baru = str(input("Masukan Nama Baru Produk : "))
                jenis_baru = str(input("Masukan Jenis Baru Produk : "))
                harga_baru = int(input("Masukan Harga Baru Produk : "))

                Produk.edit_produk(kode_produk_ubah, nama_baru, jenis_baru, harga_baru)

            elif pilih == 5:
                return
            
            else:
                print("PILIHAN MENU TIDAK TERSEDIA!!")


        except ValueError:
            print("INPUTAN SALAH SILAHKAN INPUT DENGAN ANGKA!!")

def menu_pegawai():
    while True:
        try:
            print("="*10 + "MENU PEGAWAI" + "="*10)
            print("1. Tambah Pegawai")
            print("2. Lihat Pegawai")
            print("3. Hapus Pegawai")
            print("4. Ubah Informasi Pegawai")
            print("5. Keluar")

            pilih = int(input("Masukan Pilihan Menu : "))

            if pilih == 1:
                NIK = str(input("Masukan NIK Pegawai : "))
                Nama = str(input("Masukan Nama Pegawai : "))
                Alamat = str(input("Masukan Alamat Pegawai : "))

                # objek pegawai
                pegawai = Pegawai(NIK, Nama, Alamat)
                pegawai.tambah_pegawai()

            elif pilih == 2:
                Pegawai.lihat_pegawai()

            elif pilih == 3:
                NIK = str(input("Masukan NIK Pegawai Yang Ingin Dihapus : "))
                Pegawai.hapus_pegawai(NIK)

            elif pilih == 4:
                NIK = str(input("Masukan NIK Pegawai Yang Akan Diubah : "))
                nama_baru = str(input("Masukan Nama Baru Pegawai : "))
                alamat_baru = str(input("Masukan Alamat baru Pegawai : "))
                Pegawai.edit_pegawai(nama_baru, alamat_baru, NIK)

            elif pilih == 5:
                return

            else:
                print("PILIHAN MENU TIDAK TERSEDIA!!")

        except ValueError:
            print("INPUTAN SALAH SILAHKAN INPUT DENGAN ANGKA!!")

def menu_transaksi():
    print("="*10 + "MENU TRANSAKSI" + "="*10)
    print("1. Tambah Transaksi")
    print("2. Lihat Riwayat Transaksi")
    print("3. Keluar")

def main():
    while True:
        try:
            print("="*10 + "TOKO KUE BHARATA" + "="*10)
            print("1. Produk")
            print("2. Pegawai")
            print("3. Transaksi")
            print("4. Keluar")

            pilih = int(input("Masukan Pilihan Menu : "))

            if pilih == 1:
                menu_produk()

            elif pilih == 2:
                menu_pegawai()
                
            elif pilih == 3:
                menu_transaksi()
            
            elif pilih == 4:
                print("="*20 + " TERIMAKASIH " + "="*20)
                return
            
            else:
                print("PILIHAN MENU TIDAK TERSEDIA!!")
            
        except ValueError:
            print("INPUTAN SALAH SILAHKAN INPUT DENGAN ANGKA!!")


if __name__ == "__main__":
    main()
