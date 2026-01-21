import csv
import os

def fifo_page_replacement(capacity, pages):
    memory = []
    page_faults = 0
    hits = 0
    
    print("\n" + "="*65)
    print(f"{'Step':<5} | {'Aset Genshin':<15} | {'Isi RAM HP':<25} | {'Status'}")
    print("-" * 65)

    for i, page in enumerate(pages):
        if page not in memory:
            if len(memory) < capacity:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)
            page_faults += 1
            status = "MISS (Loading...)"
        else:
            hits += 1
            status = "HIT (Lancar)"
        
        ram_state = " | ".join(memory)
        print(f"{i+1:<5} | {page:<15} | [{ram_state:<23}] | {status}")

    hit_ratio = (hits / len(pages)) * 100 if len(pages) > 0 else 0
    return page_faults, hit_ratio

def main():
    print("=== SISTEM MONITORING RAM HP - GENSHIN IMPACT ===")
    
    base_path = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(base_path, "1asset.csv")
    
    try:
        if not os.path.exists(filename):
            print(f"Error: File '{filename}' tidak ditemukan!")
            print("Pastikan file 1asset.csv ada di folder yang sama dengan script ini.")
            return

        capacity = int(input("Masukkan kapasitas slot RAM HP: "))
        
        pages = []
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                pages.append(row['asset_name'])

        if not pages:
            print("Error: File CSV kosong atau format salah (Pastikan ada header 'asset_name').")
            return

        faults, ratio = fifo_page_replacement(capacity, pages)

        print("-" * 65)
        print(f"HASIL ANALISIS:")
        print(f"- Total Aset yang diproses : {len(pages)}")
        print(f"- Total Page Faults        : {faults} (HP Mengalami Loading ulang)")
        print(f"- Hit Ratio                : {ratio:.2f}%")
        print("=" * 65)

    except ValueError:
        print("Error: Input kapasitas RAM harus berupa angka!")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    main()