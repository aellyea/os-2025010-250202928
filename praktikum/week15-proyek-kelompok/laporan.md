
# Laporan Praktikum Minggu 15
Topik: Proyek Kelompok – Mini Simulasi Sistem Operasi (Scheduling + Memory + Container)






---

## 1. Pendahuluan

**A. Latar Belakang**

Sistem operasi berfungsi sebagai dasar utama bagi semua kegiatan komputasi saat ini, baik pada komputer maupun smartphone. Tugas pokoknya meliputi pengelolaan proses, pengaturan memori, serta pembagian sumber daya supaya aplikasi berjalan lancar dan efisien. Akan tetapi, cara kerja internalnya seperti algoritma penjadwalan CPU, metode penggantian halaman memori, dan pengendalian pada deadlock, sering kali terasa abstrak dan sulit dibayangkan tanpa contoh nyata.

Untuk mengatasi hal ini, diperlukan alat bantu belajar yang mampu menyederhanakan konsep rumit tersebut melalui situasi sehari-hari yang mudah dikenali. Pendekatan menggunakan analogi dari aktivitas digital umum, terutama bermain game, bisa menjadi cara efektif agar lebih mudah memahami prinsip kerja sistem operasi.

Oleh karena itu, kami mengembangkan ketiga modul yang meliputi:

1. **Simulasi CPU Scheduling menggunakan algoritma First-Come First-Served (FCFS)**, yang direpresentasikan melalui proses loading berbagai komponen game Genshin Impact seperti launcher, pembaruan, dan inisialisasi aset. Simulasi ini menggambarkan bagaimana CPU memprioritaskan eksekusi proses berdasarkan urutan kedatangan.

2. **Simulasi Page Replacement dengan pendekatan FIFO (First-In First-Out)**, yang divisualisasikan melalui mekanisme pemuatan aset game ke dalam RAM ponsel dan menjelaskan bagaimana sistem operasi mengelola keterbatasan memori dengan mengganti data yang paling lama dimuat ketika kapasitas penuh.
   
3. **Simulasi Deadlock Detection**, yang mengilustrasikan kondisi deadlock melalui skenario perebutan material ascension karakter dalam Genshin Impact. Dua proses (karakter) saling menunggu resource yang dipegang oleh proses lainnya, menciptakan kondisi deadlock yang dapat diidentifikasi dan dianalisis.

**B. Tujuan Proyek**

1. Memahami konsep inti sistem operasi secara aplikatif
2. Menyederhanakan konsep sistem operasi melalui pendekatan analogi pada game
3. Mengintergrasikan beberapa modul sistem operasi dalam satu aplikasi terpadu
4. Melatih kemampuan kerja kolaboratif dalam pengembangan perangkat lunak
5. Menerapkan praktik pengelolaan proyek berbasis git secara baik
6. Mengembangkan penyusunan dokumentasi proyek yang sistematis


---

## 2. Arsitektur aplikasi

**A. Gambaran Arsitektur Aplikasi**

Aplikasi ini dirancang sebagai aplikasi berbasis terminal (CLI) yang terdiri dari beberapa modul simulasi sistem operasi yang berdiri secara modular dan independen.
Setiap modul merepresentasikan satu konsep utama sistem operasi dan dapat dijalankan secara terpisah, namun tetap berada dalam satu konteks aplikasi pembelajaran terpadu.

Secara umum, arsitektur aplikasi terdiri dari:

1. **Input**: dataset statis
2. **Prosseing Modul**: simulasi algoritma sistem operasi
3. **Output**: tabel ASCII dan ringkasan metrik hasil simulasi


**B. Modul dan Alur Data**




**Modul A – CPU Scheduling (FCFS)**

Modul CPU Scheduling mengimplementasikan algoritma First-Come First-Served (FCFS) untuk mensimulasikan proses masuk ke dalam game Genshin Impact.



1. Dataset proses direpresentasikan dalam bentuk list berisi:

 - Nama proses (contoh: Launcher, LoadAssets)
 - Arrival Time (AT)
 - Burst Time (BT)

2. Data proses diurutkan berdasarkan arrival time untuk memenuhi prinsip FCFS.

3. Modul menghitung:
   
- Start Time (ST)
- Finish Time (FT)
- Waiting Time (WT)
- Turnaround Time (TAT)

4. Hasil simulasi ditampilkan dalam bentuk tabel ASCII beserta rata-rata WT dan TAT.

Peran Modul:

Menggambarkan bagaimana CPU mengeksekusi proses berdasarkan urutan kedatangan tanpa preemption, dianalogikan sebagai tahapan loading saat pemain masuk ke dunia game.

--- 

**Modul B – Page Replacement (FIFO)**

Modul Page Replacement mengimplementasikan algoritma First-In First-Out (FIFO) untuk mensimulasikan pengelolaan RAM pada perangkat saat game berjalan.

Struktur dan Alur Data:

1. Dataset aset game dibaca dari file CSV
   
2. Pengguna memasukkan kapasitas RAM (jumlah frame).
   
3. Modul memproses setiap aset secara berurutan:

- Jika aset belum ada di RAM = page fault (MISS)

- Jika aset sudah ada = page hit (HIT)

4. Jika RAM penuh, aset paling lama dimuat akan dikeluarkan (FIFO)
   
5. Output ditampilkan per langkah berupa:

- Isi RAM

- Status HIT/MISS

6. Di akhir simulasi, modul menghitung total page fault dan hit ratio.
 
Peran Modul:

Menunjukkan bagaimana sistem operasi mengelola keterbatasan memori dengan mengganti data lama saat kapasitas penuh, dianalogikan sebagai pemuatan aset game di RAM HP.

---


**Modul C – Deadlock Simulation**

1. Dua resource direpresentasikan sebagai objek Lock:
   
- Resource A (Nagadus Emerald)

- Resource B (Vajrada Amethyst)
  
2. Dua thread (proses) dijalankan secara paralel:

- Proses Raiden Shogun

- Proses Zhongli
  
3. Masing-masing proses:

- Mengunci satu resource terlebih dahulu

- Menunggu resource lain yang sedang dipegang proses lain

4. Kondisi ini menyebabkan circular wait dan deadlock.
   
5. Program berhenti tanpa menyelesaikan seluruh proses, menandakan deadlock terjadi.

Peran Modul:

Modul ini mengilustrasikan konsep deadlock secara nyata, di mana dua proses saling menunggu resource, sesuai dengan teori deadlock pada sistem operasi.

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.

---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.  
2. Perintah yang dijalankan.  
3. File dan kode yang dibuat.  
4. Commit message yang digunakan.

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
uname -a
lsmod | head
dmesg | head
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

---

## Analisis
- Jelaskan makna hasil percobaan.  
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## Quiz
1. [Pertanyaan 1]  
   **Jawaban:**  
2. [Pertanyaan 2]  
   **Jawaban:**  
3. [Pertanyaan 3]  
   **Jawaban:**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
