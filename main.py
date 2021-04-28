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
    operating_matrix = A.copy()
    min_in_rows = find_min_in_row(operating_matrix)
    for i in range(len(operating_matrix)):
        for j in range(len(operating_matrix)):
            operating_matrix[i][j] = operating_matrix[i][j] - min_in_rows[i]
    min_in_cols = find_min_in_col(operating_matrix)
    for i in range(len(operating_matrix)):
        for j in range(len(operating_matrix)):
            operating_matrix[j][i] = operating_matrix[j][i] - min_in_cols[i]
    return operating_matrix


def find_indep_zeros(A):
    pass


def cross_out_minimal_line(A):
    pass


if __name__ == "__main__":
    M = [[1, 2, 5],
         [3, 4, 2],
         [3, 3, 3]]
