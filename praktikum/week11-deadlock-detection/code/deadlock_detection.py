import csv

def read_dataset(filename):
    processes = []
    allocation = {}
    request = {}

    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            p = row['Process']
            processes.append(p)
            allocation[p] = row['Allocation']
            request[p] = row['Request']

    return processes, allocation, request


def detect_deadlock(processes, allocation, request):
    graph = {}

    for p in processes:
        graph[p] = [request[p]]
        graph[allocation[p]] = [p]

    visited = set()
    stack = set()

    def dfs(node):
        if node in stack:
            return True
        if node in visited:
            return False

        visited.add(node)
        stack.add(node)

        for neighbor in graph.get(node, []):
            if dfs(neighbor):
                return True

        stack.remove(node)
        return False

    for node in graph:
        if dfs(node):
            return True

    return False


if __name__ == "__main__":
    processes, allocation, request = read_dataset("dataset_deadlock.csv")

    print("=== Deadlock Detection ===")
    print("Processes:", processes)

    if detect_deadlock(processes, allocation, request):
        print("Status: DEADLOCK TERDETEKSI")
        print("Proses yang terlibat:", ", ".join(processes))
    else:
        print("Status: TIDAK TERJADI DEADLOCK")
