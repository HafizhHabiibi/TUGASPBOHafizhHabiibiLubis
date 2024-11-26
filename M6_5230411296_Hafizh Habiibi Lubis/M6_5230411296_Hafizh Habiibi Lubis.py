from tabulate import tabulate

class Order: 
    orderan = []
    pengiriman = []
    id_order = 1

    def __init__(self):
        self._id_order = Order.id_order
        self.name = ""
        self.jumlah = 0
        self.detail = ""
        Order.id_order += 1

    def setOrder(self):
        self.name = str(input("Masukkan produk yang ingin dipesan: "))
        try:
            self.jumlah = int(input("Masukkan jumlah produk yang ingin dipesan: "))

        except ValueError:
            print("\n")
            print("JUMLAH HARUS BERUPA ANGKA!")
            print("\n")
            return
        
        self.detail = str(input("Masukkan detail pesanan: "))
        Order.orderan.append([self._id_order, self.name, self.jumlah, self.detail])

    @classmethod
    def lihatOrder(cls):
        headers = ["ID", "NAMA PRODUK", "JUMLAH", "DETAIL"]
        if cls.orderan:
            print("\n")
            print(tabulate(cls.orderan, headers, tablefmt="fancy_grid"))
            print("\n")
        else:
            print("\n")
            print("TIDAK ADA PESANAN!")
            print("\n")

    @classmethod
    def ambilorder(cls, id_order):
        for order in cls.orderan:
            if order[0] == id_order:
                return order
        return None

class Deliver:
    def __init__(self):
        self.pilID = ""
        self.infotmation = ""
        self.date = ""
        self.address = ""

    def antar(self):
        self.pilID = int(input("Masukan ID orderan yang akan diantar : "))
        order = Order.ambilorder(self.pilID)
        if order:
            self.infotmation = str(input("Masukan Informasi Pengirimiman : "))
            self.date = str(input("Masukan Tanggal Pengirimin (Hari - Bulan - Tahun) : "))
            self.address = str(input("Masukan Alamat Pengirimiman : "))
            detailKirim = order + [self.infotmation, self.date, self.address]
            Order.pengiriman.append(detailKirim)
        else:
            print("\n")
            print("ID ORDER TIDAK DITEMUKAN!")
            print("\n")

    @classmethod
    def lihatPengiriman(cls):
        headers = ["ID", "NAMA PRODUK", "JUMLAH", "DETAIL", "INFORMASI", "TANGGAL", "ALAMAT"]
        if Order.pengiriman:
            print("\n")
            print(tabulate(Order.pengiriman, headers, tablefmt="fancy_grid"))
            print("\n")
        else:
            print("\n")
            print("BELUM ADA ORDERAN YANG DIKIRIMKAN!")
            print("\n")

def menuOrder():
    while True:
        try:
            print("="*20 + " BEGAL ORDER " + "="*20)
            print("1. Buat Order")
            print("2. Lihat Order")
            print("3. Antar Orderan")
            print("4. Lihat Data Pengantaran")
            print("5. Keluar")

            pilih = int(input("Masukkan menu yang ingin dipilih: "))

            if pilih == 1:
                order = Order()
                order.setOrder()
            elif pilih == 2:
                Order.lihatOrder()
            elif pilih == 3:
                deliver = Deliver()
                deliver.antar()
            elif pilih == 4:
                Deliver.lihatPengiriman()
            elif pilih == 5:
                print("="*20 + " TERIMAKASIH " + "="*20)
                return
            
        except ValueError:
            print("Inputan salah, silakan masukkan angka.")
            print("\n")

menuOrder()

