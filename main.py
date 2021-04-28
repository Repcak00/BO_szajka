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

def cross_out_minimal_line(A):
    pass


if __name__ == "__main__":
    A = [[1, 2, -1],
         [3, 4, 0],
         [0, 1, 3]]
    print(find_min_in_row(A))