# program calon mahasiswa
Diketahui hasil pendaftaran mahasiswa baru diextract dari database ke suatu array CalonMhs. Data CalonMhs yang disimpan adalah sebagai berikut:
-	Nomor peserta calon mahasiswa
-	Nama peserta calon mahasiswa
-	Jurusan yang dipilih
-	Nilai ujian tes masuk
Contoh data array CalonMhs sebagai berikut:
Index Array	0	1	2
No Peserta 	A12	B13	A45
Nama Peserta 	Daniel	Rina	Merry
Jurusan dipilih	FT2	FT2	FBE1
Nilai Ujian	355	298	145

Selain itu juga terdapat array yang menampung data jurusan dimana class jurusan terdiri dari:
-	Kode jurusan
-	Nama jurusan
-	Kapasitas
-	Nilai minimal
Contoh data array Jurusan adalah sebagai berikut
Index Array	0	1	2
Kode Jurusan 	FT1	FBE1	FT2
Nama Jurusan 	Teknik Industri	Manajemen	Teknik Informatika
Kapasitas	300	500	250
Nilai minimal	250	190	300

Syarat seorang calon mahasiswa dapat diterima disuatu jurusan adalah:
1.	Kapasitas masih tersedia (penerimaan sesuai index array)
2.	Nilau Ujian minimal sama dengan Nilai minimal yang ditetapkan oleh jurusan.
Untuk setiap jurusan, selain ditentukan calon mahasiswa sesuai kapasitas yang tersedia, juga dipilih cadangan yang jumlahnya senilai 10 persen dari kapasitas yang tersedia.
Buatlah program untuk mendapatkan data calon mahasiswa yang diterima serta data calon mahasiswa cadangan dari suatu jurusan tertentu.





#program pemilu
Dalam sebuah system pemilihan umum, data nama calon kepala daerah disimpan dalam sebuah array, contohnya seperti berikut:
Index	0	1	2
Nama kepala daerah	Daniel	Budi	Rina

Selain itu, hasil pilihan public juga disimpan dalam sebuah array, seperti contoh berikut:
Index	0	1	2	3	4	…
Nomor Calon	2	0	1	1	2	

Buatkan programnya untuk menentukan pemenang dalam pemilu dimana pemenang ditentukan oleh jumlah total suara terbanyak



#program trading
Seorang programmer mencoba menganalisa hasil pembelian dan penjualan saham sebuah perusahaan dengan tujuan untuk mendapatkan keuntungan melalui transaksi saham. Diasumsikan terdapat array yang menyimpan data harga saham (dalam USD) pada menit tertentu setelah pasar saham dibuka.
Contoh:
Jika pasar saham dibuka pukul 9.00, maka index 0 menyatakan harga saham pada pukul 9.00, index 30 menyatakan harga saham pada pukul 9.30, index 60 menyatakan harga saham pada pukul 10.00. 
Jadi jika Array[75] = 100, artinya pada jam 10.15 harga saham = 100USD.
Buatkan program untuk mencari keuntungan maksimal yang dapat diperoleh berdasarkan isi array.
Contoh:
Misalnya isi array adalah [100,89,70,80,78,75,90,95,88,84,93,90,85]
Maka keuntungan maksimal adalah 95-70=25USD
Penjelasan:
Harga terendah adalah 70USD, maka saham dibeli pada saat itu
Harga tertinggi setelah waktu pembelian adalah 95USD, maka saham dijual pada saat itu. Harga 100 diabaikan karena terjadi sebelum pembelian. 
