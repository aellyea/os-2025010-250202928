import threading
import time

# Resource yang diperebutkan
resource_a = threading.Lock()  # Contoh: Nagadus Emerald
resource_b = threading.Lock()  # Contoh: Vajrada Amethyst

def raiden_process():
    print("Raiden Shogun: Mencoba mengambil Nagadus Emerald...")
    with resource_a:
        print("Raiden Shogun: Berhasil mengambil Nagadus Emerald.")
        time.sleep(2)  # Simulasi proses berpikir/animasi
        print("Raiden Shogun: Menunggu Vajrada Amethyst untuk Ascension...")
        with resource_b:
            print("Raiden Shogun: Ascension Selesai!")

def zhongli_process():
    print("Zhongli: Mencoba mengambil Vajrada Amethyst...")
    with resource_b:
        print("Zhongli: Berhasil mengambil Vajrada Amethyst.")
        time.sleep(2)
        print("Zhongli: Menunggu Nagadus Emerald untuk Ascension...")
        with resource_a:
            print("Zhongli: Ascension Selesai!")

if __name__ == "__main__":
    print("=== SIMULASI DEADLOCK GENSHIN IMPACT ===")
    print("Skenario: Dua karakter memperebutkan material yang saling silang.\n")
    
    t1 = threading.Thread(target=raiden_process)
    t2 = threading.Thread(target=zhongli_process)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print("Proses Selesai (Ini tidak akan pernah tercetak jika Deadlock terjadi)")