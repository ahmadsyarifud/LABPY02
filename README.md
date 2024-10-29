# BIODATA
# AHMAD SYARIFUDIN
# 312410355
# TI.24.A4
# BAHASA PEMOGRAMAN

## LATIHAN 1
### MEMBUAT PROGRAM MENENTUKAN NILAI AKHIR
### DESKRIPSI

Program ini dirancang untuk menghitung nilai akhir mahasiswa berdasarkan beberapa komponen penilaian, seperti nilai UTS (Ujian Tengah Semester), UAS (Ujian Akhir Semester), dan tugas. Program akan menampilkan nilai akhir dan memberikan keterangan mengenai status kelulusan.
- 20% untuk nilai tugas
- 40% untuk nilai UTS
- 40% untuk nilau UAS
- 
### PENJELASAN PROGRAM

 1.Input: Meminta nama siswa dan nilai UTS, UAS, serta tugas.
 
 2. Perhitungan: Menghitung nilai akhir dengan bobot yang sesuai.
    
 3. Keterangan: Menentukan apakah siswa lulus atau tidak berdasarkan nilai akhir.
    
 4. Penentuan Huruf: Mengonversi nilai akhir menjadi huruf sesuai dengan kriteria yang diberikan.
    
 5. Output: Menampilkan hasil perhitungan.

### STRUKTUR PROGRAM

Input:

* Nama siswa

* Nilai UTS (float)

* Nilai UAS (float)

* Nilai Tugas (float)

Output:

* Nama siswa

* Nilai UTS

* Nilai UAS

* Nilai Tugas

* Nilai Akhir

* Nilai Huruf

* Keterangan ("LULUS" atau "TIDAK LULUS")

## BERIKUT SCREENSHOT VISUALCODE


![image](https://github.com/user-attachments/assets/12bccc6a-cc15-42d0-aeab-e1ac44d8db0e)



## LATIHAN 2
### MEMBUAT PROGRAM MENAMPILKAN GAJI KARYAWAN
### DESKRIPSI

Program ini menerima input gaji, status keluarga (sudah berkeluarga atau belum), dan status kepemilikan rumah dari pengguna, kemudian melakukan beberapa pengecekan sebagai berikut:

1. Apakah gaji di atas UMR (Upah Minimum Regional).

2. Jika gaji di atas UMR, program akan mengecek apakah pengguna sudah berkeluarga untuk menentukan kewajibam mengikuti asuransi dan menabung.

3. Program juga mengecek apakah pengguna memiliki rumah untuk menentukan kewajiban membayar pajak rumah.

### PENJELASAN PROGRAM
1. Input Data Karyawan:

Program meminta input dari pengguna untuk nama karyawan, gaji pokok, dan total potongan gaji.
Menghitung Gaji Bersih:

2. Menghitung Gaji Bersih:

   Gaji bersih dihitung dengan mengurangi gaji pokok dengan total potongan:
   
gaji_bersih

gaji_pokok
−
potongan

gaji_bersih=gaji_pokok−potongan

4. Output:

   Program mencetak rincian gaji karyawan, termasuk nama, gaji pokok, potongan, dan gaji bersih.

### STRUKTUR PROGRAM

• Input:

• Gaji (int)

• Status berkeluarga (Y/T)

• Status kepemilikan rumah (Y/T)

• Output:

• Apakah gaji sudah di atas UMR atau belum

• Kewajiban mengikuti asuransi jika sudah berkeluarga

• Kewajiban membayar pajak rumah jika punya rumah


### GAJI DI BAWAH UMR

![image](https://github.com/user-attachments/assets/010e70b8-3482-40b1-8bea-bcaa1d566b92)


## BERIKUT SCREENSHOT VISUALCODE

![image](https://github.com/user-attachments/assets/e1c5cdab-f081-4208-89a1-e79eac4ff526)


## LATIHAN 3
### PENGGUNAAN KONDISI OR
### DESKRIPSI 
Kondisi OR adalah operator logika yang digunakan untuk mengevaluasi dua atau lebih ekspresi kondisi. Dalam bahasa pemrograman Python, operator ini memungkinkan kita untuk memeriksa beberapa kondisi sekaligus. Jika salah satu atau lebih dari kondisi tersebut bernilai True, maka keseluruhan pernyataan akan dianggap True. Sebaliknya, jika semua kondisi bernilai False, maka hasilnya adalah False.
Penggunaan kondisi OR sangat berguna dalam berbagai situasi di mana beberapa kondisi perlu dievaluasi. Operator ini memudahkan pengambilan keputusan dalam logika program, sehingga membuat kode menjadi lebih ringkas dan efisien. Dengan memahami cara kerja OR, programmer dapat menciptakan skrip yang lebih kompleks dan dinamis.

### PENJELASAN OR
1. Definisi
Operator OR adalah operator logika yang digunakan untuk mengevaluasi dua atau lebih kondisi. Dalam Python, operator ini ditulis sebagai or. Jika salah satu dari kondisi tersebut bernilai True, maka keseluruhan ekspresi juga akan bernilai True. Sebaliknya, jika semua kondisi bernilai False, maka hasilnya adalah False.
2. Sintaksis
Penggunaan dasar operator OR dalam Python adalah sebagai berikut:

```PYTHON
if kondisi1 or kondisi2:
    # lakukan sesuatu
```
3. Contoh Penggunaan
   
a. Pemeriksaan Sederhana Misalnya, kita ingin mengecek apakah sebuah angka berada di luar rentang tertentu:

```PYHTON
angka = 7
if angka < 5 or angka > 10:
    print("Angka tidak dalam rentang 5 hingga 10")
else:
    print("Angka dalam rentang 5 hingga 10")
```

b. Kelayakan dalam Konteks Bisnis Dalam bisnis, kita mungkin perlu memverifikasi kelayakan berdasarkan beberapa syarat:

```PYTHON
gaji = 2500000
memiliki_rumah = True

if gaji > 5000000 or memiliki_rumah:
    print("Kelayakan pinjaman terverifikasi")
else:
    print("Kelayakan pinjaman tidak terpenuhi")
```
Jika gaji lebih dari 5.000.000 atau pemohon memiliki rumah, mereka dianggap layak untuk pinjaman.

c. Logika dalam Pendidikan Dalam konteks pendidikan, kita dapat menggunakan OR untuk mengevaluasi nilai siswa:

```PYHTON
if a + b == c or b + c == a or c + a == b:
    print("BENAR")
else:
    print("SALAH")
```

Program ini memeriksa apakah jumlah dua bilangan sama dengan bilangan ketiga. Jika salah satu kondisi terpenuhi, outputnya adalah "BENAR".

4. Keuntungan Menggunakan OR
   
Menyederhanakan Kode: Operator OR memungkinkan kita untuk menggabungkan beberapa kondisi dalam satu pernyataan, yang membuat kode lebih bersih dan mudah dibaca.

Fleksibilitas: Dengan menggunakan OR, kita bisa menetapkan kriteria yang lebih fleksibel untuk logika keputusan.

### KESIMPULAN
Operator OR adalah alat yang sangat berguna dalam pemrograman untuk mengevaluasi beberapa kondisi. Memahami cara kerjanya memungkinkan programmer untuk membuat logika yang lebih kompleks dan dinamis dalam aplikasi mereka. Jika ada yang ingin Anda tanyakan lebih lanjut, silakan beri tahu!

### STRUKTUR PROGRAM
1. Input Data:

Menggunakan input() untuk meminta pengguna memasukkan nama, gaji, dan status kepemilikan rumah.
Gaji diambil sebagai float untuk memungkinkan nilai desimal.
Status kepemilikan rumah diubah menjadi boolean dengan membandingkan input dengan "Y".

2. Proses Logika Menggunakan OR:

Menggunakan pernyataan if untuk mengevaluasi apakah gaji lebih dari 5.000.000 atau jika pengguna memiliki rumah.
Jika salah satu kondisi bernilai True, maka variabel kelayakan diatur menjadi "layak untuk mendapatkan pinjaman." Jika tidak, diatur menjadi "tidak layak untuk mendapatkan pinjaman."

3. Output Hasil:

Menggunakan print() untuk menampilkan hasil kepada pengguna, termasuk nama, gaji, dan kelayakan pinjaman.

## BERIKUT HASIL SCREENSHOOT VISUALCODE

![image](https://github.com/user-attachments/assets/27c69565-aafc-42ab-a25b-a0db679af7af)


## Latihan 3
## Pemesanan tiket bioskop

Kasus 1: Program Pemesanan Tiket Bioskop
Buat program yang menghitung harga tiket bioskop. Tiket reguler berharga Rp50.000,
sedangkan tiket VIP berharga Rp100.000. Jika user memiliki kartu member, mereka
mendapatkan diskon 20% dari harga tiket. Program ini harus meminta tipe tiket dan status
member dari user, lalu menghitung total harga yang harus dibayar.

Petunjuk:

    ● Gunakan if else dan operator ternary.
    
```python
harga_reguler = 50000
harga_vip = 100000

tipe_tiket = (input("Masukkan tipe tiket (reguler/VIP): "))
status_member = (input("Apakah Anda memiliki kartu member? (ya/tidak): "))

 Menghitung total harga
if tipe_tiket == "reguler":
    total_harga = harga_reguler
elif tipe_tiket == "vip":
    total_harga = harga_vip
else:
    print("Tipe tiket tidak valid.")
    exit()
```
 Menghitung diskon jika pengguna memiliki kartu member

```
if status_member == "ya":
        total_harga *= 0.8  # Diskon 20%
    
        print(f"Total harga yang harus dibayar: Rp{total_harga:.2f}")
elif status_member == "tidak":
            total_harga
            print(f"total harga yang harua dibayar: Rp{total_harga:.2f}")
else:
    print("Harga tidak dapat dihitung.")
 ````
Program ini akan menentukan harga pesanan tiket bioskop, Yang reguler/Vip, dan jika Vip harga 100.000, dan jika reguler 80.0000, dan jika memiliki kartu member pelanggan tersebut akan mendapatkan diskon 20%

```python
harga_reguler = 50000
harga_vip = 100000
````
variable ini menentukan harga tiket bioskop

```python
tipe_tiket = (input("Masukkan tipe tiket (reguler/VIP): "))
status_member = (input("Apakah Anda memiliki kartu member? (ya/tidak): "))
````
memasukan inputan sesuai Output Program (Reguler/Vip) di variable (Tipe_Tiket), dan Memasukan inputan yang output tersebut Bertanya memiliki kartu member atau tidak.

```python
if tipe_tiket == "reguler":
    total_harga = harga_reguler
elif tipe_tiket == "vip":
    total_harga = harga_vip
else:
    print("Tipe tiket tidak valid.")
    exit()
````
Jika tipe tiket reguler total harga proses ke Harga reguler, dan jika tiket vip Total harga proses keharga vip

dan jika Selain memasukan inputan reguler/vip Output yang keluar "Tipe tiket tidak valid" dan berproses ke fungsi exit() yang artinya program dihentikan.

```python
if status_member == "ya":
        total_harga *= 0.8  # Diskon 20%
    
        print(f"Total harga yang harus dibayar: Rp{total_harga:.2f}")
elif status_member == "tidak":
            total_harga
            print(f"total harga yang harua dibayar: Rp{total_harga:.2f}")
else:
    print("Harga tidak dapat dihitung.")
````
desision ini menentukan mempunyai kartu member atau tidak, Jika Inputan status member menjawab "ya", maka total harga akan di kalikan dengan operator * 0,8 yang disebut diskon 20%

dan jika inputan status member "tidak", maka total harga normal

jika menginputkan selain (ya/tidak) output yang keluar "Harga tidak dapat dihitung"

Dan ini hasil program tersebut:


![image](https://github.com/user-attachments/assets/77402493-13dd-4e4b-bd3a-d04017c5ff3a)



Eksekusi dari program tersebut:

![image](https://github.com/user-attachments/assets/4bdd4875-acd9-445e-b1ed-835bdb3dfb8c)


Dan flowchartnya:

![Screenshot 2024-10-26 200214](https://github.com/user-attachments/assets/19f37011-2198-4889-8b5c-01199022dc09)

## Kalkulator sederhana 

 # Kasus 2: Program Kalkulator Sederhana

Buat program kalkulator yang menerima dua angka dan satu operator aritmatika dari
pengguna (penjumlahan, pengurangan, perkalian, atau pembagian). Program akan
menghitung hasil sesuai dengan operator yang dipilih.

# Petunjuk:

    ● Gunakan if elif else untuk menentukan operasi aritmatika.

    angka1 = float(input("Masukkan angka pertama: "))
operator = input("Masukkan operator (+, -, *, /): ")
angka2 = float(input("Masukkan angka kedua: "))

# Menghitung hasil berdasarkan operator

```python
if operator == '+':
    hasil = angka1 + angka2
    print(f"Hasil penjumlahan: {hasil}")
elif operator == '-':
    hasil = angka1 - angka2
    print(f"Hasil pengurangan: {hasil}")
elif operator == '*':
    hasil = angka1 * angka2
    print(f"Hasil perkalian: {hasil}")
elif operator == '/':
    if angka2 != 0:
        hasil = angka1 / angka2
        print(f"Hasil pembagian: {hasil}")
    else:
        print("Error: Pembagian dengan nol tidak diperbolehkan.")

else:
    print("Error: Operator tidak valid. Silakan gunakan +, -, *, atau /.")
````
Program kalkulator sederhana dalam Python adalah proyek yang baik untuk pemula dan programmer tingkat lanjut. Program ini memungkinkan pengguna untuk melakukan operasi matematika seperti penjumlahan, pengurangan, perkalian, dan pembagian.

```python

angka1 = float(input("Masukkan angka pertama: "))
operator = input("Masukkan operator (+, -, *, /): ")
angka2 = float(input("Masukkan angka kedua: "))

````
fungsi yang digunakan dalam inputan ini menggunakan float mengubah nilai menjadi angka floating point, yaitu angka desimal atau pecahan, dan variable operator yang menginputkan suatu operator fungsi berupa (+, -, *, /) yang artinya pertambahan, perkurang, perkali, pembagian.

```python
if operator == '+':
    hasil = angka1 + angka2
    print(f"Hasil penjumlahan: {hasil}")
```
Jika operator (+), maka hasil tersbur inputan variable angka1 ditambahkan angka2, dan Output akan mengeluarkan hasil program tersebut, Hingga seterusnya dengan (*) perkalian, dan (-) perkurangan

```python
elif operator == '/':
    if angka2 != 0:
        hasil = angka1 / angka2
        print(f"Hasil pembagian: {hasil}")
    else:
        print("Error: Pembagian dengan nol tidak diperbolehkan.")
```
Jika oprator (/), maka Inputan Variable angka1 dibagi angka2, dan dicetak semestinya, untuk desision (angka2 !=0:) tidak diperkenankan oleh program, karna output yang keluar "Error: Pembagian dengan nol tidak diperbolehkan"

```python
else:
    print("Error: Operator tidak valid. Silakan gunakan +, -, *, atau /.")
```
saya memasukan desision else ini Karna jika menjawab selain fungsi operator ini Output yang keluar "Error: Operator tidak valid. Silakan gunakan +, -, *, atau /."

dan ini hasil program tersebut:

![image](https://github.com/user-attachments/assets/42e43cb8-8da6-4a41-a92e-72a00a6d2576)


Eksekusi program tersebut:

![image](https://github.com/user-attachments/assets/59a89243-633a-42fc-ad66-8eae363d3d19)

dan flowchartnya


![Screenshot 2024-10-26 204442](https://github.com/user-attachments/assets/94b3f701-54fe-4e56-bf46-2354363fcfc2)

