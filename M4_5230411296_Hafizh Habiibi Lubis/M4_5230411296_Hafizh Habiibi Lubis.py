from tabulate import tabulate

class Debitur():
    def __init__(self, nama, ktp, limit):
        self.nama = nama
        self.__ktp = ktp
        self._limit = limit

    def display(self):
        data = [[self.nama, self.__ktp, self._limit]]
        headers = ["Nama Debitur", "Nomor KTP", "Limit Pinjaman (Rp.)"] 
        print(tabulate(data, headers, tablefmt="fancy_grid"))

class Pinjaman(Debitur):
    def __init__(self, nama, ktp, limit, jmlPinjaman, bunga, bulan, angsuran):
        super().__init__(nama, ktp, limit)

        self.jmlPinjaman = jmlPinjaman
        self.bunga = bunga
        self.bulan = bulan
        self.angsuran = angsuran

    def display_pinjam(self):
        data = [[self.nama, self.jmlPinjaman, self.bunga, self.bulan, self.angsuran]]
        headers = ["Nama Debitur", "Jumlah Pinjaman (Rp.)", "Bunga Pinjaman", "Bulan", "Angsuran Perbulan (Rp.)"]
        print(tabulate(data, headers, tablefmt="fancy_grid"))

deb1 = Debitur("Ciko", 123, 1200000)
deb2 = Debitur("Ciki", 123, 1000000)

debitur = [deb1, deb2]
simpanPinjaman = []

# Debitur
def tambah_debitur():
    nama = str(input("Masukan nama debitur baru : "))
    ktp = int(input("Masukan nomor KTP debitur baru : "))

    for i in debitur:
        if i._Debitur__ktp == ktp:
            print("NO KTP SUDAH ADA, SILAHKAN MASUKAN NO KTP YANG BERBEDA! \n")
            return
        
    limit = int(input("Masukan Limit Pinjam : "))
    masuk = Debitur(nama, ktp, limit)
    debitur.append(masuk)
    print("Debitur baru berhaisl ditambahkan! \n")

def tampil_debitur():
    for i in debitur:
        i.display()

def cari_debitur():
    nama = str(input("Masukan nama debitur yang akan dicari : "))
    
    for i in debitur:
        if i.nama == nama:
            i.display()
            break
    else:
        print("Nama Debitur tidak ditemukan")

# Pinjaman
def pinjam():
    nama = str(input("Masukan nama debitur : "))
    namaTerdaftar = False
    for i in debitur:
        if i.nama == nama:
            namaTerdaftar = True
            break

    if not namaTerdaftar:
        print("NAMA DEBITUR BELUM TERDAFTAR!")
        print("\n")
        return
        
    for i in debitur:
        if i.nama == nama:

            jmlPinjaman = int(input("Masukan jumlah pinjaman : "))
            if jmlPinjaman > i._limit:
                print("JUMLAH PINJAMAN MELEBIHI LIMIT!")
                print("\n")
                return
            
            bunga = int(input("Masukan suku bunga (%) : ")) / 100
            bulan = int(input("Masukan jumlah bulan peminjaman : "))
            angsuranPokok = jmlPinjaman * (bunga / 100)
            angsuranBulanan = angsuranPokok / bulan
            angsuranTotal = angsuranPokok + angsuranBulanan
            masuk = Pinjaman(nama, i._Debitur__ktp, i._limit, jmlPinjaman, bunga, bulan, angsuranTotal)
            simpanPinjaman.append(masuk)

def tampil_pinjaman():
    for i in simpanPinjaman:
        i.display_pinjam()

def kelola_debitur():
    while True:
        try:
            print("="*10 + "RUMAH PINJOL" + "="*10)
            print("1. Tampilkan Semua Debitur")
            print("2. Cari Debitur")
            print("3. Tambah Debitur")
            print("4. Keluar")

            pilih = int(input("Pilih Menu : "))
            print("\n")
            if pilih == 1:
                tampil_debitur()
                print("\n")
            elif pilih == 2:
                cari_debitur()
                print("\n")
            elif pilih == 3:
                tambah_debitur()
            elif pilih == 4:
                return

        except ValueError:
            print("INPUTAN SALAH, SILAHKAN INPUT ULANG!")
            continue

def kelola_pinjaman():
    while True:
        try:
            print("="*10 + "RUMAH PINJOL" + "="*10)
            print("1. Tambah Pinjaman")
            print("2. Tampilkan Pinjaman")
            print("3. Keluar")

            pilih = int(input("Pilih Menu : "))
            print("\n")
            if pilih == 1:
                pinjam()
            elif pilih == 2:
                tampil_pinjaman()
                print("\n")
            elif pilih == 3:
                return
            
        except ValueError:
            print("INPUTAN SALAH, SILAHKAN INPUT ULANG!")
            continue

def rumah_pinjol():
    while True:
        try:
            print("="*10 + "RUMAH PINJOL" + "="*10)
            print("1. Kelola Debitur")
            print("2. Kelola Pinjaman")
            print("3. Keluar")

            pilih = int(input("Pilih Menu : "))
            print("\n")
            if pilih == 1:
                kelola_debitur()
            elif pilih == 2:
                kelola_pinjaman()
            elif pilih == 3:
                print("TERIMAKASIH TELAH MENGGUNAKAN RUMAH PINJOL")
                return
            
        except ValueError: 
            print("INPUTAN SALAH, SILAHKAN INPUT ULANG!")
            continue

rumah_pinjol()