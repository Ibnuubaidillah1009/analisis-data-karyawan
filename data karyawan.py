import csv
import os

# Nama file untuk menyimpan data karyawan
nama_file = r'C:\Users\User\Desktop\python\data_karyawan.csv'

# Fungsi untuk mengecek apakah file data sudah ada, jika tidak buat baru
def initialize_data_file():
    if not os.path.isfile(nama_file):
        with open(nama_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Nama', 'Posisi', 'Gaji'])

# Fungsi untuk menambahkan karyawan baru
def tambah_karyawan():
    id_karyawan = input("Masukkan ID Karyawan: ")
    nama = input("Masukkan Nama Karyawan: ")
    posisi = input("Masukkan Jabatan: ")
    gaji = input("Masukkan Gaji Karyawan: ")

    with open(nama_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([id_karyawan, nama, posisi, gaji])

    print("Karyawan berhasil ditambahkan.")

# Fungsi untuk menampilkan semua karyawan
def tampilkan_karyawan():
    with open(nama_file, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

# Fungsi untuk menghapus karyawan berdasarkan ID
def hapus_karyawan():
    id_karyawan = input("Masukkan ID Karyawan yang akan dihapus: ")

    rows = []
    with open(nama_file, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] != id_karyawan:
                rows.append(row)

    with open(nama_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print(f"Karyawan dengan ID {id_karyawan} berhasil dihapus.")

# Fungsi untuk mengedit data karyawan
def edit_karyawan():
    id_karyawan = input("Masukkan ID Karyawan yang akan diedit: ")

    rows = []
    found = False
    with open(nama_file, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == id_karyawan:
                found = True
                print(f"Data Karyawan: {row}")
                nama_baru = input("Masukkan Nama Baru (Kosongkan jika tidak ingin mengubah): ")
                posisi_baru = input("Masukkan Posisi Baru (Kosongkan jika tidak ingin mengubah): ")
                gaji_baru = input("Masukkan Gaji Baru (Kosongkan jika tidak ingin mengubah): ")
                row[1] = nama_baru if nama_baru else row[1]
                row[2] = posisi_baru if posisi_baru else row[2]
                row[3] = gaji_baru if gaji_baru else row[3]
            rows.append(row)

    if not found:
        print(f"Tidak ada karyawan dengan ID {id_karyawan}.")
        return

    with open(nama_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print(f"Karyawan dengan ID {id_karyawan} berhasil diubah.")

# Fungsi utama untuk menampilkan menu
def menu():
    initialize_data_file()
    
    while True:
        print("\nSistem Manajemen Data Karyawan")
        print("1. Tambah Karyawan")
        print("2. Tampilkan Karyawan")
        print("3. Edit Karyawan")
        print("4. Hapus Karyawan")
        print("5. Keluar")

        pilihan = input("Pilih opsi: ")

        if pilihan == '1':
            tambah_karyawan()
        elif pilihan == '2':
            tampilkan_karyawan()
        elif pilihan == '3':
            edit_karyawan()
        elif pilihan == '4':
            hapus_karyawan()
        elif pilihan == '5':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == '__main__':
    initialize_data_file()
    menu()
