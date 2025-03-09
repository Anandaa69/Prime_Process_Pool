# Prime Number Calculation with Multiprocessing

This Python project calculates prime numbers in large numerical ranges using the `multiprocessing` module. It splits the task into smaller chunks and processes them in parallel using a **Process Pool**. This approach significantly speeds up the calculation for large datasets by utilizing multiple processes to check for prime numbers concurrently.

## Example Output

```
Starting prime number calculation...
Total prime numbers found: 283146
Duration: 5.34 seconds
```

## Features
- **Parallel calculation** of prime numbers using multiple processes.
- Utilizes Python's **multiprocessing** module for faster computation.
- Efficient handling of large numerical ranges.

## How It Works
1. The program splits the task into multiple ranges (e.g., 1 million numbers per range).
2. Each range is processed in parallel using a **Process Pool**.
3. The final result is the total number of prime numbers found across all ranges.

## Benefits
- **Speed**: Parallel processing makes it faster to calculate primes in large datasets.
- **Efficiency**: The use of multiprocessing ensures that the computation is distributed across multiple processes, reducing the overall execution time.
