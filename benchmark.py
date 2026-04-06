import time
import sys
import matplotlib.pyplot as plt

from src.hvlcs import HighestValueCommonSubsequence

results = []

for i in range(1, 11):
    fname = f"test/test{i:02d}.in"
    
    with open(fname) as f:
        lines = [l.strip() for l in f if l.strip()]

    # Parse K and alphabet values [cite: 15-18, 21-23]
    k = int(lines[0])
    char_values = {}
    for j in range(1, k + 1):
        parts = lines[j].split()
        if len(parts) == 2:
            char_values[parts[0]] = int(parts[1])
            
    A = lines[k + 1]
    B = lines[k + 2]

    # Time the core algorithm execution
    start = time.perf_counter()
    value, subseq = HighestValueCommonSubsequence.maximumValue(A, B, char_values)
    elapsed = time.perf_counter() - start

    results.append((len(A), len(B), elapsed, value))
    print(f"{fname} | |A|={len(A):3d}, |B|={len(B):3d} | time={elapsed*1000:.4f} ms | value={value}")

print("\nDone.")

sizes = [r[0] for r in results]  
times = [r[2] * 1000 for r in results] 
plt.plot(sizes, times, marker='o')
plt.xlabel("Length of String A")
plt.ylabel("Runtime (ms)")
plt.title("HVLCS Runtime vs Input Size")
plt.savefig("runtime_graph.png")
plt.show()