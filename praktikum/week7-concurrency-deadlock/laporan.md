
# Laporan Praktikum Minggu 7
Topik: Sinkronisasi Proses dan Masalah Deadlock

---

## Identitas

**Nama dan NIM Anggota Kelompok**  :
  1. Aster Rifani (250202915)
  2. Lutfi Khoerunnisa (250202947)
  3. Muslimah Nuraini (250202980)
  4. Alya Deviana Putri Reynaldi (250202928)

**Kelas** : 1IKRB

---

## Tujuan

1. Memahami risiko deadlock dalam proses konkurensi melalui simulasi Dining Philosophers.
2. Mengimplementasikan versi sederhana yang menimbulkan deadlock dan versi yang diperbaiki.
3. Menganalisis empat kondisi utama penyebab deadlock serta solusinya.
4. Membandingkan efisiensi antara simulasi deadlock dan versi fixed menggunakan semaphore atau monitor.
5. Mendokumentasikan hasil eksperimen dan diskusi kelompok dalam laporan terstruktur.

---

## Dasar Teori

**Deadlock**

Keadaan ketika beberapa proses saling menunggu sumber daya yang sedang dikuasai oleh proses lainnya, sehingga tidak ada proses yang dapat melanjutkan tugasnya. Kondisi ini biasanya muncul pada sistem dengan sumber daya terbatas dan ketika sejumlah proses berjalan secara bersamaan.

**Masalah Dining Philosophers**

Model ini menggambarkan lima filsuf yang duduk melingkar, dan setiap filsuf membutuhkan dua garpu untuk bisa makan karena garpu tersebut merupakan sumber daya yang terbatas, tanpa mekanisme pengendalian, semua filsuf bisa jadi hanya memegang satu garpu dan terus menunggu garpu lainnya, yang menyebabkan terjadinya deadlock.

**Semaphore**

Sebuah teknik sinkronisasi yang menggunakan penghitung untuk mengatur akses ke sumber daya bersama. Semaphore biner (atau mutex) hanya memperbolehkan satu proses menggunakan sumber daya dalam satu waktu, sementara semaphore dengan penghitung dapat memperbolehkan beberapa proses mengakses sumber daya sekaligus. Dengan cara ini, semaphore membantu mencegah terjadinya race condition dan deadlock.

**Monitor**

Sebuah struktur data yang menyediakan mekanisme sinkronisasi secara otomatis, seperti penguncian (lock) dan pembukaan kunci (unlock), untuk mengatur akses ke sumber daya tertentu. Monitor beroperasi pada tingkat yang lebih tinggi dibanding semaphore, sehingga mempermudah pengelolaan sinkronisasi tanpa risiko kesalahan yang biasanya muncul saat penanganan manual.

**Empat kondisi utama terjadinya deadlock (Coffman Conditions)**

**1. Mutual Exclusion**

Sumber daya hanya bisa digunakan oleh satu proses dalam satu waktu.

**2. Hold and Wait**

Proses menahan sejumlah sumber daya sementara menunggu sumber daya tambahan.

**3. No Preemption**

Sumber daya tidak dapat diambil secara paksa dari proses yang sedang menggunakannya.

**4. Circular Wait**

Terjadi siklus penantian di antara beberapa proses yang saling menunggu satu sama lain.

---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.  
2. Perintah yang dijalankan.  
3. File dan kode yang dibuat.  
4. Commit message yang digunakan.

---

## IMRaD

**A. Pendahuluan**

Masalah Dining Philosophers adalah sebuah model klasik dalam bidang sistem operasi yang menggambarkan potensi terjadinya deadlock pada proses yang berjalan secara bersamaan. Dalam contoh ini, terdapat lima filsuf yang duduk mengelilingi meja dengan lima garpu di antara mereka. Setiap filsuf membutuhkan dua garpu agar bisa makan. Jika tidak ada pengaturan yang tepat, bisa terjadi situasi di mana setiap filsuf hanya memegang satu garpu dan terus menunggu garpu yang dipegang oleh filsuf di sebelahnya, sehingga menciptakan kondisi saling tunggu yang menyebabkan deadlock.

**B. Metode**

 *Eksperimen 1 – Simulasi Dining Philosophers (Deadlock Version)*
 
   Pada eksperimen ini simulasi dasar Dining Philosophers di mana setiap proses mengambil garpu kiri lalu garpu kanan tanpa mekanisme pencegah deadlock. Tujuannya adalah mengamati kapan deadlock terjadi, yaitu saat semua Philosopher memegang satu garpu dan menunggu garpu lainnya secara bersamaan.
   

*Eksperimen 2 – Versi Fixed (Menggunakan Semaphore)*

   Pada eksperimen ini ditambahkan mekanisme sinkronisasi berupa *semaphore dengan nilai N−1* untuk membatasi hanya maksimal empat Philosopher yang dapat memasuki area makan. Pembatasan ini mencegah semua garpu diambil bersamaan sehingga memutus terjadinya circular wait dan menghilangkan deadlock.
   
 *Eksperimen 3 – Analisis Deadlock*
 
   Menganalisis empat kondisi penyebab deadlock pada versi pertama serta menjelaskan bagaimana versi fixed memecah tiap kondisi. Hasil analisis disajikan dalam tabel yang membandingkan kondisi deadlock pada kedua versi.

   C. Hasil Eksekusi

   
  *Eksperimen 1 – Simulasi Dining Philosophers (Deadlock Version)*

  

 

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
