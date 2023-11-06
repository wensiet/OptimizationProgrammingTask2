def pivot(A, b, c, row, col):
    pivot_element = A[row][col]
    num_rows = len(A)
    num_cols = len(A[0])

    # Divide pivot row by pivot element
    A[row] = [x / pivot_element for x in A[row]]
    b[row] /= pivot_element

    # Eliminate other elements in pivot column
    for i in range(num_rows):
        if i != row:
            factor = A[i][col]
            A[i] = [A[i][j] - factor * A[row][j] for j in range(num_cols)]
            b[i] -= factor * b[row]

    # Adjust objective function coefficients
    factor = c[col]
    c = [c[j] - factor * A[row][j] for j in range(num_cols)]

    return A, b, c


def simplex(C, A, b, epsilon):
    num_rows = len(A)
    num_cols = len(A[0])

    # Add slack variables to the constraint matrix
    for i in range(num_rows):
        A[i].extend([0] * i + [1] + [0] * (num_rows - i - 1))
        C.append(0)

    while True:
        # Find entering variable (most negative coefficient in objective function)
        entering_col = min(range(num_cols), key=lambda j: C[j])

        if C[entering_col] >= 0:
            break  # Optimal solution found

        # Find leaving variable (minimum ratio test)
        min_ratio = float('inf')
        leaving_row = -1
        for i in range(num_rows):
            if A[i][entering_col] > 0:
                ratio = b[i] / A[i][entering_col]
                if ratio < min_ratio:
                    min_ratio = ratio
                    leaving_row = i

        if leaving_row == -1:
            print("The method is not applicable!")
            return None

        A, b, C = pivot(A, b, C, leaving_row, entering_col)

    return sum(b[i] * C[i] for i in range(num_cols))


# Example Usage
C = [-3, -2]  # Coefficients of objective function
A = [[1, 1], [2, 1], [1, 2]]  # Coefficients of constraint matrix
b = [4, 7, 5]  # Right-hand side values
epsilon = 1e-10  # Approximation accuracy

result = simplex(C, A, b, epsilon)

if result is not None:
    print(f"Maximum value of the objective function: {result}")
from algorithm.simplex import Simplex
