import tkinter as tk
import datetime as dt
import uuid
from tkinter import ttk, messagebox
from reportlab.pdfgen import canvas

class TilangApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SITILANG ODNI")
        self.root.geometry("1366x768")
        self.root.configure(bg = "white")

        self.cek_nik = []
        self.cek_plat = []
        self.default_font = ("Courier New", 10)
        self.widget_create()
    
    # Tampilan
    def widget_create(self):
        # TItle
        title_label = tk.Label(text="SATUAN LALU LINTAS KEPOLISIAN NEGERI ODNI", font=("Courier New", 20, "bold"), bg="white")
        title_app = tk.Label(text="SITILANG ODNI", font=("Courier New", 18, "bold"), bg="white")
        title_label.pack()
        title_app.pack()

        # Frame
        frame_left = tk.Frame(root, highlightbackground="black", highlightthickness=3)
        frame_left.pack(side="left",padx=20, pady=20, anchor="n", expand=True, fill="both")

        frame_right = tk.Frame(root, highlightbackground="black", highlightthickness=3)
        frame_right.pack(side="right", padx=20, pady=20, anchor="n", expand=True, fill="both")

        # Menu Terdakwa
        td_menu = tk.Label(frame_left, text="DATA DIRI TERDAKWA", font=("Courier New", 12, "bold"))
        td_menu.pack(anchor="center", pady=20)

        # Nama Terdakwa
        name_label = tk.Label(frame_left, text="NAMA TERDAKWA", font=self.default_font)
        name_label.pack(anchor="w", padx=10)
        self.name_var = tk.StringVar()
        self.name_entry = tk.Entry(frame_left, textvariable=self.name_var)
        self.name_entry.pack(fill="x", anchor="w", padx=10, pady=2)

        # NIK Terdakwa
        nik_label = tk.Label(frame_left, text="NIK TERDAKWA", font=self.default_font)
        nik_label.pack(anchor="w", padx=10, pady=8)
        self.nik_var = tk.StringVar()
        self.nik_entry = tk.Entry(frame_left, textvariable=self.nik_var)
        self.nik_entry.pack(fill="x", anchor="w", padx=10, pady=2)

        # Alamat Terdakwa
        alm_label = tk.Label(frame_left, text="ALAMAT TERDAKWA", font=self.default_font)
        alm_label.pack(anchor="w", padx=10, pady=8)
        self.alm_var = tk.StringVar()
        self.alm_entry = tk.Entry(frame_left, textvariable=self.alm_var)
        self.alm_entry.pack(fill="x", anchor="w", padx=10, pady=2)

        # Menu Kendaraan
        td_menu = tk.Label(frame_left, text="DATA KENDARAAN", font=("Courier New", 12, "bold"))
        td_menu.pack(anchor="center", pady=20)

        # Jenis Kendaraan
        jnk_list = ["Motor", "Mobil", "Truck"]
        jnk_label = tk.Label(frame_left, text="JENIS KENDARAAN", font=self.default_font)
        jnk_label.pack(anchor="w", padx=10, pady=8)
        self.jnk_menu = ttk.Combobox(frame_left, values=jnk_list, font=self.default_font)
        self.jnk_menu.pack(fill="x", anchor="w", padx=10, pady=2)
        self.jnk_menu.bind("<<ComboboxSelected>>", self.update_pelanggaran)

        # Nomor Plat Kendaraan
        plt_label = tk.Label(frame_left, text="NO PLAT KENDARAAN", font=self.default_font)
        plt_label.pack(anchor="w", padx=10, pady=8)
        self.plt_var = tk.StringVar()
        self.plt_entry = tk.Entry(frame_left, textvariable=self.plt_var)
        self.plt_entry.pack(fill="x", anchor="w", padx=10, pady=2)

        # Merk Kendaraan
        mrk_label = tk.Label(frame_left, text="MERK KENDARAAN", font=self.default_font)
        mrk_label.pack(anchor="w", padx=10, pady=8)
        self.mrk_var = tk.StringVar()
        self.mrk_entry = tk.Entry(frame_left, textvariable=self.mrk_var)
        self.mrk_entry.pack(fill="x", anchor="w", padx=10, pady=2)

        # Seri Kendaraan
        seri_label = tk.Label(frame_left, text="SERI KENDARAAN", font=self.default_font)
        seri_label.pack(anchor="w", padx=10, pady=8)
        self.seri_var = tk.StringVar()
        self.seri_entry = tk.Entry(frame_left, textvariable=self.seri_var)
        self.seri_entry.pack(fill="x", anchor="w", padx=10, pady=2)

        # Menu Petugas
        td_menu = tk.Label(frame_right, text="MENU PETUGAS", font=("Courier New", 12, "bold"))
        td_menu.pack(anchor="center", pady=20)

        # Jenis Pelanggaran 1
        plg_label = tk.Label(frame_right, text="JENIS PELANGGARAN 1", font=self.default_font)
        plg_label.pack(anchor="w", padx=10, pady=8)
        self.plg_menu = ttk.Combobox(frame_right, font=self.default_font)
        self.plg_menu.pack(fill="x", anchor="w", padx=10, pady=2)

        # Jenis Pelanggaran 2
        plg_label2 = tk.Label(frame_right, text="JENIS PELANGGARAN 2", font=self.default_font)
        plg_label2.pack(anchor="w", padx=10, pady=5)
        self.plg_menu2 = ttk.Combobox(frame_right, font=self.default_font)
        self.plg_menu2.pack(fill="x", anchor="w", padx=10, pady=2)
        self.plg_menu2.bind("<<ComboboxSelected>>", self.cek_pelanggaran1)

        # Nama Petugas
        ptg_label = tk.Label(frame_right, text="NAMA PETUGAS", font=self.default_font)
        ptg_label.pack(anchor="w", padx=10, pady=8)
        self.ptg_var = tk.StringVar()
        self.ptg_entry = tk.Entry(frame_right, textvariable=self.ptg_var)
        self.ptg_entry.pack(fill="x", anchor="w", padx=10, pady=2)

        # riwayat
        rwy_frame = tk.Label(frame_right, text="RIWAYAT TIKET", font=self.default_font)
        rwy_frame.pack(fill="both", padx=10, pady=5)

        self.rwy_preview = ttk.Treeview(rwy_frame, columns=("No Tiket", "Nama Terdakwa", "Pelanggaran", "Pelanggaran 2"), show="headings")
        self.rwy_preview.heading("No Tiket", text="No Tiket")
        self.rwy_preview.heading("Nama Terdakwa", text="Nama Terdakwa")
        self.rwy_preview.heading("Pelanggaran", text="Pelanggaran")
        self.rwy_preview.heading("Pelanggaran 2", text="Pelanggaran 2")
        self.rwy_preview.pack(fill="x", expand=True, padx=10, pady=10)

        # Setting ke tengah
        self.rwy_preview.column("No Tiket", anchor="center")
        self.rwy_preview.column("Nama Terdakwa", anchor="center")
        self.rwy_preview.column("Pelanggaran", anchor="center")
        self.rwy_preview.column("Pelanggaran 2", anchor="center")

        # Tombol Cetak
        ctk_button = tk.Button(frame_right, text="CETAK TIKET", width=50, command=self.buat_pdf)
        ctk_button.pack(padx=10, pady=5, anchor="center")

        # Tombol Hapus Riwayat
        reset_button = tk.Button(frame_right, text="RESET", width=50,command=self.hapus_riwayat)
        reset_button.pack(padx=10, pady=10, anchor="center")

    # Fungsi
    def update_pelanggaran(self, event):
        kendaraan = self.jnk_menu.get()

        pelanggaran = {
            "Motor":[("Surat Tidak Lengkap", 150000), ("Tidak Pakai Helm", 100000), ("Plat Tidak Standar", 100000)],
            "Mobil":[("Surat Tidak Lengkap", 250000), ("Tidak Pakai Seatbelt", 120000), ("Kebut Kebutan", 200000)],
            "Truck":[("Surat Tidak Lengkap", 350000), ("Tidak Pakai Seatbelt", 220000), ("Muatan Berlebih", 300000)]
        }

        if kendaraan in pelanggaran:
            pelanggaran_list = [f"{plg[0]} - Denda : RP.{plg[1]:,}" for plg in list(pelanggaran[kendaraan])]
            self.plg_menu['values'] = pelanggaran_list
            self.plg_menu2['values'] = pelanggaran_list

            #Reset Pilihan ketika pilihan jenis kendaraan berubah
            self.plg_menu.set('') 
            self.plg_menu2.set('')

    def cek_pelanggaran1(self, event):
        if not self.plg_menu.get():
            messagebox.showerror("ERROR", "HARAP ISI PELANGGARAN 1 TERLEBIH DAHULU!")
            self.plg_menu2.set('')

    def nomor_tiket(self):
        now = dt.date.today().strftime("%d-%m-%Y")
        return f"TILANG-{now}-{str(uuid.uuid4())[:4]}"
    
    # Ekstrak Denda dari Pelanggaran
    def ekstrak_denda(self, pelanggaran):
        if "Denda : RP." in pelanggaran:
            try:
                # Mengambil angka setelah "Denda : RP."
                return int(pelanggaran.split("Denda : RP.")[-1].replace(",", ""))
            except ValueError:
                return 0  # Jika format tidak sesuai, anggap denda 0
        return 0
    
    def buat_pdf(self):
        no_tiket = self.nomor_tiket()
        pdf = canvas.Canvas(filename=f"tikettilang_{no_tiket}.pdf")
        pdf.setTitle(title=f"tikettilang_{no_tiket}")

        # Ambil Value Semua Entry / Combobox
        nama_terdakwa = self.name_entry.get()
        nik_terdakwa = self.nik_entry.get()
        alamat_terdakwa = self.alm_entry.get()
        jenis_kendaraan = self.jnk_menu.get()
        plat_kendaraan = self.plt_entry.get()
        merk_kendaraan = self.mrk_entry.get()
        seri_kendaraan = self.seri_entry.get()
        pelanggaran = self.plg_menu.get()
        pelanggaran2 = self.plg_menu2.get()
        nama_petugas = self.ptg_entry.get()

        # Validasi Form Kosong
        if not all([nama_terdakwa, nik_terdakwa, alamat_terdakwa, jenis_kendaraan,
                    plat_kendaraan, merk_kendaraan, seri_kendaraan, nama_petugas]):
            messagebox.showerror("ERROR", "PASTIKAN SEMUA DATA TERISI!")
            return
        
        # Validasi Format NIK
        if not nik_terdakwa.isdigit() or len(nik_terdakwa) != 5:
            messagebox.showerror("ERROR", "NIK TERDAKWA HARUS ANGKA DAN BERJUMLAH 5 DIGIT!")
            return
        
        # Validasi Pelanggaran
        if pelanggaran == pelanggaran2:
            messagebox.showerror("ERROR", "INPUTAN PELANGGARAN HARUS BERBEDA!")
            self.plg_menu2.set('')
            return
        
        # Validasi NIK
        if nik_terdakwa in self.cek_nik:
            messagebox.showerror("ERROR", "NIK TERDAKWA SUDAH ADA!")
            return
        
        # Validasi Plat
        if plat_kendaraan in self.cek_plat:
            messagebox.showerror("ERROR", "NOMOR PLAT SUDAH ADA!")
            return
            
        # Simpan NIK dan Plat setelah semuanya valid
        self.cek_plat.append(plat_kendaraan)
        self.cek_nik.append(nik_terdakwa)

        # Hapus Isi Form Setelah Pencet Tombol Cetak Tiket 
        self.name_var.set("")
        self.nik_var.set("")
        self.alm_var.set("")
        self.plt_var.set("")
        self.mrk_var.set("")
        self.seri_var.set("")
        self.ptg_var.set("")
        self.plg_menu.set("")
        self.plg_menu2.set("")
        self.jnk_menu.set("")

        # menghitung total denda
        denda_1 = self.ekstrak_denda(pelanggaran)
        denda_2 = self.ekstrak_denda(pelanggaran2) if pelanggaran2 else 0
        total_denda = denda_1 + denda_2

        # Header
        pdf.setFont('Courier', 20)
        pdf.drawString(180,770, "KEPOLISIAN NEGERI ODNI") 

        pdf.setFont('Courier', 12)
        pdf.drawString(163,750, "SATUAN LALU LINTAS KEPOLISIAN NEGERI ODNI")

        pdf.setFont('Courier', 12)
        pdf.drawString(225, 730, f"{no_tiket}")
        pdf.drawString(100, 710, "="*60)

        # isi
        pdf.setFont('Courier', 12)
        pdf.drawString(100, 670, f"Nama Terdakwa: {nama_terdakwa}")
        pdf.drawString(100, 650, f"NIK: {nik_terdakwa}")
        pdf.drawString(100, 630, f"Alamat: {alamat_terdakwa}")
        pdf.drawString(100, 610, f"Jenis Kendaraan: {jenis_kendaraan}")
        pdf.drawString(100, 590, f"Nomor Plat: {plat_kendaraan}")
        pdf.drawString(100, 570, f"Merk: {merk_kendaraan}")
        pdf.drawString(100, 550, f"Seri: {seri_kendaraan}")
        pdf.drawString(100, 530, f"Pelanggaran: {pelanggaran}")
        if pelanggaran2:
            pdf.drawString(100, 510, f"Pelanggaran 2: {pelanggaran2}")

        pdf.drawString(225, 470, f"Total Denda : RP.{total_denda:,}")

        pdf.setFont('Courier',15)
        pdf.drawString(140, 430, "SEGERA BAYARKAN UANG DENDA KE PETUGAS :)")

        # Footer
        pdf.setFont('Courier', 12)
        pdf.drawString(420, 390, "PETUGAS")
        pdf.drawString(420, 370, f"{nama_petugas}")
        pdf.drawString(100,350, "="*60)
        
        pdf.save()

        # tambah ke treeview
        self.rwy_preview.insert("", "end", values=(no_tiket, nama_terdakwa, pelanggaran, pelanggaran2))

    # Hapus Isi Treeview + Validasi
    def hapus_riwayat(self):
        confirm = messagebox.askquestion("", "YAKIN HAPUS SEMUA RIWAYAT?")
        if confirm == "YES".lower():
            for item in self.rwy_preview.get_children():
                self.rwy_preview.delete(item)

if __name__ == "__main__":
    root = tk.Tk()
    app = TilangApp(root)
    root.mainloop()