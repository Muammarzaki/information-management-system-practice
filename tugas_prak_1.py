nama = input("Masukkan Nama Mahasiswa :")
nim = input("Masukkan NIM Mahasiswa :")
jurusan = input("Masukkan Jurusan Mahasiswa :")
ipk = float(input("Masukkan IPK Mahasiswa :"))

print('\nData Mahasiswa')
print(f'Nama: {nama}')
print(f'NIM: {nim}')
print(f'Jurusan: {jurusan}')
print(f'IPK: {ipk}')
if ipk == 4.0:
    print("Status IPK: Cum laude")