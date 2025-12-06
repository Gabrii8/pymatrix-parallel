import numpy as np
from multiprocessing import Pool

# SEQUENTIAL LOGIC 
def multiply_sequential(A, B):
    n = len(A)
    C = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            total = 0
            for k in range(n):
                total += A[i][k] * B[k][j]
            C[i][j] = total
    return C

# PARALLEL LOGIC
def worker_task(args):
    row_idx, A_row, B, n = args
    row_result = np.zeros(n)
    for j in range(n):
        total = 0
        for k in range(n):
            total += A_row[k] * B[k][j]
        row_result[j] = total
    return row_idx, row_result

def multiply_parallel(A, B, num_cores):
    n = len(A)
    tasks = [(i, A[i], B, n) for i in range(n)]
    
    with Pool(processes=num_cores) as pool:
        results = pool.map(worker_task, tasks)
        
    C = np.zeros((n, n))
    for row_idx, row_data in results:
        C[row_idx] = row_data
    return C

# VECTORIZED LOGIC
def multiply_vectorized(A, B):
    return np.dot(A, B)