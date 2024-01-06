from datetime import datetime, timedelta

def beli_tiket(kapal, kelas, stok):
    if stok[kelas] > 0:
        kapal.append([kelas, harga[kelas]])
        total_pembelian = sum(item[1] for item in kapal)
        stok[kelas] -= 1
        return total_pembelian
    else:
        print("Stok tiket kelas tersebut telah habis.")
        return 0

def pilih_kelas(stok):
    while True:
        pilihan = input("Pilih kelas tiket (BISNIS/EKONOMI/REGULER): ").upper()
        if pilihan in kelas and stok[pilihan] > 0:
            return pilihan
        elif pilihan in kelas:
            print("Stok tiket kelas tersebut telah habis.")
        else:
            print("Kelas tidak tersedia. Silahkan pilih kelas lain.")

def info_tiket(kapal):
    print("Tiket yang telah Anda beli:")
    for item in kapal:
        print(f"Kelas: {item[0]}, Harga: {item[1]}")

def get_jadwal():
    while True:
        tanggal = input("Masukkan tanggal berangkat (contoh: 2022-05-01): ")
        try:
            datetime.strptime(tanggal, '%Y-%m-%d')
            return tanggal
        except ValueError:
            print("Tanggal yang dimasukkan tidak valid. Silahkan masukkan tanggal yang benar.")

def get_jam():
    while True:
        jam = input("Masukkan jam berangkat (contoh: 07:00): ")
        try:
            datetime.strptime(jam, '%H:%M')
            return jam
        except ValueError:
            print("Jam yang dimasukkan tidak valid. Silahkan masukkan jam yang benar.")

harga = {'BISNIS': 500000, 'EKONOMI': 200000, 'REGULER': 100000}
kelas = ['BISNIS', 'EKONOMI', 'REGULER']
kapal = []
total_pembelian = 0
stok = {'BISNIS': 50, 'EKONOMI': 100, 'REGULER': 150}

print("Selamat datang di Pembelian Tiket Kapal")
tanggal = get_jadwal()
jam = get_jam()

while True:
    pilihan = input("Apakah ingin membeli tiket? (Y/N): ").upper()
    if pilihan == 'Y':
        kelas_pilih = pilih_kelas(stok)
        total_pembelian = beli_tiket(kapal, kelas_pilih, stok)
        print(f"Total pembelian: {total_pembelian}")
    elif pilihan == 'N':
        print("Terima kasih atas kunjungan Anda. Berikut ini informasi tiket yang telah Anda beli:")
        info_tiket(kapal)
        print(f"Jadwal berangkat: {tanggal} pukul {jam}")
        break
    else:
        print("Pilihan tidak valid. Silahkan pilih Y atau N.")