DataKaryawan={
    (11011):{
        'NAMA': 'Alvin',
        'UMUR': 32,
        'GENDER': 'Pria',
        'JABATAN': 'Manajer Keuangan',
        'GAJI': 25000000,
        'PENDIDIKAN TERAKHIR': 'S2 Manajemen'
    },
    (11012):{
        'NAMA': 'Benny',
        'UMUR': 29,
        'GENDER': 'Pria',
        'JABATAN': 'Manajer Operasional',
        'GAJI': 23000000,
        'PENDIDIKAN TERAKHIR': 'S2 Teknik Elektro'
    },
    (11013):{
        'NAMA': 'Fina',
        'UMUR': 27,
        'GENDER': 'Wanita',
        'JABATAN': 'Manajer Pemasaran',
        'GAJI': 18000000,
        'PENDIDIKAN TERAKHIR': 'S1 Desain Produk'
     }
}
Judul=['ID','NAMA','UMUR','GENDER','JABATAN','GAJI','PENDIDIKAN TERAKHIR']

def Menu():    
    print('''
Menu Utama
1. Menampilkan Data Karyawan
2. Menambah Data Karyawan
3. Memperbarui Data Karyawan
4. Menghapus Data Karyawan
5. Exit
    ''')
    InputMenu=int(input('Masukan Angka Menu yang Ingin Anda Akses: '))
    if InputMenu==1:
        Read()
    elif InputMenu==2:
        Create()
    elif InputMenu==3:
        Update()
    elif InputMenu==4:
        Delete()
    elif InputMenu==5:
        ExitMenu=(input('Apakah Anda Yakin Keluar dari Program (Iya/Tidak): '))
        if ExitMenu.lower()=='iya':
            print('Terimakasih')
        elif ExitMenu.lower()=='tidak':
            print('Kembali ke Halaman Utama')
            Menu()
        else:
            print('''
    Angka yang Anda Masukan Tidak Terdapat Didalam Menu
    Kembali Ke Menu Sebelumnya
                ''')
            Menu()

def Read():
    print('''
1. Menampilkan Data
2. Mengakses Data ID
3. Kembali ke Menu Utama
    ''')
    MenuRead=int(input('Pilih Angka Menu yg Ingin Diakses: '))
    if MenuRead==1:
        Data()
        Read()
    elif MenuRead==2:
        Data()
        while True:
            PrimaryKey=int(input('Masukan ID Data yang akan Diakses: '))
            if PrimaryKey in DataKaryawan.keys():
                print(F'{Judul[0]}\t|\t{Judul[1]}\t|\t{Judul[2]}\t|\t{Judul[3]}\t|\t{Judul[4]}\t\t\t|\t{Judul[5]}\t\t|\t{Judul[6]}')
                print('='*150)
                print(f'{PrimaryKey}\t|\t{DataKaryawan[PrimaryKey]["NAMA"]}\t|\t{DataKaryawan[PrimaryKey]["UMUR"]}\t|\t{DataKaryawan[PrimaryKey]["GENDER"]}\t|\t{DataKaryawan[PrimaryKey]["JABATAN"]}\t|\t{DataKaryawan[PrimaryKey]["GAJI"]}\t|\t{DataKaryawan[PrimaryKey]["PENDIDIKAN TERAKHIR"]}')
                Read()
                break
            else:
                print('''
ID yang Dimasukan Tidak Ditemukan
Silahkan Masukan ID Kembali                
                ''')
                False
    elif MenuRead==3:
        while True:
            ExitRead=input('Apakah Anda Yakin Keluar dari Menu (Iya/Tidak):')
            if ExitRead.lower()=='iya':
                print('Kembali ke Menu Utama')
                Menu()
                break  
            elif ExitRead.lower()=='tidak':
                print('Kembali ke Halaman Sebelumnya')
                Read()
                break
            else:
                print('''
Angka Menu yang Anda Masukan Tidak Valid
Silahkam Masukan Angka Menu Kembali
                ''')
                False
    else:
        print('''
Angka yang Anda Masukan Tidak Terdapat Didalam Menu
Silahkan Masukan Angka Kembali
        ''')
        Read()

def Create():
    print('''
1. Menambah Data
2. Kembali ke Menu Utama
    ''')
    MenuCreate=int(input('Pilih Angka Menu yg Ingin Diakses: '))
    if MenuCreate==1:
        while True:
            global ID, Nama, Umur, Gender, Jabatan, Gaji, PendidikanTerakhir
            ID=int(input('Masukan ID: '))
            if ID in DataKaryawan.keys():
                print('''
ID yang Dimasukan Sudah Digunakan
Silahkan Masukan ID Kembali
            ''')
                False
            else:
                break
        Nama=input('Masukan Nama: ')
        Umur=int(input('Masukan Umur: '))
        Gender=input('Masukan Gender (Pria/Wanita): ')
        Jabatan=input('Masukan Jabatan: ')
        Gaji=int(input('Masukan Gaji: '))
        PendidikanTerakhir=input('Masukan Pendidikan Terakhir: ')
        Confirmation1=input('Simpan Data(Iya/Tidak): ')
        if Confirmation1.lower()=='iya':
            DataKaryawan.update({(ID):{'NAMA':Nama, 'UMUR':Umur, 'GENDER':Gender, 'JABATAN':Jabatan, 'GAJI':Gaji, 'PENDIDIKAN TERAKHIR':PendidikanTerakhir}})
            print('Data Berhasil Tersimpan!')
            Data()
            Create()
        elif Confirmation1.lower()=='tidak':
            print('Data Belum Tersimpan')
            Create()
        else:
            print('''
Input yang Anda Masukan Tidak Valid
Kembali ke Menu Sebelumnya
                    ''')
            Create()
    elif MenuCreate==2:
        while True:
            ExitCreate=input('Apakah Anda Yakin Keluar dari Menu (Iya/Tidak):')
            if ExitCreate.lower()=='iya':
                print('Kembali ke Menu Utama')
                Menu()
                break
            elif ExitCreate.lower()=='tidak':
                print('Kembali ke Halaman Sebelumnya')
                Create()
                break
            else:
                print('''
Angka Menu yang Anda Masukan Tidak Valid
Silahkam Masukan Angka Menu Kembali
                ''')
                False
    else:
        print('''
Angka yang Anda Masukan Tidak Terdapat Didalam Menu
Silahkan Masukan Angka Kembali
        ''')
        Create()

def Update():
    print('''
1. Mengubah Data
2. Kembali ke Menu Utama
    ''')
    MenuUpdate=int(input('Pilih Angka Menu yg Ingin Diakses: '))
    if MenuUpdate==1:
        Data()
        while True:
            UpdateID=int(input('Masukan ID yang ingin Dirubah: '))
            if UpdateID in DataKaryawan.keys():
                break
            else:
                print('ID Tidak Ditemukan!')
                False
        while True:
            UpdateKolom=input('Masukan Kolom yang Akan Dirubah: ').upper()
            if UpdateKolom.upper() in DataKaryawan[UpdateID].keys():
                UpdateNilai=input('Masukan Nilai Baru: ')
                Confirmation2=input('Simpan Data(Iya/Tidak): ')
                if Confirmation2.lower()=='iya':
                    print('Data Berhasil Tersimpan')
                    DataKaryawan[UpdateID].update({UpdateKolom:UpdateNilai})
                    Data()
                    Update()
                    break
                elif Confirmation2.lower()=='tidak':
                    print('Data Belum Tersimpan')
                    Update()
                    break
                else:
                    print('''
Input yang Anda Masukan Tidak Valid
Kembali ke Menu Sebelumnya
                    ''')
                    Update()
            else:
                print('''
Kolom Tidak Ditemukan
Silahkan Masukan Kembali
                ''')
                False
    elif MenuUpdate==2:
        while True:
            ExitUpdate=input('Apakah Anda Yakin Keluar dari Menu (Iya/Tidak):')
            if ExitUpdate.lower()=='iya':
                print('Kembali ke Menu Utama')
                Menu()
                break
            elif ExitUpdate.lower()=='tidak':
                print('Kembali ke Halaman Sebelumnya')
                Update()
                break
            else:
                print('''
Angka Menu yang Anda Masukan Tidak Valid
Silahkam Masukan Angka Menu Kembali
                ''')
                False
    else:
        print('''
Angka yang Anda Masukan Tidak Terdapat Didalam Menu
Silahkan Masukan Angka Kembali
        ''')
        Update()

def Delete():
    print('''
1. Menghapus Data
2. Kembali ke Menu Utama
    ''')
    MenuDelete=int(input('Pilih Angka Menu yg Ingin Diakses: '))
    if MenuDelete==1:
        while True:
            DeleteID=int(input('Masukan ID yang Ingin Dihapus: '))
            if DeleteID in DataKaryawan.keys():
                Confirmation3=input('Apakah Anda Yakin Akan Menghapus ID(Iya/Tidak): ')
                if Confirmation3.lower()=='iya':
                    DataKaryawan.pop(DeleteID)
                    print('Data Berhasil Dihapus!')
                    break
                elif Confirmation3.lower()=='tidak':
                    print('Data Belum Tersimpan')
                    Delete()
                    break
                else:
                    print('''
Input yang Anda Masukan Tidak Valid
Kembali ke Menu Sebelumnya
                    ''')
                    Delete()
                    break
            else:
                print('''
ID yang Anda Masukan Tidak Ditemukan
Silahkan Masukan ID Kembali
            ''')
                False
        Data()
        Delete()
    elif MenuDelete==2:
        while True:
            ExitDelete=input('Apakah Anda Yakin Keluar dari Menu (Iya/Tidak):')
            if ExitDelete.lower()=='iya':
                print('Kembali ke Menu Utama')
                Menu()
                break
            elif ExitDelete.lower()=='tidak':
                print('Kembali ke Halaman Sebelumnya')
                Delete()
                break
            else:
                print('''
Angka Menu yang Anda Masukan Tidak Valid
Silahkan Masukan Angka Menu Kembali
                ''')
                False
    else:
        print('''
Angka yang Anda Masukan Tidak Terdapat Didalam Menu
Silahkan Masukan Angka Kembali
        ''')
        Delete()

def Data():
    print(f'{Judul[0]:5}|{Judul[1]:15}|{Judul[2]:4}|{Judul[3]:7}|{Judul[4]:20}|{Judul[5]:8}|{Judul[6]:20}')
    print('='*90)
    for a in DataKaryawan.keys():
        print(f'{a:5}|{DataKaryawan[a]["NAMA"]:15}|{DataKaryawan[a]["UMUR"]:4}|{DataKaryawan[a]["GENDER"]:7}|{DataKaryawan[a]["JABATAN"]:20}|{DataKaryawan[a]["GAJI"]:8}|{DataKaryawan[a]["PENDIDIKAN TERAKHIR"]:20}')

print('Selamat Datang di Program Data Karyawan Perusahaan')
Menu()


