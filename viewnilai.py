print("=================================")
print("Program Input Nilai")
print("=================================")
print("Data Nilai Mahasiswa Kelas TI21A1")
print("=================================")

daftar = {}

while True:
    
    perintah = input("(L) Lihat, (T) Tambah, (U) Ubah, \n"
                     "(H) Hapus, (C) Cari, (K) Keluar: ")
    print("=================================")

    # Keluar
    if perintah.lower() == 'k':
        break

    # Lihat
    elif perintah.lower() == 'l':
        print("Daftar Nilai:")
        print("===================================================================")
        print("| No |      Nama      |    NIM    | Tugas |  UTS  |  UAS  | Akhir |")
        print("===================================================================")
        no = 1
        for tabel in daftar.values():
            print("| {0:2} | {1:14} | {2:9} | {3:5} | {4:5} | {5:5} | {6:5} |".format
                  (no, tabel[0],
                   tabel[1], tabel[2],
                   tabel[3], tabel[4], tabel[5]))
            no += 1
        print("===================================================================")

    # Tambah
    elif perintah.lower() == 't':
        print("data mahasiswa")
        print("...")
        nama = input("nama: ")
        nim = input("NIM: ")
        n_tugas = int(input("Tugas: "))
        n_UTS = int(input("UTS: "))
        n_UAS = int(input("UAS: "))
        a = n_tugas * 30 / 100
        b = n_UTS * 35 / 100
        c = n_UAS * 35 / 100
        n_akhir = a + b + c
        daftar[nama] = [nama, nim, n_tugas, n_UTS, n_UAS, n_akhir]

    # Ubah
    elif perintah.lower() == 'u':
        nama = input("Masukan nama untuk mengubah data: ")
        if nama in daftar.keys():
            print("Masukan data yang ingin di ubah :")
            data = input("(Semua), (Nama), (NIM), "
                         "(Tugas), (UTS), (UAS) : ")
            if data.lower() == "semua":
                print("==========================")
                print("Ubah data {}.".format(nama))
                print("==========================")
                daftar[nama][1] = input("Edit NIM:")
                daftar[nama][2] = int(input("Edit Nilai Tugas: "))
                daftar[nama][3] = int(input("Edit Nilai UTS: "))
                daftar[nama][4] = int(input("Edit Nilai UAS: "))
                # print(daftar)
            elif data.lower() == "nim":
                daftar[nama][1] = input("NIM:")
            elif data.lower() == "tugas":
                daftar[nama][2] = int(input("Nilai Tugas: "))
            elif data.lower() == "uts":
                daftar[nama][3] = int(input("Nilai UTS: "))
            elif data.lower() == "uas":
                daftar[nama][4] = int(input("Nilai UAS: "))
            else:
                print("Perintah tidak ditemukan.")
    #Cari
    elif perintah.lower()=='C':
        nama = input("masukan nilai yang dicari: ")
        ketemu = False
        for i in range(0, len(daftar)):
            if nama == daftar[i]:i
            ketemu = True
            break 
            if ketemu:
                print ("Nilai : ", nama, "Berhasil ditemukan")
            else:
                print("Nilai : ", nama, "Tidak ditemukan")