def get_accepted_candidates(jurusan):
    data_calon_mhs = [
        {"No Peserta": "A12", "Nama Peserta": "Daniel", "Jurusan dipilih": "FT2", "Nilai Ujian": 355},
        {"No Peserta": "B13", "Nama Peserta": "Rina", "Jurusan dipilih": "FT2", "Nilai Ujian": 298},
        {"No Peserta": "A45", "Nama Peserta": "Merry", "Jurusan dipilih": "FBE1", "Nilai Ujian": 145}
    ]

    data_jurusan = [
        {"Kode Jurusan": "FT1", "Nama Jurusan": "Teknik Industri", "Kapasitas": 300, "Nilai minimal": 250},
        {"Kode Jurusan": "FBE1", "Nama Jurusan": "Manajemen", "Kapasitas": 500, "Nilai minimal": 190},
        {"Kode Jurusan": "FT2", "Nama Jurusan": "Teknik Informatika", "Kapasitas": 250, "Nilai minimal": 300}
    ]

    calon_mhs_diterima = []
    calon_mhs_cadangan = []

    for calon_mhs in data_calon_mhs: #iterasi elemen list - elemen disimpan di variabel calon_mhs
        if calon_mhs["Jurusan dipilih"] == jurusan: #cek kondisi jurusan yg dipilih
            for j in data_jurusan: #iterasi elemen list jurusan - elemen disimpan divariabel j
                if j["Kode Jurusan"] == jurusan: #cek kodejurusan
                    if len(calon_mhs_diterima) < j["Kapasitas"]: #cek diterima -lebih besar atau sama dengan nilai minimal yang ditetapkan oleh jurusan
                        if calon_mhs["Nilai Ujian"] >= j["Nilai minimal"]: #Jika calon mahasiswa memenuhi semua syarat, maka calon mahasiswa tersebut ditambahkan ke dalam list 
                            calon_mhs_diterima.append(calon_mhs)
                        else:
                            calon_mhs_cadangan.append(calon_mhs) #jika tidak masuk cadangan
                    else:
                        calon_mhs_cadangan.append(calon_mhs)
                    break

    return calon_mhs_diterima, calon_mhs_cadangan

# Contoh pemanggilan fungsi untuk mendapatkan data calon mahasiswa diterima dan cadangan di jurusan FT2
calon_mhs_diterima, calon_mhs_cadangan = get_accepted_candidates("FT2")

print("Calon Mahasiswa Diterima:")
for calon_mhs in calon_mhs_diterima:
    print("Nomor Peserta:", calon_mhs["No Peserta"])
    print("Nama Peserta:", calon_mhs["Nama Peserta"])
    print("Jurusan Dipilih:", calon_mhs["Jurusan dipilih"])
    print("Nilai Ujian:", calon_mhs["Nilai Ujian"])
    print()

print("Calon Mahasiswa Cadangan:")
for calon_mhs in calon_mhs_cadangan:
    print("Nomor Peserta:", calon_mhs["No Peserta"])
    print("Nama Peserta:", calon_mhs["Nama Peserta"])
    print("Jurusan Dipilih:", calon_mhs["Jurusan dipilih"])
    print("Nilai Ujian:", calon_mhs["Nilai Ujian"])
    print()
