import psycopg2
import threading
import time

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="genshin_db",
        user="postgres",
        password="password"
    )

def player_transaction(player_name, first_item, second_item):
    conn = get_connection()
    cur = conn.cursor()
    try:
        print(f"[{player_name}] Memulai transaksi...")
        
        # Langkah 1: Kunci item pertama
        cur.execute("SELECT * FROM inventory WHERE item_name = %s FOR UPDATE;", (first_item,))
        print(f"[{player_name}] BERHASIL mengunci {first_item}")
        
        time.sleep(3) # Memberi waktu agar player lain mengunci item kedua

        # Langkah 2: Mencoba kunci item kedua
        print(f"[{player_name}] Mencoba mengunci {second_item}...")
        cur.execute("SELECT * FROM inventory WHERE item_name = %s FOR UPDATE;", (second_item,))
        
        conn.commit()
        print(f"[{player_name}] Transaksi Sukses!")
    except Exception as e:
        print(f"[{player_name}] ERROR: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

# Menjalankan dua thread yang saling berlawanan
t1 = threading.Thread(target=player_transaction, args=("Player_Diluc", "Primogems", "Fate"))
t2 = threading.Thread(target=player_transaction, args=("Player_Zhongli", "Fate", "Primogems"))

t1.start()
t2.start()
t1.join()
t2.join()