def find_winner(nama_calon, nomor_calon): #parameter cek array
    total_suara = {} #simpan jumlah suara

    for i in range(len(nomor_calon)): #setiap nomor calon yg dihitung disimpan ditotal suara
        nomor = nomor_calon[i]
        if nomor in total_suara:
            total_suara[nomor] += 1 #jika sudah ada suara tambah 1
        else:
            total_suara[nomor] = 1 

    pemenang = max(total_suara, key=total_suara.get) #nilai terbesar total suara
    jumlah_suara_terbanyak = total_suara[pemenang]
    nama_pemenang = nama_calon[pemenang]

    return nama_pemenang, jumlah_suara_terbanyak

# Data calon kepala daerah
nama_calon = ["Daniel", "Budi", "Rina"]

# Data hasil pemilihan
nomor_calon = [2, 0, 1, 1, 2]

# Memanggil fungsi untuk menentukan pemenang
nama_pemenang, jumlah_suara_terbanyak = find_winner(nama_calon, nomor_calon)

print("Pemenang Pemilihan Umum:")
print("Nama:", nama_pemenang)
print("Jumlah Suara:", jumlah_suara_terbanyak)
