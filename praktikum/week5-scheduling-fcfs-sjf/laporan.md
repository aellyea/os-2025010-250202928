
# Laporan Praktikum Minggu 5
Topik: Penjadwalan CPU – FCFS dan SJF


---

## Identitas
- **Nama**  : Alya Deviana Putri Reynaldi
- **NIM**   : 250202928
- **Kelas** : 1IKRB

---

## Tujuan
1. Memahami prinsip dasar algoritma penjadwalan CPU FCFS dan SJF dalam menentukan urutan eksekusi proses.
2. Menghitung secara manual waktu tunggu (waiting time) dan waktu penyelesaian (turnaround time) untuk setiap proses pada kedua algoritma.
3. Menganalisis perbedaan performa antara FCFS dan SJF melalui perbandingan rata-rata waktu tunggu dan turnaround time.
4. Membuat dan menginterpretasikan Gantt chart sebagai representasi visual dari simulasi penjadwalan.
5. Menerapkan simulasi penjadwalan pada skenario proses yang berbeda
---

## Dasar Teori

**1. Konsep Dasar Penjadwalan CPU**
   
Penjadwalan CPU adalah bagian dari manajemen proses yang mengatur pembagian waktu prosesor di antara sejumlah proses yang sedang menunggu eksekusi.

**2. FCFS (First Come First Served)**

Metode penjadwalan yang mengeksekusi proses berdasarkan urutan kedatangannya. Proses yang datang terlebih dahulu akan diproses lebih dulu hingga selesai tanpa adanya interupsi. Meskipun sederhana dan mudah diimplementasikan, algoritma ini memiliki kelemahan berupa waktu tunggu yang tinggi apabila terdapat proses dengan waktu eksekusi panjang, yang dikenal dengan istilah convoy effect.

**3. SJF (Shortest Job First)**

Metode penjadwalan yang memilih proses dengan waktu eksekusi (burst time) paling singkat di antara proses yang telah tiba. Pendekatan ini dapat menghasilkan waktu tunggu rata-rata yang lebih rendah dibandingkan FCFS, sehingga dianggap lebih efisien. Namun, algoritma ini memiliki kelemahan berupa kemungkinan starvation terhadap proses berdurasi panjang apabila terus muncul proses dengan durasi pendek.

**4. Parameter Evaluasi (WT dan TAT)**

Dalam mengevaluasi performa suatu algoritma penjadwalan, terdapat dua parameter utama yang digunakan, yaitu:

**Waiting Time (WT)**

Waktu yang dihabiskan proses dalam antrian sebelum dieksekusi.

**Turnaround Time (TAT)**

Total waktu sejak proses tiba hingga selesai dieksekusi.


>*Nilai rata-rata WT dan TAT*
digunakan untuk membandingkan efisiensi algoritma penjadwalan.





 
---

## Langkah Praktikum
1. Menyiapkan data proses yang berisi waktu kedatangan dan waktu eksekusi untuk digunakan pada percobaan penjadwalan.

2. Menjalankan simulasi algoritma FCFS untuk menentukan urutan proses berdasarkan waktu kedatangan.

3. Menerapkan algoritma SJF dengan mengurutkan proses sesuai waktu eksekusi terpendek.

4. Menghitung nilai Waiting Time (WT) dan Turnaround Time (TAT) pada setiap proses.

5. Membuat Gantt Chart untuk menggambarkan urutan eksekusi proses pada masing-masing algoritma.

6. Menganalisis hasil perhitungan guna membandingkan performa antara FCFS dan SJF.

7. Mendokumentasikan seluruh hasil percobaan dan mengunggah laporan ke repositori Git sesuai ketentuan praktikum.

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
uname -a
lsmod | head
dmesg | head
```

---


---

## Analisis
Eks

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
