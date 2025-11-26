
# Laporan Praktikum Minggu 7
Topik: Sinkronisasi Proses dan Masalah Deadlock

---

## Identitas

**Nama dan NIM Anggota Kelompok**  :
  1. Aster Rifani (250202915) : Analisis
  2. Lutfi Khoerunnisa (250202947) : Dokumentasi
  3. Muslimah Nuraini (250202980) : Implementasi
  4. Alya Deviana Putri Reynaldi (250202928) : Ketua

**Kelas** : 1IKRB

---

## Tujuan

1. Memahami risiko deadlock dalam proses konkurensi melalui simulasi Dining Philosophers.
2. Mengimplementasikan versi sederhana yang menimbulkan deadlock dan versi yang diperbaiki.
3. Menganalisis empat kondisi utama penyebab deadlock serta solusinya.
4. Membandingkan efisiensi antara simulasi deadlock dan versi fixed menggunakan semaphore atau monitor.
5. Mendokumentasikan hasil eksperimen dan diskusi kelompok dalam laporan terstruktur.

---

## Kode / Perintah

1. **Persiapan Tim**
   - Membentuk kelompok beranggotakan 3–4 orang.  
   - Menentukan ketua dan pembagian tugas (analisis, implementasi, dokumentasi).

2. **Eksperimen 1 – Simulasi Dining Philosophers (Deadlock Version)**
   - Implementasikan versi sederhana dari masalah *Dining Philosophers* tanpa mekanisme pencegahan deadlock.  
   - Contoh pseudocode:
     ```text
     while true:
       think()
       pick_left_fork()
       pick_right_fork()
       eat()
       put_left_fork()
       put_right_fork()
     ```
   - Jalankan simulasi atau analisis alur (boleh menggunakan pseudocode atau diagram alur).  
   - Identifikasi kapan dan mengapa deadlock terjadi.

3. **Eksperimen 2 – Versi Fixed (Menggunakan Semaphore / Monitor)**
   - Modifikasi pseudocode agar deadlock tidak terjadi, misalnya:
     - Menggunakan *semaphore (mutex)* untuk mengontrol akses.
     - Membatasi jumlah filosof yang dapat makan bersamaan (max 4).  
     - Mengatur urutan pengambilan garpu (misal, filosof terakhir mengambil secara terbalik).  
   - Analisis hasil modifikasi dan buktikan bahwa deadlock telah dihindari.

4. **Eksperimen 3 – Analisis Deadlock**
   - Jelaskan empat kondisi deadlock dari versi pertama dan bagaimana kondisi tersebut dipecahkan pada versi fixed.  
   - Sajikan hasil analisis dalam tabel seperti contoh berikut:

     | Kondisi Deadlock | Terjadi di Versi Deadlock | Solusi di Versi Fixed |
     |------------------|---------------------------|------------------------|
     | Mutual Exclusion | Ya (satu garpu hanya satu proses) | Gunakan semaphore untuk kontrol akses |
     | Hold and Wait | Ya | Hindari proses menahan lebih dari satu sumber daya |
     | No Preemption | Ya | Tidak ada mekanisme pelepasan paksa |
     | Circular Wait | Ya | Ubah urutan pengambilan sumber daya |

5. **Eksperimen 4 – Dokumentasi**
   - Simpan semua diagram, screenshot simulasi, dan hasil diskusi di:
     ```
     praktikum/week7-concurrency-deadlock/screenshots/
     ```
   - Tuliskan laporan kelompok di `laporan.md` (format IMRaD singkat: *Pendahuluan, Metode, Hasil, Analisis, Diskusi*).

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 7 - Sinkronisasi Proses & Deadlock"
   git push origin main
   ```

   
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

1. Bentuk kelompok 3–4 orang, tentukan ketua, dan bagi tugas (analisis, implementasi, dokumentasi).
   
2. Mengimplementasikan versi Dining Philosophers dengan deadlock (pseudocode: think, pick_left, pick_right, eat, put_left, put_right).

3. Jalankan simulasi atau analisis alur, identifikasi kapan dan mengapa deadlock terjadi.
Modifikasi pseudocode untuk versi fixed menggunakan semaphore/monitor (batasi jumlah makan, ubah urutan garpu).

4. Analisis hasil modifikasi, buktikan deadlock dihindari.
   
5. Jelaskan empat kondisi deadlock dalam tabel, bandingkan versi deadlock vs. fixed.
   
6. Dokumentasikan diagram/screenshot di folder screenshots, tulis laporan.md (IMRaD), jawab quiz, lalu git add, commit, push.

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

   **C. Hasil Eksekusi**

   
  **Eksperimen 1 – Simulasi Dining Philosophers (Deadlock Version)**
  
![Deadlock Simulation](screenshots/deadlock.png)


  **Eksperimen 2 – Versi Fixed (Menggunakan Semaphore / Monitor)**

 ![Fixed Simulation](screenshots/fixed.png)

 **D. Analisis**
 
Eksperimen 1 – Simulasi Dining Philosophers (Deadlock Version)

 Deadlock pada kode Dining Philosophers terjadi ketika semua philosopher secara bersamaan berhasil mengambil garpu kiri, lalu masing-masing mencoba mengambil garpu kanan yang ternyata sedang dipegang oleh philosopher di sebelahnya, sehingga setiap thread memegang satu garpu dan menunggu garpu lainnya tanpa ada satu pun yang bisa melanjutkan; kondisi ini memenuhi pola circular wait, sehingga tidak ada garpu yang dilepas dan seluruh proses berhenti di pemanggilan `right.acquire()`

 Eksperimen 2 – Versi Fixed (Menggunakan Semaphore / Monitor)

 Strategi penanganan Deadlock yang paling efektif adalah dengan membatasi jumlah proses yang dapat bersaing untuk sumber daya (N-1), seperti membatasi 4 filosof untuk 5 garpu. Modifikasi ini secara langsung melanggar kondisi Tunggu Melingkar (Circular Wait) dan Tahan dan Tunggu (Hold and Wait), sehingga sistem dijamin tidak akan pernah masuk ke dalam kondisi kebuntuan permanen (Deadlock).

  Eksperimen 3 – Analisis Deadlock

  | Kondisi Deadlock   | Terjadi di Versi Deadlock | Solusi di Versi Fixed |
|--------------------|---------------------------|-------------------------|
| **Mutual Exclusion** | Ya | Dipertahankan (dibutuhkan untuk integritas data). Dikontrol menggunakan lock/semaphore. |
| **Hold and Wait**    | Ya | Dihindari dengan memastikan proses mengambil semua resource sekaligus atau melepas jika gagal. |
| **No Preemption**    | Ya | Dihindari dengan membolehkan proses melepas resource saat permintaan tambahan gagal. |
| **Circular Wait**    | Ya | Dihindari dengan mengatur urutan pengambilan resource, misalnya satu filosof mengambil garpu secara terbalik atau dengan urutan global. |

 **E. Diskusi**
 
Dari hasil percobaan, dapat diketahui bahwa versi pertama program mengalami deadlock karena setiap filosof saling menunggu garpu yang tidak pernah dilepas. Setelah diterapkan mekanisme pencegahan (semaphore/aturan pengambilan garpu), program dapat berjalan tanpa kebuntuan. Hal ini menunjukkan bahwa sinkronisasi sangat penting untuk memastikan proses dapat berjalan bersamaan tanpa saling menghambat, serta membuktikan bahwa pengaturan akses sumber daya mampu mencegah deadlock secara efektif.


---


## Kesimpulan

Analisis Kode Awal (Deadlock Terjadi) 

1. Kode Filosof Makan awal membuktikan bahwa jika semua empat kondisi Deadlock (Mutual Exclusion, Hold and Wait, No Preemption, dan Circular Wait) terpenuhi secara simultan, Deadlock pasti terjadi, mengakibatkan sistem macet permanen (Starvation).

2. Sinkronisasi Proses menekankan bahwa Mutual Exclusion (Saling Pengecualian) adalah syarat fundamental untuk menjaga integritas data dan mencegah Race Condition di Critical Section. 

Namun, meskipun Mutual Exclusion diterapkan, kegagalan dalam manajemen sumber daya tetap dapat terjadi.

3. Solusi untuk Deadlock terletak pada pelanggaran salah satu dari empat kondisi pembentuknya.

Analisis modifikasi kode, seperti membatasi jumlah proses menjadi N-1 (misalnya, 4 filosof untuk 5 garpu), secara efektif menghindari kebuntuan permanen. Strategi ini berhasil karena memutus rantai tunggu melingkar dan menjamin bahwa selalu ada jalan keluar (safe state), sehingga semua proses pada akhirnya dapat maju.

---

## Quiz
1. Sebutkan empat kondisi utama penyebab deadlock.
   
   **Jawaban:**

1. Mutual Exclusion

   Sumber daya hanya bisa digunakan oleh satu proses sekaligus.
   
2. Hold and wait
   
 Proses yang sudah memegang sumber daya menunggu yang lain tanpa melepaskan yang dimilikinya.
 
3. No preemption
   
  Sumber daya tidak bisa diambil paksa dari proses yang memegangnya.

4. Circular wait
  
  Proses-proses saling menunggu sumber daya dalam siklus tertutup.
   
2. Mengapa sinkronisasi diperlukan dalam sistem operasi?
   
   **Jawaban:**
   
   Sinkronisasi penting karena dapat mencegah kondisi balapan (race conditions) di mana beberapa proses atau thread mengakses data bersama secara bersamaan, yang bisa menyebabkan inkonsistensi atau kesalahan. Ini memastikan akses teratur ke sumber daya bersama, menjaga integritas data, dan menghindari deadlock atau starvation dalam lingkungan multi-tugas.
   
3. Jelaskan perbedaan antara semaphore dan monitor.
   
   **Jawaban:**

   Semaphore adalah alat sinkronisasi tingkat rendah yang menggunakan penghitung (counter) untuk mengontrol akses ke sumber daya, seperti sinyal untuk menunggu atau melepaskan, dan bisa menyebabkan kesalahan jika tidak digunakan dengan benar.

    Monitor adalah konstruksi tingkat tinggi yang menggabungkan data bersama dengan prosedur untuk mengaksesnya, menggunakan variabel kondisi untuk menunggu dan memberi sinyal, sehingga lebih aman dan mudah digunakan karena mengelola sinkronisasi secara otomatis.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?

Mengimplementasikan versi fixed dari Dining Philosophers Problem menggunakan semaphore untuk menghindari deadlock, karena sulit memastikan semua kondisi deadlock benar-benar teratasi tanpa simulasi berulang.

- Bagaimana cara Anda mengatasinya?

Saya mengatasinya dengan berdiskusi intensif dalam kelompok, mereferensikan pseudocode dari sumber online dan melakukan simulasi.

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
