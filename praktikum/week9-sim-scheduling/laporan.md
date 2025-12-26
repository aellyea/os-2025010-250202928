
# Laporan Praktikum Minggu 9
Topik: Simulasi Algoritma Penjadwalan CPU

---

## Identitas
- **Nama**  : Alya Deviana Putri Reynaldi 
- **NIM**   : 250202928 
- **Kelas** : 1IKRB

---

## Tujuan

1. Menyiapkan dataset proses sebagai masukan simulasi.  
2. Mengembangkan aplikasi scheduling CPU berbasis command line.  
3. Menerapkan algoritma FCFS dan/atau SJF tanpa preemption.  
4. Mengeksekusi program dengan data tes.  
5. Mendokumentasikan dan menyimpan output hasil program.

---

## Dasar Teori

*Pengelolaan Eksekusi Proses dalam Sistem Operasi*

Memiliki peran penting dalam mengatur eksekusi berbagai proses yang berjalan secara bersamaan. Pengelolaan ini bertujuan agar penggunaan CPU dapat dilakukan secara efektif dengan membagi waktu pemrosesan kepada setiap proses yang berada dalam kondisi siap. Tanpa mekanisme pengaturan yang baik, proses dapat saling berebut sumber daya sehingga menurunkan kinerja sistem secara keseluruhan.

*Algoritma Penjadwalan CPU*

Algoritma penjadwalan CPU digunakan sebagai aturan untuk menentukan urutan proses yang akan dieksekusi oleh prosesor. Setiap algoritma memiliki pendekatan dan karakteristik yang berbeda dalam menentukan prioritas eksekusi proses. Pemilihan algoritma penjadwalan yang tepat dapat memengaruhi kinerja sistem, khususnya dalam hal waktu tunggu dan waktu penyelesaian proses.

*Simulasi Algoritma Penjadwalan*

Simulasi algoritma penjadwalan CPU merupakan metode untuk memodelkan cara kerja penjadwalan secara sederhana melalui program komputer. Dengan menggunakan simulasi, proses perhitungan waktu eksekusi dapat dilakukan secara otomatis dan hasilnya dapat dianalisis serta dibandingkan dengan perhitungan manual. Simulasi ini membantu dalam memahami perilaku algoritma penjadwalan secara lebih praktis dan terstruktur.

---

## Langkah Praktikum

1. Memahami prinsip scheduling CPU lewat pembuatan kode program.  
2. Membuat program simulasi untuk penjadwalan proses.  
3. Melakukan uji coba algoritma FCFS maupun SJF dengan dataset proses.  
4. Menghitung otomatis waktu tunggu dan waktu penyelesaian proses.  
5. Menampilkan output simulasi dalam format tabel dengan baik.

---

## Kode / Perintah

1. **Menyiapkan Dataset**

   | Proses | Arrival Time | Burst Time |
   |:--:|:--:|:--:|
   | P1 | 0 | 6 |
   | P2 | 1 | 8 |
   | P3 | 2 | 7 |
   | P4 | 3 | 3 |

2. **Mengimplementasi Algoritma**

   Dengan ketentuan
   
   1. Menghitung *waiting time* dan *turnaround time*.  
   2. Mendukung minimal **1 algoritma (FCFS atau SJF non-preemptive)**.  
   3. Menampilkan hasil dalam tabel.


 4. **Eksekusi & Validasi**

    Menjalankan program menggunakan dataset uji.  
  

 5. **Analisis**

    Menjelaskan alur program dan membandingkan hasil simulasi dengan perhitungan manual serta menjelaskan kelebihan dan keterbatasan simulasi.

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

1. Mengapa simulasi diperlukan untuk menguji algoritma scheduling?

   **Jawaban:**

   Karena simulasi memungkinkan evaluasi algoritma penjadwalan CPU pada skenario proses rumit yang menyerupai kondisi nyata, seperti variasi waktu kedatangan, durasi eksekusi, dan pola acak operasi sistem aktual dan dapat mengatasi masalah seperti kelaparan proses atau overhead memori cache.

   
2. Apa perbedaan hasil simulasi dengan perhitungan manual jika dataset besar?
   
   **Jawaban:**
   
   Simulasi jauh lebih praktis karena otomatis menangani kerumitan durasi proses, sedangkan manual memerlukan waktu panjang dan sulit diverifikasi untuk optimasi. Untuk data skala besar, hitungan tangan rawan kesalahan karena faktor manusia dan terhambat pada sampel terbatas, menyebabkan selisih besar dengan simulasi yang mengolah semua data secara menyeluruh.

   
3. Algoritma mana yang lebih mudah diimplementasikan? Jelaskan.
 
   **Jawaban:**

   Algoritma FCFS (First-Come-First-Served) paling sederhana untuk diimplementasikan karena hanya memproses proses berdasarkan urutan kedatangan menggunakan struktur antrian FIFO standar, tanpa memerlukan logika tambahan seperti pemilihan burst time terkecil atau pengelolaan prioritas. Berbeda dengan SJF yang harus mencari proses terpendek, Priority yang membandingkan nilai prioritas secara dinamis, atau Round Robin yang melibatkan pembagian time quantum, FCFS memerlukan kode minimal dan cocok untuk lingkungan batch processing sederhana.

   

---

## Refleksi Diri
1. Apa bagian yang paling menantang minggu ini?

   **Jawaban:**
   
   Memahami perbedaan simulasi dengan manual calculation untuk dataset besar pada algoritma scheduling karena manual mudah error.
  
2. Bagaimana cara Anda mengatasinya?  

   **Jawaban:**
   
   Belajar dari simulasi kode Python sederhana dan membandingkan hasil.


---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
