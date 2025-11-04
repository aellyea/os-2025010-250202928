
# Laporan Praktikum Minggu 3
Topik: Konsep Ownership dan Permission dalam Manajemen File di Linux

---

## Identitas
- **Nama**  : Alya Deviana Putri Reynaldi
- **NIM**   : 250202928
- **Kelas** : 1IKRB

---

## Tujuan
1. Memahami konsep dasar sistem file pada linux, yaitu struktur direktori dan hubungan antar folder.
2. Mengoperasikan perintah-perintah linux untuk menavigasi, menampilkan, dan membaca isi file maupun direktori.
3. Mengidentifikasi serta menginterpretasikan hak akses dan kepemilikan file di sistem Linux.
4. Bisa menganalisis hasil percobaan dan mendokumentasikannya
---

## Dasar Teori


**1. Sistem File Linux**

Sistem file linux menggunakan struktur hierarki dengan direktori `root (/)` yaitu perintah navigasi seperti ``pwd`` , ``ls`` , ``cd`` yang mengorganisir akses ke sumber daya sistem.

**2. Peran Keamanan dalam Manajemen File**

Permission dan ownership berperan banyak dalam keamanan Linux yaitu, mencegah modifikasi tidak sah atau eksekusi kode berbahaya yang mendukung prinsip least privilage untuk melindungi sistem dari ancaman eksternal.

**3. Peran Permission**

Permission ini mencegah akses tidak sah dan memastikan keamanan, dengan perintah ``chmod`` digunakan untuk mengubahnya, direpresentasikan dalam format oktal atau simbolik.

**4. Ownership dan Kepemilikan**

Kepemilikan bisa diubah dengan perintah chown (mengganti pemilik) dan chgrp (mengganti grup) yang gunanya agar file penting hanya bisa diakses oleh pengguna yang diizinkan mengakses.

**5. File Tersembunyi**

File tersembunyi dimulai dengan titik ``e.g., .bashrc`` , yang dapat dilihat dengan ``ls -a`` untuk menyimpan konfigurasi sistem tanpa mengganggu tampilan umum, mendukung efisiensi navigasi dan pengelolaan direktori.


---

## Langkah Praktikum
1. Menjalankan semua eksperimen sesuai perintah tugas praktikum di Ubuntu/WSL
2. Menganalisis hasil tiap perintah dan mendokumentasikan seluruh perintah pada tabel observasi.
3. Mengerjakan tugas dan quiz
4. Setelah semua sudah lengkap, commit dan push di GitHub.

---

## Kode / Perintah

Eksperimen 1 - Navigasi Sistem File
```bash
pwd
ls -l
cd /tmp
ls -a
```

Eksperimen 2 - Membaca file
```bash
cat /etc/passwd | head -n 5
```
Eksperimen 3 - Permission & Ownership 
```bash
echo "Hello <NAME><NIM>" > percobaan.txt
ls -l percobaan.txt
chmod 600 percobaan.txt
ls -l percobaan.txt
```


## Hasil Eksekusi
![Screenshot](screenshots/Hasil%20Eksekusi.png)




---

## Analisis

 ## Eksperimen 1 - Navigasi Sistem File

| No | Perintah  | Hasil Output                                                                                | Analisis                                                                                                                                                                                                     |
| -- | --------- | ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1  | `pwd`     | `/home/aelyea`                                                                                        | Menampilkan file aktif saat ini.                                                                                                                               |
| 2  | `ls -l`   | `total 0`                                                                                             | Menunjukkan isi folder kosong yaitu tidak ada file.                                                                                                                                            |
| 3  | `cd /tmp` | tidak ada output                                                                                  | Berpindah ke direktori `/tmp`, yaitu folder sementara di sistem Linux.                                                                                                                                       |
| 4  | `ls -a`   | Menampilkan: `.`, `..`, `.X11-unix`, `snap-private-tmp`, dan lain lain | `ls -a` menampilkan semua file termasuk **file tersembunyi** (yang diawali titik `.`). Folder `.` berarti direktori saat ini, `..` berarti direktori induk. Folder `.X11-unix` dan lainnya adalah file sistem sementara. |

## Eksperimen 2 - Membaca file

| No                                              | Perintah                                                                                                            | Hasil Output  | Analisis                                                                                               |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ---------------------- | ------------------------------------------------------------------------------------------------------------------ |
| 1                                               | `cat /etc/passwd \| head -n 5`                                                                                      | ```                    |                                                                                                                    |
| root:x:0:0:root:/root:/bin/bash                 |                                                                                                                     |                        |                                                                                                                    |
| daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin |                                                                                                                     |                        |                                                                                                                    |
| bin:x:2:2:bin:/bin:/usr/sbin/nologin            |                                                                                                                     |                        |                                                                                                                    |
| sys:x:3:3:sys:/dev:/usr/sbin/nologin            |                                                                                                                     |                        |                                                                                                                    |
| sync:x:4:65534:sync:/bin:/bin/sync              |                                                                                                                     |                        |                                                                                                                    |
             
              
  **Isi File ``/etc/passwd``**
Berisi daftar seluruh akun pengguna yang ada di sistem Linux, baik user biasa maupun sistem yang tiap barisnya mewakili satu akun pengguna.

1. username → Nama pengguna (contoh: ``root``, ``daemon``).

2. password → ditandai dengan ``x`` artinya password disimpan terenkripsi di file lain (``/etc/shadow``).

3. UID (User ID) → Nomor identitas unik untuk setiap pengguna. ``0`` adalah UID untuk root (administrator).

4. GID (Group ID) → Nomor identitas grup tempat user tersebut tergabung.

5. user info → Informasi tambahan tentang pengguna, biasanya nama lengkap atau deskripsi.

6. home directory → Lokasi direktori pribadi user (``home/user``)

7. shell → Program shell yang dijalankan saat user login (``/usr/sbin/nologin``)



## Eksperimen 3 - Permission & Ownership

| No | Perintah                                                                | Hasil                                             | Analisis                                                                                                                                 |
| -- | ----------------------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| 1  | `echo "Hello <Alya Deviana Putri Reynaldi><250202928>" > percobaan.txt` | Membuat file baru bernama `percobaan.txt`.                 | File berhasil dibuat di direktori `/tmp` dengan isi teks yang ditentukan.                                                                |
| 2  | `ls -l percobaan.txt`                                                   | `-rw-r--r-- 1 aelyea aelyea 47 Oct 21 17:01 percobaan.txt` | Permission awal: rw-r--r--, artinya pemilik bisa membaca dan mengedit, sedangkan grup dan lainnya hanya bisa membaca.                |
| 3  | `chmod 600 percobaan.txt`                                               | *(tidak ada output)*                                       | Mengubah izin file menjadi hanya bisa diakses pemilik.                                                                |
| 4  | `ls -l percobaan.txt`                                                   | `-rw------- 1 aelyea aelyea 47 Oct 21 17:01 percobaan.txt` | Permission berubah menjadi rw-------, hanya pemilik yang bisa membaca dan menulis file; grup dan pengguna lain tidak memiliki akses. |


| Kondisi             | Permission   | Keterangan                                                                                            |
| ------------------- | ------------ | ----------------------------------------------------------------------------------------------------- |
| Sebelum `chmod 600` | `-rw-r--r--` | Pemilik bisa membaca dan menulis, grup dan pengguna lain hanya bisa membaca.                          |
| Sesudah `chmod 600` | `-rw-------` | Hanya pemilik yang bisa membaca dan menulis, grup dan pengguna lain tidak memiliki akses sama sekali. |


| Perintah                        | Hasil                                        | Analisis                                                                                       |
| ------------------------------- | -------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `sudo chown root percobaan.txt` | Kepemilikan file berubah menjadi `root pemilik`.          | Perintah `chown` mengubah pemilik file menjadi user root, sementara grup tetap milik pemilik. |
| `ls -l percobaan.txt`           | `-rw------- 1 root aelyea 47 Oct 21 17:01 percobaan.txt` | Menunjukkan bahwa file sekarang dimiliki oleh root, dengan permission tetap `rw-------`.   |








---

## Kesimpulan

1. Sistem Linux memiliki mekanisme pengelolaan file yang terstruktur dan aman melalui konsep permission dan ownership, yang memastikan setiap file hanya dapat diakses oleh pengguna yang berhak.
   
2. Dari hasil percobaan dengan perintah ``pwd``, ``ls``, dan ``cd``, dapat disimpulkan bahwa pengguna dapat dengan mudah menavigasi sistem file Linux untuk memahami letak serta isi direktori.

3. Melalui percobaan ``chmod dan chown``, terbukti bahwa Linux memberikan fleksibilitas dalam mengatur hak akses dan kepemilikan file, yang penting untuk menjaga keamanan data serta kontrol administratif dalam sistem.

4. Perintah seperti ``cat /etc/passwd`` memperlihatkan bahwa Linux menyimpan informasi pengguna secara transparan namun tetap aman, dengan sistem identifikasi berbasis UID dan GID.


---

## Quiz
1. Apa fungsi dari perintah ``chmod``

**Jawaban:**



Mengubah izin akses (permission) suatu file atau direktori dan memberi kontrol penuh ke pemilik file di Linux.

Menjaga kerahasiaan data dan melindungi file dari akses yang tidak dikenali.

Mendukung format izin simbolik maupun numerik.
   

2. Apa arti dari kode permission ``rwxr-xr--``?

**Jawaban:**  

>   ``rwx`` (owner)
   
   
   ``r`` = (read) bisa membaca file
   
   ``w`` = (write) bisa mengedit file
   
   ``x`` = (execute) bisa menjalankan file
   



>  ``r-x`` (group)
   
   
   ``r`` = bisa membaca file
   
   ``-`` = tidak bisa mengedit file
     
   ``x`` = bisa menjalankan file
  

> ``r--`` (others)
   

 ``r``= bisa membaca file
   
  ``-`` = tidak bisa mengedit file
     
   ``-`` = tidak bisa menjalankan file
   

  
   ``rwxr-xr--`` artinya adalah (owner) pemilik mempunyai akses penuh file, untuk grup (group) bisa membaca dan menjalankan, sedangkan untuk (others) orang lain hanya bisa membaca.

   3. Jelaskan perbedaan antara ``chown`` dan ``chmod``
      
  **Jawaban:**

``chown`` artinya ``change owner`` yang berfungsi untuk mengubah kepemilikan file.

``chmod`` artinya ``change mode`` yang berfungsi untuk mengubah izin akses file.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?

Sedikit sulit memahami permission dan ownership di Linux karena logikanya sulit dan materinya dalam.

- Bagaimana cara Anda mengatasinya?

Fokus mempelajari secara bertahap dengan eksperimen berulang dan mencari referensi tambahan dari internet untuk memperluas pemahaman.
  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
