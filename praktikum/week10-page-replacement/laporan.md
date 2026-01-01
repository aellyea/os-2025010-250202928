
# Laporan Praktikum Minggu 10
Topik: Manajemen Memori – Page Replacement (FIFO & LRU)

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
1. Apa perbedaan utama FIFO dan LRU?
   
   **Jawaban:**

   FIFO (First In First Out) mengganti halaman yang paling lama berada di memori, tanpa memedulikan kapan halaman itu terakhir kali digunakan. Sementara itu, LRU (Least Recently Used) menargetkan halaman yang paling lama tidak diakses, dengan mempertimbangkan waktu akses terakhirnya, sehingga lebih mengutamakan halaman yang baru saja dipakai.


   
2. Mengapa FIFO dapat menghasilkan Belady’s Anomaly?
   
   **Jawaban:**
   
   FIFO bisa menimbulkan Belady's Anomaly karena algoritma ini mengabaikan pola akses ke depan maupun riwayat penggunaan halaman. Saat jumlah frame memori bertambah, halaman yang sudah lama masuk mungkin tetap disimpan meski tak lagi dibutuhkan, sehingga page faults justru meningkat secara tak terduga seperti kasus di mana frame lebih banyak malah menurunkan performa.
   
3. Mengapa LRU umumnya menghasilkan performa lebih baik dibanding FIFO?
  
   **Jawaban:**
   
LRU biasanya lebih unggul karena memanfaatkan riwayat akses halaman untuk mengganti yang paling lama tak digunakan atau lebih tepatnya memprediksi halaman yang tak lagi dibutuhkan. Akibatnya, page faults berkurang dibanding FIFO, yang hanya mengandalkan urutan masuk dan berisiko mengusir halaman masih relevan, khususnya pada pola akses berulang atau lokalitas temporal. LRU pun terhindar dari anomali Belady dan terbukti lebih efisien di skenario nyata.


---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?

 **Jawaban:**

 Memahami LRU pada simulasi CPU scheduling terutama dalam menangani stack distance untuk prediksi akses halaman secara efisien.
  
- Bagaimana cara Anda mengatasinya?  

 **Jawaban:**

 Mencoba mempelajari dan mencermati.



---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
