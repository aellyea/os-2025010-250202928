
# Laporan Praktikum Minggu 11
Topik:  Simulasi dan Deteksi Deadlock

---

## Identitas
- **Nama**  : Alya Deviana Putri Reynaldi
- **NIM**   : 250202928
- **Kelas** : 1IKRB

---

## Tujuan
1. Merancang dan mengembangkan aplikasi sederhana berbasis terminal untuk mengidentifikasi kondisi deadlock pada sistem.

2. Melakukan pengujian algoritma deteksi deadlock menggunakan data uji yang telah disediakan.

3. Mengolah dan menyajikan hasil pendeteksian deadlock secara terstruktur dalam bentuk tabel.

4. Menganalisis serta menjelaskan hasil pengujian berdasarkan alur logika dan konsep sistem operasi.

---

## Dasar Teori

Pengertian Deadlock

Deadlock merujuk pada situasi dalam sistem operasi di mana dua atau lebih proses saling menunggu sumber daya yang sedang dipegang oleh proses lainnya, sehingga tidak ada proses yang mampu melanjutkan eksekusinya. Keadaan ini menyebabkan penghentian permanen proses kecuali dilakukan tindakan intervensi oleh sistem.

Kondisi Terjadinya Deadlock

Deadlock akan terjadi jika keempat kondisi berikut terpenuhi secara simultan: mutual exclusion (sumber daya bersifat eksklusif dan tidak dapat dibagikan), hold and wait (proses mempertahankan sumber daya sambil menunggu sumber daya lain), no preemption (sumber daya tidak dapat diambil secara paksa), dan circular wait (terjadi rantai siklus saling menunggu antarproses).

Pendekatan Deteksi Deadlock

Pendekatan deteksi deadlock memperbolehkan sistem berjalan tanpa upaya pencegahan deadlock. Sistem melakukan pemeriksaan periodik menggunakan algoritma spesifik, seperti Resource Allocation Graph atau Wait-For Graph, guna mengidentifikasi siklus yang mengindikasikan keberadaan deadlock.

Pemulihan Deadlock (Recovery)

Jika deadlock terdeteksi, sistem operasi dapat melakukan pemulihan melalui berbagai mekanisme, seperti terminasi proses tertentu, rollback ke keadaan sebelumnya, atau preemption sumber daya. Pemilihan strategi pemulihan harus mempertimbangkan implikasi terhadap performa dan integritas sistem.

---

## Langkah Praktikum

1. Menyusun dataset sederhana yang berisi daftar proses, alokasi sumber daya, serta permintaan sumber daya sebagai data uji deteksi deadlock.

2. Mengimplementasikan algoritma deteksi deadlock untuk menganalisis hubungan antara proses dan sumber daya berdasarkan dataset yang digunakan.

3. Menjalankan program deteksi deadlock menggunakan dataset uji yang telah disiapkan.

4. Mengidentifikasi proses yang terlibat dalam kondisi deadlock berdasarkan hasil eksekusi program.

5. Menyajikan hasil pendeteksian deadlock dalam bentuk tabel yang memuat status setiap proses.

6. Menganalisis dan menjelaskan hasil deteksi deadlock dengan mengaitkannya pada teori dan kondisi terjadinya deadlock.

---

## Kode / Perintah

**Ketentuan Teknis**

Bahasa pemrograman bebas (Python / C / Java / lainnya).
Program berbasis terminal, tidak memerlukan GUI.
Fokus penilaian pada logika algoritma deteksi deadlock, bukan kompleksitas bahasa.

Gunakan dataset sederhana yang berisi:

Daftar proses
Resource Allocation
Resource Request / Need

Contoh tabel:

Proses	Allocation	Request

P1	R1	R2
P2	R2	R3
P3	R3	R1

**Implementasi Algoritma Deteksi Deadlock**

Program minimal harus:

Membaca data proses dan resource.

Menentukan apakah sistem berada dalam kondisi deadlock.

Menampilkan proses mana saja yang terlibat deadlock.

**Eksekusi & Validasi**

Jalankan program dengan dataset uji.
Validasi hasil deteksi dengan analisis manual/logis.
Simpan hasil eksekusi dalam bentuk screenshot.

**Analisis Hasil**

Sajikan hasil deteksi dalam tabel (proses deadlock / tidak).

Jelaskan mengapa deadlock terjadi atau tidak terjadi.

Kaitkan hasil dengan teori deadlock (empat kondisi).

**Commit & Push**

git add .
git commit -m "Minggu 11 - Deadlock Detection"
git push origin main

---

## Hasil Eksekusi

Hasil Deteksi

![Hasil Deteksi Deadlock](screenshots/hasil_deteksi.png)


---

## Analisis

Dari hasil pengujian menggunakan dataset, proses yang terlibat dalam deadlock adalah:

| Proses | Status   |
| ------ | -------- |
| P1     | Deadlock |
| P2     | Deadlock |
| P3     | Deadlock |

Deadlock terjadi karena setiap proses menahan satu resource dan menunggu resource lain yang sedang digunakan oleh proses lain. Kondisi ini menyebabkan tidak ada proses yang dapat melanjutkan eksekusi, sehingga sistem berada dalam keadaan deadlock.

Hasil deteksi menunjukkan terjadinya deadlock karena sistem memenuhi keempat kondisi deadlock, yaitu mutual exclusion, hold and wait, no preemption, dan circular wait. Ketiga proses tersebut saling menunggu resource yang dipegang oleh proses lain, sehingga tidak ada proses yang dapat menyelesaikan eksekusinya.


**Validasi Hasil Deteksi dengan Analisis Manual/Logis**

Berdasarkan analisis manual terhadap dataset, setiap proses memegang satu resource dan menunggu resource lain yang sedang digunakan oleh proses lain. Kondisi ini membentuk **circular wait** (P1 → P2 → P3 → P1), sehingga tidak ada proses yang dapat melanjutkan eksekusi. Hasil analisis manual ini sesuai dengan hasil program yang mendeteksi adanya deadlock, sehingga hasil deteksi dinyatakan valid.

---



## Kesimpulan

1. Program deteksi deadlock berhasil mengidentifikasi bahwa sistem berada dalam kondisi deadlock dan menentukan proses yang terlibat, yaitu P1, P2, dan P3, berdasarkan analisis hubungan antara proses dan resource.

2. Deadlock terjadi karena keempat kondisi deadlock terpenuhi, yaitu mutual exclusion, hold and wait, no preemption, dan circular wait, sehingga tidak ada proses yang dapat melanjutkan eksekusi dan hasil deteksi dinyatakan valid secara logis.


---

## Quiz
1. Apa perbedaan antara deadlock prevention, avoidance, dan detection?
   
   **Jawaban:**

Pembeda utama antara ketiga ini terletak pada waktu dan cara mereka menangani kondisi deadlock:

Prevention (Pencegahan)

Pendekatan ini mencegah deadlock dari awal secara permanen dengan melanggar salah satu kondisi deadlock misalnya no circular wait via resource ordering). Deadlock jadi mustahil terjadi, tapi dengan biaya efisiensi tinggi.

Avoidance (Penghindaran)

Pada saat keputusan dinamis saat runtime, sistem akan mengecek terlebih dahulu apakah alokasi resource akan membuat state "unsafe" (bisa deadlock) sebelum izinkan dan membutuhkan info maksimum kebutuhan resource.

Detection (Deteksi)

Membiarkan deadlock terjadi dulu, baru deteksi secara periodik dan recovery setelahnya.


2. Mengapa deteksi deadlock tetap diperlukan dalam sistem operasi?
   
   **Jawaban:**

   Deteksi deadlock tetap diperlukan karena pencegahan dan penghindaran sering tidak praktis atau terlalu mahal dalam sistem operasi modern yang mengutamakan performa, fleksibilitas, dan skalabilitas. Daripada mencoba mencegah deadlock 100% dengan biaya tinggi, lebih realistis membiarkan kemungkinan terjadi lalu mendeteksi dan menanganinya ketika benar-benar muncul
   
4. Apa kelebihan dan kekurangan pendekatan deteksi deadlock?
   
   **Jawaban:**

Kelebihan Pendekatan Deteksi Deadlock

| No | Kelebihan | Penjelasan |
|----|-----------|------------|
| 1 | Pemanfaatan sumber daya optimal | Tidak membatasi alokasi sumber daya secara ketat, sehingga penggunaan lebih efisien dan fleksibel. |
| 2 | Tidak memerlukan data awal | Sistem tidak membutuhkan informasi kebutuhan maksimum sumber daya dari tiap proses sejak awal. |
| 3 | Cocok untuk risiko deadlock rendah | Overhead hanya terjadi saat pemeriksaan berkala, bukan secara terus-menerus. |
| 4 | Deteksi relatif cepat | Deadlock dapat ditemukan lebih awal jika pemeriksaan dilakukan secara rutin. |

Kekurangan Pendekatan Deteksi Deadlock

| No | Kekurangan | Penjelasan |
|----|------------|------------|
| 1 | Beban komputasi tinggi | Algoritma deteksi membutuhkan sumber daya besar, terutama pada sistem dengan banyak proses dan sumber daya (hingga O(m × n²)). |
| 2 | Pemulihan kompleks | Penghentian proses atau perebutan sumber daya dapat menyebabkan kehilangan hasil komputasi sementara. |
| 3 | Tidak mencegah deadlock | Deadlock tetap dapat terjadi dan membuat proses terhenti sementara sebelum pemulihan dilakukan. |
| 4 | Penjadwalan deteksi sulit | Deteksi terlalu sering meningkatkan beban sistem, sedangkan deteksi jarang memperpanjang durasi deadlock. |

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?

Menerapkan algoritma deteksi deadlock secara akurat, khususnya dalam menghitung sumber daya yang tersedia dan mengelola simulasi proses yang selesai karena rawan error

- Bagaimana cara Anda mengatasinya?  

Mengulang-ulang uji serta mempelajari kembali 


---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
