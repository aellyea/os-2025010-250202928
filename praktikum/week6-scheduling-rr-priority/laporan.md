
# Laporan Praktikum Minggu 6
Topik: Round Robin (RR) dan Priority Scheduling

---

## Identitas
- **Nama**  : Alya Deviana Putri Reynaldi
- **NIM**   : 250202928
- **Kelas** : 1IKRB

---

## Tujuan
1. Memahami prinsip dasar algoritma Round Robin dan Priority Scheduling dalam penjadwalan CPU.
2. Melakukan simulasi perhitungan manual untuk menentukan waiting time dan turnaround time pada kedua algoritma.
3. Membuat dan menginterpretasi Gantt Chart untuk menggambarkan urutan eksekusi proses.
4. Menganalisis bagaimana variasi time quantum memengaruhi performa Round Robin.
5. Membandingkan efisiensi dan kelemahan kedua algoritma berdasarkan metrik rata-rata waiting time dan turnaround time.
6. Mengidentifikasi risiko starvation dan solusi potensial dalam algoritma Priority Scheduling.


---

## Dasar Teori
1. Penjadwalan CPU adalah cara kerja sistem operasi dalam menentukan urutan proses mana yang dijalankan terlebih dahulu, supaya penggunaan CPU lebih optimal, waktu menganggur berkurang, dan kebutuhan sistem seperti respons cepat maupun efisiensi bisa terpenuhi.
Burst time menggambarkan berapa lama sebuah proses membutuhkan waktu CPU secara terus-menerus hingga selesai, sedangkan arrival time menunjukkan kapan proses tersebut masuk ke ready queue.

2. Gantt Chart digunakan sebagai visualisasi untuk memperlihatkan bagaimana CPU membagi waktu eksekusi pada setiap proses, sehingga memudahkan analisis simulasi dan menemukan potensi hambatan.

3. Metrik seperti rata-rata waiting time dan rata-rata turnaround time digunakan untuk menilai seberapa baik performa suatu algoritma penjadwalan. Waiting time dihitung dari waktu kedatangan proses hingga proses tersebut mulai dieksekusi, sementara turnaround time dihitung dari waktu kedatangan hingga proses benar-benar selesai.

4. Preemptive scheduling memungkinkan sistem menghentikan proses yang sedang berjalan lalu memindahkan eksekusi ke proses lain sesuai aturan tertentu, misalnya penggunaan time quantum, demi menciptakan pembagian CPU yang lebih adil dalam lingkungan multitasking.

---

## Langkah Praktikum

1. Siapkan data proses dengan burst time, arrival time, dan priority.

2. Menjalankan Round Robin dengan time quantum tertentu, hitung waiting time dan turnaround time, serta buat Gantt Chart.
   
3. Menjalankan Priority Scheduling non-preemptive, urutkan berdasarkan prioritas, hitung WT dan TAT.
   
4. Membandingkan hasil rata-rata WT dan TAT antara RR dan Priority.
   
5. Analisis perubahan performa.
   
6. Dokumentasikan tabel, Gantt Chart, dan analisis dalam laporan.
    
7. Simpan bukti ke folder screenshots dan commit ke repository.

---

## Kode / Perintah

1. **Siapkan Data Proses**
   Gunakan contoh data berikut (boleh dimodifikasi sesuai kebutuhan):
   | Proses | Burst Time | Arrival Time | Priority |
   |:--:|:--:|:--:|:--:|
   | P1 | 5 | 0 | 2 |
   | P2 | 3 | 1 | 1 |
   | P3 | 8 | 2 | 4 |
   | P4 | 6 | 3 | 3 |

2. **Eksperimen 1 – Round Robin (RR)**
   - Gunakan *time quantum (q)* = 3.  
   - Hitung *waiting time* dan *turnaround time* untuk tiap proses.  
   - Simulasikan eksekusi menggunakan Gantt Chart (manual atau spreadsheet).  
     ```
     | P1 | P2 | P3 | P4 | P1 | P3 | ...
     0    3    6    9   12   15   18  ...
     ```
   - Catat sisa *burst time* tiap putaran.

3. **Eksperimen 2 – Priority Scheduling (Non-Preemptive)**
   - Urutkan proses berdasarkan nilai prioritas (angka kecil = prioritas tinggi).  
   - Lakukan perhitungan manual untuk:
     ```
     WT[i] = waktu mulai eksekusi - Arrival[i]
     TAT[i] = WT[i] + Burst[i]
     ```
   - Buat tabel perbandingan hasil RR dan Priority.

4. **Eksperimen 3 – Analisis Variasi Time Quantum (Opsional)**
   - Ubah *quantum* menjadi 2 dan 5.  
   - Amati perubahan nilai rata-rata *waiting time* dan *turnaround time*.  
   - Buat tabel perbandingan efek *quantum*.

5. **Eksperimen 4 – Dokumentasi**
   - Simpan semua hasil tabel dan screenshot ke:
     ```
     praktikum/week6-scheduling-rr-priority/screenshots/
     ```
   - Buat tabel perbandingan seperti berikut:

     | Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
     |------------|------------------|----------------------|------------|-------------|
     | RR | ... | ... | Adil terhadap semua proses | Tidak efisien jika quantum tidak tepat |
     | Priority | ... | ... | Efisien untuk proses penting | Potensi *starvation* pada prioritas rendah |


---



## Analisis

**1. Eksperimen 1 - Round Robin (RR)**

![Screenshot hasil RR](screenshots/round%20robin.png)


 **Eksperimen 2 – Priority Scheduling (Non-Preemptive)**

 ![Screenshot hasil Priority Scheduling](screenshots/priority%20scheduling.png)

**Perbandingan Algoritma Penjadwalan CPU**

| Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
|-----------|------------------:|----------------------:|-----------|------------|
| RR (q = 2) | 9.75 | 15.25 | Adil & responsif | Banyak context switching |
| RR (q = 3) | 8.50 | 14.00 | Seimbang antara fairness & efisiensi | Masih sensitif ke pemilihan quantum |
| RR (q = 5) | 7.00 | 12.50 | Lebih efisien, mirip FCFS | Fairness menurun untuk proses kecil |
| Priority (Non-Preemptive) | 5.25 | 10.75 | Sangat efisien untuk proses penting | Risiko **starvation** untuk prioritas rendah |

**Eksperimen 3 – Analisis Variasi Time Quantum (Opsional)**

## Quantum q = 2

### Gantt Chart
| P1 | P2 | P3 | P1 | P4 | P2 | P3 | P1 | P4 | P3 | P4 | P3 |

- **P1**: 0–2, 6–8, 13–14 → finish = 14  
- **P2**: 2–4, 10–11 → finish = 11  
- **P3**: 4–6, 11–13, 16–18, 20–22 → finish = 22  
- **P4**: 8–10, 14–16, 18–20 → finish = 20  

| Proses | Finish | Arrival Time | Burst Time | Turnaround Time (TAT) | Waiting Time (WT) |
|:------:|:------:|:-------------:|:-----------:|:-----------------------:|:------------------:|
| P1 | 14 | 0 | 5 | 14 | 9 |
| P2 | 11 | 1 | 3 | 10 | 7 |
| P3 | 22 | 2 | 8 | 20 | 12 |
| P4 | 20 | 3 | 6 | 17 | 11 |

- **Total WT** = 39  
- **Rata-rata WT** = 9.75  
- **Total TAT** = 61  
- **Rata-rata TAT** = 15.25

## Quantum q = 5

### Gantt Chart
| P1 | P2 | P3 | P4 | P3 | P4 |

- **P1**: 0–5 → finish = 5  
- **P2**: 5–8 → finish = 8  
- **P3**: 8–13, 18–21 → finish = 21  
- **P4**: 13–18, 21–22 → finish = 22  

### Hasil Akhir per Proses
| Proses | Finish | Arrival Time | Burst Time | Turnaround Time (TAT) | Waiting Time (WT) |
|:------:|:------:|:-------------:|:-----------:|:-----------------------:|:------------------:|
| P1 | 5  | 0 | 5 | 5  | 0  |
| P2 | 8  | 1 | 3 | 7  | 4  |
| P3 | 21 | 2 | 8 | 19 | 11 |
| P4 | 22 | 3 | 6 | 19 | 13 |

- **Total WT** = 28  
- **Rata-rata WT** = 7.00  
- **Total TAT** = 50  
- **Rata-rata TAT** = 12.50
     
| Quantum | Avg WT | Avg TAT | Pengaruh |
|:-------:|:------:|:--------:|-----------|
| 2 | 9.75 | 15.25 | Lebih adil, tapi overhead tinggi (context switch sering) |
| 3 | 8.50 | 14.00 | Keseimbangan antara keadilan dan efisiensi |
| 5 | 7.00 | 12.50 | Lebih efisien untuk proses panjang, tapi kurang adil |

---

## Kesimpulan

1. Algoritma Round Robin memberikan keadilan eksekusi proses melalui time quantum, namun performanya bergantung pada nilai quantum yang tepat untuk meminimalkan waiting time rata-rata.
   
2. Priority Scheduling lebih efisien untuk proses prioritas tinggi, tetapi berisiko menyebabkan starvation pada proses dengan prioritas rendah.
   
3. Perbandingan kedua algoritma menunjukkan bahwa RR lebih adil dalam distribusi waktu, sedangkan Priority lebih optimal untuk skenario dengan kebutuhan prioritas spesifik.
   
4. Variasi time quantum pada RR secara signifikan memengaruhi turnaround time, di mana quantum kecil meningkatkan responsivitas tetapi dapat menambah overhead switching.

---

## Quiz
1. Apa perbedaan utama antara Round Robin dan Priority Scheduling?
   
   **Jawaban:**

   RR adalah preemptive dengan time quantum untuk keadilan, memberikan kesempatan eksekusi sama secara bergantian. Priority adalah non-preemptive, memprioritaskan berdasarkan nilai prioritas (angka kecil = tinggi), sehingga proses penting dulu tanpa interupsi.
   
2. Apa pengaruh besar/kecilnya time quantum terhadap performa sistem?
     
   **Jawaban:**

   Time quantum kecil meningkatkan responsivitas, tapi meningkatkan overhead context switch. Time quantum besar lebih efisien untuk proses panjang, tapi bisa menyebabkan starvation pada proses pendek dan kurang adil.

    
3. Mengapa algoritma Priority dapat menyebabkan starvation?
   
   **Jawaban:**  

   Karena proses prioritas rendah mungkin terus ditunda jika proses prioritas tinggi selalu datang, sehingga tidak pernah mendapat giliran eksekusi.


---

## Refleksi Diri

Apa bagian yang paling menantang minggu ini?

 **Jawaban:**
  
Menghitung percobaan eksperimen di praktikum ini.

Bagaimana cara Anda mengatasinya?

 **Jawaban:**
  
Saya mengatasinya dengan mengeksekusi proses langkah demi langkah menggunakan tabel manual dan Gantt Chart, serta memverifikasi perhitungan waiting time dan turnaround time beberapa kali untuk memastikan.


---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
