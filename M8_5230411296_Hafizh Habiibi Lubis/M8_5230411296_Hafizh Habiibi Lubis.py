import tkinter as tk
import datetime
from tkinter import ttk, messagebox
from reportlab.pdfgen import canvas

class TilangApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SITILANG ODNI")
        self.root.geometry("1240x720")
        self.root.configure(bg = "white")

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
        self.name_entry = tk.Entry(frame_left)
        self.name_entry.pack(fill="x", anchor="w", padx=10, pady=2)

        # NIK Terdakwa
        nik_label = tk.Label(frame_left, text="NIK TERDAKWA", font=self.default_font)
        nik_label.pack(anchor="w", padx=10, pady=8)
        self.nik_entry = tk.Entry(frame_left)
        self.nik_entry.pack(fill="x", anchor="w", padx=10, pady=2)

        # Alamat Terdakwa
        alm_label = tk.Label(frame_left, text="ALAMAT TERDAKWA", font=self.default_font)
        alm_label.pack(anchor="w", padx=10, pady=8)
        self.alm_entry = tk.Entry(frame_left)
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
        self.alm_entry = tk.Entry(frame_left)
        self.alm_entry.pack(fill="x", anchor="w", padx=10, pady=2)

        # Merk Kendaraan
        mrk_label = tk.Label(frame_left, text="MERK KENDARAAN", font=self.default_font)
        mrk_label.pack(anchor="w", padx=10, pady=8)
        self.mrk_entry = tk.Entry(frame_left)
        self.mrk_entry.pack(fill="x", anchor="w", padx=10, pady=2)

        # Seri Kendaraan
        seri_label = tk.Label(frame_left, text="SERI KENDARAAN", font=self.default_font)
        seri_label.pack(anchor="w", padx=10, pady=8)
        self.seri_entry = tk.Entry(frame_left)
        self.seri_entry.pack(fill="x", anchor="w", padx=10, pady=2)

        # Menu Petugas
        td_menu = tk.Label(frame_right, text="MENU PETUGAS", font=("Courier New", 12, "bold"))
        td_menu.pack(anchor="center", pady=20)

        # Jenis Pelanggaran
        plg_label = tk.Label(frame_right, text="JENIS PELANGGARAN", font=self.default_font)
        plg_label.pack(anchor="w", padx=10, pady=8)
        self.plg_menu = ttk.Combobox(frame_right, font=self.default_font)
        self.plg_menu.pack(fill="x", anchor="w", padx=10, pady=2)

        # Nama Petugas
        ptg_label = tk.Label(frame_right, text="NAMA PETUGAS", font=self.default_font)
        ptg_label.pack(anchor="w", padx=10, pady=8)
        self.ptg_entry = tk.Entry(frame_right)
        self.ptg_entry.pack(fill="x", anchor="w", padx=10, pady=2)

    # Fungsi
    def update_pelanggaran(self, event):
        kendaraan = self.jnk_menu.get()

        pelanggaran = {
            "Motor":[("Surat Tidak Lengkap", 150000), ("Tidak Pakai Helem", 100000), ("Plat tidak standar", 100000)],
            "Mobil":[("Surat Tidak Lengkap", 250000), ("Tidak Pakai Seatbelt", 120000), ("Kebut Kebutan", 200000)],
            "Truck":[("Surat Tidak Lengkap", 350000), ("Tidak Pakai Seatbelt", 220000), ("Muatan Berlebih", 300000)]
        }

        if kendaraan in pelanggaran:
            pelanggaran_list = [f"{plg[0]} - Denda: {plg[1]}" for plg in list(pelanggaran[kendaraan])]
            self.plg_menu['values'] = pelanggaran_list
            self.plg_menu.set('') #Reset Pilihan




if __name__ == "__main__":
    root = tk.Tk()
    app = TilangApp(root)
    root.mainloop()

