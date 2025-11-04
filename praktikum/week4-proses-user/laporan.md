
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
EKSPERIMEN 1 - IDENTITAS USER

| Perintah | Output  | Fungsi / Penjelasan |
|-----------|-----------------|---------------------|
| `whoami` | `aelyea` | Menampilkan nama user yang sedang login ke sistem. |
| `id` | `uid=1000(aelyea) gid=1000(aelyea) groups=1000(aelyea),4(adm),27(sudo),46(plugdev)` | Menampilkan informasi lengkap user seperti UID (User ID), GID (Group ID), dan grup yang diikuti. |
| `groups` | `aelyea adm dialout cdrom floppy sudo audio dip video plugdev netdev` | Menampilkan daftar grup tempat user tergabung. |

---

EKSPERIMEN 2 - MONITORING USER
| Kolom       | Penjelasan                                                                             |
| ----------- | -------------------------------------------------------------------------------------- |
| **PID**     | Menandakan identitas unik setiap proses yang aktif di sistem.                          |
| **USER**    | Menunjukkan siapa pemilik atau akun yang menjalankan proses tersebut.                  |
| **%CPU**    | Menggambarkan seberapa besar kapasitas prosesor yang sedang digunakan oleh proses itu. |
| **%MEM**    | Menunjukkan jumlah penggunaan memori relatif terhadap total RAM yang tersedia.         |
| **COMMAND** | Menampilkan nama program atau perintah yang memicu proses berjalan.                    |

---
EKSPERIMEN 3 - KONTROL PROSES

PID PROSES ``sleep`` 2541
y        2541  0.0  0.0   2600   600 pts/0    S    00:15   0:00 sleep 1000

---

EKSPERIMEN 4 - ANALISIS HIERARKI PROSES
Hasil pengamatan hierarki proses:

Proses induk yang terdeteksi adalah **systemd (PID 1)**.  

---



## Kesimpulan

1. Setiap user di Linux memiliki identitas unik (UID dan GID) serta tergabung dalam beberapa grup yang menentukan hak aksesnya.  
2. Proses di Linux dapat dimonitor dan dikendalikan menggunakan perintah seperti `ps`, `top`, dan `kill`, yang membantu mengelola kinerja sistem.  
3. Semua proses di sistem Linux berawal dari proses induk utama, yaitu `systemd`, yang bertugas memulai dan mengatur seluruh proses lainnya.


---
## TUGAS
## Fungsi Tiap Perintah

| Perintah | Fungsi |
|-----------|---------------------|
| `whoami` | Menampilkan nama user yang sedang aktif di sistem. |
| `id` | Menunjukkan UID, GID, serta grup yang terhubung dengan user. |
| `groups` | Menampilkan daftar grup tempat user tergabung. |
| `adduser <nama_user>` | Membuat akun pengguna baru di sistem Linux. |
| `passwd <nama_user>` | Mengatur atau mengganti password pengguna. |
| `ps aux` | Menampilkan semua proses yang sedang berjalan di sistem beserta detailnya. |
| `top` | Memantau proses dan penggunaan sumber daya sistem secara langsung. |
| `sleep 1000 &` | Menjalankan proses “sleep” di latar belakang selama 1000 detik. |
| `ps aux | grep sleep` | Menyaring daftar proses untuk menampilkan yang berhubungan dengan “sleep”. |
| `kill <PID>` | Mengakhiri proses berdasarkan nomor PID-nya. |
| `pstree -p` | Menampilkan struktur hierarki proses beserta nomor PID masing-masing. |

```
systemd(1)-+-agetty(224)
           |-agetty(232)
           |-cron(186)
           |-dbus-daemon(188)
           |-init-systemd(Ub(2)-+-SessionLeader(305)---Relay(307)(306)---bash(307)-+-head(533)
           |                    |                                                  `-pstree(532)
           |                    |-init(7)---{init}(8)
           |                    |-login(308)---bash(370)
           |                    `-{init-systemd(Ub}(9)
           |-networkd-dispat(193)
           |-rsyslogd(194)-+-{rsyslogd}(200)
           |               |-{rsyslogd}(201)
           |               `-{rsyslogd}(202)
           |-systemd(354)---(sd-pam)(355)
           |-systemd-journal(64)
           |-systemd-logind(197)
           |-systemd-resolve(127)
           |-systemd-timesyn(131)---{systemd-timesyn}(149)
           |-systemd-udevd(92)-+-systemd-udevd(530)
           |                   `-systemd-udevd(531)
```


---          
Hubungan antara User Management dan Keamanan Sistem Linux

Manajemen user memiliki hubungan erat dengan keamanan sistem Linux karena pengaturan user, group, dan permission berfungsi untuk membatasi hak akses setiap pengguna. Dengan sistem ini, hanya user tertentu yang dapat menjalankan perintah atau mengubah file penting, sehingga mencegah tindakan yang tidak sah. Pengelolaan user yang baik juga membantu melindungi sistem dari penyalahgunaan, menjaga integritas data, dan memastikan hanya pengguna berwenang yang dapat mengatur konfigurasi sistem.


## Quiz
1. Apa fungsi dari proses `init` atau `systemd` dalam sistem Linux?
   
   **Jawaban:**
   Fungsi ``init`` atau ``systemd`` dalam sistem Linux adalah untuk memulai dan mengatur seluruh proses ketika sistem dinyalakan. Proses ini bertugas menjalankan layanan penting, mengelola proses lain, serta menjaga agar sistem berjalan dengan stabil dan teratur. Dengan demikian, ``systemd`` berperan sebagai pengendali utama yang memastikan semua komponen sistem Linux berfungsi dengan baik sejak proses booting hingga sistem dimatikan.


2. Apa perbedaan antara kill dan killall?
   
   **Jawaban:**
   Perintah ``kill`` digunakan untuk menghentikan proses berdasarkan nomor PID (Process ID), sedangkan ``killall`` digunakan untuk menghentikan semua proses yang memiliki nama program yang sama.
   
4. Mengapa user root memiliki hak istimewa di sistem Linux?  
   **Jawaban:**  
Karena ia dirancang sebagai superuser yang dapat mengakses, mengubah, dan mengontrol semua aspek sistem tanpa batasan, seperti file sistem, proses, dan perangkat keras. Hak ini diperlukan untuk tugas administrasi penting, seperti instalasi perangkat lunak, konfigurasi jaringan, dan pemeliharaan keamanan, yang tidak bisa dilakukan oleh user biasa. Namun, penggunaan root berisiko tinggi karena kesalahan dapat merusak sistem secara permanen, sehingga biasanya dihindari untuk tugas sehari-hari.
---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?
   Belajar tentang sistem Linux dan hak istimewa user root terasa sulit karena banyak istilah teknis yang baru, dan saya sering bingung membedakan antara user biasa dan root.
- Bagaimana cara Anda mengatasinya?  
  Mengatasi dengan cara memahami konsepnya secara bertahap.
---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
