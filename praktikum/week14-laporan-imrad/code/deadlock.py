# Deadlock Detection - Dungeon Game Simulation (DEADLOCK)
# Player = Process
# Resource = Dungeon Keys (Key A, Key B, Key C)

players = ["Knight", "Mage", "Archer", "Rogue"]
keys = ["KeyA", "KeyB", "KeyC"]

# Allocation Matrix
allocation = [
    [1, 0, 0],  # Knight memegang KeyA
    [0, 1, 0],  # Mage memegang KeyB
    [0, 0, 1],  # Archer memegang KeyC
    [0, 0, 0]   # Rogue tidak memegang kunci
]

# Request Matrix
# SEMUA player butuh resource tambahan
request = [
    [0, 1, 0],  # Knight butuh KeyB
    [0, 0, 1],  # Mage butuh KeyC
    [1, 0, 0],  # Archer butuh KeyA
    [1, 0, 0]   # Rogue butuh KeyA
]

# Available Vector
available = [0, 0, 0]  # tidak ada kunci tersedia

n = len(players)
m = len(keys)

finish = [False] * n
work = available.copy()

while True:
    progress = False
    for i in range(n):
        if not finish[i]:
            if all(request[i][j] <= work[j] for j in range(m)):
                for j in range(m):
                    work[j] += allocation[i][j]
                finish[i] = True
                progress = True
    if not progress:
        break

deadlocked = []
for i in range(n):
    if not finish[i]:
        deadlocked.append(players[i])

print("=== Deadlock Detection: Dungeon Game ===")
if deadlocked:
    print("Deadlock terdeteksi!")
    print("Player terjebak di dungeon:")
    for p in deadlocked:
        print("-", p)
else:
    print("Tidak terjadi deadlock")
