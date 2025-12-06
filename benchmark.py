import time
import os
import csv
import numpy as np
from multiprocessing import cpu_count
from matrix_ops import multiply_sequential, multiply_parallel, multiply_vectorized
from plot_results import generate_plots


TEST_SIZES = [100, 300, 500, 700] 
RESULTS_DIR = 'results'

def run_benchmark():
    num_cores = cpu_count()    
    if not os.path.exists(RESULTS_DIR):
        os.makedirs(RESULTS_DIR)
        print(f" -> Folder '{RESULTS_DIR}' created/verified.")

    results_data = []
    
    print("")
    print("-" * 95)
    print(f"{'Size':<12} | {'Sequential Time (s)':<20} | {'Parallel Time (s)':<20} | {'Vectorized Time (s)':<20} | {'Speedup (x)':<12}")
    print("-" * 95)

    for size in TEST_SIZES:
        A = np.random.rand(size, size)
        B = np.random.rand(size, size)

        # Sequential
        start = time.time()
        multiply_sequential(A, B)
        dur_seq = time.time() - start

        # Parallel
        start = time.time()
        multiply_parallel(A, B, num_cores)
        dur_par = time.time() - start

        # Vectorized
        start = time.time()
        multiply_vectorized(A, B)
        dur_vec = time.time() - start

        # Metrics
        speedup = dur_seq / dur_par if dur_par > 0 else 0
        efficiency = speedup / num_cores if num_cores > 0 else 0

        results_data.append([size, dur_seq, dur_par, dur_vec, speedup, efficiency])
        print(f"{size:<12} | {dur_seq:<20.4f} | {dur_par:<20.4f} | {dur_vec:<20.6f} | {speedup:<12.2f}")

    # Save CSV to results folder
    csv_path = os.path.join(RESULTS_DIR, 'benchmark_data.csv')
    
    with open(csv_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Matrix_Size', 'Sequential_Time_Seconds', 'Parallel_Time_Seconds', 'Vectorized_Time_Seconds', 'Speedup_Factor', 'Efficiency_Per_Core'])
        writer.writerows(results_data)
    
    # Generate graphics
    generate_plots()
    print("\nProcess finished. Check the results/ folder.")

if __name__ == '__main__':
    run_benchmark()