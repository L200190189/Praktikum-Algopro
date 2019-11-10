## Program Akun
## Dibuat oleh Muhammad Habiburrahman L200190189
import random
angka = random.randint(0,1000)

Nama = 'Muhammad Habiburrahman'
TanggalLahir = '27 Agustus 2001'
NamaSingkat = Nama[0] + '.' + Nama[9:14]
Username = Nama[0] + TanggalLahir[0:2] + TanggalLahir[11:15]
Password = Nama[0:3] + str(angka)

print(Nama)
print(TanggalLahir)
print(NamaSingkat)
print(Username)
print(Password)
