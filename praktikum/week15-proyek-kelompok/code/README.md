# Simulasi Sistem Operasi - Genshin Impact Theme

Repositori ini berisi simulasi CPU Scheduling (FCFS), Page Replacement (FIFO), dan Deadlock menggunakan skenario game Genshin Impact.

## Struktur Folder
- `cpu_scheduling.py`: Simulasi FCFS (Masuk Game).
- `FIFO/`: Folder berisi script `asset_name.py` dan data `1asset.csv`.
- `Deadlock/`: Folder berisi script `main.py` (Simulasi Deadlock karakter).

---

## Menjalankan di Host (Tanpa Docker)
Pastikan Python 3.x sudah terinstall.

1. **CPU Scheduling:**
 ```bash
   python cpu_scheduling.py
   ```
2. **FIFO Page Replacement:**
```bash
   python FIFO/asset_name.py
   ```
3. **Deadlock Simulation:**
```bash
   python Deadlock/main.py
   ```

## Menjalankan via Docker
1. **Build Image**
Jalankan perintah ini di folder utama:
```bash
   docker build -t genshin-simulasi .
   ```
2. **Run Container (Pilih Modul)**
Gunakan flag `-it` karena aplikasi membutuhkan input interaktif.

- **Menjalankan CPU Scheduling (Default):**
```bash
   docker run -it genshin-simulasi
   ```
- **Menjalankan FIFO RAM Monitoring:**
```bash
   docker run -it genshin-simulasi python FIFO/asset_name.py
   ```
- **Menjalankan Deadlock Simulation:**
```bash
   docker run -it genshin-simulasi python Deadlock/main.py
   ```
**Tips:** Jika Anda ingin menghentikan kontainer yang sedang berjalan, tekan `Ctrl + C` pada keyboard Anda.