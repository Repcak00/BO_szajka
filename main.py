#w zadaniu będziemy iterować od zera! tzn indeks 0 oznacza pierwszy element

#posiada argument A: macierz do zredukowania
from typing import List
INF = float('inf')


# zwraca listę minimalnych wartości w kolumnach
def find_min_in_col(A: List[List[int]]) -> List[int]:
    minimal_val = INF
    result_vector = []
    for i in range(len(A)):
        for j in range(len(A)):
            if A[j][i] < minimal_val:
                minimal_val = A[j][i]
        result_vector.append(minimal_val)
        minimal_val = INF
    return result_vector


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

def find_indep_zeros(A: list(list)) -> list(tuple):

    lst_of_indep_zeros_tuple = []
    lst_of_taken_rows = []
    lst_of_taken_cols = []
    for row_id in range(len(A)):
        for col_id in range(len(A[row_id])):
            if A[row_id][col_id] == 0 and row_id not in lst_of_taken_rows and col_id not in lst_of_taken_cols:
                lst_of_indep_zeros_tuple.append((row_id, col_id))

    return lst_of_indep_zeros_tuple

def cross_out_minimal_line(A):

    pass




if __name__ == "__main__":
<<<<<<< HEAD
    M = [[1, 2, 5],
         [3, 4, 2],
         [3, 3, 3]]
=======
    A = [[1, 2, -1],
         [3, 4, 0],
         [0, 1, 3]]
    # A = [[5, 30, 0, 30], [65, 50, 0, 0], [0, 0, 55, 5], [55, 20, 0, 5]]
    print(find_indep_zeros(A))
    print(find_min_in_row(A))
>>>>>>> dfeadf8b2e5df148c6aa983f520cfd7ee353fad1
