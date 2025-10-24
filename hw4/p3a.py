from ortools.linear_solver import pywraplp

def p3():
    solver = pywraplp.Solver.CreateSolver("GLOP")
    #vars
    x_r = solver.NumVar(0, 1, "x_r")
    z = solver.NumVar(-solver.infinity(), solver.infinity(), "z")
    #constraints
    solver.Add(z <= -x_r)
    solver.Add(z <= 2*x_r - 1)
    #objective function
    solver.Maximize(z)
    #solve
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print("Optimal Value: ", round(solver.Objective().Value(), 3))
        print("x_r: ", round(x_r.solution_value(), 3))
        print("x_p: ", round(1- x_r.solution_value(), 3))
    else:
        print("No optimal solution")


if __name__ == '__main__':
    p3()