import tkinter as tk
import datetime
from tkinter import ttk, messagebox
from reportlab.pdfgen import canvas

class TilangApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SITILANG ODNI")
        self.root.geometry("1000x1000")
        self.root.configure(bg = "white")

        self.widget_create()
    
    def widget_create(self):
        # TItle
        title_label = tk.Label(text="SATUAN LALU LINTAS KEPOLISIAN NEGERI ODNI", font=("Courier New", 20, "bold"), bg="white")
        title_app = tk.Label(text="SITILANG ODNI", font=("Courier New", 18, "bold"), bg="white")
        title_label.pack()
        title_app.pack()

        # Frame
        frame_left = tk.Frame(root, highlightbackground="black", highlightthickness=3)
        frame_left.pack(side="left",padx=20, pady=20, ipadx=20, ipady=20, fill="both", expand=True)

        frame_right = tk.Frame(root, highlightbackground="black", highlightthickness=3)
        frame_right.pack(side="right", padx=20, pady=20, ipadx=20, ipady=20, fill="both", expand=True)

        # Menu Terdakwa
        td_menu = tk.Label(frame_left, text="DATA DIRI TERDAKWA", font=("Courier New", 15, "bold"))
        td_menu.pack(anchor="center", pady=20)

        # Nama Terdakwa
        name_label = tk.Label(frame_left, text="NAMA TERDAKWA")
        name_label.pack(anchor="w", padx=10)
        self.name_entry = tk.Entry(frame_left)
        self.name_entry.pack(fill="x", anchor="w", padx=10, pady=2)

        # NIK Terdakwa
        nik_label = tk.Label(frame_left, text="NIK TERDAKWA")
        nik_label.pack(anchor="w", padx=10, pady=8)
        self.nik_entry = tk.Entry(frame_left)
        self.nik_entry.pack(fill="x", anchor="w", padx=10, pady=2)

        # Alamat Terdakwa
        alm_label = tk.Label(frame_left, text="ALAMAT TERDAKWA")
        alm_label.pack(anchor="w", padx=10, pady=8)
        self.alm_entry = tk.Entry(frame_left)
        self.alm_entry.pack(fill="x", anchor="w", padx=10, pady=2)

        # Menu Kendaraan
        td_menu = tk.Label(frame_left, text="DATA KENDARAAN", font=("Courier New", 15, "bold"))
        td_menu.pack(anchor="center", pady=20)


if __name__ == "__main__":
    root = tk.Tk()
    app = TilangApp(root)
    root.mainloop()

