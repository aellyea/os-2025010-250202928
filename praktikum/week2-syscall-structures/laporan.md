
# Laporan Praktikum Minggu 2
Topik: Mekanisme System Call dan Struktur Sistem Operasi.

---

## Identitas
- **Nama**  : Alya Deviana Putri Reynaldi 
- **NIM**   : 250202928	
- **Kelas** : 1IKRB

---

## Tujuan
- Memahami konsep dan struktur alur mekanisme dari system call.
- Mengamati proses komunikasi dari aplikasi (user space) ke kernel melalui system call.
- Mengklasifikasikan berbagai jenis sytem call.
- Meningkatkan kemampuan teknis dalam lingkungan linux.

---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.

---

## Langkah Praktikum
Menyiapkan lingkungan Linux (Ubuntu/WSL) dan memastikan paket `strace`, `man`, serta `git` sudah terinstal dengan benar.

Membuka terminal dan menjalankan perintah `strace ls` untuk mengamati daftar system call yang digunakan oleh perintah `ls`.

Mencatat dan menganalisis 5–10 system call pertama yang muncul, kemudian menyimpannya dalam file `results/syscall_ls.txt`.

Melakukan pengamatan terhadap system call pada operasi file I/O menggunakan perintah `strace -e trace=open,read,write,close cat /etc/passwd`.

Mengidentifikasi urutan eksekusi system call `open`, `read`, `write`, dan `close` yang terjadi selama proses pembacaan file.

Menjalankan perintah `dmesg | tail -n 10` untuk mengamati aktivitas kernel dan membedakan log kernel dengan output program biasa.

Membuat diagram alur system call yang menggambarkan perpindahan dari mode user ke mode kernel dan kembali lagi.

Menyimpan diagram hasil observasi ke dalam folder `screenshots/syscall-diagram.png`.

Mengumpulkan seluruh hasil percobaan (file, diagram, dan analisis) ke dalam folder `praktikum/week2-syscall-structure/`.

Melakukan commit dan push hasil akhir ke repositori GitHub dengan pesan:
  ```bash
   git add .
   git commit -m "Minggu 2 - Struktur System Call dan Kernel Interaction"
   git push origin main
   ```
---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
strace ls
strace -e trace=open,read,write,close cat /etc/passwd
dmesg | tail -n 10
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
1. Apa fungsi utama system call dalam sistem operasi

    **Jawaban:**

Penghubung antara aplikasi dan kernel

→ System call menjadi antarmuka resmi agar program bisa berinteraksi dengan sumber daya sistem tanpa perlu mengaksesnya langsung.

Pengelolaan sumber daya (Resource Management)

→ System call memungkinkan aplikasi untuk menggunakan CPU, memori, dan perangkat I/O secara efisien dengan pengaturan dari kernel.

Keamanan dan kontrol akses

→ Melalui system call, kernel memeriksa izin setiap operasi agar program tidak bisa mengakses data atau perangkat tanpa otorisasi.

Komunikasi antara proses (Interprocess Communication)

→ System call menyediakan mekanisme agar proses dapat saling bertukar data atau pesan secara aman.

Penanganan perangkat keras

→ Aplikasi tidak berinteraksi langsung dengan hardware; system call yang meneruskan permintaan ke driver perangkat.

Menjaga stabilitas sistem

→ Dengan system call, semua interaksi user dengan kernel dilakukan secara terkendali, sehingga kesalahan pada aplikasi tidak merusak keseluruhan sistem operasi.
   
2. Sebutkan 4 kategori system call yang umum digunakan. 

    **Jawaban:**

System Call Manajemen Proses (Process Control)

→ Digunakan untuk membuat, menghapus, atau mengatur proses.

Contoh: fork(), exec(), exit(), wait()

Fungsi: memungkinkan sistem menjalankan program baru, menghentikan proses, atau menunggu proses lain selesai.

System Call Manajemen Berkas (File Management)

→ Digunakan untuk mengatur operasi pada file dan direktori.

Contoh: open(), read(), write(), close(), unlink()

Fungsi: memungkinkan aplikasi untuk menyimpan, membaca, menulis, atau menghapus data pada penyimpanan.

System Call Manajemen Perangkat (Device Management)

→ Digunakan untuk mengontrol dan berkomunikasi dengan perangkat input/output.

Contoh: ioctl(), read(), write()

Fungsi: memberikan akses terkontrol agar aplikasi bisa menggunakan perangkat keras seperti keyboard, printer, atau disk.

System Call Manajemen Informasi (Information Maintenance)

→ Digunakan untuk menyediakan informasi tentang sistem, proses, atau waktu.

Contoh: getpid(), alarm(), time(), getuid()

Fungsi: memberi data penting seperti ID proses, waktu sistem, atau informasi pengguna.

   
3. Mengapa system call tidak bisa dipanggil langsung oleh user program?

   **Jawaban:**

    System call tidak dapat dipanggil langsung oleh program pengguna karena alasan keamanan, stabilitas, dan desain sistem operasi. CPU membedakan level akses antara user mode (ring 3) dan kernel mode (ring 0) untuk mencegah program biasa menjalankan instruksi berprivilege tinggi yang dapat merusak sistem. Dengan mewajibkan setiap permintaan melewati kernel, sistem dapat memvalidasi parameter, memeriksa izin, dan mencegah akses tidak sah yang berpotensi menyebabkan serangan atau kebocoran data.
   
   Selain itu, mekanisme ini menjaga stabilitas dan konsistensi karena kernel menangani pengelolaan sumber daya dan penanganan kesalahan secara terpusat. System call juga berfungsi sebagai lapisan abstraksi yang memisahkan aplikasi dari detail perangkat keras, sehingga meningkatkan portabilitas dan memudahkan pembaruan keamanan tanpa mengubah aplikasi. Oleh karena itu, dipastikan bahwa setiap interaksi dengan sistem dilakukan melalui jalur yang aman, terkontrol, dan efisien.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
