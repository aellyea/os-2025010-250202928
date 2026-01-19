
# Laporan Praktikum Minggu 13
Topik: Docker – Resource Limit (CPU & Memori)

---

## Identitas
- **Nama**  : Alya Deviana Putri Reynaldi
- **NIM**   : 250202928
- **Kelas** : 1IKRB

---

## Tujuan

1. Memahami konsep dasar containerization menggunakan Docker.
2. Membuat dan menjalankan container dari Dockerfile sederhana.
3. Menerapkan pembatasan penggunaan CPU dan memori pada container.
4. Mengamati pengaruh pembatasan resource terhadap kinerja aplikasi.
5. Melatih kemampuan analisis dan dokumentasi hasil praktikum.

---

## Dasar Teori

 **Containerization**

Containerization merupakan teknologi virtualisasi yang lebih ringan dan memungkinkan aplikasi berjalan dalam lingkungan yang terisolasi di dalam sebuah container. Berbeda dengan virtual machine, container menggunakan kernel yang sama dengan sistem operasi host sehingga lebih hemat resource dan efisien dalam penggunaannya.


**Docker**

Docker adalah platform untuk containerization yang berfungsi membangun, menyebarkan, dan menjalankan aplikasi di dalam container. Platform ini memanfaatkan image sebagai template dasar untuk menciptakan container yang memiliki sifat konsisten dan dapat dipindahkan ke berbagai environment dengan mudah.

**Dockerfile**

Dockerfile merupakan file konfigurasi yang memuat serangkaian perintah untuk membuat Docker image. Dengan menggunakan Dockerfile, proses instalasi dependensi dan menjalankan aplikasi dapat dilakukan secara otomatis tanpa intervensi manual.


**Isolasi dan Pengaturan Resource**

Sistem operasi Linux memiliki kemampuan untuk mengisolasi proses dan mengatur batasan resource melalui fitur namespace dan control groups (cgroups). Fitur-fitur ini memungkinkan pengaturan dan pembatasan penggunaan CPU serta memori pada setiap container yang berjalan.

**Pembatasan Resource pada Container**

Docker menyediakan fasilitas untuk membatasi resource yang dapat digunakan oleh container, termasuk CPU dan memori. Tujuan dari pembatasan ini adalah mencegah satu container menghabiskan resource secara berlebihan yang dapat mengganggu performa container lain maupun sistem host.

**Monitoring Resource**

Penggunaan resource pada container dapat dimonitor menggunakan perintah seperti docker stats. Proses monitoring ini berguna untuk mengamati dan menganalisis bagaimana pembatasan resource mempengaruhi kinerja aplikasi yang berjalan di dalam container.
 


---

## Langkah Praktikum

1. Menyiapkan dan memverifikasi lingkungan Docker
2. Membuat program uji berbasis terminal
3. Menyusun Dockerfile untuk menjalankan program
4. Membangun image Docker dari Dockerfile
5. Menjalankan container tanpa pembatasan resource
6. Menjalankan container dengan pembatasan CPU dan memori serta melakukan monitoring

---

## Kode / Perintah

1. Pemeriksaan Docker
   
```bash
docker version
docker ps
```

2. Build Image Docker
   
```bash  
docker build -t resource-limit-test .
```

3. Menjalankan Container Tanpa Pembatasan Resource
   
```bash
docker run --rm resource-limit-test
```

4. Menjalankan Container Dengan Pembatasan CPU dan Memori
   
```bash
docker run --rm --cpus="0.5" --memory="256m" resource-limit-test
```

5. Menjalankan Container untuk Monitoring
  
```bash
docker run -d --name monitor-container resource-limit-test
```

6. Monitoring Penggunaan Resource
   
```bash
docker stats
```

7. Menghentikan dan Menghapus Container
   
```bash
docker stop monitor-container
docker rm monitor-container
```



---

## Analisis dan Hasil Eksekusi



---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## Quiz
1. Mengapa container perlu dibatasi CPU dan memori?
    
   **Jawaban:**

   Pembatasan CPU dan memori pada container diperlukan untuk menghindari satu container yang mem monopolisasi seluruh sumber daya sistem, sehingga mengganggu operasi container lainnya maupun host. Langkah ini menjamin pembagian resource yang merata di antara container, mempertahankan kestabilan sistem secara keseluruhan, serta mencegah kondisi kelaparan resource (resource starvation). Di samping itu, pembatasan resource mendukung perencanaan kapasitas yang tepat dan memastikan aplikasi beroperasi sesuai ketentuan yang telah dirancang.


   
2. Apa perbedaan VM dan container dalam konteks isolasi resource?
    
   **Jawaban:**

   Virtual Machine (VM) menerapkan isolasi berbasis hardware via hypervisor, di mana setiap VM dilengkapi kernel OS independen, menghasilkan tingkat isolasi yang lebih kokoh tetapi memakan resource lebih banyak. Sebaliknya, container memanfaatkan isolasi berbasis OS dengan berbagi kernel host yang sama, sehingga lebih hemat resource dan efisien, meskipun isolasinya kurang ketat dibanding VM. VM ideal untuk kebutuhan isolasi total dan menjalankan berbagai OS, sementara container unggul dalam deployment aplikasi yang cepat dengan overhead rendah.
   
3. Apa dampak limit memori terhadap aplikasi yang boros memori?
   
   **Jawaban:**

   Aplikasi dengan konsumsi memori berlebih akan memicu kesalahan Out of Memory (OOM) dan berpotensi dihentikan paksa oleh sistem saat menyentuh ambang batas memori yang telah ditetapkan. Kondisi ini mengakibatkan aplikasi terganggu atau runtuh sepenuhnya, berisiko menyebabkan kehilangan data yang belum tersimpan serta ketidakstabilan layanan. Solusinya mencakup optimalisasi kode program, penyesuaian ulang batas memori jika kebutuhan riil membenarkannya, atau penerapan swapping memori walaupun berpotensi menimbulkan penurunan kinerja.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?

  Memahami konsep isolasi resource antara sistem host dan guest pada Virtual Machine, terutama dalam mengaitkannya dengan konsep sandboxing dan hardening OS. Selain itu, proses konfigurasi dan penyesuaian resource VM juga memerlukan pemahaman yang baik agar sistem dapat berjalan optimal tanpa menimbulkan bottleneck.
  
- Bagaimana cara Anda mengatasinya?

  Saya melakukan beberapa langkah yaitu mempelajari dokumentasi Oracle VirtualBox dan konsep virtualisasi secara lebih mendalam, melakukan percobaan langsung
  
---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
