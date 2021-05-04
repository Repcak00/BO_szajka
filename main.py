# w zadaniu będziemy iterować od zera! tzn indeks 0 oznacza pierwszy element

# funkcja redukująca macierz

# posiada argument A: macierz do zredukowania
from copy import deepcopy
from typing import List, Tuple

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
            zeros_rows[max_idx] = 0
            crossed_r.append(max_idx)
            for col in range(len(A_copy)):
                if A[max_idx][col] == 0:
                    zeros_cols[col] -= 1
                A_copy[max_idx][col] = INF
        else:
            max_idx = zeros_cols.index(max(zeros_cols))
            zeros_cols[max_idx] = 0
            crossed_c.append(max_idx)
            for row in range(len(A_copy)):
                if A[row][max_idx] == 0:
                    zeros_rows[row] -= 1
                A_copy[row][max_idx] = INF

    min_val = min((min(v) for v in A_copy))  # minimalna wartość wśród niewykreślonych
    for row in range(len(A_copy)):
        for col in range(len(A_copy)):
            if A_copy[row][col] != INF:
                A[row][col] -= min_val

    for cr in crossed_r:
        for cc in crossed_c:
            A[cr][cc] += min_val


def find_indep_zeros(A: List[List[int]]) -> List[Tuple[int, int]]:
    lst_of_indep_zeros_tuple = []
    lst_of_taken_rows = []
    lst_of_taken_cols = []
    for row_id in range(len(A)):
        for col_id in range(len(A[row_id])):
            if A[row_id][col_id] == 0 and row_id not in lst_of_taken_rows and col_id not in lst_of_taken_cols:
                lst_of_taken_rows.append(row_id)
                lst_of_taken_cols.append(col_id)
                lst_of_indep_zeros_tuple.append((row_id, col_id))

    return lst_of_indep_zeros_tuple


def hungarian_algorithm(A):
    initial_A = deepcopy(A)
    reduce_mat(A)
    lst_of_indep_zeros_ids = find_indep_zeros(A)
    # LICZBA ZER NIEZALEZNYCH MUSI BYĆ RÓWNA ROZMIAROWI MACIERZY: - sprawdzam ten warunek:
    while len(lst_of_indep_zeros_ids) != len(A):
        cross_out_minimal_line(A)
        reduce_mat(A)
        lst_of_indep_zeros_ids = find_indep_zeros(A)

    # lst_of_indep_zeros_ids to nasza lista połączeń maszyna - zadanie
    sum = 0
    for task_machine in lst_of_indep_zeros_ids:
        sum += initial_A[task_machine[0]][task_machine[1]]

    return sum, lst_of_indep_zeros_ids


if __name__ == "__main__":
    # A = [[1, 2, -1],
    #      [3, 4, 0],
    #      [0, 1, 3]]

    A = [[5, 30, 0, 30],
         [65, 50, 0, 0],
         [0, 0, 55, 5],
         [55, 20, 0, 5]]

    print(hungarian_algorithm(A))
