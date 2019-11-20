profil = {'NIM':'L200190189','Nama':'Habib','Alamat':'Solo','Hobi':'Travelling','Umur':'18','Asal':'Solo','Sekolah':'MAN 1 Surakarta'}
def nim():
    print('NIM: ' + profil['NIM'])
def nama():
    print('Nama: ' + profil['Nama'])
def alamat():
    print('Alamat: ' + profil['Alamat'])
def hobi():
    print('Hobi: ' + profil['Hobi'])
def umur():
    print('Umur: ' + profil['Umur'])
def asal():
    print('Asal: ' + profil['Asal'])
def sekolah():
    print('Sekolah: ' + profil['Sekolah'])
def b():
    print('''Pilihan yang tersedia:
    b Menampilkan bantuan ini
    1 Menampilkan NIM
    2 Menampilkan Nama
    3 Menampilkan Alamat
    4 Menampilkan Hobi
    5 Menampilkan Umur
    6 Menampilkan Asal
    7 Menampilkan Sekolah
    k QUIT''')
b()
while True:
    x = input('Pilihan yang tersedia: ')
    if x == 'b':
        b()
    elif x == '1':
        nim()
    elif x == '2':
        nama()
    elif x == '3':
        alamat()
    elif x == '4':
        hobi()
    elif x == '5':
        umur()
    elif x == '6':
        asal()
    elif x == '7':
        sekolah()
    elif x == 'k':
        print('Thanks and Goodbye')
        break
    
    
    
