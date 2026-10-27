# variabel percabangannya #
#nama = "Azmi"
#kelas = "C1"

#nalgoritma = 90
#nagama = 90
#nbasisdata = 90

nama_mahasiswa = input("Masukkan nama mahasiswa : ")
nilai_algoritma = int(input("Masukkan nilai algoritma : "))
nilai_agama = int(input("Masukkan nilai agama : "))
nilai_basisdata = int(input("Masukkan nilai basisdata : "))
nilai_matematika = int(input("Masukkan nilai matematika : "))
nilai_fisika = int(input("Masukkan nilai fisika : "))
nilai_logika_komputer = int(input("Masukkan nilai logika komputer : "))
nilai__terapan_komputer = int(input("Masukkan nilai terapan komputer : "))
nilai_rata = (nilai_algoritma + nilai_agama + nilai_basisdata + nilai_matematika + nilai_fisika + nilai_logika_komputer + nilai__terapan_komputer) / 7

print("nilai rata-rata mahasiswa", nama_mahasiswa, "adalah", nilai_rata)
# penentuan lulus atau tidaknya mahasiswa
if nilai_rata >= 80 and nilai_rata <= 100:
    print("Nilai : A")
    #Jika terpenuhi maka akan menampilkan nilai A
    #maka
elif nilai_rata >= 70 and nilai_rata < 80:
    print("Nilai : B")
elif nilai_rata >= 60 and nilai_rata < 70:
    print("Nilai : C")
elif nilai_rata >= 50 and nilai_rata < 60:
    print("Nilai : D")
else:
    print("Nilai : E")