import mysql.connector
import uuid
import os
import datetime as dt
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

# #membuat tabel pegawai
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

# #membuat tabel transaksi
# cur.execute("""CREATE TABLE transaksi (
#             No_Transaksi VARCHAR(10),
#             Tanggal_Transaksi DATETIME,
#             Kode_Produk CHAR(5),
#             Jumlah_Produk INT(2),
#             PRIMARY KEY (No_Transaksi, Kode_Produk),
#             FOREIGN KEY (Kode_Produk) REFERENCES produk(Kode_Produk) ON DELETE CASCADE)""")

# # membuat tabel struk membuat composite key 
# cur.execute("""CREATE TABLE Struk (
#             No_Struk CHAR(5) NOT NULL PRIMARY KEY,
#             NIK CHAR(5),  -- NIK bisa NULL
#             No_Transaksi CHAR(7) NOT NULL,
#             Total_Harga INT(10),
#             FOREIGN KEY (NIK) REFERENCES Pegawai(NIK) ON DELETE SET NULL,
#             FOREIGN KEY (No_Transaksi) REFERENCES Transaksi(No_Transaksi))""")

class Pegawai:
    def __init__(self, NIK, nama_pegawai, alamat_pegawai):
        self._NIK = NIK
        self.nama_pegawai = nama_pegawai
        self.alamat_pegawai = alamat_pegawai

    def tambah_pegawai(self):
        try:
            cur.execute("""INSERT INTO pegawai (NIK, Nama_Pegawai, Alamat_Pegawai) VALUES (%s, %s, %s)""", 
                        (self._NIK, self.nama_pegawai, self.alamat_pegawai))
            conn.commit()

        except mysql.connector.errors.IntegrityError as e:

            if "Duplicate entry" in str(e):
                print(f"PEGAWAI DENGAN NIK {self._NIK} SUDAH ADA!")
            else:
                print(f"ERROR {e}")

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

    @staticmethod
    def cari_pegawai(NIK):
        cur.execute("SELECT * FROM pegawai WHERE NIK = %s", (NIK,))
        result = cur.fetchone()
        return result is not None

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

    @staticmethod
    def cari_produk(kode_produk):
        cur.execute("SELECT * FROM produk WHERE Kode_Produk = %s", (kode_produk,))
        result = cur.fetchone()
        return result is not None
    
    def get_kode_produk(self):
        return self._kode_produk

class Transaksi:
    def __init__(self):
        self.no_transaksi = f"TR{str(uuid.uuid4().int)[:5]}"
        self.tanggal_transaksi = dt.datetime.now().strftime("%Y-%m-%d %H:%M")
        self.produk_list = []  # List untuk menyimpan produk dan jumlah
        self.total_harga = 0

    def tambah_produk(self, produk, jumlah_produk):
        self.produk_list.append((produk, jumlah_produk))
        self.total_harga += produk.harga * jumlah_produk

    def tambah_transaksi(self):
        for produk, jumlah in self.produk_list:
            try:
                cur.execute(
                    """INSERT INTO transaksi (No_Transaksi, Tanggal_Transaksi, Kode_Produk, Jumlah_Produk)
                    VALUES (%s, %s, %s, %s)""",
                    (self.no_transaksi, self.tanggal_transaksi, produk.get_kode_produk(), jumlah),
                )
            except mysql.connector.IntegrityError as e:
                if "Duplicate entry" in str(e):
                    # Update jumlah jika produk sudah ada dalam transaksi
                    cur.execute(
                        """UPDATE transaksi
                        SET Jumlah_Produk = Jumlah_Produk + %s
                        WHERE No_Transaksi = %s AND Kode_Produk = %s""",
                        (jumlah, self.no_transaksi, produk.get_kode_produk()),
                    )
                else:
                    raise e  
        conn.commit()

class Struk:
    def __init__(self, transaksi, NIK_pegawai):
        self.no_struk = f"ST{str(uuid.uuid4().int)[:3]}" 
        self.transaksi = transaksi
        self.NIK_pegawai = NIK_pegawai
        self.nama_pegawai = self.get_nama_pegawai(NIK_pegawai)

    def get_nama_pegawai(self, NIK):
        cur.execute("SELECT Nama_Pegawai FROM pegawai WHERE NIK = %s", (NIK,))
        data = cur.fetchone()
        if data:
            return data[0]
        else:
            return "Pegawai Tidak Ditemukan"

    def cetak_struk(self):
        print("="*10 + "RUMAH MAKAN BHARATA" + "="*10)
        print(f"No Struk        : {self.no_struk}")
        print(f"No Transaksi    : {self.transaksi.no_transaksi}")
        for produk, jumlah in self.transaksi.produk_list:
            print("-"*39)
            print(f"Nama Produk     : {produk.nama_produk}")
            print(f"Jumlah Produk   : {jumlah}")
        print("-"*39)
        print(f"Total Harga     : Rp. {self.transaksi.total_harga}")
        print(f"Nama Pegawai    : {self.nama_pegawai}")
        print("="*39)

    def simpan_struk(self):
        cur.execute("""INSERT INTO struk (No_Struk, NIK, No_Transaksi, Total_Harga) VALUES (%s, %s, %s, %s)""",
                    (self.no_struk, self.NIK_pegawai, self.transaksi.no_transaksi, self.transaksi.total_harga))
        conn.commit()

def menu_produk():
    while True:
        os.system("cls")
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
                print("Produk Berhasil Ditambahkan!")
                os.system("pause")

            elif pilih == 2:
                Produk.lihat_produk()
                os.system("pause")

            elif pilih == 3:
                Produk.lihat_produk()
                print("\n")
                kode_produk = str(input("Masukan Kode Produk Yang Akan Dihapus : "))

                if Produk.cari_produk(kode_produk):
                    Produk.hapus_produk(kode_produk)
                    print(f"Produk Dengan Kode {kode_produk} Berhasil Dihapus!")
                else:
                    print(f"Produk Dengan Kode {kode_produk} Tidak Ditemukan!")
                os.system("pause")

            elif pilih == 4:
                Produk.lihat_produk()
                print("\n")
                kode_produk_ubah = str(input("Masukan Kode Produk Yang Akan Diubah : "))
                
                if Produk.cari_produk(kode_produk_ubah):
                    nama_baru = str(input("Masukan Nama Baru Produk : "))
                    jenis_baru = str(input("Masukan Jenis Baru Produk : "))
                    harga_baru = int(input("Masukan Harga Baru Produk : "))

                    Produk.edit_produk(kode_produk_ubah, nama_baru, jenis_baru, harga_baru)
                    print(f"Produk Dengan Kode {kode_produk_ubah} Berhasil Diubah!")

                else:
                    print(f"Produk Dengan Kode {kode_produk_ubah} Tidak Ditemukan!")
                os.system("pause")

            elif pilih == 5:
                return
            
            else:
                print("PILIHAN MENU TIDAK TERSEDIA!!")
                os.system("pause")

        except ValueError:
            print("INPUTAN SALAH SILAHKAN INPUT DENGAN ANGKA!!")
            os.system("pause")

def menu_pegawai():
    while True:
        os.system("cls")
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
                print(f"Pegawai Dengan NIK {NIK} Berhasil Ditambahkan!")
                os.system("pause")

            elif pilih == 2:
                Pegawai.lihat_pegawai()
                os.system("pause")

            elif pilih == 3:
                Pegawai.lihat_pegawai()
                print("\n")
                NIK = str(input("Masukan NIK Pegawai Yang Ingin Dihapus : "))

                if Pegawai.cari_pegawai(NIK):
                    Pegawai.hapus_pegawai(NIK)
                    print(f"Pegawai Dengan NIK {NIK} Berhasil Dihapus!")
                else:
                    print(f"Pegawai Dengan NIK {NIK} Tidak Ditemukan!")
                os.system("pause")

            elif pilih == 4:
                Pegawai.lihat_pegawai()
                print("\n")
                NIK = str(input("Masukan NIK Pegawai Yang Akan Diubah : "))

                if Pegawai.cari_pegawai(NIK):
                    nama_baru = str(input("Masukan Nama Baru Pegawai : "))
                    alamat_baru = str(input("Masukan Alamat baru Pegawai : "))
                    Pegawai.edit_pegawai(nama_baru, alamat_baru, NIK)
                    print(f"Pegawai Dengan NIK {NIK} Berhasil Diubah!")
                else:
                    print(f"Pegawai Dengan NIK {NIK} Tidak Ditemukan!")
                os.system("pause")

            elif pilih == 5:
                return

            else:
                print("PILIHAN MENU TIDAK TERSEDIA!!")
                os.system("pause")

        except ValueError:
            print("INPUTAN SALAH SILAHKAN INPUT DENGAN ANGKA!!")
            os.system("pause")

def menu_transaksi():
    while True:
        os.system("cls")
        try:
            print("="*10 + "MENU TRANSAKSI" + "="*10)
            print("1. Tambah Transaksi")
            print("2. Lihat Riwayat Transaksi")
            print("3. Keluar")

            pilih = int(input("Masukan Pilihan Menu : "))

            if pilih == 1:
                Pegawai.lihat_pegawai()
                print("\n")
                NIK_pegawai = input("Masukkan NIK Pegawai yang Melakukan Transaksi: ")

                # Mengecek apakah NIK pegawai valid
                cur.execute("SELECT * FROM pegawai WHERE NIK = %s", (NIK_pegawai,))
                pegawai = cur.fetchone()
                if not pegawai:
                    print("NIK Pegawai Tidak Ditemukan!")
                    os.system("pause")
                    continue  #pegawai tidak ditemuksn

                transaksi = Transaksi()
                while True:
                    Produk.lihat_produk()
                    print("\n")
                    kode_produk = input("Masukan Kode Produk (atau tekan Enter untuk selesai): ")
                    if kode_produk.strip() == "":
                        break

                    cur.execute("SELECT * FROM produk WHERE Kode_Produk = %s", (kode_produk,))
                    data_produk = cur.fetchone()

                    if data_produk:
                        nama_produk, jenis_produk, harga = data_produk[1], data_produk[2], data_produk[3]
                        produk = Produk(nama_produk, jenis_produk, harga)
                        produk._kode_produk = kode_produk
                        jumlah_produk = int(input(f"Masukan Jumlah Produk: "))

                        transaksi.tambah_produk(produk, jumlah_produk)
                    else:
                        print(f"PRODUK DENGAN KODE {kode_produk} TIDAK DITEMUKAN!")
                        os.system("pause")

                if transaksi.produk_list:
                    transaksi.tambah_transaksi()
                    print("TRANSAKSI BERHASIL DITAMBAHKAN!")

                    # Membuat struk dan mencetaknya
                    struk = Struk(transaksi=transaksi, NIK_pegawai=NIK_pegawai)
                    print("\n")
                    struk.cetak_struk()
                    print("\n")
                    struk.simpan_struk()  # simpan struk ke db
                    os.system("pause")

                else:
                    print("TIDAK ADA PRODUK YANG DITAMBAHKAN DALAM TRANSAKSI.")
                    os.system("pause")

            elif pilih == 2:
                cur.execute("SELECT * FROM transaksi")
                list_transaksi = cur.fetchall()
                print(tabulate(list_transaksi, headers=["No_Transaksi", "Tanggal_Transaksi", "Kode_Produk", "Jumlah_Produk"], tablefmt="pretty"))
                os.system("pause")

            elif pilih == 3:
                return

            else:
                print("PILIHAN MENU TIDAK TERSEDIA!!")
                os.system("pause")

        except ValueError:
            print("INPUTAN SALAH SILAHKAN INPUT DENGAN ANGKA!!")
            os.system("pause")

def main():
    while True:
        os.system("cls")
        try:
            print("="*10 + "RUMAH MAKAN BHARATA" + "="*10)
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
                os.system("pause")
            
        except ValueError:
            print("INPUTAN SALAH SILAHKAN INPUT DENGAN ANGKA!!")
            os.system("pause")


if __name__ == "__main__":
    main()
