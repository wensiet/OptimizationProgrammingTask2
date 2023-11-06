from algorithm import Simplex, interior_point


def main():
    # Test form Prog1.py

    # c = [9, 10, 16]
    # a = [[18, 15, 12], [6, 4, 8], [5, 3, 3]]
    # b = [360, 192, 180]
    # init_sol = [1, 1, 1, 315, 174, 169]
    # alpha1 = 0.5
    # alpha2 = 0.9
    # lpp_type = "max"
    # init_sol = [1, 1, 1, 315, 174, 169]

    alpha1 = 0.5
    alpha2 = 0.9

    lpp_type = input("Enter the type of the problem(min/max): ")
    rows = int(input("Enter the number of constraints: "))
    columns = int(input("Enter the number of x's: "))
    c = []
    print("Enter a vector of coefficients of objective function: ")
    for i in range(columns):
        c.append(int(input()))
    a = []
    print("Enter a matrix of coefficients of constraint function: ")
    for i in range(rows):
        temp = []
        for j in range(columns):
            temp.append(int(input()))
        a.append(temp)
    print("Enter the A vector of right-hand side numbers: ")
    b = []
    for i in range(rows):
        b.append(int(input()))

    print(f"Enter initial solution for this matrix(in total {columns * 2} elements): ")
    init_sol = []
    for i in range(columns * 2):
        init_sol.append(int(input()))

    interior1 = interior_point.InteriorPoint(c, a, alpha1, init_sol)
    interior2 = interior_point.InteriorPoint(c, a, alpha2, init_sol)
    print("Interior point solution with alpha = 0.5")
    interior1.solve_llp()
    print("Interior point solution with alpha = 0.9")
    interior2.solve_llp()
    s = Simplex(c, a, b, lpp_type)
    print("Simplex solution")
    s.solve()


if __name__ == "__main__":
    main()
