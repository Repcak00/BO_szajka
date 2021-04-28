
#w zadaniu będziemy iterować od zera! tzn indeks 0 oznacza pierwszy element

#funkcja redukująca macierz

#posiada argument A: macierz do zredukowania
from typing import List, Tuple
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

def find_indep_zeros(A: List[List[int]]) -> List[Tuple[int]]:

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


def cross_out_minimal_line(A):

    pass

def hungarian_algotithm(A):

    initial_A = A.copy()
    reduce_mat(A)
    lst_of_indep_zeros_ids = find_indep_zeros(A)
    #LICZBA ZER NIEZALEZNYCH MUSI BYĆ RÓWNA ROZMIAROWI MACIERZY: - sprawdzam ten warunek:
    while len(lst_of_indep_zeros_ids) != len(A):
        cross_out_minimal_line(A)
        reduce_mat(A)
        lst_of_indep_zeros_ids = find_indep_zeros(A)

    #lst_of_indep_zeros_ids to nasza lista połączeń maszyna - zadanie
    sum = 0
    for task_machine in lst_of_indep_zeros_ids:
        sum += initial_A[task_machine[0]][task_machine[1]]

    return sum, lst_of_indep_zeros_ids






if __name__ == "__main__":
    A = [[1, 2, -1],
         [3, 4, 0],
         [0, 1, 3]]
    # A = [[5, 30, 0, 30], [65, 50, 0, 0], [0, 0, 55, 5], [55, 20, 0, 5]]
    print(find_indep_zeros(A))
    print(find_min_in_row(A))
