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

if __name__ == "__main__":
    root = tk.Tk()
    app = TilangApp(root)
    root.mainloop()

