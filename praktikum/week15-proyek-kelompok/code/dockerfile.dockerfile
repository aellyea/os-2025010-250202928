# Gunakan image python yang ringan
FROM python:3.9-slim

# Set folder kerja di dalam container
WORKDIR /app

# Salin semua file script dan CSV ke dalam container
# Pastikan file 1asset.csv, genshin_deadlock.py, dan script utama Anda ada di folder yang sama
COPY . .

# Buat file CSV secara otomatis jika belum ada (opsional)
RUN echo "asset_name\nMondstadt\nLiyue\nRaidenShogun\nMondstadt\nInazuma\nLiyue\nSumeru\nRaidenShogun" > 1asset.csv

# Command default untuk menjalankan simulasi deadlock
# Anda bisa menggantinya dengan script FCFS atau Page Replacement
CMD ["python", "genshin_deadlock.py"]