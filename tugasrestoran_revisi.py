# ==========================================================
# Konsep: variabel, input/print, if-elif-else, while,
#         operasi aritmatika, break, dan continue
# ==========================================================

# ---------- 1. MULAI PROGRAM ----------
print("=" * 40)                  # mencetak tanda "=" sebanyak 40 kali (garis)
print("      RR Resto")
print("=" * 40)

nama_pelanggan = input("Masukkan nama pelanggan: ")   # simpan nama yang diketik user
total = 0                        # variabel total belanja, awalnya 0
rincian = ""                     # variabel teks untuk menyimpan rincian pesanan (awalnya kosong)

# ---------- PERULANGAN PEMESANAN ----------
while True:                      # ulangi terus sampai ada perintah break

    # ---------- 2. TAMPILKAN MENU MAKANAN ----------
    print()                      # baris kosong
    print("--- DAFTAR MENU ---")
    print("1. Nasi Goreng - Rp25000")
    print("2. Kwetiaw Daging    - Rp25000")
    print("3. Nasi Kebuli Kambing - Rp27000")
    print("4. Sate Taichan   - Rp20000")
    print("5. Sop Ayam        - Rp18000")
    print("0. Selesai Memilih")

    # ---------- 3. PILIH MENU ----------
    pilihan = int(input("Pilih menu (0-5): "))   # int() mengubah teks menjadi angka

    # ---------- 4. APAKAH PILIHAN 0? ----------
    if pilihan == 0:             # jika pilihan sama dengan 0
        break                    # keluar dari while

    # Tentukan nama dan harga sesuai pilihan
    if pilihan == 1:
        nama = "Nasi Goreng"
        harga = 25000
    elif pilihan == 2:
        nama = "Kwetiaw Daging"
        harga = 25000
    elif pilihan == 3:
        nama = "Nasi Kebuli Kambing"
        harga = 27000
    elif pilihan == 4:
        nama = "Sate Taichan"
        harga = 20000
    elif pilihan == 5:
        nama = "Sop Ayam"
        harga = 18000
    else:                        # angka selain 0-5
        print("Pilihan tidak tersedia!")
        continue                 # kembali ke awal while

    # ---------- INPUT JUMLAH & HITUNG SUBTOTAL ----------
    jumlah = int(input("Masukkan jumlah: "))

    if jumlah <= 0:              # jumlah tidak boleh 0 atau minus
        print("Jumlah harus lebih dari 0!")
        continue

    subtotal = harga * jumlah    # perkalian
    total = total + subtotal     # subtotal ditambahkan ke total

    print("Subtotal", nama, "x", jumlah, "= Rp", subtotal)
    print("Total sementara = Rp", total)

    # Catat pesanan ini ke rincian (teks ditambah terus setiap kali memesan)
    # "+" pada teks = menggabungkan, str() = mengubah angka menjadi teks, "\n" = pindah baris
    rincian = rincian + "\n"
    rincian = rincian + "Menu     : " + nama + "\n"
    rincian = rincian + "Harga    : Rp " + str(harga) + "\n"
    rincian = rincian + "Jumlah   : " + str(jumlah) + "\n"
    rincian = rincian + "Subtotal : Rp " + str(subtotal) + "\n"

# ---------- 5. HITUNG DISKON ----------
if total > 200000:               # jika total lebih dari 200000
    diskon = 20
else:
    diskon = 0

potongan = int(total * diskon / 100)   # hitung potongan harga (int agar tanpa koma)
total_bayar = total - potongan         # total dikurangi potongan

# ---------- 6. TAMPILKAN STRUK PEMBAYARAN ----------
print()
print("=" * 40)
print("         STRUK PEMBAYARAN")
print("Nama Pelanggan:", nama_pelanggan)

print(rincian)                   # tampilkan semua rincian pesanan yang sudah dicatat

print("=" * 40)
print("Total Belanja : Rp", total)
print("Diskon        :", diskon, "%")
print("Potongan      : Rp", potongan)
print("=" * 40)
print("Total Bayar   : Rp", total_bayar)
print("=" * 40)
print("           TERIMA KASIH")

print()
print("Terimakasih sudah melakukan pemesanan,", nama_pelanggan)