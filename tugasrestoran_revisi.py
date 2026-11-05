print("=" * 40)
print("      RR Resto")
print("=" * 40)

nama_pelanggan = input("Masukkan nama pelanggan: ")   
total = 0                        
rincian = ""                     
while True:

    print()
    print("--- DAFTAR MENU ---")
    print("1. Nasi Goreng - Rp25000")
    print("2. Kwetiaw Daging    - Rp25000")
    print("3. Nasi Kebuli Kambing - Rp27000")
    print("4. Sate Taichan   - Rp20000")
    print("5. Sop Ayam        - Rp18000")
    print("0. Selesai Memilih")
    
    pilihan = int(input("Pilih menu (0-5): "))

    if pilihan == 0: 
        break                    

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
    else:                        
        print("Pilihan tidak tersedia!")
        continue               

    jumlah = int(input("Masukkan jumlah: "))

    if jumlah <= 0:             
        print("Jumlah harus lebih dari 0!")
        continue

    subtotal = harga * jumlah  
    total = total + subtotal     

    print("Subtotal", nama, "x", jumlah, "= Rp", subtotal)
    print("Total sementara = Rp", total)

    rincian = rincian + "\n"
    rincian = rincian + "Menu     : " + nama + "\n"
    rincian = rincian + "Harga    : Rp " + str(harga) + "\n"
    rincian = rincian + "Jumlah   : " + str(jumlah) + "\n"
    rincian = rincian + "Subtotal : Rp " + str(subtotal) + "\n"


if total > 200000:    
    diskon = 20
else:
    diskon = 0

potongan = int(total * diskon / 100) 
total_bayar = total - potongan

print()
print("=" * 40)
print("         STRUK PEMBAYARAN")
print("Nama Pelanggan:", nama_pelanggan)

print(rincian)      

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