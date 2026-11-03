# ==========================================================
# Menggunakan: variabel, input/print, if-elif-else, while,
#              operasi aritmatika, break, dan continue
# ==========================================================

# ---------- 1. MULAI PROGRAM ----------
print("=" * 40)                 # mencetak tanda "=" sebanyak 40 kali (garis pembatas)
print("      Rotua Resto & Cafe")
print("=" * 40)

total = 0                       # variabel penyimpan total belanja, awalnya 0

# Input nama pelanggan: input() membaca ketikan user berupa teks,
# .strip() menghapus spasi di awal/akhir agar nama rapi
nama_pelanggan = input("Masukkan nama pelanggan: ").strip()

if nama_pelanggan == "":        # jika user tidak mengetik apa-apa (kosong)
    nama_pelanggan = "Pelanggan"    # pakai nama bawaan agar ucapan tetap rapi

# ---------- PERULANGAN UTAMA ----------
# "while True" artinya perulangan tanpa henti,
# baru berhenti jika bertemu perintah "break"
while True:

    # ---------- 2. TAMPILKAN MENU MAKANAN ----------
    print("\n--- DAFTAR MENU ---")   # \n = pindah baris (baris kosong sebelum judul)
    print("1. Nasi Goreng             - Rp25.000")
    print("2. Nila Bakar              - Rp27.000")
    print("3. Ayam Penyet             - Rp20.000")
    print("4. Pain au Chocolat        - Rp28.000")
    print("5. Croissant Butter        - Rp18.000")
    print("0. Selesai Memilih")

    # ---------- 3. PROSES PEMESANAN: PILIH MENU ----------
    try:                                            # "coba" jalankan kode di bawah ini
        pilihan = int(input("\nPilih menu (0-5): "))  # input() membaca ketikan (berupa teks),
                                                      # int() mengubahnya menjadi angka bulat
    except ValueError:                              # jika gagal diubah ke angka (mis. user ketik "abc")
        print("Input tidak valid! Masukkan angka 0-5.")
        continue                                    # lewati sisa kode, kembali ke awal while

    # ---------- 4. APAKAH PILIHAN 0? ----------
    if pilihan == 0:        # "==" artinya "sama dengan" (membandingkan)
        break               # keluar dari while, lanjut ke perhitungan diskon

    # ---------- MENENTUKAN NAMA & HARGA (pengganti dictionary) ----------
    if pilihan == 1:
        nama = "Nasi Goreng"
        harga = 25000
    elif pilihan == 2:      # elif = "jika tidak, tapi jika ..."
        nama = "Nila Bakar"
        harga = 27000
    elif pilihan == 3:
        nama = "Ayam Penyet"
        harga = 20000
    elif pilihan == 4:
        nama = "Pain au Chocolat"
        harga = 28000
    elif pilihan == 5:
        nama = "Croissant Butter"
        harga = 18000
    else:                   # jika angka di luar 0-5
        print("Pilihan tidak tersedia, silakan pilih 0-5!")
        continue            # ulangi dari awal while

    # ---------- INPUT JUMLAH ----------
    try:
        jumlah = int(input(f"Masukkan jumlah {nama}: "))  # f"..." = f-string, {nama} diganti isi variabel
    except ValueError:
        print("Jumlah tidak valid!")
        continue

    if jumlah <= 0:         
        print("Jumlah harus lebih dari 0!")
        continue

    # ---------- HITUNG SUBTOTAL ----------
    subtotal = harga * jumlah     # "*" = perkalian
    total += subtotal             # sama dengan: total = total + subtotal

    # f"{subtotal:,}" memberi pemisah ribuan berupa koma (25,000),
    # .replace(",", ".") mengganti koma menjadi titik (25.000) sesuai format Rupiah
    print(f"Subtotal {nama} x{jumlah} = Rp{subtotal:,}".replace(",", "."))
    print(f"Total sementara      = Rp{total:,}".replace(",", "."))

# ---------- 5. HITUNG DISKON ----------
if total > 200000:          # ">" artinya "lebih dari"
    persen_diskon = 20
else:
    persen_diskon = 0

potongan = total * persen_diskon / 100   # "/" = pembagian; contoh 215000 * 20 / 100 = 43000
total_bayar = total - potongan           # "-" = pengurangan

# ---------- 6. TAMPILKAN STRUK PEMBAYARAN ----------
print("\n" + "=" * 40)                    # "+" pada teks = menggabungkan teks
print("         STRUK PEMBAYARAN")
print("=" * 40)
print(f"Pelanggan     : {nama_pelanggan}")          # menampilkan nama pelanggan di struk
print(f"Total Belanja : Rp{total:,.0f}".replace(",", "."))   # ".0f" = tanpa angka di belakang koma
print(f"Diskon        : {persen_diskon}%")
print(f"Potongan      : Rp{potongan:,.0f}".replace(",", "."))
print("-" * 40)
print(f"Total Bayar   : Rp{total_bayar:,.0f}".replace(",", "."))
print("=" * 40)
print("           Terima Kasih")
print("=" * 40)

# Ucapan di bawah struk, nama diambil dari variabel nama_pelanggan
print(f"\nTerimakasih sudah melakukan pemesanan, {nama_pelanggan}!")