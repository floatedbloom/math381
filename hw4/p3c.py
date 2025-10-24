from ortools.linear_solver import pywraplp

def p3():
    #P1's solver
    solver = pywraplp.Solver.CreateSolver("GLOP")
    #va1
    x_rr = solver.NumVar(0, 1, "x_rr")
    x_pp = solver.NumVar(0, 1, "x_pp")
    x_ss = solver.NumVar(0, 1, "x_ss")
    z = solver.NumVar(-solver.infinity(), solver.infinity(), "z")
    #constraints
    solver.Add(z <= x_pp - x_ss)
    solver.Add(z <= -x_rr + x_ss)
    solver.Add(z <= x_rr - x_pp)
    solver.Add(x_rr + x_pp + x_ss == 1)
    #objective function
    solver.Maximize(z)
    #solve
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print("Optimal Value: ", round(solver.Objective().Value(),3))
        print("x_pp: ", round(x_pp.solution_value(),3))
        print("x_rr: ", round(x_rr.solution_value(),3))
        print("x_ss: ", round(x_ss.solution_value(),3))
    else:
        print("No optimal solution")


if __name__ == '__main__':
    p3()