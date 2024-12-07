import mysql.connector

conn = mysql.connector.connect(
    user = "root",
    host = "localhost",
    password = "",
    database = "penjualan"
)

cur = conn.cursor()

# membuat database
# cur.execute("CREATE DATABASE penjualan")

# # # membuat tabel pegawai
# cur.execute("""CREATE TABLE Pegawai (
#             NIK CHAR(16) NOT NULL PRIMARY KEY,
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
#             Detail_Transaksi VARCHAR(255))""")

# membuat tabel struk membuat composite key 
cur.execute("""CREATE TABLE Struk (
            NIK CHAR(16) NOT NULL,
            Kode_Produk CHAR(5) NOT NULL,
            No_Transaksi CHAR(7) NOT NULL,
            Jumlah_Produk INT(100),
            Total_Harga VARCHAR(30),
            PRIMARY KEY (NIK, Kode_Produk, No_Transaksi),
            FOREIGN KEY (NIK) REFERENCES Pegawai(NIK),
            FOREIGN KEY (Kode_Produk) REFERENCES Produk(Kode_Produk),
            FOREIGN KEY (No_Transaksi) REFERENCES Transaksi(No_Transaksi))""")
