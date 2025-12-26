
# Laporan Praktikum Minggu 9
Topik: Simulasi Algoritma Penjadwalan CPU

---

## Identitas
- **Nama**  : Alya Deviana Putri Reynaldi 
- **NIM**   : 250202928 
- **Kelas** : 1IKRB

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
Contoh:  
> Mahasiswa mampu menjelaskan fungsi utama sistem operasi dan peran kernel serta system call.

---

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
