from view.view_nilai import search,cetak
from model.daftar_nilai import tambah_data, hapus_data, ubah_data, data

while True :
    print("\n=================================")
    c = input((("""
            (L) Lihat  :
            (T) Tambah :
            (U) Ubah   :
            (H) Hapus  :
            (C) Cari   :
            (K) Keluar :
                    """ )))

    print("===================================")

    if c.lower() == 'k':
        print("Arigatou Sudah Memakai program ini...")
        ext = input("Press ENTER to exit")
        if ext == '':
            break
        else:
            print("Pilih Menu Yang Ada di Atas")
    if c.lower() == 't':
        tambah_data()
        print(data)

    if c.lower() == 'l':
        cetak(data)

    if c.lower() == 'u':
        ubah_data()
    if c.lower() == 'h':
        hapus_data()
    if c.lower() == 'c':
        search()