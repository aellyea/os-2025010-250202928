
# Laporan Praktikum Minggu 4
Topik: Manajemen Proses dan User di Linux

---

## Identitas
- **Nama**  : Alya Deviana Putri Reynaldi
- **NIM**   : 205202928
- **Kelas** : 1IKRB

---

## Tujuan
> Mengetahui cara kerja sistem Linux dalam menangani proses dan akun pengguna.

> Mengamati aktivitas proses yang sedang berlangsung di sistem.

> Melakukan pembuatan dan pengelolaan user menggunakan perintah dasar Linux.

> Memahami peran manajemen pengguna dalam menjaga keamanan dan kontrol akses sistem.

---

## Dasar Teori
**1. Proses dalam Sistem Linux**

Setiap aplikasi atau perintah yang dijalankan di Linux disebut proses. Sistem akan memberi setiap proses sebuah nomor unik yang disebut PID (Process ID) agar bisa dikenali dan dikelola. Proses bisa berjalan di latar depan maupun latar belakang. Linux mendukung banyak proses berjalan bersamaan dengan sistem penjadwalan (scheduler) yang mengatur waktu eksekusinya. Perintah seperti ``ps``, ``top``, dan ``kill`` dipakai untuk memantau serta mengatur proses tersebut.

**2. Struktur dan Hierarki Proses**

Semua proses di Linux memiliki induk (parent process), dan dari induk tersebut dapat muncul anak proses (child process). Hierarki ini dapat dilihat dengan perintah ``pstree``, yang menampilkan hubungan antars proses dalam bentuk pohon. Proses paling awal yang berjalan setelah sistem menyala adalah systemd (atau init pada sistem lama), yang menjadi dasar bagi semua proses lain.

**3. Pengguna dan Grup**

Linux adalah sistem multiuser, artinya bisa digunakan oleh banyak pengguna dalam satu waktu. Setiap akun pengguna memiliki identitas berupa UID, sedangkan grup memiliki GID. Manajemen pengguna dilakukan untuk mengatur hak dan ruang lingkup akses. Perintah seperti ``adduser``, ``passwd``, ``id``, dan ``groups`` digunakan untuk membuat serta memeriksa akun atau grup pengguna.

**4. Hak Akses dan Keamanan**

Setiap file di Linux dilindungi oleh sistem izin (permission) yang menentukan siapa yang boleh membaca, menulis, atau menjalankan file tersebut. Pengaturan ini ditandai dengan kombinasi huruf ``r``, ``w``, dan ``x``. Dengan pengelolaan user dan hak akses yang baik, administrator dapat mencegah penyalahgunaan sistem serta menjaga stabilitas dan keamanan data.


---

## Langkah Praktikum
1. Menjalankan perintah dasar untuk mengetahui identitas dan hak akses pengguna di Linux.
2. Melakukan percobaan untuk memantau proses yang sedang berjalan di sistem.
3. Mengontrol proses dengan menjalankan dan menghentikan program tertentu melalui terminal.
4. Menganalisis hierarki proses untuk mengenali hubungan antar proses dan mengerjakan berbagai perintah di langkah pengerjaan dengan lengkap.
5. Mengerjakan tugas & quiz sesuai dengan menjawab pertanyaan terkait proses dan manajemen user.
6. Mendokumentasikan seluruh hasil praktikum dan mengunggahnya ke repositori Git dengan commit message yang digunakan.

---

## Kode / Perintah
**Eksperimen 1 – Identitas User**

```bash
whoami
id
groups
```
Membuat user baru 
``` bash
sudo adduser praktikan
sudo passwd praktikan
```
---


**Eksperimen 2 – Monitoring Proses**

```bash
ps aux | head -10
top -n 1
```
---


**Eksperimen 3 – Kontrol Proses**
Menjalankan program latar belakang 
```bash
sleep 1000 &
ps aux | grep sleep
```

Menghentikan proses
```bash
kill <PID>
```

Memastikan proses telah berhenti dengan 
```bash
ps aux | grep sleep
```
---


**Eksperimen 4 – Analisis Hierarki Proses**
```bash
pstree -p | head -20
```
---


**Commit dan push**
```bash
git add .
git commit -m "Minggu 4 - Manajemen Proses & User"
git push origin main
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
