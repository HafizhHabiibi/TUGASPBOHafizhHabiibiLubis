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

# membuat tabel produk
cur.execute("""CREATE TABLE Produk (
            Kode_Produk CHAR(10) NOT NULL PRIMARY KEY,
            Nama_Produk VARCHAR(20),
            Jenis_Produk VARCHAR(8)),
            Harga INT(10))""")

# membuat tabel pegawai
cur.execute("""CREATE TABLE Pegawai (
            NIK CHAR(16) NOT NULL PRIMARY KEY,
            Nama_Pegawai VARCHAR(25),
            Alamat_Pegawai VARCHAR(255)
            )""")

# membuat tabel struk
cur.execute("""CREATE TABLE Struk (
            No_Transaksi CHAR(10) NOT NULL PRIMARY KEY,
            Jumlah_Produk INT(100),
            Total_Harga VARCHAR(30))""")

# membuat tabel transaksi
cur.execute("""CREATE TABLE Transaksi (
            Detail_Transaksi VARCHAR(255))""")

# Tambah foreign key

# # tabel struk
# cur.execute("""ALTER TABLE Struk
#             ADD FOREIGN KEY (NIK)
#             REFERENCES Pegawai(NIK)""")