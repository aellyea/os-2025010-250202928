
# Laporan Praktikum Minggu 14
Topik: Penyusunan Laporan Praktikum Format IMRAD (Deadlock)

---

## Identitas
- **Nama**  : Alya Deviana Putri Reynaldi
- **NIM**   : 250202928 
- **Kelas** : 1IKRB

---


## 1. Pendahuluan

**A. Latar Belakang**

Sistem operasi modern menghadapi tantangan kompleks dalam mengelola proses dan sumber daya secara bersamaan. Salah satu masalah kritis yang sering muncul adalah deadlock, yaitu kondisi di mana dua atau lebih proses saling menunggu sumber daya yang dipegang oleh proses lain, sehingga tidak ada proses yang dapat melanjutkan eksekusinya (Arpaci-Dusseau & Arpaci-Dusseau, 2023). Fenomena ini dapat menyebabkan sistem menjadi tidak responsif dan menurunkan efisiensi penggunaan sumber daya secara signifikan.

Dalam lingkungan komputasi yang semakin berkembang seperti cloud computing dan sistem terdistribusi, masalah deadlock menjadi semakin relevan dan kompleks (Kumar & Patel, 2022). Ketika deadlock terjadi, sumber daya sistem seperti CPU, memori, atau perangkat I/O menjadi terkunci dan tidak dapat digunakan, yang dapat mengakibatkan kegagalan sistem secara keseluruhan.
Menurut Arpaci-Dusseau dan Arpaci-Dusseau (2023), deadlock terjadi ketika empat kondisi terpenuhi secara bersamaan: mutual exclusion, hold and wait, no preemption, dan circular wait. Pemahaman tentang kondisi-kondisi ini sangat penting untuk mengembangkan strategi pencegahan dan penanganan deadlock yang efektif. Kumar dan Patel (2022) juga menjelaskan bahwa setiap pendekatan penanganan deadlock memiliki trade-off antara kompleksitas implementasi dan efisiensi sistem, sehingga pemilihan strategi yang tepat menjadi krusial.

---

**B. Rumusan Masalah**

1. Apa yang dimaksud dengan deadlock dan bagaimana mekanisme terjadinya dalam sistem operasi?
2. Apa saja kondisi-kondisi yang harus terpenuhi agar deadlock dapat terjadi?
3. Bagaimana strategi-strategi untuk mencegah, menghindari, mendeteksi, dan melakukan recovery dari deadlock?

---

**C. Tujuan**

1. Menjelaskan konsep deadlock dan mekanisme terjadinya dalam sistem operasi.
2. Mengidentifikasi empat kondisi yang diperlukan untuk terjadinya deadlock.
3. Menguraikan berbagai strategi penanganan deadlock meliputi pencegahan, penghindaran, deteksi, dan pemulihan.
4. Membandingkan kelebihan dan kekurangan dari setiap strategi penanganan deadlock untuk memberikan pemahaman dalam pemilihan metode yang tepat.

---

## 2. Metode

Metode pengukuran ini memungkinkan validasi algoritma deteksi deadlock dan memberikan visualisasi yang jelas tentang kondisi deadlock dalam sistem (Arpaci-Dusseau & Arpaci-Dusseau, 2023).

**A. Lingkungan Uji**

Implementasi deteksi deadlock dalam pengujian ini menggunakan simulasi game dungeon berbasis Python yang merepresentasikan kondisi deadlock dalam sistem operasi. Lingkungan uji terdiri dari:

- **Bahasa Pemrograman:** Python
- **Platform:** Sistem operasi yang mendukung interpreter Python
- **Model Sistem:** Sistem multiprogramming dengan multiple resources dan multiple processes

Dalam simulasi ini, player merepresentasikan proses, sementara dungeon keys (kunci dungeon) merepresentasikan sumber daya yang diperebutkan. Setiap player dapat memegang dan meminta kunci tertentu untuk melanjutkan permainan, yang secara konseptual sama dengan proses yang mengalokasikan dan meminta sumber daya sistem

---

**B. Langkah Eksperimen**

**1. Inisialisasi Sistem**

1. Mendefinisikan 4 player: Knight, Mage, Archer, dan Rogue sebagai representasi proses
2. Mendefinisikan 3 resource: KeyA, KeyB, dan KeyC sebagai sumber daya sistem
3. Membuat matriks alokasi yang menunjukkan sumber daya yang sedang dipegang oleh setiap proses
4. Membuat matriks request yang menunjukkan sumber daya tambahan yang diminta oleh setiap proses

**2. Pembuatan Skenario Deadlock**

Skenario ini menciptakan circular wait yang merupakan salah satu kondisi terjadinya deadlock.

1. Knight memegang Key A dan meminta Key B
2. Mage memegang Key B dan meminta Key C
3. Archer memegang Key C dan meminta Key A
4. Rogue tidak memegang kunci tetapi meminta Key A


**3. Algoritma Deteksi Deadlock**

a. Inisialisasi: Membuat array finish[] untuk menandai proses yang dapat diselesaikan, dan vector work[] yang merepresentasikan sumber daya yang tersedia

b. Iterasi: Melakukan loop untuk mencari proses yang dapat diselesaikan dengan kondisi: request proses ≤ sumber daya tersedia

c. Pembebasan Resource: Jika proses dapat diselesaikan, resource yang dipegangnya dikembalikan ke sistem

d. Terminasi: Loop berhenti ketika tidak ada lagi proses yang dapat diselesaikan

**4. Identifikasi Deadlock**

Proses yang tidak dapat menyelesaikan eksekusinya (finish[i] = False) diidentifikasi sebagai proses yang mengalami deadlock.

---

**C. Parameter dan Dataset**


- n (jumlah proses): 4 player
- m (jumlah resource): 3 jenis kunci

**Struktur Data**

**1. Allocation Matrix**

Menunjukkan resource yang sedang dipegang oleh tiap player.

| Player | Key A | Key B | Key C |
| ------ | ---- | ---- | ---- |
| Knight | 1    | 0    | 0    |
| Mage   | 0    | 1    | 0    |
| Archer | 0    | 0    | 1    |
| Rogue  | 0    | 0    | 0    |

**2. Request Matrix**

Menunjukkan resource tambahan yang dibutuhkan agar player bisa lanjut.

| Player | Key A | Key B | Key C |
| ------ | ---- | ---- | ---- |
| Knight | 0    | 1    | 0    |
| Mage   | 0    | 0    | 1    |
| Archer | 1    | 0    | 0    |
| Rogue  | 1    | 0    | 0    |


Hasil:

1. Knight butuh KeyB
2. Mage butuh KeyC
3. Archer butuh KeyA
4. Rogue butuh KeyA


**3. Available Vector**

Menunjukkan resource yang tersedia di sistem.

Available = [0, 0, 0]


Hasil: 

Tidak ada satu pun kunci yang bebas

**4. Variabel Pendukung**

`work` → salinan dari available

`finish[i]` → status apakah player ke-i bisa diselesaikan

`deadlocked[]` → daftar player yang terjebak deadlock

---
**D. Cara pengukuran**

Deadlock Detection Algorithm (Resource Allocation Graph – berbasis matriks)
Digunakan untuk mendeteksi apakah terdapat proses yang tidak dapat diselesaikan karena kekurangan resource.

**Langkah Pengukuran**

**1. Inisialisasi**

`work = available`

Semua `finish[i] = False`

**2. Pengecekan Request**

Jika `request[i] ≤ work`, maka proses dapat dijalankan.

**3. Simulasi Eksekusi**

`work = work + allocation[i]`

`finish[i] = True`

**4. Iterasi**

Ulangi hingga tidak ada proses yang bisa dijalankan.

**5. Deteksi Deadlock**

Proses dengan *finish[i] == False* dinyatakan deadlock.

---

## 3. Hasil dan ringkasan

**Hasil**


![Deadlock](screenshots/deadlock.png)


**Ringkasan**

1. Tidak ada resource yang tersedia (available = [0,0,0])

2. Semua player masih membutuhkan resource tambahan

3. Tidak ada satu pun request yang dapat dipenuhi

4. Algoritma tidak menemukan proses yang bisa diselesaikan

5. Deadlock total terdeteksi pada seluruh player


---

## 4. Pembahasan

**1. Interpretasi Hasil**

Eksperimen menunjukkan bahwa algoritma deteksi deadlock berhasil mengidentifikasi kondisi deadlock dalam sistem. Tiga player utama (Knight, Mage, dan Archer) terdeteksi mengalami deadlock, dan Rogue juga terjebak karena ketergantungan pada sumber daya yang terlibat dalam circular wait.

**Analisis Mekanisme Deadlock**

Deadlock terjadi karena terpenuhinya keempat kondisi secara bersamaan karena:

1. Mutual Exclusion: Setiap kunci hanya dapat dipegang oleh satu player. Terlihat dalam allocation matrix bahwa setiap kunci hanya dialokasikan kepada satu player.
   
2. Hold and Wait: Knight memegang Key A sambil menunggu Key B, Mage memegang Key B sambil menunggu Key C, dan Archer memegang Key C sambil menunggu Key A.
   
3. No Preemption: Tidak ada mekanisme untuk mengambil paksa kunci dari player yang memegangnya.
   
4. Circular Wait: Terdapat rantai sirkular yang jelas: Knight → Key B (dipegang Mage) → Key C (dipegang Archer) → Key A (dipegang Knight).

Algoritma bekerja dengan mencoba menyelesaikan proses secara iteratif berdasarkan ketersediaan sumber daya. Dengan available = [0, 0, 0], tidak ada request yang dapat dipenuhi, sehingga loop berhenti dan semua proses yang belum selesai diidentifikasi sebagai deadlock.

---
   
**2. Keterbatasan**

1. Skala sistem terbatas
2. Skenario deterministik
3. Tidak ada mekanisme recovery
4. Overhead tidak diukur
5. Model statis

**Perbandingan Teori dan Hasil Eksperimen Deadlock**

| **Aspek**                   | **Teori Deadlock (Arpaci-Dusseau & Arpaci-Dusseau, 2023)**                                                                     | **Hasil Eksperimen**                                                                                                 |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------- |
| Kondisi Terjadinya Deadlock | Deadlock terjadi apabila keempat kondisi terpenuhi: *mutual exclusion*, *hold and wait*, *no preemption*, dan *circular wait*. | Seluruh kondisi deadlock terpenuhi pada skenario eksperimen yang melibatkan beberapa player dan resource.            |
| Ketersediaan Sumber Daya    | Deadlock akan terjadi ketika tidak ada sumber daya tambahan yang tersedia untuk memenuhi permintaan proses.                    | Tidak terdapat sumber daya bebas sehingga setiap player harus menunggu resource yang sedang dipegang player lain.    |
| Circular Wait               | Circular wait menjadi indikator utama terjadinya deadlock dan dapat dimodelkan dalam *resource allocation graph*.              | Terbentuk circular wait antar player yang saling bergantung, sesuai dengan teori.                                    |
| Deteksi Deadlock            | Deadlock dapat dideteksi melalui analisis *resource allocation graph* yang menunjukkan siklus.                                 | Deadlock berhasil terdeteksi pada seluruh player yang terlibat dalam siklus ketergantungan.                          |
| Kesesuaian dengan Teori     | Secara teori, deadlock bersifat deterministik ketika semua kondisi terpenuhi.                                                  | Hasil eksperimen sepenuhnya memvalidasi teori deadlock yang dikemukakan oleh Arpaci-Dusseau & Arpaci-Dusseau (2023). |


---

## 5. Kesimpulan

1. Mekanisme Deadlock Teridentifikasi: Deadlock terjadi ketika empat kondisi terpenuhi secara bersamaan (mutual exclusion, hold and wait, no preemption, dan circular wait), dengan circular wait sebagai inti masalah yang menyebabkan proses saling menunggu sumber daya secara melingkar (Arpaci-Dusseau & Arpaci-Dusseau, 2023).
   
2. Algoritma Deteksi Efektif: Algoritma berbasis resource allocation graph berhasil mendeteksi seluruh proses yang terjebak deadlock melalui analisis ketersediaan sumber daya dan pemeriksaan iteratif, memvalidasi teori deadlock secara deterministik.
   
3. Strategi Penanganan Memiliki Trade-off: Pendekatan deteksi deadlock cocok untuk sistem skala terbatas namun bersifat reaktif tanpa mekanisme recovery, sehingga pemilihan strategi harus mempertimbangkan kompleksitas implementasi dan efisiensi sistem terutama untuk aplikasi modern seperti cloud computing (Kumar & Patel, 2022).

---

## Quiz

1. **Mengapa sitasi dan daftar pustaka penting, bahkan untuk laporn praktikum?**

   **Jawaban**

Karena menunjukkan bahwa teori, metode, dan konsep yang digunakan memiliki dasar ilmiah yang jelas. Dengan mencantumkan sumber, penulis menghargai karya orang lain serta menghindari plagiarisme. Selain itu, sitasi membantu pembaca memahami asal konsep yang digunakan dan memungkinkan mereka menelusuri referensi untuk pendalaman materi. Dalam konteks akademik, hal ini juga melatih sikap ilmiah, kejujuran akademik, dan kebiasaan penulisan yang benar sejak dini.


2.  **Apa perbedaan antara bagian hasil dan pembahasan**

   **Jawaban**

| **Aspek**                | **Hasil**                                                   | **Pembahasan**                                                                    |
| ------------------------ | ----------------------------------------------------------- | --------------------------------------------------------------------------------- |
| Tujuan                   | Menyajikan data mentah dan fakta objektif dari eksperimen   | Memberikan interpretasi, analisis, dan makna dari hasil eksperimen                |
| Isi Utama                | Data numerik, tabel, grafik, dan output eksperimen          | Penjelasan sebab-akibat, analisis konseptual, dan implikasi                       |
| Sifat Penulisan          | Deskriptif (melaporkan apa yang terjadi)                    | Analitis dan interpretatif (menjelaskan mengapa dan apa artinya)                  |
| Interpretasi Penulis     | Tidak mengandung interpretasi atau opini                    | Mengandung interpretasi berdasarkan teori dan literatur                           |
| Keterkaitan dengan Teori | Tidak membahas teori secara mendalam                        | Membandingkan hasil dengan teori dan penelitian sebelumnya                        |
| Contoh Pernyataan        | “Deadlock terdeteksi pada Knight, Mage, Archer, dan Rogue.” | “Deadlock terjadi karena terpenuhinya keempat kondisi deadlock sesuai teori [1].” |
| Keterbatasan Penelitian  | Tidak dibahas                                               |                                                                                   |


3. Mengapa sitasi dan daftar pustaka penting, bahkan untuk laporan praktikum?

   **Jawaban**

   1. Menghindari plagiarisme
   2. Menunjukan argumen yang didukung sumber terpercaya dan riset literatur memadai
   3. Dapat memeriksa sumber asli untuk validasi informasi
   4. Melatih kebiasaan penulisan ilmiah dan membedakan karya ilmiah dari opini pribadi.
   

   



   
## Daftar Pustaka
1. Arpaci-Dusseau, R. H., & Arpaci-Dusseau, A. C. (2023). Operating Systems: Three Easy Pieces (Version 1.10). Arpaci-Dusseau Books.
   
2. Kumar, S., & Patel, R. (2022). Machine Learning Approaches for Deadlock Prediction in Operating Systems. Journal of Systems and Software






