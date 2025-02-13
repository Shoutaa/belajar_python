absen = int(input("\nBerapa Absen : "))
tugas = int(input("Nilai Tugas : "))
uts = int(input("Nilai UTS : "))
uas = int(input("Nilai UAS : "))

nilai = (((absen/14) * 10)+((tugas/100) * 20)+((uts/100) * 30)+((uas/100) * 40))
ipk = (nilai*4)*0.01

if (absen/14) < 0.75:
    indeks = "E"
else:
    if nilai >= 80:
        indeks = "A"
    elif nilai >= 75:
        indeks = "AB"
    elif nilai >= 70:
        indeks = "B"
    elif nilai >= 65:
        indeks = "BC"
    elif nilai >= 60:
        indeks = "C"
    elif nilai >= 55:
        indeks = "D"
    else:
        indeks = "E"                                
print("Nilai : ", nilai)
print("Nilai IPK : ",ipk)
print("Indeks : ", indeks)
