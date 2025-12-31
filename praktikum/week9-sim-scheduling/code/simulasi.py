import csv

def read_dataset(filename):
    processes = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            processes.append({
                'process': row['Process'],
                'arrival': int(row['Arrival']),
                'burst': int(row['Burst'])
            })
    return processes


def sjf_non_preemptive(processes):
    time = 0
    completed = []
    ready = processes.copy()

    while ready:
        available = [p for p in ready if p['arrival'] <= time]

        if not available:
            time += 1
            continue

        shortest = min(available, key=lambda x: x['burst'])
        ready.remove(shortest)

        waiting = time - shortest['arrival']
        turnaround = waiting + shortest['burst']
        time += shortest['burst']

        completed.append({
            'process': shortest['process'],
            'arrival': shortest['arrival'],
            'burst': shortest['burst'],
            'waiting': waiting,
            'turnaround': turnaround
        })

    return completed


def print_table(results):
    print("\nSJF Non-Preemptive Scheduling")
    print("-" * 55)
    print(f"{'Process':<8}{'Arrival':<10}{'Burst':<8}{'Waiting':<10}{'Turnaround'}")
    print("-" * 55)

    for r in results:
        print(f"{r['process']:<8}{r['arrival']:<10}{r['burst']:<8}{r['waiting']:<10}{r['turnaround']}")

    avg_wait = sum(r['waiting'] for r in results) / len(results)
    avg_turn = sum(r['turnaround'] for r in results) / len(results)

    print("-" * 55)
    print(f"Average Waiting Time    : {avg_wait:.2f}")
    print(f"Average Turnaround Time : {avg_turn:.2f}")


if __name__ == "__main__":
    data = read_dataset("code/dataset.csv")
    result = sjf_non_preemptive(data)
    print_table(result)
