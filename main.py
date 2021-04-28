from copy import deepcopy
from math import inf

#funkcja redukująca macierz
#posiada argument A: macierz do zredukowania
from typing import List
INF = float('inf')

# zwraca listę minimalnych wartości w kolumnach
def find_min_in_col(A: List[List[int]]) -> List[int]:
    pass

# zwraca listę minimalnych wartości w wierszach
def find_min_in_row(A: List[List[int]]) -> List[int]:
    minimal_val = INF
    result_vector = []
    for i in range(len(A)):
        for j in range(len(A)):
            if A[i][j] < minimal_val:
                minimal_val = A[i][j]
        result_vector.append(minimal_val)
        minimal_val = INF
    return result_vector

def reduce_mat(A):
    pass

def find_indep_zeros(A):
    pass

def cross_out_minimal_line(A: List[List]):
    zeros_rows = [0 for _ in range(len(A))]
    zeros_cols = [0 for _ in range(len(A))]
    A_copy = deepcopy(A)
    for row in range(len(A_copy)):
        for col in range(len(A_copy)):
            if A_copy[row][col] == 0:
                zeros_rows[row] += 1
                zeros_cols[col] += 1

    crossed_r = []
    crossed_c = []
    while sum(zeros_rows) != 0:
        max_rows = max(zeros_rows)
        max_cols = max(zeros_cols)
        if max_rows >= max_cols:
            max_idx = zeros_rows.index(max(zeros_rows))
            crossed_r.append(max_idx)
            for col in range(len(A_copy)):
                if A[max_idx][col] == 0:
                    zeros_cols -= 1
                A[max_idx][col] = inf
        else:
            max_idx = zeros_rows.index(max(zeros_cols))
            crossed_c.append(max_idx)
            for row in range(len(A_copy)):
                if A[row][max_idx] == 0:
                    zeros_rows -= 1
                A[row][max_idx] = inf

    min_val = min((min(v) for v in A))
    for row in range(len(A_copy)):
        for col in range(len(A_copy)):
            if A_copy[row][col] != inf:
                A[row][col] -= min_val

    for cr in crossed_r:
        for cc in crossed_c:
            A[cr][cc] += min_val


if __name__ == "__main__":
    A = [[1, 2, -1],
         [3, 4, 0],
         [0, 1, 3]]
    print(find_min_in_row(A))

    print(int("inf"))