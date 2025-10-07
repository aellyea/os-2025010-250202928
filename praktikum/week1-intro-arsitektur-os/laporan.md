# Perbedaan Monolithic Kernel, Microkernel, dan Layered Architecture serta Contoh OS Nyata Masing-Masing Model Kernel.

#	1. Monolithic Kernel
Model arsitektur fungsionalitas kernel yang memuat manajemen proses, sistem file, driver perangkat, dan protokol jaringan, diimplementasikan sebagai satu blok kode besar dalam kernel space. Kelebihan dari Monolithic Kernel adalah performa tinggi antar-komponen cepat, sedangkan kekurangannya adalah sulit untuk debugging dan kurang aman karena semua kode memiliki akses penuh ke hardware.

Contoh OS nyata dari model kernel Monolithic Kernel :

	Linux Kernel 

Inti dari sistem operasi Linux yang berfungsi menghubungkan hardware dengan software.

	FreeBSD

Sistem operasi bebas dan open-source yang berasal dari sistem UNIX yang dirancang untuk kinerja tinggi, stabilitas, keamanan, dan kompatibilitas jaringan.

	Windows NT Kernel

Inti dari sistem operasi Windows modern yang bertugas mengatur semua interaksi antara hardware dan software.

#  2.	Microkernel
Model arsitektur kernel sistem operasi yang hanya memuat komponen inti paling dasar ke dalam kernel, sementara fungsi-fungsi lainnya dijalankan di luar kernel sebagai layanan terpisah atau user space. Kelebihan dari Microkernel adalah sangat fleksibel dan lebih aman karena server tetap stabil, sedangkan kekurangannya adalah overhead performa dan kompleksitas desain yang tinggi.

Contoh OS nyata dari model kernel Microkernel :

	Minix

Sistem operasi berbasis UNIX yang dibuat untuk tujuan pendidikan dan digunakan sebagai inspirasi untuk Linux awal versi modern (Minix 3) yang fokus pada keamanan dan reliabilitas seperti di perangkat IoT.

	QNX

digunakan di otomotif, medis, dan embedded systems. Kernelnya sangat minimal, dengan IPC untuk komunikasi dikenal karena stabilitasnya di lingkungan kritis.

	seL4 (L4 Microkernel Family)

Kernel mikro open-source yang diverifikasi secara formal untuk keamanan yang digunakan di sistem militer, aerospace dan prototipe seperti OKL4 di perangkat mobile.

#  3.	Layered Architecture
Model arsitektur sistem operasi atau perangkat lunak yang membagi sistem menjadi beberapa lapisan yang tersusun secara hierarkis. Kelebihan dari Layered Architecture adalah mudah untuk memahami dan maintain karena pemisahan tanggung jawab sedangkan kekurangannya adalah kurang fleksibel untuk perubahan horizontal.

Contoh OS nyata dari model kernel Layered Architecture :

	THE Multiprogramming System

Sistem operasi eksperimental yang membagi sistem menjadi beberapa lapisan, di mana setiap lapisan hanya berinteraksi dengan lapisan di atas atau di bawahnya.

	Multics

Sistem operasi yang dikembangkan untuk mendukung penggunaan komputer oleh banyak pengguna secara bersamaan.

	IBM OS/360

Sistem operasi mainframe yang dikembangkan Sistem ini dirancang untuk menjadi sistem operasi universal yang digunakan di berbagai jenis komputer dalam keluarga System/360, mulai dari yang kecil hingga besar.

# Analisis Relevan Model Kernel untuk Sistem Modern.

Monolithic kernel menjadi pilihan utama dan paling relevan di era digital kini, terutama karena kemampuannya handle beban kerja yang baik dan juga bisa menyeimbangkan kecepatan, skalabilitas, maupun adaptasi. Berikut ini adalah penjelasan mengenai alasan monolithic kernel menjadi paling relevan.

	Efisiensi Performa Tinggi

Semua komponen berjalan baik di dalam kernel space, minim overhead dan sangat baik untuk cloud computing.

	Skalabilitas untuk Hardware Modern

Sangat mendukung untuk multi-core dan monolithic membantu proses dengan cepat tensor karena akses hardwarenya yang langsung ke GPU/TPU.

	Adaptasi Fleksibel

 Fitur seperti Loadable bisa menambah atau menghapus driver runtime tanpa reboot. Ditambah, fitur containers bisa mengatasi kelemahan keamanan tanpa ganti arsitektur.

	Biaya Rendah & Open-Source

 Gratis dan customizable, ideal untuk startup AI atau perusahaan.




