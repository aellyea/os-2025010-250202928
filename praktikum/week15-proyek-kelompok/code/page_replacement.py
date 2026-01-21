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

    hit_ratio = (hits / len(pages)) * 100 if pages else 0

    print("-" * 65)
    print("HASIL ANALISIS:")
    print(f"- Total Aset Diproses : {len(pages)}")
    print(f"- Page Fault          : {page_faults}")
    print(f"- Hit Ratio           : {hit_ratio:.2f}%")
    print("=" * 65)


def main():
    print("=== MODUL B – PAGE REPLACEMENT FIFO (GENSHIN) ===")

    base_path = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(base_path, "FIFO", "1asset.csv")

    capacity = 3  # FIXED untuk Docker

    pages = []
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            pages.append(row['asset_name'])

    fifo_page_replacement(capacity, pages)


if __name__ == "__main__":
    main()