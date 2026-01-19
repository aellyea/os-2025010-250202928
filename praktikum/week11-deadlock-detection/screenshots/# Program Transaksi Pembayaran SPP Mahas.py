# Program Transaksi Pembayaran SPP Mahasiswa
print("=== Program Pembayaran SPP Mahasiswa ===")

# Input data mahasiswa
nim = input("Masukkan NIM: ")
nama = input("Masukkan Nama Mahasiswa: ")
semester = input("Masukkan Semester: ")

# Input nominal SPP
nominal_spp = float(input("Masukkan Nominal SPP: "))

if nama.lower() == "andri":
    persentase_potongan = 20
    print("Mahasiswa mendapat potongan beasiswa sebesar 20%")
elif nama.lower() == "budi":
    persentase_potongan = 10
    print("Mahasiswa mendapat potongan beasiswa KIP sebesar 10%")
else:
    persentase_potongan = 0

potongan = nominal_spp * persentase_potongan / 100
total_spp = nominal_spp - potongan

status_cicilan = input("Apakah pembayaran dicicil? (ya/tidak): ")

if status_cicilan.lower() == "ya":
    # Input nominal per cicilan
    nominal_per_cicilan = float(input("Masukkan nominal per cicilan: Rp "))
    # Hitung jumlah cicilan otomatis
    jumlah_cicilan = total_spp / nominal_per_cicilan
    # Bulatkan ke atas supaya semua terbayar
    import math
    jumlah_cicilan = math.ceil(jumlah_cicilan)
    # Hitung ulang nominal per cicilan agar total pas
    pembayaran_per_cicilan = total_spp / jumlah_cicilan
else:
    pembayaran_per_cicilan = total_spp
    jumlah_cicilan = 1  # untuk keperluan output

# ===== Output akhir =====
print("\n=== Detail Pembayaran SPP ===")
print("NIM            :", nim)
print("Nama Mahasiswa :", nama)
print("Semester       :", semester)
print("Nominal SPP    : Rp", nominal_spp)
print("Potongan       : Rp", potongan)
print("Total SPP      : Rp", total_spp)

if status_cicilan.lower() == "ya":
    print("Jumlah Cicilan :", jumlah_cicilan)
    print("Bayar/Cicilan  : Rp", pembayaran_per_cicilan)
else:
    print("Pembayaran     : Rp", pembayaran_per_cicilan)

print("\nTransaksi Pembayaran SPP Selesai.")
