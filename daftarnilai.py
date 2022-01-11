#Membuat List
r = [7,8,9,6,"Billy Alfauzi Caesar"]
s = []

print(30*"=")

#Ubah Element List
r[3]=10
print (r) #Mengubah Nilai Ke-4
r[3:5]= 5,"Weh"
print (r) #Mengubah Elemen Ke-4 s/d Terakhir

print(30*"=")

#Tambah Element List
s.append(r[3:5])
print(s) # Mengambil 2 bagian dari List r Dan Dijadikan List s 
s.extend(["Iya"])
print(s) 
s.extend([2,3,4])
print(s)

#Hapus Data
del r[4]
print (r)
print(30*"=")

#Mencari Data
Cari = input("masukan nilai yang dicari: ")
ketemu = False
for i in range(0, len(r)):
    if Cari == r[i]:
        ketemu = True
        break
if ketemu:
    print ("Nilai : ", Cari, "Berhasil ditemukan")
else:
    print("Nilai : ", Cari, "Tidak ditemukan")