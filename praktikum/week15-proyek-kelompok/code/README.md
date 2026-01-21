# Simulasi Sistem Operasi - Genshin Impact Theme

Repositori ini berisi simulasi CPU Scheduling (FCFS), Page Replacement (FIFO), dan Deadlock menggunakan skenario game Genshin Impact.

## Struktur Folder
- `cpu_scheduling.py`: Simulasi FCFS (Masuk Game).
- `FIFO/`: File berisi data `1asset.csv`.
- `Deadlock/`: File berisi script `main.py` (Simulasi Deadlock karakter).
- `run_all`: File eksekutor utama yang menjalankan seluruh modul secara berurutan

---

## Menjalankan di Host (Tanpa Docker)
Pastikan Python 3.x sudah terinstall.

1. **CPU Scheduling:**
 ```bash
   python cpu_scheduling.py
   ```
2. **FIFO Page Replacement:**
```bash
   python page_replacement.py
   ```
3. **Deadlock Simulation:**
```bash
   python Deadlock.py
   ```

## Menjalankan via Docker
Container akan menjalankan file `run_all.py` secara otomatis, yang mengeksekusi seluruh modul

```bash
docker run --rm week15-os
   ```
