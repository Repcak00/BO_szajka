
#w zadaniu będziemy iterować od zera! tzn indeks 0 oznacza pierwszy element

#funkcja redukująca macierz
#posiada argument A: macierz do zredykowania
def reduce_mat(A): #Dawid Lisek:
    pass

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
    A = [[5, 30, 0, 30], [65, 50, 0, 0], [0, 0, 55, 5], [55, 20, 0, 5]]
    print(find_indep_zeros(A))

