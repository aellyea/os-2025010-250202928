def read_reference_string(filename):
    with open(filename, "r") as f:
        return [int(x.strip()) for x in f.read().split(",")]

def fifo(reference, frame_size):
    frames = []
    index = 0
    faults = 0

    print("\n=== FIFO ===")
    for page in reference:
        if page in frames:
            status = "HIT"
        else:
            faults += 1
            status = "FAULT"
            if len(frames) < frame_size:
                frames.append(page)
            else:
                frames[index] = page
                index = (index + 1) % frame_size
        print(page, frames, status)

    return faults

def lru(reference, frame_size):
    frames = []
    recent = []
    faults = 0

    print("\n=== LRU ===")
    for page in reference:
        if page in frames:
            status = "HIT"
            recent.remove(page)
        else:
            faults += 1
            status = "FAULT"
            if len(frames) < frame_size:
                frames.append(page)
            else:
                old = recent.pop(0)
                frames[frames.index(old)] = page
        recent.append(page)
        print(page, frames, status)

    return faults

if __name__ == "__main__":
    reference = read_reference_string("reference_string.txt")
    frame = 3

    fifo_fault = fifo(reference, frame)
    lru_fault = lru(reference, frame)

    print("\nTOTAL PAGE FAULT")
    print("FIFO:", fifo_fault)
    print("LRU :", lru_fault)
