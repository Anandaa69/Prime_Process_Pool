import multiprocessing
import time


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def count_primes(start, end):
    result = 0
    for i in range(start, end):
        if is_prime(i):
            result += 1
    return result

def find_sums(ranges):
    with multiprocessing.Pool() as pool:
        results = pool.starmap(count_primes, ranges)  # ใช้ starmap เพื่อ unpack tuple
    return sum(results)


if __name__ == "__main__":
    # Specify the range of numbers to check
    ranges = [(1_000_000 * i, 1_000_000 * (i + 1)) for i in range(4)]

    print("Starting prime number calculation...")
    start_time = time.time()

    # Use the find_sums function
    total_primes = find_sums(ranges)

    duration = time.time() - start_time
    print(f"Total prime numbers found: {total_primes}")
    print(f"Duration: {duration:.2f} seconds")
