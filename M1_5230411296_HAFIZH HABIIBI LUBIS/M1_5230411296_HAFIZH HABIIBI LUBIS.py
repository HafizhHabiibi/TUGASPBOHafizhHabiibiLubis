import math

print("Menghitung Luas Permukaan & Volume Limas Segi Empat\n")
a = int(input("Masukan Panjang Sisi Persegi (CM) : "))
b = int(input("Masukan Tinggi Segitiga (CM) : "))

def luasPermukaanLimas(a, b):
    global Lpersegi
    Lpersegi = a**2
    Lsegitiga = 4 * (1/2 * a * b)
    Llimas = Lpersegi + Lsegitiga

    return Llimas

def volumeLimas(a, b):
    Tlimas = math.sqrt(b**2 - (a/2)**2)
    Vlimas = 1/3 * (Lpersegi * Tlimas)

    return Vlimas


lp = luasPermukaanLimas(a, b)
vo = volumeLimas(a, b)
print(f"Luas Permukaan Limas Segi Empat Tersebut Adalah : {lp} CM Persegi")
print(f"Volume Limas Tersebut Segi Empat Adalah : {vo} CM Kubik")