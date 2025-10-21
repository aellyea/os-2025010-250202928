
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
4. Menganalisis hasil percobaan dan mendokumentasikan
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
