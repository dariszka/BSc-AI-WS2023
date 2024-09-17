import argparse
import math
from multiprocessing import Pool

def sum_of_fractions(start: int, end: int) -> float:
    sum = 0.0
    for k in range(start,end+1):
        sum += 1/k
    return sum

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--processes", type=int, default=1, help="number of processes")
    parser.add_argument("-n", type=int, default=1000, help="number of terms in the sum")

    args = parser.parse_args()

    n = args.n
    p = args.processes

    ranges = []
    step = n // p
    for i in range(p):
        start = i * step + 1
        end = min((i + 1) * step, n)
        ranges.append((start, end))

    with Pool(p) as pool:
        pool_returns = pool.starmap(sum_of_fractions, ranges)

    gamma = sum(pool_returns) - math.log(n)

    print(f"Euler-Mascheroni constant approximation ({n} terms): {gamma:0.9f}")