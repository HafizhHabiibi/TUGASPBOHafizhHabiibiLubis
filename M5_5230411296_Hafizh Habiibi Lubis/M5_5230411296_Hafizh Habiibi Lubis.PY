class Music:
    def __init__(self, judul, penyanyi, genre):
        self.judul = judul
        self.penyanyi = penyanyi
        self.genre = genre

class Hiphop(Music):
    def __init__(self):
        self.hiphop = []

    def tambah_hiphop(self, judul, penyanyi, genre):
        hiphop = next((hiphop for hiphop in self.hiphop if hiphop.judul == judul), None)
        if hiphop is None:
            new_song = Music(judul, penyanyi, genre)
            self.hiphop.append(new_song)
        else:
            print(f" Musik dengan judul {judul} sudah ada!")

    def display(self):
        if not self.hiphop:
            print("Musik tidak ditemukan")
        else:
            for i in self.hiphop:
                print(f"Judul {i.judul}, Penyanyi {i.penyanyi}, Genre {i.genre}")

class Jpop(Music):
    def __init__(self):
        self.jpop = []

    def tambah_jpop(self, judul, penyanyi, genre):
        jpop = next((jpop for jpop in self.jpop if jpop.judul == judul), None)
        if jpop is None:
            new_song = Music(judul, penyanyi, genre)
            self.jpop.append(new_song)

        else:
            print(f" Musik dengan judul {judul} sudah ada!")

    def display(self):
        if not self.jpop:
            print("Musik tidak ditemukan")
        else:
            for i in self.jpop:
                print(f"Judul {i.judul}, Penyanyi {i.penyanyi}, Genre {i.genre}")

class Rock(Music):
    def __init__(self):
        self.rock = []

    def tambah_rock(self, judul, penyanyi, genre):
        rock = next((rock for rock in self.rock if rock.judul == judul), None)
        if rock is None:
            new_song = Music(judul, penyanyi, genre)
            self.rock.append(new_song)
        
        else:
            print(f" Musik dengan judul {judul} sudah ada!")

    def display(self):
        if not self.rock:
            print("Musik tidak ditemukan")
        else:
            for i in self.rock:
                print(f"Judul {i.judul}, Penyanyi {i.penyanyi}, Genre {i.genre}")

def tmb_hiphop():
    judul = str(input("Masukan Judul Lagu : "))
    penyanyi = str(input("Masukan Nama Penyanyi : "))
    genre = str(input("Masukan Genre Musik : "))

    masuk = Hiphop()
    masuk.tambah_hiphop(judul, penyanyi, genre)

def tmp_hiphop():
    tampil = Hiphop()
    tampil.display()

def tmb_jpop():
    judul = str(input("Masukan Judul Lagu : "))
    penyanyi = str(input("Masukan Nama Penyanyi : "))
    genre = str(input("Masukan Genre Musik : "))

    masuk = Jpop()
    masuk.tambah_jpop(judul, penyanyi, genre)

def tmp_jpop():
    tampil = Jpop()
    tampil.display()

def tmb_rock():
    judul = str(input("Masukan Judul Lagu : "))
    penyanyi = str(input("Masukan Nama Penyanyi : "))
    genre = str(input("Masukan Genre Musik : "))

    masuk = Rock()
    masuk.tambah_rock(judul, penyanyi, genre)

def tmp_rock():
    tampil = Rock()
    tampil.display()

hiphop1 = Hiphop()
hiphop1.tambah_hiphop("Hit emp up", "2pac", "hiphop")

def hiphop():
    while True:
        try:
            print("="*5 + "HIP HOP" + "="*5)
            print("1. Display Song")
            print("2. Add Song")
            print("3. Delete Song")
            print("4. Keluar")

            pilih = int(input("Masukan Pilihan Anda : "))

            if pilih == 1:
                tmp_hiphop()
            elif pilih == 2:
                tmb_hiphop()
            elif pilih == 4:
                return

        except ValueError:
            print("INPUTAN SALAH SILAHKAN INPUT ULANG")
            continue
def jpop():
    while True:
        try:
            print("="*5 + "J POP" + "="*5)
            print("1. Display Song")
            print("2. Add Song")
            print("3. Delete Song")
            print("4. Keluar")

            pilih = int(input("Masukan Pilihan Anda : "))
            
            if pilih == 1:
                tmp_jpop()

            elif pilih == 2:
                tmb_jpop()

            elif pilih == 4:
                return

        except ValueError:
            print("INPUTAN SALAH SILAHKAN INPUT ULANG")
            continue

def rock():
    while True:
        try:
            print("="*5 + "ROCK" + "="*5)
            print("1. Display Song")
            print("2. Add Song")
            print("3. Delete Song")
            print("4. Keluar")

            pilih = int(input("Masukan Pilihan Anda : "))

            if pilih == 1:
                tmp_rock()

            elif pilih == 2:
                tmb_rock()

            elif pilih == 4:
                return

        except ValueError:
            print("INPUTAN SALAH SILAHKAN INPUT ULANG")
            continue


def music():
    while True:
        try:
            print("="*5 + "MUSIC" + "="*5)
            print("1. Hip Hop")
            print("2. J Pop")
            print("3. Rock")
            print("4. Display")
            print("5. Search Musik")
            print("6. Keluar")

            pilih = int(input("Masukan menu yang ingin anda pilih : "))

            if pilih == 1:
                hiphop()

            elif pilih == 2:
                jpop()

            elif pilih == 3:
                rock()

        except ValueError:
            print("INPUTAN SALAH SILAHKAN INPUT ULANG")
            continue

music()


