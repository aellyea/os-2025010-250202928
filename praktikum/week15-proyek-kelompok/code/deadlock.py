import threading
import time

resource_a = threading.Lock()  # Nagadus Emerald
resource_b = threading.Lock()  # Vajrada Amethyst

def raiden_process():
    print("Raiden: Mengambil Nagadus Emerald")
    with resource_a:
        time.sleep(2)
        print("Raiden: Menunggu Vajrada Amethyst")
        with resource_b:
            print("Raiden: Ascension Selesai")

def zhongli_process():
    print("Zhongli: Mengambil Vajrada Amethyst")
    with resource_b:
        time.sleep(2)
        print("Zhongli: Menunggu Nagadus Emerald")
        with resource_a:
            print("Zhongli: Ascension Selesai")

if __name__ == "__main__":
    print("=== SIMULASI DEADLOCK  ===\n")

    t1 = threading.Thread(target=raiden_process)
    t2 = threading.Thread(target=zhongli_process)

    t1.start()
    t2.start()

    
    t1.join(timeout=5)
    t2.join(timeout=5)

    print("\nDeadlock terdeteksi: Thread tidak selesai")
