import matplotlib.pyplot as plt
import csv
import os

RESULTS_DIR = 'results'
CSV_FILENAME = 'benchmark_data.csv'

# Read the CSV file and generate 4 graphics
def generate_plots():
    csv_path = os.path.join(RESULTS_DIR, CSV_FILENAME)
    
    if not os.path.exists(csv_path):
        print(f"ERROR: '{csv_path}' not found.")
        return

    sizes = []
    times_seq = []
    times_par = []
    times_vec = []
    speedups = []
    efficiencies = [] 
      
    with open(csv_path, 'r') as f:
        reader = csv.reader(f)
        next(reader) 
        for row in reader:
            sizes.append(int(row[0]))
            times_seq.append(float(row[1]))
            times_par.append(float(row[2]))
            times_vec.append(float(row[3]))
            speedups.append(float(row[4]))
            efficiencies.append(float(row[5])) 
    
    # 1 - TIMES (Linear)
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times_seq, 'o-', label='Sequential', color='red')
    plt.plot(sizes, times_par, 's-', label='Parallel', color='blue')
    plt.plot(sizes, times_vec, '^-', label='Vectorized', color='green')
    plt.xlabel('Matrix Size (N)')
    plt.ylabel('Time (seconds)')
    plt.title('Execution Time (Linear Scale)')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.savefig(os.path.join(RESULTS_DIR, 'execution_time.png'))
    plt.close()

    # 2 - TIMES (Logarithmic)
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times_seq, 'o-', label='Sequential', color='red')
    plt.plot(sizes, times_par, 's-', label='Parallel', color='blue')
    plt.plot(sizes, times_vec, '^-', label='Vectorized', color='green')
    plt.yscale('log') 
    plt.xlabel('Matrix Size (N)')
    plt.ylabel('Time (seconds) - Log Scale')
    plt.title('Execution Time (Logarithmic Scale)')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7, which="both")
    plt.savefig(os.path.join(RESULTS_DIR, 'execution_time_log.png'))
    plt.close()

    # 3 - SPEEDUP 
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, speedups, 'd-', label='Speedup', color='purple')
    plt.axhline(y=1, color='gray', linestyle='--', alpha=0.5)
    plt.xlabel('Matrix Size (N)')
    plt.ylabel('Speedup Factor (x)')
    plt.title('Parallel Speedup Analysis')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.savefig(os.path.join(RESULTS_DIR, 'speedup.png'))
    plt.close()

    # 4 - EFFICIENCY 
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, efficiencies, 'x-', label='Efficiency per Core', color='orange')
    plt.axhline(y=1, color='gray', linestyle='--', alpha=0.5)
    plt.xlabel('Matrix Size (N)')
    plt.ylabel('Efficiency (Speedup / Num Cores)')
    plt.title('Parallel Efficiency Analysis')
    plt.legend()
    plt.ylim(0, 1.2) 
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.savefig(os.path.join(RESULTS_DIR, 'efficiency.png'))
    plt.close()

if __name__ == '__main__':
    generate_plots()