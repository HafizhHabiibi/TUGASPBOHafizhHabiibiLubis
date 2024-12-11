import mysql.connector
from tabulate import tabulate
from uuid import uuid4


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
#             NIK CHAR(16) NOT NULL,
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